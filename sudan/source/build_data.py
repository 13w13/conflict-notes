# Construit data.js a partir de raw/. Lancer : .venv/bin/python build_data.py
import re,glob,json,csv,collections,math,datetime
from shapely.geometry import MultiPoint
from shapely.ops import voronoi_diagram
from shapely.geometry import shape,Point
from shapely.ops import unary_union
import openpyxl
MONTHS=[];y,m=2023,4
while (y,m)<=(2026,10):
    MONTHS.append(f'{y}-{m:02d}'); m+=1
    if m>12:y+=1;m=1
WIKI_END='2026-08'  # dernier releve du module Wikipedia (17 aout 2026)
MANUAL=json.load(open('manual_updates.json'))  # corrections et ajouts a la main, sources dans le fichier
CTRL_END=max([WIKI_END]+[u['from'] for u in MANUAL['updates']])
rx=re.compile(r'\{\s*lat\s*=\s*"([-\d.]+)"\s*,\s*long\s*=\s*"([-\d.]+)"\s*,\s*mark\s*=\s*"([^"]+)"\s*,\s*marksize\s*=\s*"(\d+)"(.*?)\}',re.S)
def status(mark):
    k=mark.lower()
    if 'anim' in k: return 'x'
    if k.startswith('location dot') or k.startswith('dot '):
        for c,s in (('red','saf'),('blue','rsf'),('green','rsf'),('lime','rsf'),('yellow','spl'),('orange','spl'),('purple','slm'),('teal','oth'),('cyan','oth')):
            if c in k: return s
    return None
def clean(l):
    l=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',l); return l.strip()
snaps={}
for f in sorted(glob.glob('raw/wiki/*.lua')):
    s=open(f).read(); mo=f[-11:-4]; towns={}; sieges={}
    for lat,lon,mark,size,rest in rx.findall(s):
        lab=re.search(r'label\s*=\s*"([^"]*)"',rest); name=clean(lab.group(1)) if lab else ''
        key=(round(float(lat),2),round(float(lon),2))
        if 'map-arc' in mark.lower() or 'map-circle' in mark.lower(): sieges[key]=max(sieges.get(key,0),2 if 'circle' in mark.lower() else 1); continue  # 2 = siege, 1 = pression d'un cote
        st=status(mark)
        if st and name: towns[key]=dict(n=name,lat=float(lat),lon=float(lon),z=int(size),s=st)
    for k in sieges:
        if k in towns: towns[k]['b']=sieges[k]
    snaps[mo]=towns
# universe of towns = those in final snapshots (keyed by coords); track by name too
allk={}
for mo in sorted(snaps):
    for k,t in snaps[mo].items(): allk[k]=t
def hist_for(t):
    h={}
    for mo,tw in snaps.items():
        c=[x for x in tw.values() if abs(x['lat']-t['lat'])<0.07 and abs(x['lon']-t['lon'])<0.07]
        if not c: c=[x for x in tw.values() if x['n']==t['n'] and abs(x['lat']-t['lat'])<0.5 and abs(x['lon']-t['lon'])<0.5]
        if c: h[mo]=max(c,key=lambda x:(x['z'],-abs(x['lat']-t['lat'])-abs(x['lon']-t['lon'])))
    return h
final=snaps[max(snaps)]
towns=[]
for k,t in final.items():
    hist=hist_for(t); ser=[];bes=[];last=None;lastb=0
    first=min(hist)
    for mo in MONTHS:
        if mo<=WIKI_END and mo in hist: last=hist[mo]['s']; lastb=hist[mo].get('b',0)
        ser.append(last);bes.append(lastb)
    towns.append(dict(n=t['n'],lat=t['lat'],lon=t['lon'],z=t['z'],s=ser,b=bes,first=first))
# Une ville absente de la carte source n'est pas devinee : 'u' (pas de releve) jusqu'a sa premiere apparition.
for t in towns: t['s']=[v or 'u' for v in t['s']]
# Corrections et ajouts manuels (voir manual_updates.json). 'to' est inclus ; sans 'to', jusqu'au bout.
for u in MANUAL['updates']:
    if 'add' in u: a=u['add']; towns.append(dict(n=u['town'],lat=a['lat'],lon=a['lon'],z=a['z'],s=['u']*len(MONTHS),b=[0]*len(MONTHS),first=u['from']))
