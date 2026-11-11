import json,urllib.request,urllib.parse,time,os,sys
UA={'User-Agent':'sudan-map-research/0.1'}
T='Module:2023 Sudanese Clashes detailed map'
def api(**p):
    p.update(format='json',formatversion=2)
    u='https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode(p)
    for k in range(8):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60))
        except Exception as e: time.sleep(5*(k+1))
    raise SystemExit('fail')
revs=[];cont={}
while True:
    d=api(action='query',prop='revisions',titles=T,rvprop='ids|timestamp',rvlimit=500,rvdir='newer',**cont)
    revs+=d['query']['pages'][0]['revisions']
    if 'continue' in d: cont=d['continue']
    else: break
print(len(revs),revs[0]['timestamp'],revs[-1]['timestamp'])
last={}
for r in revs: last[r['timestamp'][:7]]=r
os.makedirs(sys.argv[1],exist_ok=True)
for m,r in sorted(last.items()):
    f=f'{sys.argv[1]}/{m}.lua'
    if os.path.exists(f): continue
    d=api(action='query',prop='revisions',revids=r['revid'],rvprop='content|timestamp',rvslots='main')
    c=d['query']['pages'][0]['revisions'][0]['slots']['main']['content']
    open(f,'w').write('-- '+r['timestamp']+'\n'+c); time.sleep(2)
print(sorted(last))
json.dump({m:len([1 for r in revs if r['timestamp'][:7]==m]) for m in last},open(sys.argv[1]+'/_edits.json','w'))
