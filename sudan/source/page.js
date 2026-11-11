(function(){
var root=document.getElementById('root'),bf=document.getElementById('b-fr'),be=document.getElementById('b-en');
var D=window.SUDAN; if(!D){document.getElementById('m-ev').textContent='Données de carte indisponibles. Map data unavailable.';return;}
var LG='fr';
var T={
 fr:{months:['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'],
  play:'Lecture',pause:'Pause',mapAria:'Carte du Soudan',
  saf:'Armée',rsf:'RSF',spl:'SPLM-N, allié des RSF',slm:'SLM d\'al-Nur',mix:'Disputé ou mixte',none:'Sans relevé',
  lFight:'personnes tuées dans le mois (ACLED)',lRoad:'axe schématique',lSiege:'ville assiégée',lPress:'pression d\'un côté',
  ctrlNote:' · contrôle au 17 août 2026',inM:' en ',M:' M',
  miniFat:'Personnes tuées, recensées par mois (ACLED)',
  shareLab:['Armée','Disputé ou mixte','RSF et alliés','Autres, sans relevé'],
  netLab:'Villes passées à l\'armée moins villes passées aux RSF, cumul',
  ann:{'2023-12':'Décembre 2023 : les RSF entrent à Wad Madani','2024-09':'Septembre 2024 : l\'armée lance son offensive au centre','2025-03':'Mars 2025 : l\'armée reprend Khartoum','2025-10':'Octobre 2025 : les RSF prennent El Fasher'},
  dAnn:{'2023-06':'El Geneina','2024-10':'Gezira','2025-04':'Zamzam','2025-10':'El Fasher'},
  dLeg:['dont violences visant des civils','autres personnes tuées (combats, frappes)'],
  reg:['Kordofan','Darfour','Khartoum','Centre','Nil Bleu','Autres'],
  idpReg:['Darfour','Kordofan','Khartoum et centre','Est et nord'],
  mk:{'Al Fashir':'El Fasher','Kadugli':'Kadugli','El Obeid':'El Obeid','El Geneina':'El Geneina'},ps:'Prix du sorgho rapporté à Port-Soudan',
  pAnn:{'2025-05':'Mai 2025 : début de la levée de terre','2025-10':'Octobre 2025 : dernier relevé à El Fasher'},
  drone:'par drone',inc:' incidents',
  fund:'{f} reçus sur {r} Md$ ({p} %)',cur:', en cours',
  th:['État','Contrôle','Faim aiguë (IPC 3+)','Personnes déplacées accueillies','Personnes tuées, 12 mois','Organisations'],
  nb:['ÉGYPTE','LIBYE','TCHAD','RCA','SOUDAN DU SUD','ÉTHIOPIE','ÉRYTHRÉE'],
  entry:['Amdjarass (Tchad), frontière fermée en février 2026','Koufra (Libye), depuis juin 2025','Égypte','mer Rouge'],
  towns:{'Port Sudan':'Port-Soudan','El-Obeid':'El Obeid','Ad-Damazin':'Damazin','Barah':'Bara','Singa':'Sinja','Al-Fulah':'El Fula','Al Muthalathu':'Triangle frontalier','Geneina':'El Geneina','Al-Khiwai':'Al-Khuwei','Tine':'Tina'},
  states:{'Aj Jazirah':'Gezira','Blue Nile':'Nil Bleu','Central Darfur':'Darfour-Central','East Darfur':'Darfour-Est','North Darfur':'Darfour-Nord','South Darfur':'Darfour-Sud','West Darfur':'Darfour-Ouest','North Kordofan':'Kordofan-Nord','South Kordofan':'Kordofan-Sud','West Kordofan':'Kordofan-Ouest','Northern':'Nord','Red Sea':'Mer Rouge','River Nile':'Nil','White Nile':'Nil Blanc'},
  facts:{'Wad Madani|2023-12':'RSF, 18 déc. 2023','Wad Madani|2025-03':'armée, 11 janv. 2025','Khartoum|2025-03':'armée, 21 mars 2025','Nyala|2025-11':'26 oct. 2023','Zalingei|2025-11':'31 oct. 2023','Geneina|2025-11':'nov. 2023','Ed Daein|2025-11':'21 nov. 2023','El Fasher|2025-11':'26 oct. 2025','Tawila|2025-11':'665 000 personnes déplacées','Barah|2026-10':'5 mars, 16 mars, 25 juil. 2026','Sodari|2026-10':'25 sept. 2026, confirmation faible','Kazgeil|2026-10':'5 nov. 2026, disputée','Babanusa|2026-10':'1er déc. 2025'},
  ev:{'2023-04':'<b>15 avril 2023.</b> Les combats ont commencé à Khartoum entre l\'armée et les Forces de soutien rapide. La carte source ne suivait alors qu\'une vingtaine de villes.','2023-06':'<b>Juin 2023.</b> Les RSF et des milices alliées ont tué des milliers de civils massalit à El Geneina, selon Human Rights Watch.','2023-08':'<b>24 août 2023.</b> Le général Burhan a quitté son quartier général assiégé. Le gouvernement s\'est installé à Port-Soudan.','2023-10':'<b>26 octobre 2023.</b> Les RSF ont pris Nyala, puis Zalingei le 31.','2023-11':'<b>Novembre 2023.</b> Les RSF ont pris Ardamata, près d\'El Geneina, puis Ed Daein.','2023-12':'<b>18 décembre 2023.</b> Les RSF sont entrées à Wad Madani.','2024-03':'<b>12 mars 2024.</b> L\'armée a repris le siège de la radio-télévision à Omdurman.','2024-05':'<b>Printemps 2024.</b> Les RSF ont encerclé El Fasher.','2024-06':'<b>Juin 2024.</b> Les RSF ont pris El Fula, le Jebel Moya puis Sinja.','2024-08':'<b>1er août 2024.</b> Le comité d\'examen de la famine a confirmé la famine dans le camp de Zamzam.','2024-10':'<b>Octobre 2024.</b> L\'armée a repris le Jebel Moya. Le chef de milice Abu Aqla Kikil a quitté les RSF pour l\'armée.','2025-01':'<b>11 janvier 2025.</b> L\'armée a repris Wad Madani.','2025-03':'<b>21 mars 2025.</b> L\'armée a repris le palais présidentiel à Khartoum.','2025-04':'<b>11 au 13 avril 2025.</b> Les RSF ont attaqué le camp de Zamzam. L\'ONU a compté au moins 1 013 civils tués.','2025-05':'<b>4 au 9 mai 2025.</b> Des drones ont frappé Port-Soudan six jours de suite.','2025-06':'<b>11 juin 2025.</b> L\'armée s\'est retirée du triangle frontalier avec la Libye et l\'Égypte. Les RSF l\'ont occupé.','2025-08':'<b>30 août 2025.</b> Hemedti a prêté serment à Nyala comme chef d\'un gouvernement parallèle.','2025-10':'<b>26 octobre 2025.</b> Les RSF ont pris El Fasher. L\'ONU a documenté plus de 6 000 personnes tuées en trois jours.','2025-12':'<b>Décembre 2025.</b> Les RSF ont pris Babanusa, puis le champ pétrolier de Heglig.','2026-01':'<b>Janvier 2026.</b> Le gouvernement a annoncé son retour à Khartoum. L\'armée a annoncé la réouverture de la route de Dilling.','2026-02':'<b>3 février 2026.</b> L\'armée a annoncé avoir levé le siège de Kadugli.','2026-03':'<b>Mars 2026.</b> Bara a changé deux fois de main. Les RSF et le SPLM-N ont pris Kurmuk.','2026-07':'<b>25 juillet 2026.</b> L\'armée a repris Bara. La route d\'El Obeid à Omdurman a rouvert.','2026-08':'<b>13 août 2026.</b> Les RSF et le SPLM-N ont repris Kurmuk. Dernier relevé de la carte source le 17.','2026-09':'<b>25 septembre 2026.</b> L\'armée et la Force conjointe sont entrées à Sodari.','2026-10':'<b>Octobre 2026.</b> Des drones ont frappé trois marchés en neuf jours, à Dibab, Amiet et Nyala.'}},
 en:{months:['January','February','March','April','May','June','July','August','September','October','November','December'],
  play:'Play',pause:'Pause',mapAria:'Map of Sudan',
  saf:'Army',rsf:'RSF',spl:'SPLM-N, allied to the RSF',slm:'al-Nur\'s SLM',mix:'Disputed or mixed',none:'No reading',
  lFight:'people killed in the month (ACLED)',lRoad:'schematic route',lSiege:'besieged town',lPress:'pressure from one side',
  ctrlNote:' · control as of 17 August 2026',inM:' in ',M:' M',
  miniFat:'People killed, recorded per month (ACLED)',
  shareLab:['Army','Disputed or mixed','RSF and allies','Others, no reading'],
  netLab:'Towns that went to the army minus towns that went to the RSF, cumulative',
  ann:{'2023-12':'December 2023: the RSF enters Wad Madani','2024-09':'September 2024: the army launches its offensive in the centre','2025-03':'March 2025: the army retakes Khartoum','2025-10':'October 2025: the RSF takes El Fasher'},
  dAnn:{'2023-06':'El Geneina','2024-10':'Gezira','2025-04':'Zamzam','2025-10':'El Fasher'},
  dLeg:['of which violence targeting civilians','other people killed (fighting, strikes)'],
  reg:['Kordofan','Darfur','Khartoum','Centre','Blue Nile','Other'],
  idpReg:['Darfur','Kordofan','Khartoum and centre','East and north'],
  mk:{'Al Fashir':'El Fasher','Kadugli':'Kadugli','El Obeid':'El Obeid','El Geneina':'El Geneina'},ps:'Sorghum price relative to Port Sudan',
  pAnn:{'2025-05':'May 2025: berm begun','2025-10':'October 2025: last reading in El Fasher'},
  drone:'by drone',inc:' incidents',
  fund:'{f} received of {r} bn$ ({p}%)',cur:', in progress',
  th:['State','Control','Acute hunger (IPC 3+)','Displaced people hosted','People killed, 12 months','Organisations'],
  nb:['EGYPT','LIBYA','CHAD','CAR','SOUTH SUDAN','ETHIOPIA','ERITREA'],
  entry:['Amdjarass (Chad), border closed in February 2026','Kufra (Libya), since June 2025','Egypt','Red Sea'],
  towns:{'El-Obeid':'El Obeid','Ad-Damazin':'Damazin','Barah':'Bara','Singa':'Sinja','Al-Fulah':'El Fula','Al Muthalathu':'Border triangle','Geneina':'El Geneina','Al-Khiwai':'Al-Khuwei','Tine':'Tina'},
  states:{'Aj Jazirah':'Gezira'},
  facts:{'Wad Madani|2023-12':'RSF, 18 Dec 2023','Wad Madani|2025-03':'army, 11 Jan 2025','Khartoum|2025-03':'army, 21 Mar 2025','Nyala|2025-11':'26 Oct 2023','Zalingei|2025-11':'31 Oct 2023','Geneina|2025-11':'Nov 2023','Ed Daein|2025-11':'21 Nov 2023','El Fasher|2025-11':'26 Oct 2025','Tawila|2025-11':'665,000 displaced people','Barah|2026-10':'5 Mar, 16 Mar, 25 Jul 2026','Sodari|2026-10':'25 Sep 2026, weak confirmation','Kazgeil|2026-10':'5 Nov 2026, disputed','Babanusa|2026-10':'1 Dec 2025'},
  ev:{'2023-04':'<b>15 April 2023.</b> Fighting began in Khartoum between the army and the Rapid Support Forces. The source map then tracked only about twenty towns.','2023-06':'<b>June 2023.</b> The RSF and allied militias killed thousands of Masalit civilians in El Geneina, according to Human Rights Watch.','2023-08':'<b>24 August 2023.</b> General Burhan left his besieged headquarters. The government moved to Port Sudan.','2023-10':'<b>26 October 2023.</b> The RSF took Nyala, then Zalingei on the 31st.','2023-11':'<b>November 2023.</b> The RSF took Ardamata, near El Geneina, then Ed Daein.','2023-12':'<b>18 December 2023.</b> The RSF entered Wad Madani.','2024-03':'<b>12 March 2024.</b> The army retook the broadcasting headquarters in Omdurman.','2024-05':'<b>Spring 2024.</b> The RSF encircled El Fasher.','2024-06':'<b>June 2024.</b> The RSF took El Fula, Jebel Moya and then Sinja.','2024-08':'<b>1 August 2024.</b> The Famine Review Committee confirmed famine in Zamzam camp.','2024-10':'<b>October 2024.</b> The army retook Jebel Moya. The militia leader Abu Aqla Kikil left the RSF for the army.','2025-01':'<b>11 January 2025.</b> The army retook Wad Madani.','2025-03':'<b>21 March 2025.</b> The army retook the presidential palace in Khartoum.','2025-04':'<b>11 to 13 April 2025.</b> The RSF attacked Zamzam camp. The UN counted at least 1,013 civilians killed.','2025-05':'<b>4 to 9 May 2025.</b> Drones struck Port Sudan on six consecutive days.','2025-06':'<b>11 June 2025.</b> The army withdrew from the border triangle with Libya and Egypt. The RSF occupied it.','2025-08':'<b>30 August 2025.</b> Hemedti was sworn in at Nyala as head of a parallel government.','2025-10':'<b>26 October 2025.</b> The RSF took El Fasher. The UN documented more than 6,000 people killed in three days.','2025-12':'<b>December 2025.</b> The RSF took Babanusa, then the Heglig oil field.','2026-01':'<b>January 2026.</b> The government announced its return to Khartoum. The army announced that the Dilling road had reopened.','2026-02':'<b>3 February 2026.</b> The army announced it had lifted the siege of Kadugli.','2026-03':'<b>March 2026.</b> Bara changed hands twice. The RSF and the SPLM-N took Kurmuk.','2026-07':'<b>25 July 2026.</b> The army retook Bara. The El Obeid to Omdurman road reopened.','2026-08':'<b>13 August 2026.</b> The RSF and the SPLM-N retook Kurmuk. Last revision of the source map on the 17th.','2026-09':'<b>25 September 2026.</b> The army and the Joint Force entered Sodari.','2026-10':'<b>October 2026.</b> Drones struck three markets in nine days, at Dibab, Amiet and Nyala.'}}
};
function t(k){return T[LG][k];}
var M=D.months,N=M.length,CE=M.indexOf(D.ctrlEnd),WE=M.indexOf(D.wikiEnd),KX=Math.cos(15*Math.PI/180);
function mlab(m){var p=m.split('-');return t('months')[+p[1]-1]+' '+p[0];}
function ml(i){return mlab(M[i]);}
function P(lon,lat){return [(lon-21.5)*KX*40,(23.4-lat)*40];}
function css(v){return getComputedStyle(document.documentElement).getPropertyValue(v).trim();}
var COL={s:css('--saf'),r:css('--rsf'),p:css('--spl'),l:css('--slm'),o:css('--oth'),u:css('--none')},INK=css('--ink'),PAPER=css('--paper'),MUTED=css('--muted'),RULE=css('--rule'),GRID=css('--grid'),G2='#b9bcc2',G3='#8c9099';
function num(n){return Math.round(n).toLocaleString(LG==='fr'?'fr-FR':'en-GB');}
function dec(n,d){var s=n.toFixed(d==null?1:d);return LG==='fr'?s.replace('.',','):s;}
function nm(n){return t('towns')[n]||n;}
function fill(s,o){return s.replace(/\{(\w+)\}/g,function(_,k){return o[k];});}
function pct(){return LG==='fr'?' %':'%';}
function wOf(el){return Math.max(280,Math.round(el.clientWidth||el.parentNode.clientWidth||700));}
function tx(x,y,s,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-size="'+(o.size||12)+'" fill="'+(o.fill||MUTED)+'"'+(o.anchor?' text-anchor="'+o.anchor+'"':'')+(o.bold?' font-weight="600"':'')+(o.halo?' stroke="'+PAPER+'" stroke-width="3" paint-order="stroke"':'')+'>'+s+'</text>';}
var ROADS=[[[37.19,19.58],[33.98,17.70],[32.56,15.50]],[[32.48,15.65],[30.37,13.70],[30.22,13.18]],[[30.22,13.18],[28.43,12.70],[26.14,13.60],[25.35,13.62]],[[30.22,13.18],[29.65,12.05],[29.71,11.01]],[[22.20,13.47],[22.45,13.45],[23.47,12.91],[24.88,12.05]],[[32.56,15.50],[33.54,14.39],[33.63,13.55],[34.36,11.79]],[[30.22,13.18],[32.66,13.16],[33.63,13.55]],[[24.88,12.05],[25.35,13.62]],[[28.43,12.70],[27.81,11.32]]];
/* points d'entree : depart, arrivee, camp servi, 1 si ferme ou rapporte */
var ENTRY=[[[22.83,16.07],[24.6,14.3],'r',1],[[24.6,21.6],[25.2,15.2],'r',0],[[31.3,21.9],[31.8,19.4],'s',0],[[38.3,19.9],[37.3,19.6],'s',0]];
var NB=[[30.5,22.9],[22.9,21.2],[21.9,15.2],[22.6,9.9],[30.5,8.9],[36.6,11.2],[37.6,15.6]];
var cen={};D.a2.forEach(function(a){cen[a.pc]=a.c;});
var bigPc={};(function(){var c={};D.a2.forEach(function(a){c[a.pc]=(c[a.pc]||0)+1;});for(var k in c)if(c[k]>1)bigPc[k]=1;})();
var uid=0;
/* Carte. Les tailles de texte sont calculees pour faire 12 px au moins a l'ecran, quelle que soit la largeur. */
function draw(el,o){
  var i=o.i,ci=Math.min(i,CE),b=o.box,x0=-14,y0=40,w=700,h=560;
  if(b){var a=P(b[0],b[3]),c=P(b[2],b[1]);x0=a[0];y0=a[1];w=c[0]-a[0];h=c[1]-a[1];}
  var W=wOf(el),u=w/W,k=w/700,id='h'+(o.id||(++uid)),s=[],small=W<480;
  s.push('<svg viewBox="'+[x0,y0,w,h].map(function(v){return v.toFixed(1);}).join(' ')+'" role="img" aria-label="'+(o.title||t('mapAria'))+', '+ml(i)+'"><defs><pattern id="'+id+'" width="'+(6*u)+'" height="'+(6*u)+'" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="'+(6*u)+'" height="'+(6*u)+'" fill="'+COL.s+'"/><rect width="'+(3*u)+'" height="'+(6*u)+'" fill="'+COL.r+'"/></pattern></defs>');
  s.push('<rect x="'+x0+'" y="'+y0+'" width="'+w+'" height="'+h+'" fill="'+PAPER+'"/>');
  D.a2.forEach(function(a){var c=a.s[ci];if(c==='u'){s.push('<path d="'+a.d+'" fill="'+COL.u+'" stroke="'+PAPER+'" stroke-width="'+(.5*u)+'"/>');return;}
    var op=o.fade?.3:(bigPc[a.pc]?.45:(c==='x'?.6:.8));
    s.push('<path d="'+a.d+'" fill="'+(c==='x'?'url(#'+id+')':COL[c])+'" fill-opacity="'+op+'" stroke="'+PAPER+'" stroke-opacity=".7" stroke-width="'+(.5*u)+'"/>');});
  D.a1.forEach(function(a){s.push('<path d="'+a.d+'" fill="none" stroke="'+INK+'" stroke-opacity=".4" stroke-width="'+(.6*u)+'"/>');});
  s.push('<path d="'+D.outline+'" fill="none" stroke="'+INK+'" stroke-opacity=".9" stroke-width="'+(1*u)+'"/>');
  if(o.nb&&!small){NB.forEach(function(n,j){var p=P(n[0],n[1]);s.push('<text x="'+p[0]+'" y="'+p[1]+'" font-size="'+(12*u)+'" fill="'+MUTED+'" letter-spacing="'+(1*u)+'">'+t('nb')[j]+'</text>');});}
  var lab=[];
  if(o.road){
    ROADS.forEach(function(r){s.push('<polyline points="'+r.map(function(q){return P(q[0],q[1]).join(',');}).join(' ')+'" fill="none" stroke="'+INK+'" stroke-opacity=".8" stroke-width="'+(1.2*u)+'" stroke-dasharray="'+(4*u)+' '+(3*u)+'"/>');});
    if(!b){ENTRY.forEach(function(e,j){var a=P(e[0][0],e[0][1]),c=P(e[1][0],e[1][1]);s.push('<line x1="'+a[0]+'" y1="'+a[1]+'" x2="'+c[0]+'" y2="'+c[1]+'" stroke="'+COL[e[2]]+'" stroke-width="'+(3*u)+'"'+(e[3]?' stroke-dasharray="'+(3*u)+' '+(3*u)+'"':'')+'/><circle cx="'+c[0]+'" cy="'+c[1]+'" r="'+(4*u)+'" fill="'+COL[e[2]]+'" stroke="'+PAPER+'" stroke-width="'+u+'"/>');
      var right=j===3,parts=t('entry')[j].split(', ');
      parts.forEach(function(pt,q){lab.push('<text x="'+(a[0]+(right?-6:6)*u)+'" y="'+(a[1]+(j===0?-20:(j===3?-8:16))*u+q*14*u)+'" '+(right?'text-anchor="end" ':'')+'font-size="'+(12*u)+'" font-weight="'+(q?400:600)+'" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(3*u)+'" paint-order="stroke">'+pt+'</text>');});});}
  }
  if(o.fight){D.acled[i].forEach(function(e){var c=cen[e[0]];if(c&&e[2]>0)s.push('<circle cx="'+c[0]+'" cy="'+c[1]+'" r="'+(Math.sqrt(e[2])*1.1*k)+'" fill="'+INK+'" fill-opacity=".1" stroke="'+INK+'" stroke-opacity=".85" stroke-width="'+(.8*u)+'"/>');});}
  var names=o.names||[],F=t('facts'),maxN=small?(o.maxSmall||4):99;
  D.towns.forEach(function(tw){
    var c=tw.s[ci];if(c==='u')return;
    if(b){var q=tw.p;if(q[0]<x0||q[0]>x0+w||q[1]<y0||q[1]>y0+h)return;}
    var ni=names.indexOf(tw.n),big=ni>=0&&ni<maxN,r=(big?4:(o.dots===false?0:1.6))*u;if(!r)return;
    var bs=tw.b[ci];
    if(o.siege&&bs==='2')s.push('<circle cx="'+tw.p[0]+'" cy="'+tw.p[1]+'" r="'+(r+4*u)+'" fill="none" stroke="'+INK+'" stroke-width="'+(1.4*u)+'" stroke-dasharray="'+(3*u)+' '+(2*u)+'"/>');
    else if(o.siege&&bs==='1')s.push('<circle cx="'+tw.p[0]+'" cy="'+tw.p[1]+'" r="'+(r+4*u)+'" fill="none" stroke="'+INK+'" stroke-width="'+(1*u)+'" stroke-dasharray="'+(1*u)+' '+(2.4*u)+'"/>');
    s.push('<circle cx="'+tw.p[0]+'" cy="'+tw.p[1]+'" r="'+r+'" fill="'+(c==='x'?PAPER:COL[c])+'" stroke="'+(big?INK:PAPER)+'" stroke-width="'+((big?1.2:.4)*u)+'"/>');
    if(big){var left=(tw.p[0]-x0)>w*.7||tw.n==='Tawila',xx=tw.p[0]+(left?-(r+4*u):(r+4*u)),an=left?' text-anchor="end"':'',f=o.facts?F[tw.n+'|'+M[i]]:null,up=tw.n==='Omdurman'?-10*u:(tw.n==='Kosti'?10*u:0);
      lab.push('<text x="'+xx+'" y="'+(tw.p[1]+4*u+up)+'"'+an+' font-size="'+(13*u)+'" font-weight="600" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(3.2*u)+'" paint-order="stroke">'+nm(tw.n)+'</text>');
      if(f&&!(small&&ni>2))lab.push('<text x="'+xx+'" y="'+(tw.p[1]+18*u)+'"'+an+' font-size="'+(12*u)+'" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(3.2*u)+'" paint-order="stroke">'+f+'</text>');}
  });
  if(o.zones){[[33.4,17.7,'saf'],[24.4,10.9,'rsf']].forEach(function(z){var p=P(z[0],z[1]);lab.push('<text x="'+p[0]+'" y="'+p[1]+'" text-anchor="middle" font-size="'+(14*u)+'" font-weight="600" letter-spacing="'+(.6*u)+'" fill="'+INK+'" stroke="'+PAPER+'" stroke-width="'+(3.5*u)+'" paint-order="stroke">'+t(z[2]).toUpperCase()+'</text>');});}
  s.push(lab.join(''));s.push('</svg>');el.innerHTML=s.join('');
}
function legend(o){
  function sw(c,l){return '<span><i class="sw" style="background:'+c+'"></i>'+l+'</span>';}
  var h=sw(COL.s,t('saf'))+sw(COL.r,t('rsf'));
  if(o.spl)h+=sw(COL.p,t('spl'));if(o.slm)h+=sw(COL.l,t('slm'));
  h+='<span><i class="sw x"></i>'+t('mix')+'</span>'+'<span><i class="sw" style="background:'+COL.u+';border:1px solid '+RULE+'"></i>'+t('none')+'</span>';
  if(o.fight)h+='<span><i class="sw c" style="border:1px solid '+INK+';background:rgba(22,24,29,.1)"></i>'+t('lFight')+'</span>';
  if(o.road)h+='<span><i style="display:block;width:16px;border-top:2px dashed '+INK+'"></i>'+t('lRoad')+'</span>';
  if(o.siege)h+='<span><i class="sw c" style="border:1.5px dashed '+INK+'"></i>'+t('lSiege')+'</span><span><i class="sw c" style="border:1.5px dotted '+INK+'"></i>'+t('lPress')+'</span>';
  return h;
}
function frames(){
  uid=0;
  document.querySelectorAll('.frame').forEach(function(f){
    var d=f.dataset,i=M.indexOf(d.m),o={i:i,title:LG==='fr'?d.tfr:d.ten,box:d.box?d.box.split(',').map(Number):null,names:d.names?d.names.split(','):[],road:!!d.road,fight:!!d.fight,nb:!!d.nb,siege:!!d.siege,facts:!!d.facts,spl:!!d.spl,slm:!!d.slm,dots:!d.nodots,fade:!!d.fade,maxSmall:d.maxsmall?+d.maxsmall:4};
    f.innerHTML='<div class="map-h"><span class="map-d">'+ml(i)+(i>WE?t('ctrlNote'):'')+'</span></div><div class="fs"></div>'+(d.nolegend?'':'<div class="map-l">'+legend(o)+'</div>');
    draw(f.querySelector('.fs'),o);
  });
}
/* ---- graphiques : SVG en pixels reels, texte a 12 px au moins sur telephone ---- */
function yearTicks(months,x,H){var s='';months.forEach(function(m,j){if(m.slice(5)==='01')s+='<line x1="'+x(j)+'" x2="'+x(j)+'" y1="0" y2="'+H+'" stroke="'+GRID+'"/>';});return s;}
function yearLabs(months,x,y){var s='';months.forEach(function(m,j){if(m.slice(5)==='01')s+=tx(x(j)+3,y,m.slice(0,4));});return s;}
function stack(el,months,series,o){
  o=o||{};var W=wOf(el),H=o.h||220,padR=W<480?0:150,padT=o.ann?22:8,padB=20,n=months.length,iw=W-padR,ih=H-padT-padB;
  var tot=months.map(function(_,j){return series.reduce(function(a,s){return a+(s.v[j]||0);},0);}),mx=o.pct?1:Math.max.apply(null,tot)*1.05,e=o.until==null?n-1:o.until;
  function xl(j){return j*iw/n;}function x(j){return (j+.5)*iw/n;}function y(v){return padT+ih-v/mx*ih;}
  var s='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+(o.aria||'')+'">';
  var acc=months.map(function(){return 0;});
  series.forEach(function(se){
    var top=acc.map(function(a,j){return a+(o.pct?(tot[j]?(se.v[j]||0)/tot[j]:0):(se.v[j]||0));});
    if(o.bars){for(var j=0;j<=e;j++){var a=y(acc[j]),b=y(top[j]);s+='<rect x="'+(xl(j)+.5)+'" y="'+b+'" width="'+Math.max(1,iw/n-1)+'" height="'+Math.max(0,a-b)+'" fill="'+se.c+'"/>';}}
    else{var p='M';for(var j2=0;j2<=e;j2++)p+=(j2?'L':'')+x(j2).toFixed(1)+','+y(top[j2]).toFixed(1);for(j2=e;j2>=0;j2--)p+='L'+x(j2).toFixed(1)+','+y(acc[j2]).toFixed(1);s+='<path d="'+p+'Z" fill="'+se.c+'" stroke="'+PAPER+'" stroke-width="1"/>';}
    se.mid=y((acc[e]+top[e])/2);se.last=o.pct?(top[e]-acc[e]):se.v[e];acc=top;});
  s+=yearTicks(months,xl,padT+ih).replace(/stroke="[^"]+"/g,'stroke="'+PAPER+'" stroke-opacity=".6"');
  if(e<n-1)s+='<rect x="'+x(e)+'" y="'+padT+'" width="'+(iw-x(e))+'" height="'+ih+'" fill="'+GRID+'"/>';
  (o.ann||[]).forEach(function(a,q){var j=months.indexOf(a[0]);if(j<0)return;s+='<line x1="'+x(j)+'" x2="'+x(j)+'" y1="18" y2="'+(padT+ih)+'" stroke="'+INK+'" stroke-width="1"/><circle cx="'+x(j)+'" cy="10" r="9" fill="'+INK+'"/><text x="'+x(j)+'" y="14" text-anchor="middle" font-size="12" font-weight="600" fill="'+PAPER+'">'+(q+1)+'</text>';});
  s+=yearLabs(months,xl,H-5);
  function val(se){return se.last==null?'':' · '+(o.pct?Math.round(se.last*100)+pct():o.fmt(se.last));}
  if(padR){var ys=series.map(function(se){return se.mid+4;});for(var q=1;q<ys.length;q++)if(ys[q-1]-ys[q]<14)ys[q]=ys[q-1]-14;series.forEach(function(se,q){s+=tx(iw+8,ys[q],se.l+val(se),{fill:INK});});}
  s+='</svg>';
  if(!padR)s+='<div class="legend">'+series.map(function(se){return '<span><i style="background:'+se.c+'"></i>'+se.l+val(se)+'</span>';}).join('')+'</div>';
  if(o.ann&&o.ann.length)s+='<ol class="annl">'+o.ann.map(function(a){return '<li>'+a[1]+'</li>';}).join('')+'</ol>';
  el.innerHTML=s;
}
function lines(el,months,series,o){
  var W=wOf(el),H=o.h||220,padL=o.padL||34,padR=W<480?86:130,padT=o.ann?22:10,padB=20,n=months.length,iw=W-padL-padR,ih=H-padT-padB,e=o.until==null?n-1:o.until;
  function xl(j){return padL+j*iw/n;}function x(j){return padL+(j+.5)*iw/n;}
  function y(v){v=Math.max(o.min,Math.min(o.max,v));return o.log?padT+ih-(Math.log(v)-Math.log(o.min))/(Math.log(o.max)-Math.log(o.min))*ih:padT+ih-(v-o.min)/(o.max-o.min)*ih;}
  var s='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+(o.aria||'')+'">'+yearTicks(months,xl,padT+ih);
  o.ticks.forEach(function(v){s+='<line x1="'+padL+'" x2="'+(padL+iw)+'" y1="'+y(v)+'" y2="'+y(v)+'" stroke="'+(v===o.base?INK:GRID)+'" stroke-width="1"/>'+tx(padL-5,y(v)+4,(o.pre||'')+v,{anchor:'end'});});
  if(e<n-1)s+='<rect x="'+x(e)+'" y="'+padT+'" width="'+(padL+iw-x(e))+'" height="'+ih+'" fill="'+GRID+'" fill-opacity=".7"/>';
  (o.ann||[]).forEach(function(a,q){var j=months.indexOf(a[0]);if(j<0)return;s+='<line x1="'+x(j)+'" x2="'+x(j)+'" y1="18" y2="'+(padT+ih)+'" stroke="'+INK+'" stroke-width="1" stroke-dasharray="2 3"/><circle cx="'+x(j)+'" cy="10" r="9" fill="'+INK+'"/><text x="'+x(j)+'" y="14" text-anchor="middle" font-size="12" font-weight="600" fill="'+PAPER+'">'+(q+1)+'</text>';});
  series.forEach(function(se){var p='',pen=0,lj=-1;se.v.forEach(function(v,j){if(v==null||(o.log&&v<=0)||j>e){pen=0;return;}p+=(pen?'L':'M')+x(j).toFixed(1)+','+y(v).toFixed(1);pen=1;lj=j;});
    s+='<path d="'+p+'" fill="none" stroke="'+se.c+'" stroke-width="'+(se.main?2.5:1.5)+'" stroke-linejoin="round"/>';
    if(lj>=0)s+='<circle cx="'+x(lj)+'" cy="'+y(se.v[lj])+'" r="'+(se.main?4:3)+'" fill="'+se.c+'"/>'+tx(x(lj)+7,y(se.v[lj])+(se.dy||4),se.l+(se.end?' · '+se.end:''),{fill:INK,bold:se.main,halo:1});});
  s+=yearLabs(months,xl,H-5)+'</svg>';
  if(o.ann&&o.ann.length)s+='<ol class="annl">'+o.ann.map(function(a){return '<li>'+a[1]+'</li>';}).join('')+'</ol>';
  el.innerHTML=s;
}
function mini(el,vals,cur){var W=wOf(el),H=56,bw=W/vals.length,mx=Math.max.apply(null,vals),s='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'" aria-hidden="true">';
  vals.forEach(function(v,j){var hh=v/mx*H;s+='<rect x="'+(j*bw+.5)+'" y="'+(H-hh)+'" width="'+Math.max(1,bw-1)+'" height="'+hh+'" fill="'+(j===cur?INK:G2)+'"/>';});el.innerHTML=s+'</svg>';}
var FAT=D.nat.map(function(n){return n[1];}),CIV=D.nat.map(function(n){return n[2];}),IDP=D.idp.map(function(v){return v||0;});
var a1n={};D.a1.forEach(function(a){a1n[a.pc]=a.n;});
function regOf(n){if(n==='Khartoum')return 2;if(n==='Aj Jazirah'||n==='Sennar'||n==='White Nile')return 3;if(/Darfur/.test(n))return 1;if(/Kordofan/.test(n))return 0;if(n==='Blue Nile')return 4;return 5;}
var st={i:N-1,timer:null};
var sl=document.getElementById('slider'),pb=document.getElementById('play');sl.max=N-1;
function lastEv(i){var E=t('ev');for(var j=i;j>=0;j--){if(E[M[j]])return E[M[j]];}return '';}
function upd(){
  var i=st.i;sl.value=i;
  draw(document.getElementById('m-svg'),{i:i,id:'main',fight:true,nb:true,zones:i>=8,names:['Khartoum','Port Sudan','El Fasher','Nyala','El-Obeid','Wad Madani','Kadugli'],maxSmall:5,siege:true,title:t('mapAria')});
  document.getElementById('m-date').textContent=ml(i)+(i>WE?t('ctrlNote'):'');
  document.getElementById('m-leg').innerHTML=legend({fight:true,spl:true,slm:true,siege:true});
  document.getElementById('m-ev').innerHTML=lastEv(i);
  document.getElementById('m-fat').textContent=num(FAT[i])+t('inM')+ml(i);
  mini(document.getElementById('ch-fat'),FAT,i);
  pb.textContent=st.timer?t('pause'):t('play');
}
sl.addEventListener('input',function(){st.i=+sl.value;upd();});
function stop(){clearInterval(st.timer);st.timer=null;pb.textContent=t('play');}
pb.addEventListener('click',function(){if(st.timer){stop();return;}if(st.i>=N-1)st.i=0;st.timer=setInterval(function(){if(st.i>=N-1){stop();return;}st.i++;upd();},700);upd();});
function ticks(){var h='';M.forEach(function(m,j){if(m.slice(5)==='01')h+='<span style="left:'+(j/(N-1)*100)+'%">'+m.slice(0,4)+'</span>';});document.getElementById('sl-ticks').innerHTML=h;}
function charts(){
  var A=t('ann'),ann=Object.keys(A).map(function(k){return [k,A[k]];}),i,k,h;
  /* part des localites tenue par chaque camp */
  var sh=[[],[],[],[]];M.forEach(function(_,j){var c=[0,0,0,0];D.a2.forEach(function(a){var s=a.s[Math.min(j,CE)],q=s==='s'?0:s==='x'?1:(s==='r'||s==='p')?2:3;c[q]+=a.w;});c.forEach(function(v,q){sh[q].push(v);});});
  stack(document.getElementById('ch-share'),M,[{v:sh[0],c:COL.s,l:t('shareLab')[0]},{v:sh[1],c:G2,l:t('shareLab')[1]},{v:sh[2],c:COL.r,l:t('shareLab')[2]},{v:sh[3],c:COL.u,l:t('shareLab')[3]}],{pct:1,ann:ann,until:WE,h:250,aria:t('shareLab').join(', ')});
  /* solde cumule des villes */
  var net=[],cum=0;for(i=0;i<N;i++){if(i>0&&i<=WE)D.towns.forEach(function(tw){if(i-1<tw.f)return;var a=tw.s[i-1],c=tw.s[i];if(a===c||a==='u')return;if(c==='s')cum++;else if(c==='r'||c==='p')cum--;});net.push(cum);}
  var mn=Math.min.apply(null,net),mxn=Math.max.apply(null,net);
  lines(document.getElementById('ch-net'),M,[{v:net,c:INK,l:(net[WE]>0?'+':'')+net[WE],main:1}],{min:mn-3,max:mxn+3,ticks:[Math.ceil(mn/5)*5,0,Math.floor(mxn/5)*5].filter(function(v,q,a){return a.indexOf(v)===q;}),base:0,until:WE,ann:[ann[1],ann[3]],h:210,aria:t('netLab')});
  /* personnes tuees par mois, dont violences visant des civils */
  var dA=t('dAnn');
  (function(){var el=document.getElementById('ch-deaths'),W=wOf(el),H=240,padT=22,padB=20,ih=H-padT-padB,bw=W/N,mx=Math.max.apply(null,FAT)*1.08;
    var s='<svg width="'+W+'" height="'+H+'" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+t('miniFat')+'">'+yearTicks(M,function(j){return j*bw;},padT+ih);
    [1000,2000,3000].forEach(function(v){var yy=padT+ih-v/mx*ih;s+='<line x1="0" x2="'+W+'" y1="'+yy+'" y2="'+yy+'" stroke="'+GRID+'"/>'+tx(2,yy-3,num(v));});
    FAT.forEach(function(v,j){var h1=v/mx*ih,h2=CIV[j]/mx*ih;s+='<rect x="'+(j*bw+.5)+'" y="'+(padT+ih-h1)+'" width="'+Math.max(1,bw-1)+'" height="'+(h1-h2)+'" fill="'+G2+'"/><rect x="'+(j*bw+.5)+'" y="'+(padT+ih-h2)+'" width="'+Math.max(1,bw-1)+'" height="'+h2+'" fill="'+INK+'"/>';});
    FAT.forEach(function(v,j){var a=dA[M[j]];if(a)s+=tx(j*bw+bw/2,padT+ih-v/mx*ih-5,a,{fill:INK,bold:1,anchor:j<3?'start':(j>N-5?'end':'middle'),halo:1});});
    s+=yearLabs(M,function(j){return j*bw;},H-5)+'</svg>';
    el.innerHTML=s+'<div class="legend"><span><i style="background:'+INK+'"></i>'+t('dLeg')[0]+'</span><span><i style="background:'+G2+'"></i>'+t('dLeg')[1]+'</span></div>';})();
  /* part de chaque region dans les personnes tuees, par trimestre */
  (function(){var q=[],lab=[];for(var j=0;j<N;j+=3){var c=[0,0,0,0,0,0];for(var m=j;m<Math.min(N,j+3);m++)D.acled[m].forEach(function(e){c[regOf(a1n[e[0].slice(0,4)])]+=e[2];});q.push(c);lab.push(M[j]);}
    var cols=[INK,G3,G2,'#d2d4d9','#e2e3e7',GRID],R=t('reg');
    stack(document.getElementById('ch-reg'),lab,R.map(function(l,r){return {v:q.map(function(c){return c[r];}),c:cols[r],l:l};}),{pct:1,bars:1,h:220,aria:R.join(', ')});})();
  /* prix du sorgho rapporte a Port-Soudan, echelle logarithmique */
  (function(){var PR=D.extra.price,ps=PR.series['Port Sudan'],i0=PR.months.indexOf('2023-01'),pm=PR.months.slice(i0),MK=t('mk'),PA=t('pAnn');
    function ratio(mk){return PR.series[mk].slice(i0).map(function(v,j){var b=ps[i0+j];return v&&b?v/b:null;});}
    var fa=ratio('Al Fashir'),mxv=Math.max.apply(null,fa.map(function(v){return v||0;}));
    lines(document.getElementById('ch-price'),pm,[{v:ratio('El Geneina'),c:G2,l:MK['El Geneina'],dy:16},{v:ratio('El Obeid'),c:G3,l:MK['El Obeid'],dy:-6},{v:ratio('Kadugli'),c:G3,l:MK['Kadugli'],dy:5},{v:fa,c:INK,l:MK['Al Fashir'],end:'×'+Math.round(mxv),main:1}],{log:1,min:.5,max:130,ticks:[1,3,10,30,100],pre:'×',base:1,ann:Object.keys(PA).map(function(k){return [k,PA[k]];}),h:260,aria:t('ps')});})();
  /* drones : part par an, barres a 100 % */
  var y={};D.expl.forEach(function(e,i){var k=M[i].slice(0,4);y[k]=y[k]||[0,0];y[k][0]+=e[0];y[k][1]+=e[1];});h='<div class="hb">';
  for(k in y){var v=y[k],p=v[1]/v[0]*100;h+='<span>'+k+'</span><span class="bar100"><i style="width:'+p+'%;background:'+INK+'"></i><i style="flex:1;background:'+G2+'"></i></span><b>'+Math.round(p)+pct()+' '+t('drone')+' · '+v[0]+t('inc')+'</b>';}
  document.getElementById('ch-drone').innerHTML=h+'</div>';
  /* personnes deplacees par region d'accueil */
  (function(){var first=0;while(first<N&&!IDP[first])first++;var mm=M.slice(first),g=[[],[],[],[]];
    for(var j=first;j<N;j++){var c=[0,0,0,0],v=D.idp1[j]||{};for(var pc in v){var r=regOf(a1n[pc]);c[r===1?0:r===0?1:(r===2||r===3)?2:3]+=v[pc];}c.forEach(function(x,q){g[q].push(x);});}
    var cols=[INK,G3,G2,'#dcdee2'],L=t('idpReg');
    stack(document.getElementById('ch-idp'),mm,L.map(function(l,q){return {v:g[q],c:cols[q],l:l};}),{h:240,fmt:function(v){return dec(v/1e6)+t('M');},aria:L.join(', ')});})();
  /* financement */
  var F=D.extra.fts,mx=Math.max.apply(null,F.map(function(f){return f[1];}));h='<div class="hb">';
  F.forEach(function(f,q){var last=q===F.length-1,c=last?INK:G3;h+='<span>'+f[0]+(last?t('cur'):'')+'</span><span style="display:flex;width:'+(f[1]/mx*100)+'%;height:16px"><i style="width:'+(f[2]/f[1]*100)+'%;background:'+c+'"></i><i style="flex:1;background:repeating-linear-gradient(135deg,'+c+' 0 2px,transparent 2px 6px);outline:1px solid '+c+';outline-offset:-1px"></i></span><b>'+fill(t('fund'),{f:dec(f[2]/1e9,2),r:dec(f[1]/1e9,2),p:Math.round(f[2]/f[1]*100)})+'</b>';});
  document.getElementById('ch-fund').innerHTML=h+'</div>';
  /* tableau par Etat (annexe repliee) */
  var li=IDP.length-1;
  var rows=D.a1.filter(function(a){return D.ipc[a.pc];}).map(function(a){var c={s:0,r:0,p:0,l:0,o:0,x:0,u:0},n=0;D.a2.forEach(function(l){if(l.a1===a.pc){c[l.s[CE]]+=l.w;n+=l.w;}});var f=0;for(var i=N-12;i<N;i++)D.acled[i].forEach(function(e){if(e[0].slice(0,4)===a.pc)f+=e[2];});var ip=D.ipc[a.pc];return {n:a.n,c:c,t:n,ipc:ip['3+']/ip.all,idp:(D.idp1[li]||{})[a.pc]||0,f:f,o:D.extra.orgs[a.pc]||0};}).sort(function(x,y){return y.ipc-x.ipc;});
  var th=t('th');h='<thead><tr>'+th.map(function(x){return '<th>'+x+'</th>';}).join('')+'</tr></thead><tbody>';
  rows.forEach(function(r){var cb='';['s','x','r','p','l','o','u'].forEach(function(k){if(r.c[k])cb+='<i style="width:'+(r.c[k]/r.t*100)+'%;background:'+(k==='x'?'repeating-linear-gradient(135deg,'+COL.s+' 0 3px,'+COL.r+' 3px 6px)':COL[k])+'"></i>';});
   h+='<tr><td>'+(t('states')[r.n]||r.n)+'</td><td><span class="cb">'+cb+'</span></td><td class="n">'+Math.round(r.ipc*100)+pct()+'</td><td class="n">'+num(Math.round(r.idp/1000)*1000)+'</td><td class="n">'+num(Math.round(r.f/10)*10)+'</td><td class="n">'+r.o+'</td></tr>';});
  document.getElementById('tbl').innerHTML=h+'</tbody>';
}
function renderAll(){frames();charts();ticks();upd();}
function setLang(l,keep){LG=l;root.setAttribute('data-l',l);bf.setAttribute('aria-pressed',l==='fr');be.setAttribute('aria-pressed',l==='en');document.documentElement.lang=l;if(keep){try{localStorage.setItem('lang',l);}catch(e){}}renderAll();}
var l0='fr';try{l0=localStorage.getItem('lang')||l0;}catch(e){}
if(location.hash==='#en')l0='en';if(location.hash==='#fr')l0='fr';
bf.addEventListener('click',function(){setLang('fr',true);location.hash='fr';});be.addEventListener('click',function(){setLang('en',true);location.hash='en';});
window.addEventListener('hashchange',function(){if(location.hash==='#en'&&LG!=='en')setLang('en',false);if(location.hash==='#fr'&&LG!=='fr')setLang('fr',false);});
var rz=null,lastW=window.innerWidth;window.addEventListener('resize',function(){if(window.innerWidth===lastW)return;lastW=window.innerWidth;clearTimeout(rz);rz=setTimeout(renderAll,150);});
document.querySelectorAll('details').forEach(function(d){d.addEventListener('toggle',function(){if(d.open)renderAll();});});
setLang(l0,false);
})();