byname=collections.defaultdict(list)
for t in towns: byname[t['n']].append(t)
for u in MANUAL['updates']:
    ts=byname.get(u['town'])
    if not ts: raise SystemExit('ville inconnue dans manual_updates.json : '+u['town'])
    for t in ts:
        for i,mo in enumerate(MONTHS):
            if mo>=u['from'] and mo<=u.get('to','9999'):
                t['s'][i]=u['status']
                if 'besieged' in u: t['b'][i]=u['besieged']
        if u['from']<t['first']: t['first']=u['from']
print('towns',len(towns))
# geometry
LAT0=15.0;KX=math.cos(math.radians(LAT0))
def proj(lon,lat): return ((lon-21.5)*KX*40,(23.4-lat)*40)
def path(geom,tol):
    g=geom.simplify(tol,preserve_topology=True); polys=[g] if g.geom_type=='Polygon' else list(g.geoms); d=''
    for p in polys:
        if p.area<0.002: continue
        for ring in [p.exterior]+list(p.interiors):
            pts=[proj(x,y) for x,y in ring.coords]
            d+='M'+'L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
    return d
a2=json.load(open('raw/cod/sdn_admin2.geojson'))['features']; a1=json.load(open('raw/cod/sdn_admin1.geojson'))['features']
A2=[]
for f in a2:
    g=shape(f['geometry']).buffer(0); p=f['properties']
    A2.append(dict(pc=p['adm2_pcode'],n=p['adm2_name'],a1=p['adm1_pcode'],g=g,c=(p['center_lon'],p['center_lat'])))
A1=[dict(pc=f['properties']['adm1_pcode'],n=f['properties']['adm1_name'],g=shape(f['geometry']).buffer(0)) for f in a1]
# assign towns to admin2
for t in towns:
    pt=Point(t['lon'],t['lat']); t['a2']=None
    for a in A2:
        if a['g'].contains(pt): t['a2']=a['pc'];break
ctrl={}
for a in A2:
    ser=[]
    for i,mo in enumerate(MONTHS):
        ins=[t for t in towns if t['a2']==a['pc'] and t['s'][i]!='u']
        if ins: pool=[(t,t['z']) for t in ins]
        else:
            ds=sorted([t for t in towns if t['s'][i]!='u'],key=lambda t:(t['lon']-a['c'][0])**2*KX*KX+(t['lat']-a['c'][1])**2)[:3]
            pool=[(t,t['z']/(0.2+math.hypot((t['lon']-a['c'][0])*KX,t['lat']-a['c'][1]))) for t in ds if math.hypot((t['lon']-a['c'][0])*KX,t['lat']-a['c'][1])<250/111.32]
        if not pool: ser.append('u'); continue  # aucune ville suivie a moins de 250 km : pas de couleur
        w=collections.Counter()
        for t,wt in pool: w[t['s'][i]]+=wt
        tot=sum(w.values()); top,tv=w.most_common(1)[0]
        ser.append(top if tv/tot>=0.6 and top!='x' else ('x' if top=='x' or len(w)>1 else top))
    ctrl[a['pc']]=ser
# Grandes localites desertiques (plus de 40 000 km2) : decoupees autour de leurs villes.
# Chaque ville colore ce qui est plus proche d'elle que des autres, dans un rayon de 150 km. Le reste est 'u', sans releve.
def km2(g): return g.area*111.32**2*math.cos(math.radians(g.centroid.y))
R_DEG=150/111.32
PIECES=[]
for a in A2:
    ins=[t for t in towns if t['a2']==a['pc']]
    if km2(a['g'])<40000 or not ins:
        PIECES.append(dict(a=a,g=a['g'],s=ctrl[a['pc']],w=1)); continue
    cells=[]
    if len(ins)>1:
        vd=voronoi_diagram(MultiPoint([(t['lon'],t['lat']) for t in ins]),envelope=a['g'].envelope.buffer(1))
        for c in vd.geoms:
            t=next(t for t in ins if c.contains(Point(t['lon'],t['lat']))); cells.append((t,c))
    else: cells=[(ins[0],a['g'])]
    rest=a['g']; tot=a['g'].area
    for t,c in cells:
        disc=shape({'type':'Polygon','coordinates':[[(t['lon']+R_DEG/KX*math.cos(k*math.pi/24),t['lat']+R_DEG*math.sin(k*math.pi/24)) for k in range(49)]]})
        g=c.intersection(a['g']).intersection(disc)
        if g.is_empty: continue
        rest=rest.difference(g)
        PIECES.append(dict(a=a,g=g,s=[t['s'][i] if t['s'][i]!='u' else ctrl[a['pc']][i] for i in range(len(MONTHS))],w=g.area/tot))
    if not rest.is_empty and rest.area/tot>0.01: PIECES.append(dict(a=a,g=rest,s=['u']*len(MONTHS),w=rest.area/tot))
    print('decoupe',a['n'],len(cells),'villes')
