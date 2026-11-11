(function(){
var root=document.getElementById('root'),bf=document.getElementById('b-fr'),be=document.getElementById('b-en');
var D=window.SUDAN; if(!D){document.getElementById('m-ev').textContent='Données de carte indisponibles. Map data unavailable.';return;}
var LG='fr';
var T={
 fr:{months:['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'],
  mainTitle:'Qui tient quoi, mois par mois',cFight:'Combats du mois',cIdp:'Déplacés accueillis',cRoad:'Routes clés',
  miniFat:'Morts recensés par mois (ACLED)',miniIdp:'Personnes déplacées internes (OIM DTM)',play:'Lecture',pause:'Pause',
  mapAria:'Carte du Soudan',saf:'armée (SAF)',rsf:'RSF',spl:'SPLM-N et alliés des RSF',slm:'SLM d\'al-Nur',mix:'disputé ou mixte',none:'sans relevé',
  lFight:'morts du mois (ACLED)',lIdp:'déplacés accueillis',lRoad:'- - axes schématiques',lSiege:'assiégée',lPress:'sous pression',
  ctrlNote:' · contrôle du 17 août, 2 ajouts',inM:' en ',noIdp:'pas encore de relevé',millions:' millions',M:' M',
  times:' fois',first:'avr. 2023',from2023:' (dès avril)',ofWhich:' dont ',byDrone:' par drone',
  n1:'déplacés internes fin août 2026, après un maximum de {pk} M en janvier 2025',n2:'personnes en insécurité alimentaire aiguë, soit {p} % de la population (IPC, février à mai 2026)',n3:'personnes en phase 5, dite catastrophe, sur la même période',n4:'morts recensés par ACLED d\'avril 2023 à octobre 2026, un minimum',n5:'réfugiés et demandeurs d\'asile soudanais à l\'étranger fin 2025 (HCR)',n6:'personnes dans le besoin en 2026, pour {t} M visées par le plan',
  th:['État','Contrôle','Faim aiguë (IPC 3+)','Déplacés accueillis','Morts, 12 mois','Organisations'],
  reg:['Khartoum','Centre','Darfour','Kordofan','Nil Bleu'],regMax:'max. {n} en {m}',
  mk:{'Al Fashir':'El Fasher','Kadugli':'Kadugli','El Obeid':'El Obeid','El Geneina':'El Geneina'},prMax:'max. ×{r} en {m}',
  fund:'{f} reçus sur {r} Md$ ({p} %)',bn:'Md$',
  nb:['ÉGYPTE','LIBYE','TCHAD','RCA','SOUDAN DU SUD','ÉTHIOPIE','ÉRYTHRÉE'],entry:['Amdjarass (Tchad)','Koufra (Libye)','Égypte','mer Rouge'],
  towns:{'Port Sudan':'Port-Soudan','El-Obeid':'El Obeid','Ad-Damazin':'Damazin','Barah':'Bara','Singa':'Sinja','Al-Fulah':'El Fula','Khartoum North':'Bahri','Al Muthalathu':'Triangle','Qaysān':'Qaysan'},
  states:{'Aj Jazirah':'Gezira','Blue Nile':'Nil Bleu','Central Darfur':'Darfour-Central','East Darfur':'Darfour-Est','North Darfur':'Darfour-Nord','South Darfur':'Darfour-Sud','West Darfur':'Darfour-Ouest','North Kordofan':'Kordofan-Nord','South Kordofan':'Kordofan-Sud','West Kordofan':'Kordofan-Ouest','Northern':'Nord','Red Sea':'Mer Rouge','River Nile':'Nil','White Nile':'Nil Blanc'},
  ev:{'2023-04':'<b>15 avril.</b> Les combats éclatent à Khartoum entre l\'armée et les RSF. Chaque camp accuse l\'autre. La carte source ne suit alors qu\'une vingtaine de villes.','2023-06':'Les combats gagnent le Darfour. À El Geneina, des civils massalit sont tués par milliers.','2023-08':'<b>24 août.</b> Le général Burhan quitte son quartier général assiégé. Port-Soudan devient capitale de fait.','2023-10':'<b>26 octobre.</b> Les RSF prennent Nyala, puis Zalingei le 31.','2023-11':'<b>4 et 21 novembre.</b> Les RSF prennent Ardamata puis Ed Daein. Elles tiennent quatre des cinq capitales du Darfour.','2023-12':'<b>18 décembre.</b> Les RSF entrent à Wad Madani. Des centaines de milliers de personnes fuient à nouveau.','2024-03':'<b>12 mars.</b> L\'armée reprend le siège de la radio-télévision à Omdurman.','2024-05':'Le siège d\'El Fasher se referme. C\'est la dernière capitale du Darfour tenue par l\'armée et ses alliés.','2024-06':'Les RSF prennent El Fula, le Jebel Moya puis Sinja. C\'est leur extension maximale vers le sud-est.','2024-08':'<b>1er août.</b> La famine est confirmée dans le camp de Zamzam, près d\'El Fasher.','2024-10':'<b>5 octobre.</b> L\'armée reprend le Jebel Moya. Le 20, le chef de milice Kikil quitte les RSF pour l\'armée.','2025-01':'<b>11 janvier.</b> L\'armée reprend Wad Madani. Le nombre de déplacés atteint son maximum.','2025-03':'<b>21 mars.</b> L\'armée reprend le palais présidentiel, puis l\'aéroport de Khartoum le 26.','2025-04':'<b>11 au 13 avril.</b> Les RSF attaquent le camp de Zamzam. Au moins 1 013 civils tués selon l\'ONU.','2025-05':'<b>4 au 9 mai.</b> Des drones frappent Port-Soudan six jours de suite. Les RSF prennent En Nahud.','2025-06':'<b>11 juin.</b> L\'armée se retire du triangle frontalier avec la Libye et l\'Égypte. Les RSF l\'occupent.','2025-08':'<b>30 août.</b> Hemedti prête serment à Nyala à la tête du gouvernement parallèle Tasis.','2025-10':'<b>26 octobre.</b> Les RSF prennent El Fasher. L\'ONU documente plus de 6 000 morts en trois jours.','2025-12':'<b>1er et 8 décembre.</b> Les RSF prennent Babanusa, puis le champ pétrolier de Heglig.','2026-01':'<b>11 janvier.</b> Le gouvernement annonce son retour à Khartoum. L\'armée dit avoir rouvert la route de Dilling.','2026-02':'<b>3 février.</b> L\'armée annonce avoir brisé le siège de Kadugli.','2026-03':'Bara change deux fois de main. Les RSF et le SPLM-N prennent Kurmuk, sur le Nil Bleu.','2026-07':'<b>25 juillet.</b> L\'armée reprend Bara. La route d\'El Obeid à Omdurman rouvre.','2026-08':'<b>13 août.</b> Les RSF et le SPLM-N reprennent Kurmuk. Dernier relevé de la carte source le 17.','2026-09':'<b>25 septembre.</b> L\'armée et la Force conjointe entrent à Sodari. Seul changement confirmé après le dernier relevé.','2026-10':'Trois marchés frappés par drone en neuf jours, à Dibab, Amiet et Nyala. Le 6, Burhan écarte toute négociation.'}},
 en:{months:['January','February','March','April','May','June','July','August','September','October','November','December'],
  mainTitle:'Who holds what, month by month',cFight:'Fighting this month',cIdp:'Displaced people hosted',cRoad:'Key roads',
  miniFat:'Recorded deaths per month (ACLED)',miniIdp:'Internally displaced people (IOM DTM)',play:'Play',pause:'Pause',
  mapAria:'Map of Sudan',saf:'army (SAF)',rsf:'RSF',spl:'SPLM-N and RSF allies',slm:'al-Nur\'s SLM',mix:'disputed or mixed',none:'no reading',
  lFight:'deaths this month (ACLED)',lIdp:'displaced people hosted',lRoad:'- - schematic routes',lSiege:'besieged',lPress:'under pressure',
  ctrlNote:' · control as of 17 August, 2 additions',inM:' in ',noIdp:'no reading yet',millions:' million',M:' M',
  times:' times',first:'Apr 2023',from2023:' (from April)',ofWhich:', of which ',byDrone:' by drone',
  n1:'internally displaced at end August 2026, after a peak of {pk} M in January 2025',n2:'people acutely food insecure, {p}% of the population (IPC, February to May 2026)',n3:'people in phase 5, called catastrophe, over the same period',n4:'deaths recorded by ACLED from April 2023 to October 2026, a minimum',n5:'Sudanese refugees and asylum seekers abroad at end 2025 (UNHCR)',n6:'people in need in 2026, of whom the plan targets {t} M',
  th:['State','Control','Acute hunger (IPC 3+)','Displaced hosted','Deaths, 12 months','Organisations'],
  reg:['Khartoum','Centre','Darfur','Kordofan','Blue Nile'],regMax:'max {n} in {m}',
  mk:{'Al Fashir':'El Fasher','Kadugli':'Kadugli','El Obeid':'El Obeid','El Geneina':'El Geneina'},prMax:'max ×{r} in {m}',
  fund:'{f} received of {r} bn$ ({p}%)',bn:'bn$',
  nb:['EGYPT','LIBYA','CHAD','CAR','SOUTH SUDAN','ETHIOPIA','ERITREA'],entry:['Amdjarass (Chad)','Kufra (Libya)','Egypt','Red Sea'],
  towns:{'El-Obeid':'El Obeid','Ad-Damazin':'Damazin','Barah':'Bara','Singa':'Sinja','Al-Fulah':'El Fula','Khartoum North':'Bahri','Al Muthalathu':'Triangle','Qaysān':'Qaysan'},
  states:{'Aj Jazirah':'Gezira'},
  ev:{'2023-04':'<b>15 April.</b> Fighting breaks out in Khartoum between the army and the RSF. Each side blames the other. The source map tracks only about twenty towns at this point.','2023-06':'Fighting spreads to Darfur. In El Geneina, Masalit civilians are killed in their thousands.','2023-08':'<b>24 August.</b> General Burhan leaves his besieged headquarters. Port Sudan becomes the de facto capital.','2023-10':'<b>26 October.</b> The RSF takes Nyala, then Zalingei on the 31st.','2023-11':'<b>4 and 21 November.</b> The RSF takes Ardamata, then Ed Daein. It holds four of Darfur\'s five state capitals.','2023-12':'<b>18 December.</b> The RSF enters Wad Madani. Hundreds of thousands flee again.','2024-03':'<b>12 March.</b> The army retakes the broadcasting headquarters in Omdurman.','2024-05':'The siege of El Fasher closes in. It is the last Darfur capital held by the army and its allies.','2024-06':'The RSF takes El Fula, Jebel Moya and then Sinja. Its furthest reach to the south-east.','2024-08':'<b>1 August.</b> Famine is confirmed in Zamzam camp, near El Fasher.','2024-10':'<b>5 October.</b> The army retakes Jebel Moya. On the 20th the militia leader Kikil leaves the RSF for the army.','2025-01':'<b>11 January.</b> The army retakes Wad Madani. The number of displaced people peaks.','2025-03':'<b>21 March.</b> The army retakes the presidential palace, then Khartoum airport on the 26th.','2025-04':'<b>11 to 13 April.</b> The RSF attacks Zamzam camp. At least 1,013 civilians killed according to the UN.','2025-05':'<b>4 to 9 May.</b> Drones hit Port Sudan six days running. The RSF takes En Nahud.','2025-06':'<b>11 June.</b> The army withdraws from the border triangle with Libya and Egypt. The RSF moves in.','2025-08':'<b>30 August.</b> Hemedti is sworn in at Nyala as head of the parallel Tasis government.','2025-10':'<b>26 October.</b> The RSF takes El Fasher. The UN documents more than 6,000 killed in three days.','2025-12':'<b>1 and 8 December.</b> The RSF takes Babanusa, then the Heglig oil field.','2026-01':'<b>11 January.</b> The government announces its return to Khartoum. The army says it has reopened the Dilling road.','2026-02':'<b>3 February.</b> The army announces it has broken the siege of Kadugli.','2026-03':'Bara changes hands twice. The RSF and SPLM-N take Kurmuk in Blue Nile.','2026-07':'<b>25 July.</b> The army retakes Bara. The El Obeid to Omdurman road reopens.','2026-08':'<b>13 August.</b> The RSF and SPLM-N retake Kurmuk. Last revision of the source map on the 17th.','2026-09':'<b>25 September.</b> The army and the Joint Force enter Sodari. The only confirmed change after the last revision.','2026-10':'Three markets hit by drones in nine days, at Dibab, Amiet and Nyala. On the 6th Burhan rules out negotiation.'}}
};
function t(k){return T[LG][k];}
var M=D.months,N=M.length,CE=M.indexOf(D.ctrlEnd),WE=M.indexOf(D.wikiEnd),KX=Math.cos(15*Math.PI/180);
function mlab(m){var p=m.split('-');return t('months')[+p[1]-1]+' '+p[0];}
function ml(i){return mlab(M[i]);}
function P(lon,lat){return [(lon-21.5)*KX*40,(23.4-lat)*40];}
function css(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim();}
var COL={s:css('--saf'),r:css('--rsf'),p:css('--spl'),l:css('--slm'),o:css('--oth'),u:css('--none')},TITLE=css('--accent'),IDPC=css('--idp'),INK=css('--ink'),PAPER=css('--paper'),MUTED=css('--muted'),RULE=css('--rule'),GRID=css('--grid');
function num(n){return Math.round(n).toLocaleString(LG==='fr'?'fr-FR':'en-GB');}
function dec(n,d){var s=n.toFixed(d==null?1:d);return LG==='fr'?s.replace('.',','):s;}
function nm(n){return t('towns')[n]||n;}
function fill(s,o){return s.replace(/\{(\w+)\}/g,function(_,k){return o[k];});}
var ROADS=[[[37.19,19.58],[33.98,17.70],[32.56,15.50]],[[32.48,15.65],[30.37,13.70],[30.22,13.18]],[[30.22,13.18],[28.43,12.70],[26.14,13.60],[25.35,13.62]],[[30.22,13.18],[29.65,12.05],[29.71,11.01]],[[22.20,13.47],[22.45,13.45],[23.47,12.91],[24.88,12.05]],[[32.56,15.50],[33.54,14.39],[33.63,13.55],[34.36,11.79]],[[30.22,13.18],[32.66,13.16],[33.63,13.55]],[[24.88,12.05],[25.35,13.62]],[[28.43,12.70],[27.81,11.32]]];
var ENTRY=[[[22.83,16.07],[24.6,14.3]],[[24.6,21.9],[25.2,15.2]],[[31.3,22.0],[31.8,19.4]],[[38.6,20.6],[37.4,19.7]]];
var NB=[[30.5,22.9],[22.9,21.2],[21.9,15.2],[22.6,9.9],[30.5,8.9],[36.6,11.2],[37.6,15.6]];
var cen={};D.a2.forEach(function(a){cen[a.pc]=a.c;});
var uid=0;
function draw(el,o){
  var i=o.i,ci=Math.min(i,CE),b=o.box,x0=0,y0=44,w=672,h=552;
  if(b){var a=P(b[0],b[3]),c=P(b[2],b[1]);x0=a[0];y0=a[1];w=c[0]-a[0];h=c[1]-a[1];}
  var k=w/672,id='h'+(o.id||(++uid)),s=[];
  s.push('<svg viewBox="'+[x0,y0,w,h].map(function(v){return v.toFixed(1);}).join(' ')+'" role="img" aria-label="'+(o.title||t('mapAria'))+', '+ml(i)+'"><defs><pattern id="'+id+'" width="'+(7*k)+'" height="'+(7*k)+'" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="'+(7*k)+'" height="'+(7*k)+'" fill="'+COL.s+'"/><rect width="'+(3.5*k)+'" height="'+(7*k)+'" fill="'+COL.r+'"/></pattern></defs>');
  s.push('<rect x="'+x0+'" y="'+y0+'" width="'+w+'" height="'+h+'" fill="'+PAPER+'"/>');
  D.a2.forEach(function(a){var c=a.s[ci];if(c==='u'){s.push('<path d="'+a.d+'" fill="'+COL.u+'" stroke="'+RULE+'" stroke-width="'+(.5*k)+'"/>');return;}s.push('<path d="'+a.d+'" fill="'+(c==='x'?'url(#'+id+')':COL[c])+'"  fill-opacity="'+(c==='x'?.55:.78)+'"  stroke="'+PAPER+'" stroke-opacity=".7" stroke-width="'+(.5*k)+'"/>');});
  D.a1.forEach(function(a){s.push('<path d="'+a.d+'" fill="none" stroke="'+INK+'" stroke-opacity=".45" stroke-width="'+(.6*k)+'"/>');});
  s.push('<path d="'+D.outline+'" fill="none" stroke="'+INK+'" stroke-opacity=".9" stroke-width="'+(1*k)+'"/>');
  if(o.nb){NB.forEach(function(n,j){var p=P(n[0],n[1]);s.push('<text x="'+p[0]+'" y="'+p[1]+'" font-size="'+(9*k)+'" fill="'+MUTED+'" letter-spacing="1">'+t('nb')[j]+'</text>');});}
  if(o.road){
    ROADS.forEach(function(r){s.push('<polyline points="'+r.map(function(q){return P(q[0],q[1]).join(',');}).join(' ')+'" fill="none" stroke="'+INK+'" stroke-opacity=".85" stroke-width="'+(1.3*k)+'" stroke-dasharray="'+(4*k)+' '+(3*k)+'"/>');});
    if(!b||b[0]<23){ENTRY.forEach(function(e,j){var a=P(e[0][0],e[0][1]),c=P(e[1][0],e[1][1]);s.push('<line x1="'+a[0]+'" y1="'+a[1]+'" x2="'+c[0]+'" y2="'+c[1]+'" stroke="'+TITLE+'" stroke-width="'+(1.6*k)+'" stroke-dasharray="'+(2*k)+' '+(3*k)+'"/><circle cx="'+c[0]+'" cy="'+c[1]+'" r="'+(2.6*k)+'" fill="'+TITLE+'"/>');if(!b)s.push('<text x="'+(a[0]+4*k)+'" y="'+(a[1]-4*k)+'" font-size="'+(10.5*k)+'" font-weight="600" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(2.2*k)+'" paint-order="stroke">'+t('entry')[j]+'</text>');});}
  }
  if(o.fight){D.acled[i].forEach(function(e){var c=cen[e[0]];if(c&&e[2]>0)s.push('<circle cx="'+c[0]+'" cy="'+c[1]+'" r="'+(Math.sqrt(e[2])*1.15*Math.max(k,.55))+'" fill="'+INK+'" fill-opacity=".14" stroke="'+INK+'" stroke-opacity=".75" stroke-width="'+(.6*k)+'"/>');});}
  var minZ=o.minZ||20,names=o.names||null,lab=[];
  D.towns.forEach(function(tw){
    var c=tw.s[ci];if(c==='u')return;
    var r=(1.2+tw.z/9)*Math.max(k,.5),big=names?names.indexOf(tw.n)>=0:tw.z>=minZ;
    if(b){var q=tw.p;if(q[0]<x0||q[0]>x0+w||q[1]<y0||q[1]>y0+h)return;}
    var bs=tw.b[ci];
    if(bs==='2')s.push('<circle cx="'+tw.p[0]+'" cy="'+tw.p[1]+'" r="'+(r+3.2*k)+'" fill="none" stroke="'+INK+'" stroke-width="'+(1.1*k)+'" stroke-dasharray="'+(2.4*k)+' '+(1.6*k)+'"/>');
    else if(bs==='1')s.push('<circle cx="'+tw.p[0]+'" cy="'+tw.p[1]+'" r="'+(r+3.2*k)+'" fill="none" stroke="'+INK+'" stroke-width="'+(.8*k)+'" stroke-dasharray="'+(.7*k)+' '+(1.8*k)+'"/>');
    s.push('<circle cx="'+tw.p[0]+'" cy="'+tw.p[1]+'" r="'+r+'" fill="'+(c==='x'?PAPER:COL[c])+'" stroke="'+INK+'" stroke-width="'+(.6*k)+'"/>');
    if(big)lab.push('<text x="'+(tw.p[0]+r+2*k)+'" y="'+(tw.p[1]+3*k)+'" font-size="'+(12*k)+'" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(2.6*k)+'" paint-order="stroke" font-weight="600">'+nm(tw.n)+'</text>');
  });
  if(o.idp){var v=D.idp1[Math.min(i,N-1)]||{};D.a1.forEach(function(a){var n=v[a.pc];if(!n)return;var r=Math.sqrt(n)/52*k;s.push('<circle cx="'+a.c[0]+'" cy="'+a.c[1]+'" r="'+r+'"  fill="'+IDPC+'" fill-opacity=".22" stroke="'+IDPC+'" stroke-width="'+(1.2*k)+'"/>');if(n>300000)lab.push('<text x="'+a.c[0]+'" y="'+(a.c[1]+3.5*k)+'" text-anchor="middle" font-size="'+(11.5*k)+'" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(2.4*k)+'" paint-order="stroke" font-weight="600">'+dec(n/1e6)+t('M')+'</text>');});}
  s.push(lab.join(''));s.push('</svg>');el.innerHTML=s.join('');
}
function legend(o){
  var h='<span><i class="sw" style="background:'+COL.s+'"></i>'+t('saf')+'</span><span><i class="sw" style="background:'+COL.r+'"></i>'+t('rsf')+'</span><span><i class="sw" style="background:'+COL.p+'"></i>'+t('spl')+'</span><span><i class="sw" style="background:'+COL.l+'"></i>'+t('slm')+'</span><span><i class="sw x"></i>'+t('mix')+'</span><span><i class="sw" style="background:'+COL.u+';border:1px solid '+RULE+'"></i>'+t('none')+'</span>';
  if(o.fight)h+='<span><i class="sw c" style="border:1px solid '+INK+';background:rgba(22,24,29,.14)"></i>'+t('lFight')+'</span>';
  if(o.idp)h+='<span><i class="sw c" style="border:1px solid '+IDPC+';background:rgba(178,58,58,.22)"></i>'+t('lIdp')+'</span>';
  if(o.road)h+='<span>'+t('lRoad')+'</span>';
  if(o.siege)h+='<span><i class="sw c" style="border:1.5px dashed '+INK+'"></i>'+t('lSiege')+'</span><span><i class="sw c" style="border:1.5px dotted '+INK+'"></i>'+t('lPress')+'</span>';
  return h;
}
function frames(){
  uid=0;
  document.querySelectorAll('.frame').forEach(function(f){
    var d=f.dataset,i=M.indexOf(d.m),ti=LG==='fr'?d.tfr:d.ten,o={i:i,title:ti,box:d.box?d.box.split(',').map(Number):null,minZ:d.min?+d.min:null,names:d.names?d.names.split(','):null,road:!!d.road,idp:!!d.idp,fight:!d.nofight,nb:!!d.nb,siege:!!d.box};
    f.innerHTML='<div class="map-h"><span class="map-d">'+ml(i)+(i>WE?t('ctrlNote'):'')+'</span></div><div class="fs"></div><div class="map-l">'+legend(o)+'</div>';
    draw(f.querySelector('.fs'),o);
  });
}
function bars(el,vals,cur,col,neg,H,mxIn){
  var W=400;H=H||64;var mx=mxIn||Math.max.apply(null,vals.map(function(v){return v||0;})),mn=neg?Math.max.apply(null,neg):0,bw=W/vals.length,s='<svg viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="none" aria-hidden="true">';
  var base=neg?H*mx/(mx+mn||1):H;
  vals.forEach(function(v,j){var hh=(v||0)/(mx||1)*base;s+='<rect x="'+(j*bw+.6)+'" y="'+(base-hh)+'" width="'+(bw-1.2)+'" height="'+hh+'" fill="'+col+'" fill-opacity="'+(j===cur||cur<0?1:.35)+'"/>';if(neg){var nh=neg[j]/(mn||1)*(H-base);s+='<rect x="'+(j*bw+.6)+'" y="'+base+'" width="'+(bw-1.2)+'" height="'+nh+'" fill="'+COL.r+'"/>';}});
  if(cur>=0)s+='<line x1="'+((cur+.5)*bw)+'" x2="'+((cur+.5)*bw)+'" y1="0" y2="'+H+'" stroke="'+css('--accent')+'" stroke-width="1.5" vector-effect="non-scaling-stroke"/>';
  el.innerHTML=s+'</svg>';
}
function axis(months){var n=months.length,h='<div class="axis">';months.forEach(function(m,j){if(m.slice(5)==='01'||j===0)h+='<span style="left:'+(j/n*100)+'%">'+(m.slice(5)==='01'?m.slice(0,4):t('first'))+'</span>';});return h+'</div>';}
var FAT=D.nat.map(function(n){return n[1];}),IDP=D.idp.map(function(v){return v||0;});
var st={i:N-1,fight:true,idp:false,road:false,timer:null};
var sl=document.getElementById('slider'),pb=document.getElementById('play');sl.max=N-1;
function lastEv(i){var E=t('ev');for(var j=i;j>=0;j--){if(E[M[j]])return (j===i?'':'<span class="tag">'+ml(j)+'</span> ')+E[M[j]];}return '';}
function upd(){
  var i=st.i;sl.value=i;
  draw(document.getElementById('m-svg'),{i:i,id:'main',fight:st.fight,idp:st.idp,road:st.road,nb:true,minZ:20,title:t('mainTitle')});
  document.getElementById('m-date').textContent=ml(i)+(i>WE?t('ctrlNote'):'');
  document.getElementById('m-leg').innerHTML=legend({fight:st.fight,idp:st.idp,road:st.road,siege:true});
  document.getElementById('m-ev').innerHTML=lastEv(i);
  document.getElementById('m-fat').textContent=num(FAT[i])+t('inM')+ml(i);
  document.getElementById('m-idp').textContent=IDP[i]?dec(IDP[i]/1e6)+t('millions'):t('noIdp');
  bars(document.getElementById('ch-fat'),FAT,i,INK);bars(document.getElementById('ch-idp'),IDP,i,IDPC);
  pb.textContent=st.timer?t('pause'):t('play');
}
sl.addEventListener('input',function(){st.i=+sl.value;upd();});
function stop(){clearInterval(st.timer);st.timer=null;pb.textContent=t('play');}
pb.addEventListener('click',function(){if(st.timer){stop();return;}if(st.i>=N-1)st.i=0;st.timer=setInterval(function(){if(st.i>=N-1){stop();return;}st.i++;upd();},700);upd();});
[['c-fight','fight'],['c-idp','idp'],['c-road','road']].forEach(function(c){document.getElementById(c[0]).addEventListener('change',function(e){st[c[1]]=e.target.checked;upd();});});
function charts(){
  /* villes qui changent de camp */
  var up=[],dn=[],i;for(i=0;i<N;i++){var u=0,d=0;if(i>0&&i<=CE)D.towns.forEach(function(tw){if(i-1<tw.f)return;var a=tw.s[i-1],c=tw.s[i];if(a===c||a==='u')return;if(c==='s')u++;else if(c==='r'||c==='p')d++;});up.push(u);dn.push(d);}
  var el=document.getElementById('ch-flip');bars(el,up,-1,COL.s,dn,120);el.firstChild.style.height='120px';el.firstChild.style.width='100%';el.insertAdjacentHTML('beforeend',axis(M));
  /* ou l'on meurt */
  var a1n={};D.a1.forEach(function(a){a1n[a.pc]=a.n;});
  var G=[['Khartoum'],['Aj Jazirah','Sennar','White Nile'],['North Darfur','South Darfur','West Darfur','East Darfur','Central Darfur'],['North Kordofan','South Kordofan','West Kordofan'],['Blue Nile']];
  var ser=G.map(function(){return M.map(function(){return 0;});});
  D.acled.forEach(function(mo,j){mo.forEach(function(e){var n=a1n[e[0].slice(0,4)];G.forEach(function(g,k){if(g.indexOf(n)>=0)ser[k][j]+=e[2];});});});
  var gmx=Math.max.apply(null,ser.map(function(s){return Math.max.apply(null,s);}));
  var h='<div class="rows">';ser.forEach(function(s,k){var mx=Math.max.apply(null,s),mi=s.indexOf(mx);h+='<div><span>'+t('reg')[k]+'<small>'+fill(t('regMax'),{n:num(mx),m:ml(mi)})+'</small></span><div id="rg'+k+'"></div></div>';});
  document.getElementById('ch-reg').innerHTML=h+'</div>'+axis(M);
  ser.forEach(function(s,k){bars(document.getElementById('rg'+k),s,-1,INK,null,46,gmx);});
  /* prix du siege */
  var PR=D.extra.price,ps=PR.series['Port Sudan'],i0=PR.months.indexOf('2023-01'),pm=PR.months.slice(i0);
  h='<div class="rows">';var rs=[];
  ['Al Fashir','Kadugli','El Obeid','El Geneina'].forEach(function(mk,k){var r=PR.series[mk].slice(i0).map(function(v,j){var b=ps[i0+j];return v&&b?v/b:0;}),mx=Math.max.apply(null,r),mi=r.indexOf(mx);rs.push(r);h+='<div><span>'+t('mk')[mk]+'<small>'+fill(t('prMax'),{r:dec(mx,mx>=10?0:1),m:mlab(pm[mi])})+'</small></span><div id="pr'+k+'"></div></div>';});
  document.getElementById('ch-price').innerHTML=h+'</div>'+axis(pm);
  rs.forEach(function(r,k){bars(document.getElementById('pr'+k),r,-1,k===0?TITLE:MUTED,null,46);});
  /* top des villes */
  var a=D.towns.map(function(tw){var c=0;for(var i=Math.max(tw.f,0)+1;i<=CE;i++)if(tw.s[i]!==tw.s[i-1]&&tw.s[i-1]!=='u')c++;return [nm(tw.n),c,tw.s[CE]];}).sort(function(x,y){return y[1]-x[1];}).slice(0,10),mx=a[0][1];h='<div class="hb">';
  a.forEach(function(r){h+='<span>'+r[0]+'</span><i style="width:'+(r[1]/mx*100)+'%;background:'+(r[2]==='x'?MUTED:COL[r[2]])+'"></i><b>'+r[1]+t('times')+'</b>';});document.getElementById('ch-top').innerHTML=h+'</div>';
  /* drones */
  var y={},k;D.expl.forEach(function(e,i){var k=M[i].slice(0,4);y[k]=y[k]||[0,0];y[k][0]+=e[0];y[k][1]+=e[1];});mx=0;for(k in y)mx=Math.max(mx,y[k][0]);h='<div class="hb">';
  for(k in y){var v=y[k];h+='<span>'+k+(k==='2023'?t('from2023'):'')+'</span><i style="width:'+(v[0]/mx*100)+'%;background:linear-gradient(90deg,'+TITLE+' '+(v[1]/v[0]*100)+'%,'+RULE+' '+(v[1]/v[0]*100)+'%)"></i><b>'+v[0]+t('ofWhich')+v[1]+t('byDrone')+' ('+Math.round(v[1]/v[0]*100)+(LG==='fr'?' %':'%')+')</b>';}
  document.getElementById('ch-drone').innerHTML=h+'</div>';
  /* refugies */
  var R=D.extra.ref.filter(function(r){return r[0]>=2021;});mx=Math.max.apply(null,R.map(function(r){return r[1];}));h='<div class="hb">';
  R.forEach(function(r){h+='<span>'+r[0]+'</span><i style="width:'+(r[1]/mx*100)+'%;background:'+(r[0]<2023?RULE:TITLE)+'"></i><b>'+dec(r[1]/1e6,2)+t('M')+'</b>';});document.getElementById('ch-ref').innerHTML=h+'</div>';
  /* financement */
  var F=D.extra.fts;mx=Math.max.apply(null,F.map(function(f){return f[1];}));h='<div class="hb">';
  F.forEach(function(f){h+='<span>'+f[0]+'</span><span style="display:flex;width:'+(f[1]/mx*100)+'%;height:16px"><i style="width:'+(f[2]/f[1]*100)+'%;background:'+INK+'"></i><i class="hatch" style="flex:1"></i></span><b>'+fill(t('fund'),{f:dec(f[2]/1e9,2),r:dec(f[1]/1e9,2),p:Math.round(f[2]/f[1]*100)})+'</b>';});document.getElementById('ch-fund').innerHTML=h+'</div>';
  /* chiffres */
  var tot=FAT.reduce(function(a,b){return a+b;},0),pk=Math.max.apply(null,IDP),ipc=0,pop=0,p5=0,kil=0;for(k in D.ipc){ipc+=D.ipc[k]['3+']||0;pop+=D.ipc[k].all||0;p5+=D.ipc[k]['5']||0;}for(k in D.aidKilled)kil+=D.aidKilled[k];
  var nd=D.extra.needs['2026'],rf=D.extra.ref[D.extra.ref.length-1];
  document.querySelectorAll('.aidk').forEach(function(e){e.textContent=kil;});
  document.querySelectorAll('.pin').forEach(function(e){e.textContent=dec(nd.INN/1e6);});
  document.querySelectorAll('.tgt').forEach(function(e){e.textContent=dec(nd.TGT/1e6);});
  var li=IDP.length-1;while(li>0&&!IDP[li])li--;
  document.getElementById('nums').innerHTML='<div><b>'+dec(IDP[li]/1e6)+t('M')+'</b><span>'+fill(t('n1'),{pk:dec(pk/1e6)})+'</span></div><div><b>'+dec(rf[1]/1e6)+t('M')+'</b><span>'+t('n5')+'</span></div><div><b>'+dec(ipc/1e6)+t('M')+'</b><span>'+fill(t('n2'),{p:Math.round(ipc/pop*100)})+'</span></div><div><b>'+num(p5)+'</b><span>'+t('n3')+'</span></div><div><b>'+dec(nd.INN/1e6)+t('M')+'</b><span>'+fill(t('n6'),{t:dec(nd.TGT/1e6)})+'</span></div><div><b>'+num(tot)+'</b><span>'+t('n4')+'</span></div>';
  /* tableau par Etat */
  var rows=D.a1.filter(function(a){return D.ipc[a.pc];}).map(function(a){var c={s:0,r:0,p:0,l:0,o:0,x:0,u:0},n=0;D.a2.forEach(function(l){if(l.a1===a.pc){var ar=l.w;c[l.s[CE]]+=ar;n+=ar;}});var f=0;for(var i=N-12;i<N;i++)D.acled[i].forEach(function(e){if(e[0].slice(0,4)===a.pc)f+=e[2];});var ip=D.ipc[a.pc];return {n:a.n,c:c,t:n,ipc:ip['3+']/ip.all,idp:(D.idp1[li]||{})[a.pc]||0,f:f,o:D.extra.orgs[a.pc]||0};}).sort(function(x,y){return y.ipc-x.ipc;});
  var mi=Math.max.apply(null,rows.map(function(r){return r.idp;})),th=t('th');
  h='<thead><tr>'+th.map(function(x){return '<th>'+x+'</th>';}).join('')+'</tr></thead><tbody>';
  rows.forEach(function(r){var cb='';['s','x','r','p','l','o','u'].forEach(function(k){if(r.c[k])cb+='<i style="width:'+(r.c[k]/r.t*100)+'%;background:'+(k==='x'?'repeating-linear-gradient(135deg,'+COL.s+' 0 3px,'+COL.r+' 3px 6px)':COL[k])+'"></i>';});
   h+='<tr><td>'+(t('states')[r.n]||r.n)+'</td><td><span class="cb">'+cb+'</span></td><td class="n"><span class="pc" style="width:'+(r.ipc*70)+'px;background:'+INK+'"></span>'+Math.round(r.ipc*100)+(LG==='fr'?' %':'%')+'</td><td class="n"><span class="pc" style="width:'+(r.idp/mi*60)+'px"></span>'+num(r.idp)+'</td><td class="n">'+num(r.f)+'</td><td class="n">'+r.o+'</td></tr>';});
  document.getElementById('tbl').innerHTML=h+'</tbody>';
}
function renderAll(){
  document.querySelectorAll('[data-t]').forEach(function(e){e.textContent=t(e.dataset.t);});
  frames();charts();upd();
}
function setLang(l,keep){LG=l;root.setAttribute('data-l',l);bf.setAttribute('aria-pressed',l==='fr');be.setAttribute('aria-pressed',l==='en');document.documentElement.lang=l;if(keep){try{localStorage.setItem('lang',l);}catch(e){}}renderAll();}
var l0='fr';try{l0=localStorage.getItem('lang')||l0;}catch(e){}
if(location.hash==='#en')l0='en';if(location.hash==='#fr')l0='fr';
bf.addEventListener('click',function(){setLang('fr',true);location.hash='fr';});be.addEventListener('click',function(){setLang('en',true);location.hash='en';});
window.addEventListener('hashchange',function(){if(location.hash==='#en'&&LG!=='en')setLang('en',false);if(location.hash==='#fr'&&LG!=='fr')setLang('fr',false);});
setLang(l0,false);
})();