# ACLED
def acled(fn):
    ws=openpyxl.load_workbook(fn,read_only=True)['Data']; out=collections.defaultdict(lambda:[0,0]); it=ws.iter_rows(values_only=True); h=next(it)
    MN={m:i+1 for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
    for r in it:
        mo=f"{int(r[7])}-{MN[r[6]]:02d}"
        if mo in MONTHS and (r[8] or r[9]): 
            o=out[(mo,r[4])]; o[0]+=int(r[8] or 0); o[1]+=int(r[9] or 0)
    return out
pv=acled(glob.glob('raw/*political_violence*')[0]); ct=acled(glob.glob('raw/*civilian_targeting*')[0])
ac={mo:[] for mo in MONTHS}; nat={mo:[0,0,0] for mo in MONTHS}
for (mo,pc),(e,f) in pv.items():
    ac[mo].append([pc,e,f]); nat[mo][0]+=e; nat[mo][1]+=f
for (mo,pc),(e,f) in ct.items(): nat[mo][2]+=f
# DTM
rows=[x for x in csv.DictReader(open(glob.glob('raw/sdn-iom-dtm*')[0],encoding='utf-8-sig')) if x['operation']=='Armed Clashes in Sudan (Overview)']
n0=collections.defaultdict(int); s1=collections.defaultdict(int)
for x in rows:
    d=x['reportingDate'][:10]; n=int(float(x['numPresentIdpInd'] or 0))
    if x['adminLevel']=='0': n0[d]+=n
    if x['adminLevel']=='1': s1[(d,x['admin1Pcode'])]+=n
dates=sorted(n0); idp=[];idp1=[]
for mo in MONTHS:
    ds=[d for d in dates if d[:7]<=mo]
    if not ds: idp.append(None);idp1.append({});continue
    d=ds[-1]; idp.append(n0[d]); idp1.append({pc:v for (dd,pc),v in s1.items() if dd==d})
print('idp',idp[0],max(x for x in idp if x),idp[-1],dates[-1])
# IPC level1
def norm(s): return re.sub(r'[^a-z]','',s.lower().replace('aj ','al ').replace('gedaref','gedaref').replace('kordufan','kordofan'))
n2pc={norm(a['n']):a['pc'] for a in A1}
ipc={}
for x in csv.DictReader(open(glob.glob('raw/*ipc_sdn_level1_long*')[0])):
    if x['Validity period']=='current' and x['Phase'] in('3+','4','5','all'):
        k=norm(x['Level 1']).replace('state','')
        pc=n2pc.get(k) or next((v for kk,v in n2pc.items() if kk[:6]==k[:6] and kk[-5:]==k[-5:]),None)
        if pc: d=ipc.setdefault(pc,{}); d[x['Phase']]=d.get(x['Phase'],0)+int(float(x['Number']))
print('ipc',len(ipc),[a['n'] for a in A1 if a['pc'] not in ipc])
# explosive weapons
ws=openpyxl.load_workbook(glob.glob('raw/*Explosive*')[0],read_only=True).active; it=ws.iter_rows(values_only=True); h=list(next(it)); ex={mo:[0,0] for mo in MONTHS}
for r in it:
    if not r[0]: continue
    mo=str(r[0])[:7]
    if mo in ex: ex[mo][0]+=1; ex[mo][1]+=1 if 'drone' in str(r[h.index('Launch Type')]).lower() else 0
ws=openpyxl.load_workbook(glob.glob('raw/*Aid_Worker*')[0],read_only=True).active; it=ws.iter_rows(values_only=True); h=list(next(it)); aid=collections.Counter(); killed=collections.Counter()
for r in it:
    if r[0] and str(r[0])[:4]>='2023': aid[str(r[0])[:4]]+=1; killed[str(r[0])[:4]]+=int(r[h.index('Aid Workers Killed')] or 0)
print('aid',dict(aid),dict(killed)); print('expl',sum(v[0] for v in ex.values()),sum(v[1] for v in ex.values()))
CODE={'saf':'s','rsf':'r','spl':'p','slm':'l','oth':'o','x':'x','u':'u'}
# Sources complementaires (fetch_extra.py) : financement, refugies, prix du sorgho, besoins, presence operationnelle
X='raw/extra/'
fts=[[int(p['year']),p['requirements_usd'],p['funding_usd']] for p in json.load(open(X+'fts_plans.json')) if str(p['year']) in('2022','2023','2024','2025','2026') and 'Sudan Humanitarian' in p['plan_name']]
fts.sort()
ref=[[x['year'],x['refugees']+x['asylum_seekers'],x['returned_refugees']] for x in json.load(open(X+'unhcr_origin.json')) if x['year']>=2019]
pr=collections.defaultdict(dict)
for x in json.load(open(X+'hapi_food_prices.json')):
    if x['commodity_name']=='Sorghum' and x['unit']=='3 KG' and x['price_type']=='Retail': pr[x['market_name']][x['date_start'][:7]]=x['price']
PM=['2022-01'];
while PM[-1]<'2026-09':
    y,m=map(int,PM[-1].split('-')); m+=1
    if m>12: y+=1;m=1
    PM.append(f'{y}-{m:02d}')
price=dict(months=PM,series={k:[pr[k].get(mo) for mo in PM] for k in ('Port Sudan','Al Fashir','Kadugli','El Obeid','El Geneina')})
needs=collections.defaultdict(dict)
for x in json.load(open(X+'hapi_needs.json')):
    if x['admin_level']==0 and x['sector_code']=='Intersectoral' and x['category']=='' : needs[x['date_start'][:4]][x['population_status']]=x['population']
orgs=collections.defaultdict(set); opp=''
for x in json.load(open(X+'hapi_op_presence.json')):
    pc=n2pc.get(norm(x['admin1_name'] or '')) or next((v for kk,v in n2pc.items() if kk[:6]==norm(x['admin1_name'] or 'zzzzzz')[:6] and kk[-5:]==norm(x['admin1_name'] or '')[-5:]),None)
    if pc: orgs[pc].add(x['org_acronym'] or x['org_name']); opp=x['date_start'][:7]+'/'+x['date_end'][:7]
extra=dict(fts=fts,ref=ref,price=price,needs=needs,orgs={k:len(v) for k,v in orgs.items()},orgsPeriod=opp,orgsAll=len(set().union(*orgs.values())))
print('extra',fts,ref[-3:],dict(needs),extra['orgs'],opp,extra['orgsAll'])
country=unary_union([a['g'] for a in A1])
out=dict(months=MONTHS,ctrlEnd=CTRL_END,wikiEnd=WIKI_END,
 manual=[dict(t=u['town'],m=u['from'],s=CODE[u['status']],k=u['kind']) for u in MANUAL['updates']],
 a2=[dict(pc=p['a']['pc'],n=p['a']['n'],a1=p['a']['a1'],w=round(p['w'],3),d=path(p['g'],0.012),c=[round(v,1) for v in proj(*p['a']['c'])],s=''.join(CODE[v] for v in p['s'])) for p in PIECES],
 a1=[dict(pc=a['pc'],n=a['n'],d=path(a['g'],0.03),c=[round(v,1) for v in proj(a['g'].representative_point().x,a['g'].representative_point().y)]) for a in A1],
 outline=path(country,0.02),
 towns=[dict(n=t['n'],f=MONTHS.index(max(t['first'],MONTHS[0])),p=[round(v,1) for v in proj(t['lon'],t['lat'])],z=t['z'],s=''.join(CODE[v] for v in t['s']),b=''.join(str(v) for v in t['b'])) for t in towns],
 acled=[ac[mo] for mo in MONTHS],nat=[nat[mo] for mo in MONTHS],idp=idp,idp1=idp1,ipc=ipc,expl=[ex[mo] for mo in MONTHS],aid=dict(aid),aidKilled=dict(killed),extra=extra)
js='window.SUDAN='+json.dumps(out,separators=(',',':'))+';'
open('data.js','w').write(js); print(len(js)//1024,'KB')
# quick stats
for i in (0,8,20,23,30,40):
    c=collections.Counter(a['s'][i] for a in out['a2']); print(MONTHS[i],dict(c),'fat',nat[MONTHS[i]])
ch=[sum(1 for t in out['towns'] if t['s'][i]!=t['s'][i-1]) for i in range(1,len(MONTHS))]; print(ch)

for nm in ['Nyala','Al Muthalathu','Kurmuk','Qaysan','El Geneina','Zalingei','El Fasher','Wad Madani','Khartoum','Sinja','El-Obeid','Bara','Kurmuk','Babanusa','Kadugli','Dilling','En Nahud','Ed Daein']:
    for t in out['towns']:
        if t['n']==nm: print(nm.ljust(11),t['s'],t['b'])
print(sorted(set(x['Level 1'] for x in csv.DictReader(open(glob.glob('raw/*ipc_sdn_level1_long*')[0])))))
