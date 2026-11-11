# Genere index.html (FR + EN) a partir du contenu ci-dessous et de page.js / page.css.
# Lancer : python3 build_page.py
import json,html

U=dict(
 wiki="https://en.wikipedia.org/wiki/Module:2023_Sudanese_Clashes_detailed_map",
 acled_hdx="https://data.humdata.org/dataset/sudan-acled-conflict-data",
 dtm="https://data.humdata.org/dataset/sdn-iom-dtm-from-api",
 ipc="https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data",
 ii="https://data.humdata.org/dataset/sudan-violence-against-civilians-and-vital-civilian-facilities",
 cod="https://data.humdata.org/dataset/cod-ab-sdn",
 hapi="https://hapi.humdata.org/",
 fts="https://fts.unocha.org/countries/212/summary/2026",
 unhcr="https://www.unhcr.org/refugee-statistics/",
 repo="https://github.com/13w13/humanitarian-secondary-data",
 reuters_expl="https://www.timeslive.co.za/news/africa/2023-04-18-explainer-whats-behind-sudans-crisis/",
 sas="https://smallarmssurvey.org/sites/default/files/resources/SAS-HSBA-Briefing-Paper-2025-RSF-EN.pdf",
 euaa="https://euaa.europa.eu/coi/sudan/2025/security-situation/12-actors-conflict/121-major-state-and-non-state-armed-groups",
 acled_2y="https://acleddata.com/report/two-years-war-sudan-how-saf-gaining-upper-hand",
 acled_infight="https://acleddata.com/report/how-rsf-infighting-reshaping-war-sudan",
 acled_drone="https://acleddata.com/report/how-has-sudans-drone-war-adapted-shifting-supply-lines",
 acled_obeid="https://acleddata.com/expert-comment/can-rsf-seize-el-obeid",
 acled_saf="https://acleddata.com/expert-comment/can-safs-latest-advances-reshape-sudans-war",
 acled_bn="https://acleddata.com/expert-comment/why-has-blue-nile-become-new-flashpoint-sudans-war",
 gw="https://globalwitness.org/en/campaigns/conflict-resources/exposing-rsfs-secret-financial-network/",
 reuters_gezira="https://www.thestar.com.my/news/world/2024/08/09/unruly-rsf-fighters-sow-chaos-in-sudan039s-farming-heartland",
 swm_fuel="https://sudanwarmonitor.com/p/huge-fuel-explosion-rocks-sudan-chad",
 dab_darfur="https://www.dabangasudan.org/en?p=20060169",
 hrw_geneina="https://www.hrw.org/report/2024/05/09/massalit-will-not-come-home/ethnic-cleansing-and-crimes-against-humanity-el",
 dab_burhan="https://www.dabangasudan.org/en?p=20050348",
 aawsat_madani="https://english.aawsat.com/arab-world/4738706-sudanese-army-says-its-forces-have-withdrawn-wad-madani",
 sw_sennar="https://www.info-res.org/sudan-witness/reports/sudan-monthly-update-the-rsf-makes-strategic-gains-across-sennar-state-with-takeover-of-jebel-moya-and-sinja/",
 st_kikil="https://sudantribune.com/article/293682",
 palace="https://www.arabnews.com/node/2594885/middle-east",
 zamzam="https://news.un.org/en/story/2025/12/1166624",
 portsudan="https://www.al-monitor.com/originals/2025/05/paramilitaries-attack-port-sudan-first-time-army",
 triangle="https://www.aljazeera.com/news/2025/6/11/sudans-paramilitary-rsf-say-they-seized-key-zone-bordering-egypt-libya",
 swm_triangle="https://sudanwarmonitor.com/p/rsf-captures-libya-triangle",
 tasis="https://english.alarabiya.net/News/middle-east/2025/08/30/rsf-s-hemedti-sworn-in-as-head-of-parallel-sudanese-government",
 ohchr_fasher="https://sudan.un.org/sites/default/files/2026-02/2026-02-13-rsf-offensive-fasher-capture-1-en.pdf",
 un_fasher="https://news.un.org/en/story/2026/02/1166960",
 berm1="https://www.dabangasudan.org/en?p=20120348",
 berm2="https://www.dabangasudan.org/en?p=20120755",
 wfp_fasher="https://www.arabnews.pk/node/2610731",
 aj_ambaz="https://www.aljazeera.com/news/2025/8/6/why-are-people-in-sudans-el-fasher-starving",
 mee_fasher="https://www.middleeasteye.net/news/radio-silence-how-defence-sudans-el-fasher-collapsed-after-comms-blackout",
 swm_babanusa="https://sudanwarmonitor.com/p/babanusa-captured",
 aj_dilling="https://www.aljazeera.com/news/2026/1/27/sudan-army-says-nearly-two-year-rsf-siege-of-key-town-broken",
 aj_kadugli="https://www.aljazeera.com/news/2026/2/3/sudan-military-claims-to-break-siege-of-key-kordofan-city-of-kadugli",
 newarab_obeid="https://www.newarab.com/news/sudans-el-obeid-faces-el-fasher-repeat-amid-rsf-drone-strikes",
 fao_famine="https://www.fao.org/newsroom/detail/famine-conditions-confirmed-in-sudan-fasher-and-kadugli-as-hunger-and-malnutrition-ease-where-conflict-subsides/en",
 dab_mohajer="https://www.dabangasudan.org/en?p=20077684",
 nbc_iran="https://www.nbcnews.com/news/world/iran-drones-sudan-civil-war-army-rapid-support-forces-army-rcna147138",
 tb2="https://www.turkishminute.com/2025/03/08/turkeys-baykar-sent-120-mln-in-drones-and-missiles-to-sudanese-army-report/",
 akinci="https://www.al-monitor.com/originals/2026/02/egypts-drone-deployment-border-raises-stakes-sudans-civil-war",
 hrw_nyala="https://www.hrw.org/news/2025/06/04/sudan-armed-forces-airstrikes-south-darfur",
 ch95="https://www.timeslive.co.za/news/africa/2025-02-28-sudans-rsf-operating-drones-from-darfur-base-pictures-show/",
 delta="https://www.arabnews.pk/node/2615051",
 swm_bzk="https://sudanwarmonitor.com/p/sudans-rsf-acquires-new-drones-and",
 wotr="https://warontherocks.com/how-sudan-became-a-laboratory-for-drone-warfare-thanks-to-abu-dhabi/",
 ohchr_may="https://allafrica.com/stories/202605120004.html",
 dppa="https://dppa.un.org/en/node/136540",
 ohchr_oct="https://allafrica.com/stories/202610230644.html",
 newlines="https://newlinesmag.com/reportage/drones-are-reshaping-sudans-civil-war/",
 ap_grid="https://www.news4jax.com/news/world/2026/11/01/sudans-power-grid-nears-collapse-as-drone-strikes-blamed-on-rsf-target-electric-stations/",
 panel="https://sudanwarmonitor.com/p/full-text-un-panel-of-experts-report",
 amdjarass="https://www.newarab.com/news/uae-flights-flood-airstrip-un-says-supplies-weapons-sudan",
 kufra="https://capitalethiopia.com/2025/12/28/how-a-remote-airstrip-in-libya-reshaped-sudans-civil-war/",
 swm_libya="https://sudanwarmonitor.com/p/inside-the-rsfs-libya-supply-network",
 amnesty24="https://www.amnesty.org/en/latest/news/2024/07/new-weapons-fuelling-the-sudan-conflict/",
 amnesty25="https://www.amnesty.org/en/latest/news/2025/05/sudan-advanced-chinese-weaponry-provided-by-uae-identified-in-breach-of-arms-embargo-new-investigation/",
 chad="https://www.thenationalnews.com/news/mena/2026/02/23/chad-closes-frontier-with-sudan-after-five-of-its-soldiers-killed-in-clashes-in-border-town",
 murnei="https://dabangasudan.org/en?p=20098257",
 wfp_rain="https://www.wfp.org/stories/sudan-updates-floods-frustrate-flow-aid-amid-fears-typhoid-and-cholera-will-spread",
 un_bridges="https://news.un.org/en/story/2026/06/1167688",
 fews="https://fews.net/east-africa/sudan/key-message-update/may-2026",
 aj_gov="https://www.aljazeera.com/news/2026/1/11/sudan-announces-governments-return-to-khartoum-from-wartime-capital",
 dab_bara="https://www.dabangasudan.org/en?p=20129880",
 swm_bara="https://sudanwarmonitor.com/p/sudan-army-seizes-key-towns-in-bid-to-open-major-highway",
 aj_kurmuk="https://www.aljazeera.com/news/2026/8/13/sudan-army-says-rsf-advance-on-key-town-bordering-ethiopia",
 swm_sodari="https://sudanwarmonitor.com/p/rsf-suffers-another-defeat-in-north-kordofan",
 aj_mazroub="https://www.aljazeera.com/2026/10/2/sudans-army-says-it-captured-rsf-stronghold-in-north-kordofan",
 swm_nov="https://sudanwarmonitor.com/p/heavy-fighting-outside-el-obeid",
 aj_momentum="https://www.aljazeera.com/news/2026/10/4/is-the-sudanese-army-gaining-momentum-against-the-rsf",
 un_convoy="https://news.un.org/en/story/2026/09/1168251",
 aj_driver="https://www.aljazeera.com/news/2026/10/4/air-strike-in-sudan-kills-un-aid-truck-driver-wfp",
 aj_feb="https://www.aljazeera.com/news/2026/2/7/un-us-condemn-rsf-drone-strikes-on-aid-deliveries-in-famine-hit-sudan",
 alkoma="https://www.unicef.org/sudan/press-releases/wfpunicef-humanitarian-aid-convoy-carrying-life-saving-supplies-attacked-sudans",
 sarho="https://www.timeslive.co.za/sunday-times-daily/africa/2025-03-26-sudans-rsf-squeezing-relief-supplies-as-famine-spreads-aid-workers-say/",
 adre="https://allafrica.com/stories/202610010081.html",
 msf_fasher="https://msf.lu/en/articles/soudan-un-mois-apres-la-prise-de-controle-del-fasher-par-les-fsr-la-situation-reste",
 tawila="https://www.aljazeera.com/news/2026/9/10/hundreds-of-thousands-lack-adequate-shelter-at-sudans-tawila-camp",
 unicef_ipc="https://www.unicef.org/press-releases/risk-famine-persists-nearly-195-million-people-face-acute-food-insecurity-sudan",
 iom_sep="https://news.fundsforngos.org/2026/09/23/5-million-sudanese-return-amid-crisis-iom/",
 un_idp="https://news.un.org/en/story/2025/03/1161611",
 quad="https://www.globalsecurity.org/military/library/news/2025/09/mil-250912-state03.htm",
 dab_quad="https://www.dabangasudan.org/en?p=20134749",
 acaps_access="https://www.acaps.org/fileadmin/Data_Product/Main_media/20260322_ACAPS_Sudan_-_Analysis_of_humanitarian_access_in_the_Darfur_and_Kordofan_regions__copy.pdf",
 acaps_risk="https://www.acaps.org/fileadmin/Data_Product/Main_media/20260513_ACAPS_Sudan_-_Risk_analysis__2026_.pdf",
 acled_eth="https://acleddata.com/expert-comment/why-rsf-targeting-civilian-infrastructure-drone-bases-ethiopia",
 acled_amiet="https://acleddata.com/expert-comment/amieth-market-drone-strikes-first-attack-sudans-war-began",
 acled_front="https://acleddata.com/expert-comment/where-sudans-frontline-moving-next",
 lex="https://www.youtube.com/watch?v=2hJkprFnzhY",
)
def a(k,t): return f'<a href="{U[k]}">{t}</a>'
TAGC=('<span class="tag">contesté</span>','<span class="tag">contested</span>')
TAG1=('<span class="tag">rapporté</span>','<span class="tag">reported</span>')

HEAD=dict(
 eyebrow=("Note d'analyse à partir de sources ouvertes · situation au 11 novembre 2026","Analytical note from open sources · situation as of 11 November 2026"),
 h1=("La guerre au Soudan, 2023 à 2026","The war in Sudan, 2023 to 2026"),
 src=(f"Sources principales : {a('wiki','carte de contrôle tenue par des contributeurs de Wikipedia')}, {a('acled_hdx','ACLED')} (Armed Conflict Location and Event Data) pour la violence, {a('dtm','matrice de suivi des déplacements de l’Organisation internationale pour les migrations')} (OIM DTM), {a('ipc','cadre intégré de classification de la sécurité alimentaire')} (IPC), {a('fts','service de suivi financier de l’ONU')} (FTS), analyses d'{a('acled_saf','ACLED')}, d'{a('acaps_risk','ACAPS')}, de {a('sas','Small Arms Survey')} et de {a('swm_nov','Sudan War Monitor')}. Les données sont téléchargées de HDX le 11 novembre 2026. La liste complète est en fin de page.",
      f"Main sources: the {a('wiki','control map kept by Wikipedia contributors')}, {a('acled_hdx','ACLED')} (Armed Conflict Location and Event Data) for violence, the {a('dtm','International Organization for Migration’s Displacement Tracking Matrix')} (IOM DTM), the {a('ipc','Integrated Food Security Phase Classification')} (IPC), the {a('fts','UN Financial Tracking Service')} (FTS), and analysis by {a('acled_saf','ACLED')}, {a('acaps_risk','ACAPS')}, {a('sas','Small Arms Survey')} and {a('swm_nov','Sudan War Monitor')}. Data downloaded from HDX on 11 November 2026. The full list is at the bottom of the page."),
 note=(f"Cette note accompagne des {a('lex','notes sur un entretien consacré à la guerre en Ukraine')}. Elle pose deux questions. Pourquoi se battent-ils ? Pourquoi cette guerre tue-t-elle autant de civils ?",
       f"This note is a companion to {a('lex','notes on an interview about the war in Ukraine')}. It asks two questions. Why are they fighting? Why does this war kill so many civilians?"),
)
WARN=(("Avertissement","Disclaimer"),[
 ("L'auteur travaille dans la gestion de l'information humanitaire. Il n'est pas analyste militaire. Cette note applique à des données ouvertes la grille de lecture d'analystes qui le sont. Elle peut se tromper.",
  "The author works in humanitarian information management and is not a military analyst. This note applies to open data the framework of analysts who are. It may be wrong."),
 ("Elle n'exprime pas la position de l'employeur de l'auteur, ni d'aucune organisation. Nommer les belligérants et colorer une carte ne vaut reconnaissance de rien.",
  "It does not express the position of the author's employer or of any organisation. Naming the belligerents and colouring a map recognises nothing."),
 ("Le contrôle territorial vient d'une carte tenue par des bénévoles. Elle suit environ 200 lieux et non des lignes de front. Les zones colorées sont une interprétation. Les premiers mois de 2023 reposent sur une vingtaine de villes.",
  "Territorial control comes from a map kept by volunteers. It tracks about 200 places, not front lines. The coloured areas are an interpretation. The first months of 2023 rest on about twenty towns."),
 ("Les deux camps annoncent plus qu'ils ne tiennent. Trois degrés de certitude sont employés. Un fait sans marque est établi par des sources indépendantes. Un fait <span class='tag'>rapporté</span> repose sur la parole d'un camp ou sur une seule source. Un fait <span class='tag'>contesté</span> oppose des sources qui divergent.",
  "Both sides announce more than they hold. Three degrees of certainty are used. A fact with no mark is established by independent sources. A <span class='tag'>reported</span> fact rests on one side's word or on a single source. A <span class='tag'>contested</span> fact sets sources against each other."),
 ("Les morts recensés par ACLED sont un minimum. Personne ne connaît le nombre réel. Les chiffres de déplacement, de faim et de financement sont ceux des agences qui les publient, à la date indiquée.",
  "Deaths recorded by ACLED are a minimum. Nobody knows the real number. Figures for displacement, hunger and funding are those of the agencies that publish them, at the date given."),
 ("Les affirmations datées ou chiffrées ont été vérifiées en ligne le 11 novembre 2026 et portent un lien. Certains articles, dont ceux du Sudan Tribune, n'ont pu être lus qu'en extrait. Ce qui n'a pas pu être vérifié a été retiré.",
  "Dated or numerical claims were checked online on 11 November 2026 and carry a link. Some articles, including Sudan Tribune's, could only be read as excerpts. What could not be verified was removed."),
 ("Transparence : note rédigée avec l'appui d'un modèle de langage, Claude (Anthropic, modèles Opus 5.5 et Fable 5.2), qui a aussi collecté les données, vérifié les sources et écrit le code des cartes.",
  "Transparency: note written with the support of a large language model, Claude (Anthropic, Opus 5.5 and Fable 5.2 models), which also collected the data, checked the sources and wrote the map code."),
])

SIDES=[
 ("saf",("L'armée soudanaise (SAF)","The Sudanese Armed Forces (SAF)"),
  (f"Chef : le général Abdel Fattah al-Burhan, qui préside aussi le Conseil de souveraineté. Une armée de métier, centralisée, avec des officiers, des usines d'armement, une aviation et un port. Son gouvernement siège à Port-Soudan depuis août 2023 et {a('aj_gov','a annoncé son retour à Khartoum le 11 janvier 2026')}.",
   f"Leader: General Abdel Fattah al-Burhan, who also chairs the Sovereignty Council. A professional, centralised army with an officer corps, arms factories, an air force and a port. Its government has sat in Port Sudan since August 2023 and {a('aj_gov','announced its return to Khartoum on 11 January 2026')}."),
  (f"Avec elle : une partie des anciens rebelles du Darfour, réunis dans la Force conjointe (Minni Minnawi, Jibril Ibrahim), des brigades islamistes dont al-Baraa ibn Malik, que Washington a classée terroriste en mars 2026, des civils mobilisés et, depuis {a('st_kikil','octobre 2024')}, le Bouclier du Soudan d'Abu Aqla Kikil, passé des RSF à l'armée. {a('euaa','Synthèse de l’agence européenne de l’asile')}.",
   f"With it: some of the former Darfur rebels, grouped in the Joint Force (Minni Minnawi, Jibril Ibrahim), Islamist brigades including al-Baraa ibn Malik, which Washington designated as terrorist in March 2026, mobilised civilians and, since {a('st_kikil','October 2024')}, Abu Aqla Kikil's Sudan Shield, which crossed over from the RSF. {a('euaa','EU Asylum Agency overview')}.")),
 ("rsf",("Les Forces de soutien rapide (RSF)","The Rapid Support Forces (RSF)"),
  (f"Chef : Mohamed Hamdan Dagalo, dit Hemedti. Les RSF descendent des milices arabes du Darfour, les janjawids, que l'État a armées à partir de 2003 puis régularisées en 2013. {a('acled_2y','ACLED')} les décrit comme une coalition de milices locales, où chacun obéit d'abord à son chef direct.",
   f"Leader: Mohamed Hamdan Dagalo, known as Hemedti. The RSF descend from the Arab militias of Darfur, the Janjaweed, which the state armed from 2003 and formalised in 2013. {a('acled_2y','ACLED')} describes them as a coalition of local militias in which each man answers first to his direct commander."),
  (f"Avec elles : le SPLM-N d'Abdelaziz al-Hilu, qui tient les monts Nouba. Ensemble ils ont formé un gouvernement parallèle, Tasis. {a('tasis','Hemedti a prêté serment à Nyala le 30 août 2025')}, al-Hilu est son adjoint.",
   f"With them: Abdelaziz al-Hilu's SPLM-N, which holds the Nuba Mountains. Together they formed a parallel government, Tasis. {a('tasis','Hemedti was sworn in at Nyala on 30 August 2025')}, with al-Hilu as deputy.")),
 ("slm",("Ceux qui ne sont d'aucun camp","Those on neither side"),
  ("Le mouvement d'Abdelwahid al-Nur (SLM-AW) tient le Jebel Marra, au Darfour, et se dit neutre. Des centaines de milliers de déplacés d'El Fasher s'y sont réfugiés, à Tawila surtout.",
   "Abdelwahid al-Nur's movement (SLM-AW) holds Jebel Marra in Darfur and calls itself neutral. Hundreds of thousands of people displaced from El Fasher have taken refuge there, mostly in Tawila."),
  ("Les civils qui avaient renversé Omar el-Béchir en 2019 n'ont pas d'armée. Ils n'apparaissent sur aucune carte de contrôle, y compris celle-ci.",
   "The civilians who brought down Omar al-Bashir in 2019 have no army. They appear on no control map, this one included.")),
 ("oth",("Les parrains","The backers"),
  (f"Les Émirats arabes unis sont accusés d'armer les RSF par le Tchad, la Libye et la Somalie. Le {a('panel','groupe d’experts de l’ONU')} a jugé ces accusations crédibles en janvier 2024. Abou Dhabi dément et parle de vols humanitaires.",
   f"The United Arab Emirates is accused of arming the RSF through Chad, Libya and Somalia. The {a('panel','UN Panel of Experts')} found the accusations credible in January 2024. Abu Dhabi denies it and speaks of relief flights."),
  (f"L'armée s'appuie sur l'Égypte, achète des {a('tb2','drones à la Turquie')} et en a reçu d'Iran selon {a('nbc_iran','Reuters et Bloomberg')}, ce que Khartoum a nié. Les quatre médiateurs du « Quad » comptent donc deux parrains, un dans chaque camp.",
   f"The army leans on Egypt, buys {a('tb2','drones from Turkey')} and received some from Iran according to {a('nbc_iran','Reuters and Bloomberg')}, which Khartoum denied. Two of the four 'Quad' mediators are backers, one on each side.")),
]

ORIG=(("D'où vient la guerre","Where the war comes from"),[
 ("2003",("Guerre du Darfour. Khartoum arme des milices arabes, les janjawids, contre les rébellions. Hemedti est l'un de leurs chefs.","War in Darfur. Khartoum arms Arab militias, the Janjaweed, against the rebellions. Hemedti is one of their commanders.")),
 ("2013",("Les janjawids deviennent les Forces de soutien rapide. Le régime s'en sert comme d'une garde contre sa propre armée.","The Janjaweed become the Rapid Support Forces. The regime uses them as a guard against its own army.")),
 ("2019",("Après des mois de manifestations, l'armée et les RSF renversent ensemble Omar el-Béchir. Un gouvernement de transition associe civils et militaires.","After months of protests, the army and the RSF together remove Omar al-Bashir. A transitional government pairs civilians with the military.")),
 ("2021",("Le 25 octobre, Burhan et Hemedti renversent ensemble ce gouvernement. Il ne reste que deux hommes armés au sommet de l'État.","On 25 October Burhan and Hemedti together overthrow that government. Two armed men are left at the top of the state.")),
 ("2022",("L'accord-cadre de décembre prévoit le retour des civils et l'intégration des RSF dans l'armée. L'armée veut la faire en deux ans, les RSF en dix. La question de savoir qui commanderait reste ouverte.","The December framework agreement provides for a return to civilian rule and for merging the RSF into the army. The army wants two years, the RSF ten. Who would command is left open.")),
 ("2023",(f"Le 15 avril, les combats éclatent à Khartoum, autour du quartier général, de l'aéroport et du palais. {a('reuters_expl','Chaque camp accuse l’autre d’avoir tiré le premier')}.","On 15 April fighting breaks out in Khartoum around army headquarters, the airport and the palace. "+a('reuters_expl','Each side accuses the other of firing first')+".")),
],("La guerre n'oppose donc pas un État à une rébellion. Elle oppose les deux moitiés d'un même appareil de sécurité, qui se sont partagé le pouvoir puis disputé la suite. Le Darfour y ajoute vingt ans de violences entre communautés, que les RSF ont reprises à leur compte.",
   "So the war does not pit a state against a rebellion. It pits two halves of one security apparatus against each other, after they shared power and then fought over what came next. Darfur adds twenty years of violence between communities, which the RSF took up as its own."))

KEY=[
 ("Pourquoi ils se battent. L'armée et les Forces de soutien rapide ont pris le pouvoir ensemble en 2021. Elles se battent depuis 2023 pour savoir laquelle des deux absorbera l'autre. Aucune ne défend un programme. Chacune défend sa place dans l'État et les revenus qui vont avec.",
  "Why they fight. The army and the Rapid Support Forces took power together in 2021. Since 2023 they have been fighting over which will absorb the other. Neither defends a programme. Each defends its place in the state and the revenue that goes with it."),
 ("Pourquoi autant de civils meurent. La guerre se mène dans les villes, par le siège et par le drone. Les combattants des RSF sont payés en butin. Plus d'un mort recensé sur trois a été tué dans une violence qui visait des civils.",
  "Why so many civilians die. The war is fought in towns, by siege and by drone. RSF fighters are paid in loot. More than one recorded death in three came from violence that targeted civilians."),
 ("Le pays est coupé en deux. L'armée tient le Nil, l'est et le centre. Les RSF tiennent presque tout le Darfour. Le Kordofan, entre les deux, est le théâtre où la guerre se joue en 2026.",
  "The country is cut in two. The army holds the Nile, the east and the centre. The RSF holds almost all of Darfur. Kordofan, in between, is where the war is being decided in 2026."),
 ("L'initiative a changé de camp par étapes. Au centre, l'armée a pris le dessus dès son offensive de septembre 2024. À l'ouest, les RSF ont avancé jusqu'en décembre 2025. Au Kordofan-Nord, l'impasse a duré jusqu'en juillet 2026. Les RSF ont répondu en ouvrant un front sur le Nil Bleu.",
  "The initiative changed hands in stages. In the centre the army gained the upper hand with its September 2024 offensive. In the west the RSF kept advancing until December 2025. In North Kordofan the stalemate lasted until July 2026. The RSF answered by opening a front in Blue Nile."),
 ("Une ville tombe quand ses routes sont coupées. Le siège est la méthode ordinaire des RSF. L'armée, elle, bloque les marchandises et les permis. À El Fasher en octobre 2025, le mois de la chute, trois kilos de sorgho coûtaient près de cent fois le prix de Port-Soudan.",
  "A town falls when its roads are cut. Siege is the RSF's ordinary method. The army blocks goods and permits instead. In El Fasher in October 2025, the month it fell, three kilos of sorghum cost nearly a hundred times the Port Sudan price."),
 ("En 2026, le drone a remplacé la colonne de pick-up comme arme qui tue le plus de civils. Selon le Haut-Commissariat aux droits de l'homme, plus de 80 % des morts civils recensés de janvier à avril 2026.",
  "In 2026 the drone replaced the pick-up column as the weapon that kills most civilians. According to the UN human rights office, more than 80% of recorded civilian deaths from January to April 2026."),
 ("Chaque camp revendique plus qu'il ne tient. Bara a changé de main trois fois en 2026, Kurmuk aussi. Un seul changement de camp postérieur à août 2026 a pu être confirmé par deux sources.",
  "Each side claims more than it holds. Bara changed hands three times in 2026, and so did Kurmuk. Only one change of control after August 2026 could be confirmed by two sources."),
 ("Les régions où l'on se bat sont celles où la faim est la plus grave et où l'aide passe le moins. Le plan de réponse 2026 est financé à moitié.",
  "The regions where the fighting is are those where hunger is worst and aid gets through least. The 2026 response plan is half funded."),
 ("Aucune trêve n'est en vigueur. Les deux camps sont réapprovisionnés de l'extérieur, et chacun pense que la prochaine saison sèche lui sera favorable.",
  "No truce is in force. Both sides are resupplied from outside, and each thinks the next dry season will go its way."),
]

def P(fr,en): return ('p',fr,en)
def MAP(tfr,ten,cfr,cen,**kw): return ('m',tfr,ten,cfr,cen,kw)
def CH(i,tfr,ten,cfr,cen): return ('c',i,tfr,ten,cfr,cen)
def RAW(h): return ('r',h)

S=[
 (("Quatre phases","Four phases"),[
  P(f"<b>2023, l'offensive des RSF.</b> Les combats partent de Khartoum et gagnent le Darfour. À El Geneina, des civils massalit sont tués par milliers selon {a('hrw_geneina','Human Rights Watch')}. Le groupe d'experts de l'ONU cite 10 000 à 15 000 morts. Burhan {a('dab_burhan','quitte son quartier général assiégé le 24 août')} et s'installe à Port-Soudan. À l'automne, les RSF prennent une à une les garnisons du Darfour : {a('dab_darfur','Nyala le 26 octobre, Zalingei le 31, Ardamata le 4 novembre, Ed Daein le 21')}. Le 18 décembre les RSF entrent dans {a('aawsat_madani','Wad Madani')}, deuxième ville du centre.",
    f"<b>2023, the RSF offensive.</b> Fighting starts in Khartoum and spreads to Darfur. In El Geneina, Masalit civilians are killed in their thousands according to {a('hrw_geneina','Human Rights Watch')}. The UN Panel of Experts cites 10,000 to 15,000 dead. Burhan {a('dab_burhan','leaves his besieged headquarters on 24 August')} and settles in Port Sudan. In the autumn the RSF takes the Darfur garrisons one after another: {a('dab_darfur','Nyala on 26 October, Zalingei on the 31st, Ardamata on 4 November, Ed Daein on the 21st')}. On 18 December the RSF enters {a('aawsat_madani','Wad Madani')}, the second city of the centre."),
  P(f"<b>2024, l'extension maximale.</b> En juin, les RSF prennent {a('sw_sennar','El Fula, le Jebel Moya puis Sinja')}. Elles encerclent El Fasher au printemps. La famine est confirmée dans le camp de Zamzam le 1er août. À l'automne le vent tourne. {a('acled_2y','ACLED')} date de l'offensive lancée le 26 septembre le moment où l'armée prend le dessus au centre. Elle reprend le Jebel Moya le 5 octobre, {a('st_kikil','Kikil change de camp le 20')}, elle reprend Sinja le 23 novembre.",
    f"<b>2024, maximum reach.</b> In June the RSF takes {a('sw_sennar','El Fula, Jebel Moya and then Sinja')}. It encircles El Fasher in the spring. Famine is confirmed in Zamzam camp on 1 August. In the autumn the wind turns. {a('acled_2y','ACLED')} dates the army's upper hand in the centre to the offensive launched on 26 September. It retakes Jebel Moya on 5 October, {a('st_kikil','Kikil changes sides on the 20th')}, and it retakes Sinja on 23 November."),
  P(f"<b>2025, l'armée reprend le centre, les RSF prennent l'ouest.</b> Wad Madani est reprise le 11 janvier, {a('palace','le palais présidentiel le 21 mars, l’aéroport le 26')}. Les RSF se retournent vers l'ouest. Elles attaquent le camp de Zamzam du 11 au 13 avril, où le Haut-Commissariat {a('zamzam','compte au moins 1 013 civils tués')}. Elles prennent En Nahud début mai, le {a('triangle','triangle frontalier avec la Libye et l’Égypte le 11 juin')}, El Fasher le 26 octobre, {a('swm_babanusa','Babanusa le 1er décembre et le champ pétrolier de Heglig le 8')}.",
    f"<b>2025, the army retakes the centre, the RSF takes the west.</b> Wad Madani is retaken on 11 January, {a('palace','the presidential palace on 21 March and the airport on the 26th')}. The RSF turns west. It attacks Zamzam camp from 11 to 13 April, where the UN human rights office {a('zamzam','counts at least 1,013 civilians killed')}. It takes En Nahud in early May, the {a('triangle','border triangle with Libya and Egypt on 11 June')}, El Fasher on 26 October, {a('swm_babanusa','Babanusa on 1 December and the Heglig oil field on the 8th')}."),
  P(f"<b>2026, le Kordofan.</b> L'armée annonce avoir rouvert la route de {a('aj_dilling','Dilling le 26 janvier')} et brisé le siège de {a('aj_kadugli','Kadugli le 3 février')} {TAG1[0]}. Elle prend {a('dab_bara','Bara le 5 mars, la perd le 16, la reprend le 25 juillet')}. {a('acled_saf','ACLED')} parle le 13 août de l'effondrement de l'encerclement d'El Obeid, après plus de dix-huit mois d'impasse, et juge que les RSF auront du mal à tenir trois fronts. Il décrit une troisième phase : l'armée vise le Kordofan-Ouest et le Darfour, les RSF se défendent au sol et frappent de loin les infrastructures. Les RSF et le SPLM-N répondent sur le Nil Bleu, où ils prennent {a('aj_kurmuk','Kurmuk le 13 août')}. ACLED y voit un {a('acled_bn','théâtre secondaire')} destiné à ralentir l'armée au Kordofan.",
    f"<b>2026, Kordofan.</b> The army announces it has reopened the road to {a('aj_dilling','Dilling on 26 January')} and broken the siege of {a('aj_kadugli','Kadugli on 3 February')} {TAG1[1]}. It takes {a('dab_bara','Bara on 5 March, loses it on the 16th, retakes it on 25 July')}. On 13 August {a('acled_saf','ACLED')} writes of the collapse of the encirclement of El Obeid after more than eighteen months of stalemate, and judges the RSF will struggle to hold three fronts. It describes a third phase: the army aims at West Kordofan and Darfur, while the RSF defends on the ground and strikes infrastructure from afar. The RSF and SPLM-N answer in Blue Nile, where they take {a('aj_kurmuk','Kurmuk on 13 August')}. ACLED sees a {a('acled_bn','secondary theatre')} meant to slow the army in Kordofan."),
  CH('ch-flip',"Villes suivies qui changent de camp, par mois","Tracked towns changing hands, by month",
     "Au-dessus de l'axe, les villes passées à l'armée. En dessous, celles passées aux RSF ou à leurs alliés. Les mois sans relevé de la carte source restent vides. Le compte ne porte que sur les villes déjà suivies le mois précédent.",
     "Above the axis, towns that went to the army. Below, those that went to the RSF or its allies. Months with no revision of the source map stay empty. Only towns already tracked the previous month are counted."),
  CH('ch-reg',"Où l'on meurt, mois par mois","Where people die, month by month",
     "Morts recensés par ACLED, par région, d'avril 2023 à octobre 2026. Les cinq lignes ont la même échelle. Le centre regroupe la Gezira, Sennar et le Nil Blanc. La guerre quitte Khartoum et le centre en 2025 et se concentre au Darfour puis au Kordofan.",
     "Deaths recorded by ACLED, by region, April 2023 to October 2026. The five rows share one scale. The centre groups Gezira, Sennar and White Nile. The war leaves Khartoum and the centre in 2025 and concentrates in Darfur, then Kordofan."),
  P(f"De septembre à novembre 2026, l'armée et la Force conjointe gardent l'initiative au Kordofan. Elles entrent à {a('swm_sodari','Sodari le 25 septembre')}, annoncent {a('aj_mazroub','Al-Mazroub le 2 octobre')} {TAG1[0]}, puis attaquent à l'ouest d'El Obeid à partir du 5 novembre. Vers le sud, la poussée ne tient pas. {a('swm_nov','Sudan War Monitor')} note que l'armée entre à Kazgeil le 5 novembre et que les RSF y reviennent le soir même. Au Darfour, aucune ville n'a changé de main dans les sources consultées. L'armée et la Force conjointe y tiennent encore Tina, à la frontière tchadienne, et {a('acled_front','ont repris des villages en juin et juillet')}.",
    f"From September to November 2026 the army and the Joint Force keep the initiative in Kordofan. They enter {a('swm_sodari','Sodari on 25 September')}, announce {a('aj_mazroub','Al-Mazroub on 2 October')} {TAG1[1]}, then attack west of El Obeid from 5 November. Southward the push does not hold. {a('swm_nov','Sudan War Monitor')} notes that the army enters Kazgeil on 5 November and the RSF is back the same evening. In Darfur no town changed hands in the sources consulted. The army and the Joint Force still hold Tina on the Chadian border there, and {a('acled_front','retook villages in June and July')}."),
 ]),
 (("Comment se battent les RSF","How the RSF fights"),[
  P(f"L'outil des RSF est le pick-up armé. {a('gw','Global Witness')} a retrouvé l'achat de plus de mille véhicules au premier semestre 2019, dont plus de 900 Toyota Hilux et Land Cruiser passés par des revendeurs émiriens. {a('swm_fuel','Sudan War Monitor')} parle de milliers de pick-up et d'une guerre de mouvement qui dépend du carburant de contrebande venu de Libye et du Tchad.",
    f"The RSF's tool is the armed pick-up. {a('gw','Global Witness')} traced the purchase of more than a thousand vehicles in the first half of 2019, over 900 of them Toyota Hilux and Land Cruisers bought through Emirati dealers. {a('swm_fuel','Sudan War Monitor')} speaks of thousands of pick-ups and a war of manoeuvre that depends on fuel smuggled from Libya and Chad."),
  P(f"Le recrutement passe par la <i>faza'a</i>, l'appel d'une communauté à prendre les armes sous un chef, l'<i>agid</i>, qui s'occupe aussi de l'intendance. Les combattants se rassemblent pour une opération puis se dispersent. Les soldes ont été réduites après 2023. Selon {a('sas','Small Arms Survey')}, le pillage est devenu une part nécessaire de la paie. Il règle aussi le tempo. Une zone prise est vidée, le butin repart vers le Darfour, et l'avance s'arrête le temps du transport. À la Gezira, {a('reuters_gezira','Reuters')} a trouvé des « marchés Dagalo » où se revendait le produit des razzias. Les RSF répondent que leurs hommes sont payés et que les pillards sont des éléments incontrôlés.",
    f"Recruitment runs through the <i>faza'a</i>, a community's call to arms under a leader, the <i>agid</i>, who also handles supplies. Fighters assemble for an operation and then disperse. Salaries were cut after 2023. According to {a('sas','Small Arms Survey')}, pillage became a necessary part of the wage. It also sets the tempo. A captured area is stripped, the loot travels back to Darfur, and the advance stops for as long as the haulage takes. In Gezira, {a('reuters_gezira','Reuters')} found 'Dagalo markets' where the proceeds of raids were resold. The RSF replies that its men are salaried and that looters are rogue elements."),
  MAP("Khartoum et la Gezira, décembre 2023","Khartoum and Gezira, December 2023",
      "Le 18 décembre 2023, les RSF entrent à Wad Madani. C'est leur plus grande avancée vers l'est. L'armée reprendra la ville le 11 janvier 2025.",
      "On 18 December 2023 the RSF enters Wad Madani. It is its furthest advance east. The army retakes the city on 11 January 2025.",
      m="2023-12",box="31.2,12.6,35.2,16.6",min="14"),
  P(f"Cette organisation va vite et se discipline mal. {a('acled_2y','ACLED')} attribue aux RSF 68 % des violences contre les civils recensées en deux ans de guerre, et décrit leurs assauts comme des attaques frontales en masse. Les fissures datent de 2024. En 2026 elles atteignent le noyau rizeigat, avec la défection de deux chefs mahamid. ACLED relève des {a('acled_infight','affrontements entre unités')}, des enlèvements de commerçants contre rançon, et 32 morts le 17 mars dans un combat entre miliciens nuer et misseriya du même camp.",
    f"This organisation moves fast and disciplines badly. {a('acled_2y','ACLED')} attributes to the RSF 68% of the violence against civilians recorded in two years of war, and describes its assaults as massed frontal attacks. The cracks date from 2024. In 2026 they reach the Rizeigat core, with the defection of two Mahamid commanders. ACLED records {a('acled_infight','clashes between units')}, traders kidnapped for ransom, and 32 dead on 17 March in a fight between Nuer and Misseriya militiamen on the same side."),
 ]),
 (("Le siège, méthode ordinaire","Siege, the ordinary method"),[
  P(f"Quand une ville résiste, on coupe ses routes. À El Fasher, les RSF ont commencé le 9 mai 2025 une levée de terre autour de la ville. Le laboratoire de Yale qui la suivait par satellite mesurait {a('berm1','plus de 31 km fin août')} et {a('berm2','38 km à la mi-septembre')}, avec deux brèches. Il a parlé d'une « kill box ».",
    f"When a town holds out, its roads are cut. At El Fasher the RSF began an earthen berm around the city on 9 May 2025. The Yale lab tracking it by satellite measured {a('berm1','more than 31 km in late August')} and {a('berm2','38 km by mid-September')}, with two gaps. It called it a 'kill box'."),
  P(f"Le {a('ohchr_fasher','rapport du Haut-Commissariat')} décrit le mécanisme. Toutes les routes principales étaient bloquées en août 2025. Aux sorties restantes, des barrages triaient et rançonnaient. Ceux qui tentaient d'apporter de la nourriture étaient arrêtés, parfois exécutés. La défense antiaérienne des RSF empêchait depuis la mi-2024 les parachutages de l'armée. Les cuisines collectives ont fermé. Les habitants ont mangé de l'<i>ambaz</i>, {a('aj_ambaz','le tourteau d’arachide destiné au bétail')}.",
    f"The {a('ohchr_fasher','UN human rights office report')} describes the mechanism. All main roads were blocked by August 2025. At the remaining exits, checkpoints screened and extorted. People trying to bring food in were detained, sometimes executed. RSF air defence had stopped army airdrops since mid-2024. Community kitchens closed. Residents ate <i>ambaz</i>, {a('aj_ambaz','the groundnut press-cake meant for livestock')}."),
  CH('ch-price',"Le prix du siège","The price of a siege",
     "Prix de détail de trois kilos de sorgho, rapporté au prix de Port-Soudan le même mois. Une barre à 1 signifie le même prix qu'à Port-Soudan. Chaque ligne a sa propre échelle. Les mois sans barre n'ont pas de relevé. À El Fasher la série s'arrête en octobre 2025. Données du PAM, via HDX HAPI.",
     "Retail price of three kilos of sorghum, relative to the Port Sudan price in the same month. A bar at 1 means the same price as Port Sudan. Each row has its own scale. Months with no bar have no reading. The El Fasher series stops in October 2025. WFP data, via HDX HAPI."),
  P(f"L'assaut final est parti le 21 octobre 2025 sur cinq axes. Les RSF ont pris la base de la 6e division le 26. D'après des combattants du camp vaincu interrogés par {a('mee_fasher','Middle East Eye')}, les radios et les téléphones satellite ont cessé de fonctionner cet après-midi-là. Le Haut-Commissariat a documenté {a('un_fasher','plus de 6 000 morts en trois jours')}, dont au moins 4 400 dans la ville et 1 600 sur les routes de sortie, près des levées de terre. Il juge le bilan réel bien supérieur.",
    f"The final assault began on 21 October 2025 along five axes. The RSF took the 6th Division base on the 26th. According to fighters from the defeated side interviewed by {a('mee_fasher','Middle East Eye')}, radios and satellite phones stopped working that afternoon. The UN human rights office documented {a('un_fasher','more than 6,000 killed in three days')}, at least 4,400 of them in the city and 1,600 on the exit routes, near the berms. It considers the real toll much higher."),
  MAP("Le Darfour après El Fasher","Darfur after El Fasher",
      "Novembre 2025. En violet, les zones du mouvement d'Abdelwahid al-Nur dans le Jebel Marra. Les tirets indiquent les axes de ravitaillement, tracés de façon schématique.",
      "November 2025. In purple, the areas of Abdelwahid al-Nur's movement in Jebel Marra. Dashes show supply routes, drawn schematically.",
      m="2025-11",box="21.6,9.4,28.2,17.2",min="10",road="1"),
  P(f"El Fasher n'est pas un cas isolé. Babanusa a tenu près de deux ans. La 22e division y a perdu son ravitaillement aérien quand {a('swm_babanusa','un Il-76 a été abattu')}, un mois avant la chute. Kadugli était assiégée depuis le début de la guerre. À El Obeid, encerclée au nord, à l'ouest et au sud jusqu'en juillet 2026, {a('newarab_obeid','le carburant arrivait en jerricans')}. La famine a été confirmée à Zamzam en août 2024, puis à {a('fao_famine','El Fasher et Kadugli en novembre 2025')}. Ces lieux étaient assiégés. Dans les sources lues, l'armée n'assiège pas de villes. {a('acaps_access','ACAPS')} décrit de son côté un autre outil : l'interdiction, fin 2025, de faire entrer des marchandises dans les zones tenues par les RSF.",
    f"El Fasher is not an isolated case. Babanusa held for nearly two years. The 22nd Division there lost its air resupply when {a('swm_babanusa','an Il-76 was shot down')}, a month before the fall. Kadugli had been besieged since the start of the war. In El Obeid, encircled to the north, west and south until July 2026, {a('newarab_obeid','fuel arrived in jerry cans')}. Famine was confirmed in Zamzam in August 2024, then in {a('fao_famine','El Fasher and Kadugli in November 2025')}. These places were besieged. In the sources read, the army does not besiege towns. {a('acaps_access','ACAPS')} describes a different tool on its side: the ban, in late 2025, on goods entering RSF-held areas."),
 ]),
 (("Comment se bat l'armée","How the army fights"),[
  P(f"En 2023 l'armée a perdu la capitale faute d'infanterie. Elle l'a compensé en mobilisant des civils et des brigades islamistes, en ralliant les anciens rebelles du Darfour puis Kikil, et en achetant des drones. Bloomberg a signalé des Mohajer-6 iraniens en janvier 2024. Un officier soudanais les a dits {a('dab_mohajer','décisifs dans la reprise de la radio-télévision d’Omdurman')} le 12 mars 2024. Le Washington Post a documenté un contrat d'environ {a('tb2','120 millions de dollars avec le turc Baykar')} pour des TB2. Reuters a repéré des {a('akinci','Akinci sur une base égyptienne')} à soixante kilomètres de la frontière.",
    f"In 2023 the army lost the capital for want of infantry. It made up for it by mobilising civilians and Islamist brigades, by rallying the former Darfur rebels and then Kikil, and by buying drones. Bloomberg reported Iranian Mohajer-6s in January 2024. A Sudanese officer called them {a('dab_mohajer','decisive in retaking the Omdurman broadcasting headquarters')} on 12 March 2024. The Washington Post documented a contract of about {a('tb2','120 million dollars with Turkey’s Baykar')} for TB2s. Reuters spotted {a('akinci','Akincis on an Egyptian base')} sixty kilometres from the border."),
  P("La reconquête du centre suit les routes. L'armée prend d'abord le Jebel Moya, ce qui coupe les RSF de Sennar de leurs arrières. Elle reprend ensuite Sinja, puis Wad Madani, puis Khartoum.",
    "The reconquest of the centre follows the roads. The army first takes Jebel Moya, which cuts the RSF in Sennar off from its rear. It then retakes Sinja, then Wad Madani, then Khartoum."),
  MAP("La reconquête du centre, mars 2025","Retaking the centre, March 2025",
      "Mars 2025. La même zone que la carte de décembre 2023, quinze mois plus tard.",
      "March 2025. The same area as the December 2023 map, fifteen months later.",
      m="2025-03",box="31.2,12.6,35.2,16.6",min="14"),
  P(f"Au Kordofan, l'armée s'en prend d'abord à ce qui protège les RSF du ciel et à ce qui les fait rouler. {a('acled_drone','ACLED')} compte sept destructions de batteries antiaériennes FK-2000 entre août 2025 et février 2026, une frappe sur un convoi venu de Libye le 15 mai 2026, et 70 frappes de l'armée en mai, dont 17 sur Nyala. En juillet, {a('swm_bara','Bara a été reprise par deux colonnes au sol')}. L'aviation largue aussi des bombes non guidées sur des villes tenues par les RSF. {a('hrw_nyala','Human Rights Watch')} l'a documenté à Nyala pour le 3 février 2025. L'armée dément viser des civils.",
    f"In Kordofan the army goes first for what shields the RSF from the air and what keeps it moving. {a('acled_drone','ACLED')} counts seven FK-2000 air-defence batteries destroyed between August 2025 and February 2026, a strike on a convoy from Libya on 15 May 2026, and 70 army strikes in May, 17 of them on Nyala. In July {a('swm_bara','Bara was retaken by two ground columns')}. The air force also drops unguided bombs on RSF-held towns. {a('hrw_nyala','Human Rights Watch')} documented it in Nyala for 3 February 2025. The army denies targeting civilians."),
 ]),
 (("La guerre des drones","The drone war"),[
  P(f"Du 4 au 9 mai 2025, des drones frappent {a('portsudan','Port-Soudan')} six jours de suite : la base aérienne, des dépôts de carburant, l'aéroport, une centrale. Les positions connues des RSF les plus proches étaient à environ 650 km, leurs bases du Darfour à 1 500 km. Les RSF n'ont pas revendiqué. Le 6 mai, {a('delta','Reuters et Yale')} voyaient à l'aéroport de Nyala treize drones à aile delta et seize lanceurs.",
    f"From 4 to 9 May 2025 drones hit {a('portsudan','Port Sudan')} six days running: the air base, fuel depots, the airport, a power station. The nearest known RSF positions were about 650 km away, its Darfur bases 1,500 km. The RSF did not claim the strikes. On 6 May {a('delta','Reuters and Yale')} saw thirteen delta-wing drones and sixteen launchers at Nyala airport."),
  P(f"Nyala est devenue la base de drones des RSF. Reuters y a vu des {a('ch95','CH-95 chinois dès décembre 2024')}. {a('swm_bzk','Sudan War Monitor')} y a identifié en mai 2026 un BZK-005 de 19 mètres d'envergure. En bas de l'échelle, les deux camps bricolent des quadricoptères qui lâchent des obus de mortier de 82 mm. Pour 2025, ACLED compte {a('newlines','environ 500 frappes de drones, 280 de l’armée et 200 des RSF')}, près de la moitié sur des cibles civiles. Elles ont tué au moins 2 670 personnes, combattants compris, sur plus de 17 000 morts du conflit recensés cette année-là. La semaine la plus meurtrière de la guerre reste un assaut au sol, celui d'El Fasher.",
    f"Nyala has become the RSF's drone base. Reuters saw {a('ch95','Chinese CH-95s there from December 2024')}. In May 2026 {a('swm_bzk','Sudan War Monitor')} identified a BZK-005 with a 19-metre wingspan. At the bottom of the range, both sides rig quadcopters to drop 82 mm mortar bombs. For 2025 ACLED counts {a('newlines','about 500 drone strikes, 280 by the army and 200 by the RSF')}, nearly half on civilian targets. They killed at least 2,670 people, combatants included, out of more than 17,000 conflict deaths recorded that year. The deadliest week of the war remains a ground assault, the one on El Fasher."),
  CH('ch-drone',"Incidents avec armes explosives touchant des civils ou des services, par an","Explosive-weapon incidents affecting civilians or services, by year",
     "En orange, les incidents où l'arme a été lancée par drone. Données Insecurity Insight, 2026 jusqu'à octobre. Ce relevé ne couvre que les incidents touchant la santé, l'éducation, l'aide, l'eau ou l'alimentation.",
     "In orange, incidents where the weapon was launched by drone. Insecurity Insight data, 2026 to October. This record only covers incidents affecting health, education, aid, water or food."),
  P(f"Pour les civils, le résultat se compte. Le Haut-Commissariat a recensé {a('ohchr_may','au moins 880 civils tués par drone de janvier à avril 2026')}, plus de 80 % des morts civils de la période. Sur le semestre, l'ONU cite {a('dppa','environ 1 400 civils tués dont 1 100 par drone')}. En octobre 2026, trois marchés sont frappés en neuf jours. À Dibab le 18, le Haut-Commissariat compte {a('ohchr_oct','au moins 139 morts')}. À Amiet le 19, la mission de l'ONU à Abyei parle de plus de 80 morts et {a('acled_amiet','ACLED')} de 150 à 220. À Nyala le 26, les bilans vont de 21 à plus de 100 selon la source {TAGC[0]}. Les trois frappes sont attribuées à l'armée par des sources locales ou par des organisations de défense des droits.",
    f"For civilians the result can be counted. The UN human rights office recorded {a('ohchr_may','at least 880 civilians killed by drones from January to April 2026')}, more than 80% of civilian deaths in the period. For the half-year the UN cites {a('dppa','about 1,400 civilians killed, 1,100 of them by drones')}. In October 2026 three markets are hit in nine days. At Dibab on the 18th the human rights office counts {a('ohchr_oct','at least 139 dead')}. At Amiet on the 19th the UN mission in Abyei speaks of more than 80 dead and {a('acled_amiet','ACLED')} of 150 to 220. At Nyala on the 26th the tolls run from 21 to more than 100 depending on the source {TAGC[1]}. Local sources or rights groups attribute all three strikes to the army."),
  P(f"Les RSF visent le réseau électrique du nord. L'{a('ap_grid','Associated Press')} compte quinze sous-stations touchées depuis début octobre 2026, et une production tombée de 4 400 à 1 100 mégawatts depuis l'avant-guerre. L'attribution aux RSF vient du gouvernement et d'une organisation de juristes. {a('acled_eth','ACLED')} la reprend, compte 17 attaques en deux semaines et situe des bases de drones des RSF en Éthiopie.",
    f"The RSF targets the northern power grid. The {a('ap_grid','Associated Press')} counts fifteen substations hit since early October 2026, and output down from 4,400 to 1,100 megawatts since before the war. The attribution to the RSF comes from the government and a lawyers' group. {a('acled_eth','ACLED')} shares it, counts 17 attacks in two weeks and places RSF drone bases in Ethiopia."),
 ]),
 (("Routes, carburant, pluies","Roads, fuel, rain"),[
  P(f"Le Soudan fait plus de trois fois la France et compte peu de routes goudronnées. Les RSF dépendent de ce qui entre par l'ouest. Le {a('panel','groupe d’experts de l’ONU')} a décrit en janvier 2024 des cargaisons débarquées à Amdjarass, au Tchad, puis convoyées par camion. Reuters y a {a('amdjarass','vérifié 86 vols')}. Les Émirats parlent d'aide humanitaire. Après la prise du triangle frontalier, la route passe par {a('kufra','Koufra, en Libye')}, à 300 km de la frontière. L'armée accuse une brigade liée à Khalifa Haftar d'avoir participé à l'opération, ce que Haftar dément. Amnesty International a identifié chez les RSF des {a('amnesty25','bombes guidées et des obusiers chinois')}, très probablement réexportés par les Émirats.",
    f"Sudan is more than three times the size of France and has few paved roads. The RSF depends on what comes in from the west. In January 2024 the {a('panel','UN Panel of Experts')} described cargo landed at Amdjarass in Chad and then trucked onward. Reuters {a('amdjarass','verified 86 flights')} there. The UAE speaks of humanitarian aid. After the border triangle was taken, the route runs through {a('kufra','Kufra in Libya')}, 300 km from the border. The army accuses a brigade linked to Khalifa Haftar of taking part in the operation, which Haftar denies. Amnesty International identified {a('amnesty25','Chinese guided bombs and howitzers')} with the RSF, almost certainly re-exported by the UAE."),
  P(f"Ces routes bougent. Le Tchad a {a('chad','fermé sa frontière le 23 février 2026')} après la mort de cinq de ses soldats. ACLED note que l'approvisionnement des RSF {a('acled_drone','se déplace vers l’Éthiopie et la Centrafrique')}. Le 5 décembre 2025, un stock de carburant a explosé à {a('swm_fuel','Adikong, à la frontière tchadienne')}, après une frappe de drone que personne n'a revendiquée.",
    f"These routes shift. Chad {a('chad','closed its border on 23 February 2026')} after five of its soldiers were killed. ACLED notes that RSF supply is {a('acled_drone','moving toward Ethiopia and the Central African Republic')}. On 5 December 2025 a fuel stock blew up at {a('swm_fuel','Adikong on the Chadian border')} after a drone strike nobody claimed."),
  MAP("Axes et points d'entrée","Routes and entry points",
      "Tracés schématiques entre villes, à lire comme un plan de métro et non comme une carte routière.",
      "Schematic lines between towns, to be read like a metro map and not a road map.",
      m="2026-10",road="1",names="Port Sudan,Khartoum,El-Obeid,El Fasher,Nyala,El Geneina,Kadugli,Atbara,Ad-Damazin",nb="1",nofight="1"),
  P(f"De juin à octobre, la pluie décide du reste. En août 2024, la crue a emporté le {a('murnei','pont de Murnei')}, sur la route d'El Geneina. Le PAM avait alors {a('wfp_rain','plus de 50 camions et 4 800 tonnes bloqués')}. En juin 2026, l'ONU a signalé {a('un_bridges','deux ponts détruits entre Kadugli et Dilling')} et prévenu qu'il n'y aurait pas d'autre route une fois les pluies installées. {a('fews','FEWS NET')} prévoyait pour la saison moins d'offensives au sol et autant de drones sur les marchés. ACLED écrit que la percée d'El Obeid est intervenue juste avant les pluies, ce qui a laissé à l'armée le temps de s'installer.",
    f"From June to October the rain decides the rest. In August 2024 floods swept away the {a('murnei','Murnei bridge')} on the El Geneina road. WFP then had {a('wfp_rain','more than 50 trucks and 4,800 tonnes stuck')}. In June 2026 the UN reported {a('un_bridges','two bridges destroyed between Kadugli and Dilling')} and warned there would be no other route once the rains set in. {a('fews','FEWS NET')} forecast fewer ground offensives for the season and as many drones over markets. ACLED writes that the El Obeid breakthrough came just before the rains, which gave the army time to dig in."),
 ]),
 (("Le Kordofan, puis le Nil Bleu","Kordofan, then Blue Nile"),[
  P("Le Kordofan relie le Darfour des RSF au Nil de l'armée. El Obeid en est le verrou. Tant que les RSF l'encerclaient, elles menaçaient Omdurman. Depuis juillet 2026, la route est rouverte et l'armée pousse vers l'ouest, en direction d'En Nahud. Sudan War Monitor relevait le 7 novembre que les RSF tenaient encore tout le Kordofan-Ouest.",
    "Kordofan links the RSF's Darfur to the army's Nile. El Obeid is the lock. As long as the RSF encircled it, it threatened Omdurman. Since July 2026 the road has been open again and the army is pushing west toward En Nahud. On 7 November Sudan War Monitor noted that the RSF still held all of West Kordofan."),
  MAP("Le front du Kordofan","The Kordofan front",
      "Octobre 2026. Contrôle du 17 août, avec Sodari ajoutée à la main et Kazgeil passée en disputé. Un cercle en tirets signale une ville assiégée, un cercle en pointillé une pression d'un seul côté, d'après la carte source.",
      "October 2026. Control as of 17 August, with Sodari added by hand and Kazgeil moved to disputed. A dashed ring marks a besieged town, a dotted ring pressure from one side, according to the source map.",
      m="2026-10",box="26.6,9.2,33.2,15.2",min="8",road="1"),
  P(f"Au sud, rien n'est acquis. Les RSF ont recoupé la route de Dilling à Kadugli début mars. Le 30 août, {a('un_convoy','deux camions du PAM et 50 tonnes de vivres')} ont été détruits par une frappe aérienne près de Dilling. Le 3 octobre, {a('aj_driver','un chauffeur a été tué')} sur la même route. Sur le Nil Bleu, Kurmuk a été prise par les RSF et le SPLM-N le 23 mars, reprise par l'armée le 8 juillet, reprise par les RSF le 13 août. Le gouverneur de Kurmuk affirme que les assaillants sont partis du territoire éthiopien. ACLED tient le soutien éthiopien aux RSF pour établi depuis novembre 2025. {a('acaps_risk','ACAPS')} est plus prudent et rappelle le démenti d'Addis-Abeba. Khartoum a saisi le Conseil de sécurité le 28 octobre 2026. Depuis, plusieurs garnisons sur la route de Damazin font l'objet d'annonces contradictoires.",
    f"To the south nothing is settled. The RSF cut the Dilling to Kadugli road again in early March. On 30 August {a('un_convoy','two WFP trucks and 50 tonnes of food')} were destroyed by an air strike near Dilling. On 3 October {a('aj_driver','a driver was killed')} on the same road. In Blue Nile, Kurmuk was taken by the RSF and SPLM-N on 23 March, retaken by the army on 8 July, and retaken by the RSF on 13 August. The governor of Kurmuk says the attackers set out from Ethiopian territory. ACLED treats Ethiopian support for the RSF as established since November 2025. {a('acaps_risk','ACAPS')} is more cautious and recalls Addis Ababa's denial. Khartoum took the matter to the Security Council on 28 October 2026. Since then several garrisons on the Damazin road have been the subject of contradictory announcements."),
 ]),
 (("Revendiquer et tenir","Claiming and holding"),[
  P("La leçon de l'entretien sur l'Ukraine vaut ici. Contrôler, c'est pouvoir se servir d'un lieu. Au Soudan, une colonne peut entrer dans une ville, filmer la mairie et repartir avant la nuit. Le communiqué dira qu'elle est prise.",
    "The lesson of the Ukraine interview applies here. To control a place is to be able to use it. In Sudan a column can enter a town, film the town hall and leave before dark. The communiqué will say it has been taken."),
  CH('ch-top',"Les villes qui ont le plus souvent changé de statut","The towns that changed status most often",
     "Nombre de changements de couleur sur la carte source depuis le début du suivi de chaque ville.",
     "Number of colour changes on the source map since each town started being tracked."),
  P("Pour cette note, un changement de camp postérieur au dernier relevé de la carte n'a été retenu que si deux sources indépendantes le rapportaient comme un fait. Sur une quinzaine d'annonces de septembre à novembre 2026, une seule a passé ce filtre, Sodari, et de justesse. Une carte de contrôle du Soudan est un ordre de grandeur. Celle-ci aussi.",
    "For this note, a change of control later than the map's last revision was only accepted if two independent sources reported it as fact. Of some fifteen announcements between September and November 2026, only one passed that filter, Sodari, and barely. A control map of Sudan is an order of magnitude. So is this one."),
 ]),
 (("Ce que la guerre fait aux civils","What the war does to civilians"),[
  P("C'est la partie que les analyses militaires laissent de côté. Elle se lit sur les mêmes cartes.",
    "This is the part military analysis leaves out. It can be read on the same maps."),
  RAW('<div class="nums" id="nums"></div>'),
  P(f"Le nombre de déplacés internes a culminé en {a('un_idp','janvier 2025, à 11,5 millions')}, puis baissé. L'OIM comptait {a('iom_sep','8,58 millions de déplacés et 5,15 millions de retours')} fin août 2026. La baisse vient des retours vers Khartoum et la Gezira après leur reprise par l'armée. Elle ne dit rien de l'état des quartiers où les gens rentrent. Au Darfour et au Kordofan, le déplacement continue. {a('tawila','Tawila')} abrite environ 665 000 déplacés.",
    f"The number of internally displaced people peaked in {a('un_idp','January 2025 at 11.5 million')}, then fell. IOM counted {a('iom_sep','8.58 million displaced and 5.15 million returns')} at the end of August 2026. The fall comes from returns to Khartoum and Gezira after the army retook them. It says nothing about the state of the neighbourhoods people return to. In Darfur and Kordofan displacement continues. {a('tawila','Tawila')} shelters about 665,000 displaced people."),
  MAP("Où sont les déplacés","Where the displaced are",
      "Août 2026. Chaque cercle rose est proportionnel au nombre de personnes déplacées accueillies dans l'État.",
      "August 2026. Each pink circle is proportional to the number of displaced people hosted in the state.",
      m="2026-08",idp="1",nofight="1",names="Khartoum,El Fasher,Nyala,El-Obeid,Port Sudan"),
  CH('ch-ref',"Réfugiés et demandeurs d'asile soudanais à l'étranger","Sudanese refugees and asylum seekers abroad",
     "Stock en fin d'année, HCR. Les années 2021 et 2022 donnent le niveau d'avant-guerre.",
     "Year-end stock, UNHCR. 2021 and 2022 give the pre-war level."),
  P(f"La faim suit le siège. Pour février à mai 2026, l'IPC classe {a('unicef_ipc','près de 19,5 millions de personnes en insécurité alimentaire aiguë')}. Il ne confirme plus de famine, mais signale un risque dans quatorze zones.",
    f"Hunger follows siege. For February to May 2026 the IPC classifies {a('unicef_ipc','nearly 19.5 million people as acutely food insecure')}. It no longer confirms famine but flags a risk in fourteen areas."),
  ('c2','tbl',"Contrôle, faim, déplacement, violence et présence humanitaire, État par État","Control, hunger, displacement, violence and humanitarian presence, state by state",
     "Contrôle en octobre 2026, en part des localités de l'État. IPC phase 3 ou plus, février à mai 2026. Déplacés accueillis au 31 août 2026. Morts recensés par ACLED de novembre 2025 à octobre 2026. Organisations déclarant une activité de janvier à juillet 2026, d'après le 3W d'OCHA. Une organisation présente ne signifie pas un besoin couvert.",
     "Control in October 2026, as a share of the state's localities. IPC phase 3 or above, February to May 2026. Displaced people hosted on 31 August 2026. Deaths recorded by ACLED from November 2025 to October 2026. Organisations reporting activity from January to July 2026, from OCHA's 3W. An organisation present does not mean a need met."),
  P("Le tableau montre ce que les cartes disent séparément. Les États où plus de la moitié de la population a faim sont ceux que les RSF tiennent ou que les deux camps se disputent. Ce sont aussi ceux où l'on meurt le plus.",
    "The table shows what the maps say separately. The states where more than half the population is hungry are those the RSF holds or the two sides dispute. They are also where most people die."),
 ]),
 (("L'aide : accès et argent","Aid: access and money"),[
  P(f"L'accès dépend de qui tient la route. Le poste d'Adré, à la frontière tchadienne, fonctionne par {a('adre','autorisations de trois mois')} délivrées depuis Port-Soudan. La dernière court du 1er octobre au 31 décembre 2026. Côté RSF, une agence parallèle, la SARHO, exige depuis fin 2024 que les organisations s'enregistrent auprès d'elle. Celles qui le font risquent l'expulsion par Port-Soudan. D'après {a('sarho','Reuters')}, la part des ONG signalant des retards de permis vers les zones RSF est passée de 20 ou 30 % à 60 % en janvier 2025. Le 28 janvier 2026, le gouvernement a menacé de poursuites les organisations qui coopéreraient avec la SARHO, puis retiré des licences de téléphone satellite, d'après {a('acaps_access','ACAPS')}. Le Tchad a fermé sa frontière fin février 2026. L'état réel du passage depuis n'a pas pu être vérifié. ACAPS estime aussi que les données venant des zones RSF sont trop minces et que les besoins y sont sans doute sous-estimés.",
    f"Access depends on who holds the road. The Adré crossing on the Chadian border runs on {a('adre','three-month authorisations')} issued from Port Sudan. The latest runs from 1 October to 31 December 2026. On the RSF side a parallel agency, SARHO, has demanded since late 2024 that organisations register with it. Those that do risk expulsion by Port Sudan. According to {a('sarho','Reuters')}, the share of NGOs reporting permit delays into RSF areas rose from 20 or 30% to 60% in January 2025. On 28 January 2026 the government threatened legal action against organisations cooperating with SARHO, then withdrew satellite phone licences, according to {a('acaps_access','ACAPS')}. Chad closed its border in late February 2026. The actual state of the crossing since then could not be verified. ACAPS also assesses that data from RSF areas are too thin and that needs there are probably underestimated."),
  P(f"Les convois sont devenus des cibles. Dans la nuit du 2 juin 2025, {a('alkoma','un convoi de quinze camions du PAM et de l’UNICEF')} est attaqué à Al Koma, à 1 800 km de Port-Soudan. Cinq morts. Personne ne revendique. En 2026 les attaques se déplacent au Kordofan : {a('aj_feb','la route d’El Obeid à Kosti le 6 février')}, Dilling le 30 août, Dilling encore le 3 octobre. Le PAM comptait huit attaques aériennes contre ses opérations de janvier à août. À El Fasher, {a('msf_fasher','aucune agence n’était présente un mois après la chute')}. La première visite de l'ONU a eu lieu le 26 décembre 2025. Depuis 2023, <span class='aidk'></span> travailleurs humanitaires ont été tués selon Insecurity Insight.",
    f"Convoys have become targets. On the night of 2 June 2025 {a('alkoma','a fifteen-truck WFP and UNICEF convoy')} was attacked at Al Koma, 1,800 km from Port Sudan. Five dead. Nobody claimed it. In 2026 the attacks move to Kordofan: {a('aj_feb','the El Obeid to Kosti road on 6 February')}, Dilling on 30 August, Dilling again on 3 October. WFP counted eight aerial attacks on its operations from January to August. In El Fasher {a('msf_fasher','no agency was present a month after the fall')}. The first UN visit took place on 26 December 2025. Since 2023, <span class='aidk'></span> aid workers have been killed according to Insecurity Insight."),
  CH('ch-fund',"Plan de réponse humanitaire : demandé et reçu","Humanitarian response plan: requested and received",
     "En milliards de dollars. La partie pleine est financée, la partie hachurée ne l'est pas. Données FTS (OCHA), relevées le 11 novembre 2026. L'année 2026 n'est pas close.",
     "In billions of dollars. The solid part is funded, the hatched part is not. FTS (OCHA) data, read on 11 November 2026. The year 2026 is not closed."),
  P("Le plan 2026 vise <span class='tgt'></span> millions de personnes sur <span class='pin'></span> millions dans le besoin. La demande a baissé d'un tiers par rapport à 2025. Dans le même temps, le nombre de personnes dans le besoin est passé de 30,4 à 33,7 millions.",
    "The 2026 plan targets <span class='tgt'></span> million people out of <span class='pin'></span> million in need. The request fell by a third from 2025. Over the same period the number of people in need rose from 30.4 to 33.7 million."),
 ]),
 (("Ce que chaque camp demande","What each side asks for"),[
  P(f"Le Quad réunit les États-Unis, l'Arabie saoudite, les Émirats et l'Égypte. Le {a('quad','12 septembre 2025')}, il a proposé une trêve humanitaire de trois mois, puis un cessez-le-feu permanent, puis une transition de neuf mois. D'après {a('dab_quad','Radio Dabanga')}, l'armée a donné en juillet 2026 un accord de principe assorti de réserves, dont le retrait des RSF des villes. Le 6 octobre 2026, Burhan a dit qu'il n'y aurait pas de négociation et qu'il reprendrait « chaque pouce ».",
    f"The Quad brings together the United States, Saudi Arabia, the UAE and Egypt. On {a('quad','12 September 2025')} it proposed a three-month humanitarian truce, then a permanent ceasefire, then a nine-month transition. According to {a('dab_quad','Radio Dabanga')}, in July 2026 the army gave agreement in principle with reservations, including RSF withdrawal from towns. On 6 October 2026 Burhan said there would be no negotiation and that he would retake 'every inch'."),
  P("On retrouve l'écart entre les buts et les moyens que Kofman décrit pour l'Ukraine. L'armée exige tout le pays et n'a repris aucune des capitales du Darfour. Les RSF veulent être reconnues comme un gouvernement et perdent du terrain au Kordofan. Tant que les livraisons continuent des deux côtés, la trêve n'a pas d'acheteur.",
    "The gap between ends and means that Kofman describes for Ukraine is here too. The army demands the whole country and has not retaken any of the Darfur state capitals. The RSF wants recognition as a government and is losing ground in Kordofan. As long as deliveries continue on both sides, the truce has no buyer."),
 ]),
]

MAN=json.load(open('manual_updates.json'))
def srcs(u): return ' '.join(f'<a href="{s}">[{i+1}]</a>' for i,s in enumerate(u['sources']))
KIND={'fix':("correction","correction"),'update':("mise à jour","update"),'contested':("contesté","contested")}
ST={'saf':("armée","army"),'rsf':("RSF","RSF"),'x':("disputé","disputed")}
MO_FR=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
MO_EN=['January','February','March','April','May','June','July','August','September','October','November','December']
def mo(m,i): y,k=m.split('-'); return ((MO_FR,MO_EN)[i])[int(k)-1]+' '+y
NOTE_EN={
 'Nyala':"The source map gives Nyala to the RSF from April to June 2023. The city was disputed: the army held the 16th Division base, which fell on 26 October 2023.",
 'Ed Daein':"The source map gives Ed Daein to the RSF from April 2023. The 20th Division garrison stayed in place until 21 November 2023, without fighting, under a local arrangement.",
 'Al Muthalathu':"Libya-Egypt border triangle. The army withdrew on 11 June 2025 and the RSF occupied it. The source map only shows it from January 2026.",
 'Sodari':"Army and Joint Force in the town on 25 September 2026. Sudan War Monitor geolocates their presence. Radio Tamazuj and Sudan Tribune report the announcement. Confirmation judged weak. The town is absent from the source map and has no colour before that date.",
 'Kazgeil':"The source map gives it to the army. Sudan War Monitor reports that the army entered on 5 November 2026 and the RSF returned the same evening. Early-November state, shown on the last month.",
}
NOTE_FR={
 'Nyala':"La carte source donne Nyala aux RSF d'avril à juin 2023. La ville était disputée : l'armée tenait la base de la 16e division, tombée le 26 octobre 2023.",
 'Ed Daein':"La carte source donne Ed Daein aux RSF dès avril 2023. La garnison de la 20e division est restée en place jusqu'au 21 novembre 2023, sans combats, par arrangement local.",
 'Al Muthalathu':"Triangle frontalier Libye-Égypte. L'armée s'en retire le 11 juin 2025, les RSF l'occupent. La carte source ne l'affiche qu'à partir de janvier 2026.",
 'Sodari':"Armée et Force conjointe dans la ville le 25 septembre 2026. Sudan War Monitor géolocalise leur présence. Radio Tamazuj et Sudan Tribune rapportent l'annonce. Confirmation jugée faible. Ville absente de la carte source, sans couleur avant cette date.",
 'Kazgeil':"La carte source la donne à l'armée. Sudan War Monitor rapporte que l'armée y entre le 5 novembre 2026 et que les RSF y reviennent le soir même. État de début novembre, affiché sur le dernier mois.",
}
def manual_list(i):
    o=[]
    for u in MAN['updates']:
        per=mo(u['from'],i)+((' → ' if True else '')+mo(u['to'],i) if u.get('to') else (' et après',' onward')[i])
        o.append(f"<li><b>{u['town']}</b>, {per}, {ST[u['status']][i]} <span class='tag'>{KIND[u['kind']][i]}</span>. {(NOTE_FR,NOTE_EN)[i][u['town']]} {srcs(u)}</li>")
    return "<ul class='small'>"+"".join(o)+"</ul>"

METH=[
 ((f"<b>Contrôle territorial.</b> {a('wiki','Carte détaillée de Wikipedia')}, un relevé par mois d'avril 2023 au 17 août 2026, licence CC BY-SA 4.0. Le module n'a pas été modifié depuis cette date, vérification faite le 11 novembre 2026. Les mois sans modification reprennent le mois précédent.",
   f"<b>Territorial control.</b> {a('wiki','Wikipedia detailed map')}, one snapshot a month from April 2023 to 17 August 2026, CC BY-SA 4.0. The module has not been edited since, as checked on 11 November 2026. Months with no edit repeat the previous month.")),
 (("<b>Des villes aux zones.</b> Une localité (admin2) prend la couleur majoritaire de ses villes suivies, pondérée par leur taille. Sans ville suivie, elle prend celle des trois villes les plus proches à moins de 250 km. Au-delà, elle reste sans couleur. Une ville n'a pas de couleur avant d'apparaître sur la carte source. Les localités désertiques de plus de 40 000 km² sont découpées autour de leurs villes, dans un rayon de 150 km. Le reste du désert est laissé sans relevé. C'est ce qui fait apparaître le triangle frontalier aux RSF sans leur attribuer tout le nord.",
   "<b>From towns to areas.</b> A locality (admin2) takes the majority colour of its tracked towns, weighted by size. With no tracked town, it takes that of the three nearest towns within 250 km. Beyond that it stays uncoloured. A town has no colour before it appears on the source map. Desert localities larger than 40,000 km² are split around their towns, within a 150 km radius. The rest of the desert is left with no reading. This is what shows the border triangle as RSF without giving it the whole north.")),
 (("<b>Corrections et ajouts à la main.</b> Ils sont dans le fichier <code>manual_updates.json</code>, avec leurs sources.","<b>Manual corrections and additions.</b> They are in the file <code>manual_updates.json</code>, with their sources.")),
 ('MANUAL',),
 (("<b>Annonces non retenues.</b> Al-Mazroub (armée, 2 octobre 2026), Umm Sumayma (5 novembre), Iyal Bakhit (7 et 8 novembre) et plusieurs garnisons du Nil Bleu reposent sur l'annonce d'un camp ou sur une seule source indépendante. Elles ne figurent pas sur la carte. Kurmuk et Qaysan étaient déjà aux RSF et au SPLM-N dans le relevé du 17 août, sans changement signalé depuis.",
   "<b>Announcements not applied.</b> Al-Mazroub (army, 2 October 2026), Umm Sumayma (5 November), Iyal Bakhit (7 and 8 November) and several Blue Nile garrisons rest on one side's announcement or on a single independent source. They are not on the map. Kurmuk and Qaysan were already RSF and SPLM-N in the 17 August snapshot, with no change reported since.")),
 ((f"<b>Données.</b> {a('cod','Limites COD-AB')} (OCHA). {a('acled_hdx','ACLED')}, agrégats mensuels par localité. {a('dtm','OIM DTM')}, série nationale et par État. {a('ipc','IPC')}, analyse valable de février à mai 2026. {a('ii','Insecurity Insight')}, armes explosives et travailleurs humanitaires. {a('hapi','HDX HAPI')} pour les prix du PAM, les besoins et le 3W. {a('fts','FTS')} pour le financement. {a('unhcr','HCR')} pour les réfugiés. Collecte par les scripts du dépôt {a('repo','humanitarian-secondary-data')}.",
   f"<b>Data.</b> {a('cod','COD-AB boundaries')} (OCHA). {a('acled_hdx','ACLED')}, monthly aggregates by locality. {a('dtm','IOM DTM')}, national and state series. {a('ipc','IPC')}, analysis valid February to May 2026. {a('ii','Insecurity Insight')}, explosive weapons and aid workers. {a('hapi','HDX HAPI')} for WFP prices, needs and 3W. {a('fts','FTS')} for funding. {a('unhcr','UNHCR')} for refugees. Collected with the scripts of the {a('repo','humanitarian-secondary-data')} repository.")),
 (("<b>Sources qui n'ont pas répondu.</b> ReliefWeb refuse l'identifiant de l'application sur ce poste. ACLED (événements détaillés), ACAPS et IDMC demandent une clé qui n'était pas configurée. WFP HungerMap ne publie pas le Soudan. Liveuamap a refusé la connexion. Les agrégats ACLED utilisés ici sont ceux publiés sur HDX.",
   "<b>Sources that did not respond.</b> ReliefWeb refuses the application identifier on this machine. ACLED (event-level data), ACAPS and IDMC require a key that was not configured. WFP HungerMap does not publish Sudan. Liveuamap refused the connection. The ACLED aggregates used here are those published on HDX.")),
 (("<b>Ce qui manque.</b> Les lignes de front réelles, le tracé exact des routes, un relevé du contrôle après le 17 août 2026, les effectifs des deux camps, et une lecture complète des articles du Sudan Tribune, qui bloque la lecture automatique.",
   "<b>What is missing.</b> Real front lines, the exact course of roads, a control snapshot after 17 August 2026, the strength of each side, and a full reading of Sudan Tribune articles, which block automated access.")),
]
FOOT=("Les désignations employées et la présentation des cartes n'impliquent aucune prise de position sur le statut d'un territoire ou le tracé d'une frontière. La frontière entre le Soudan et le Soudan du Sud n'est pas définitivement fixée, et le statut d'Abyei n'est pas déterminé. Données dérivées de Wikipedia sous licence CC BY-SA 4.0. Données ACLED reprises selon les conditions d'usage d'ACLED, avec attribution.",
      "The designations used and the presentation of the maps imply no position on the status of any territory or the course of any border. The border between Sudan and South Sudan is not finally settled, and the status of Abyei is not determined. Data derived from Wikipedia under CC BY-SA 4.0. ACLED data used under ACLED's terms of use, with attribution.")


# ---------- Chapitres ajoutes : les deux questions
WHY=(("Pourquoi ils se battent","Why they fight"),[
 ('tl',),
 P(f"Le motif immédiat est un calendrier. L'accord-cadre de décembre 2022 devait rendre le pouvoir aux civils et fondre les Forces de soutien rapide dans l'armée. L'armée voulait le faire en deux ans, les RSF en dix, et personne n'avait tranché la question du commandement. {a('reuters_expl','Les combats ont commencé avant la signature de l’accord final')}.",
   f"The immediate cause is a timetable. The December 2022 framework agreement was meant to hand power back to civilians and merge the Rapid Support Forces into the army. The army wanted two years, the RSF ten, and nobody had settled who would command. {a('reuters_expl','Fighting began before the final agreement was signed')}."),
 P(f"Le motif de fond est la place de chacun dans l'État. Pour Hemedti, l'intégration signifiait perdre une force autonome. Pour l'état-major, attendre dix ans signifiait garder une seconde armée à côté de la sienne. {a('acled_2y','ACLED')} ajoute un troisième acteur : les réseaux islamistes de l'ancien régime, qui avaient soutenu le coup d'État de 2021 et rejetaient l'accord-cadre.",
   f"The underlying cause is each side's place in the state. For Hemedti, integration meant losing an autonomous force. For the general staff, waiting ten years meant keeping a second army beside its own. {a('acled_2y','ACLED')} adds a third actor: the Islamist networks of the old regime, which had backed the 2021 coup and rejected the framework agreement."),
 P(f"La guerre dure pour d'autres raisons que celles qui l'ont déclenchée. Beaucoup de combattants des RSF ne se battent pas pour Hemedti. {a('sas','Small Arms Survey')} décrit des communautés mobilisées par leurs propres chefs, payées en butin et en droits de passage aux barrages. ACLED parle d'une {a('acled_infight','alliance transactionnelle')}. Au Darfour, la guerre a repris des conflits plus anciens entre communautés. Et les deux camps reçoivent de l'extérieur de quoi continuer.",
   f"The war goes on for reasons other than those that started it. Many RSF fighters are not fighting for Hemedti. {a('sas','Small Arms Survey')} describes communities mobilised by their own leaders and paid in loot and checkpoint levies. ACLED speaks of a {a('acled_infight','transactional alliance')}. In Darfur the war has taken up older conflicts between communities. And both sides receive from outside what they need to continue."),
 P("La guerre n'oppose donc pas un État à une rébellion. Elle oppose les deux moitiés d'un même appareil de sécurité, qui se sont partagé le pouvoir puis disputé la suite.",
   "So the war does not pit a state against a rebellion. It pits two halves of one security apparatus against each other, after they shared power and then fought over what came next."),
])
CIV=(("Pourquoi la guerre tue autant de civils","Why the war kills so many civilians"),[
 P(f"Sur 57 354 morts recensés par {a('acled_hdx','ACLED')} d'avril 2023 à octobre 2026, 20 398 ont été tués dans des violences qui visaient des civils. C'est plus d'un sur trois, et c'est un minimum. Cinq mécanismes l'expliquent. Les chapitres précédents les ont décrits un par un.",
   f"Of 57,354 deaths recorded by {a('acled_hdx','ACLED')} from April 2023 to October 2026, 20,398 came from violence that targeted civilians. That is more than one in three, and it is a minimum. Five mechanisms explain it. The chapters above described them one by one."),
 ('ol',[
  ("<b>La guerre se mène dans les villes.</b> Elle a commencé dans la capitale, entre deux forces casernées au milieu des habitants. D'avril à décembre 2023, Khartoum et le Darfour-Ouest comptent deux tiers des morts recensés.",
   "<b>The war is fought in towns.</b> It began in the capital, between two forces garrisoned among the residents. From April to December 2023, Khartoum and West Darfur account for two thirds of recorded deaths."),
  (f"<b>Le butin tient lieu de solde.</b> Une force payée par le pillage vit sur les civils. {a('acled_2y','ACLED')} attribue aux RSF 68 % des violences contre les civils. Au Darfour, le pillage se double d'un tri par communauté : {a('hrw_geneina','les Massalit à El Geneina en 2023')}, {a('zamzam','le camp de Zamzam en avril 2025')}, {a('un_fasher','El Fasher en octobre 2025')}.",
   f"<b>Loot stands in for pay.</b> A force paid by pillage lives off civilians. {a('acled_2y','ACLED')} attributes 68% of violence against civilians to the RSF. In Darfur, looting comes with sorting by community: {a('hrw_geneina','the Masalit in El Geneina in 2023')}, {a('zamzam','Zamzam camp in April 2025')}, {a('un_fasher','El Fasher in October 2025')}."),
  (f"<b>Le siège affame avant de tuer.</b> Les RSF coupent les routes, taxent ou arrêtent ceux qui apportent des vivres. La {a('fao_famine','famine a été confirmée')} à Zamzam, à El Fasher et à Kadugli, trois lieux assiégés.",
   f"<b>Siege starves before it kills.</b> The RSF cuts the roads and taxes or detains those who bring food. {a('fao_famine','Famine was confirmed')} in Zamzam, El Fasher and Kadugli, three besieged places."),
  (f"<b>Le drone frappe les marchés et presque rien ne l'arrête.</b> Les deux camps en ont. Selon {a('acled_drone','ACLED')}, l'armée intercepte environ 13 % des drones des RSF, et les RSF 2,3 % de ceux de l'armée. Le Haut-Commissariat aux droits de l'homme attribue aux drones {a('ohchr_may','plus de 80 % des morts civils')} de janvier à avril 2026.",
   f"<b>Drones hit markets and almost nothing stops them.</b> Both sides have them. According to {a('acled_drone','ACLED')}, the army intercepts about 13% of RSF drones, and the RSF 2.3% of the army's. The UN human rights office attributes {a('ohchr_may','more than 80% of civilian deaths')} from January to April 2026 to drones."),
  (f"<b>L'aide n'arrive pas là où l'on meurt.</b> Chaque camp contrôle les permis de l'autre côté de la ligne. Des convois sont frappés. Le plan de réponse 2026 est {a('fts','financé à moitié')}.",
   f"<b>Aid does not reach the places where people die.</b> Each side controls permits across the line. Convoys are hit. The 2026 response plan is {a('fts','half funded')}."),
 ]),
 P("Aucun de ces mécanismes n'est un accident de la guerre. Le siège, le pillage et la frappe de marchés sont les méthodes par lesquelles elle se mène.",
   "None of these mechanisms is an accident of the war. Siege, pillage and strikes on markets are the methods by which it is fought."),
])
S.insert(0,WHY)
ci=[k for k,(t,b) in enumerate(S) if t[0]=="Ce que la guerre fait aux civils"][0]
S[ci]=(("Déplacement et faim, en chiffres","Displacement and hunger, in figures"),[b for b in S[ci][1] if not (b[0]=='p' and b[1].startswith("C'est la partie"))])
S.insert(ci,CIV)

# ---------- Pieces : titre qui dit le constat, description, source, limite (charte Presse)
SRC=dict(
 ctrl=(f"{a('wiki','carte détaillée de Wikipedia')} (CC BY-SA 4.0), relevés mensuels jusqu'au 17 août 2026, et corrections manuelles décrites en méthode. Limites {a('cod','COD-AB')}, OCHA.",
       f"{a('wiki','Wikipedia detailed map')} (CC BY-SA 4.0), monthly snapshots to 17 August 2026, and manual corrections described under method. {a('cod','COD-AB')} boundaries, OCHA."),
 acled=(f"{a('acled_hdx','ACLED')}, agrégats mensuels par localité publiés sur HDX, avril 2023 à octobre 2026.",f"{a('acled_hdx','ACLED')}, monthly aggregates by locality published on HDX, April 2023 to October 2026."),
)
LIMCTRL=("Les surfaces sont une interprétation tirée d'environ 200 villes suivies. Elles surestiment le contrôle réel. Dans le désert, seul un rayon de 150 km autour d'une ville suivie est coloré.",
         "The areas are an interpretation drawn from about 200 tracked towns. They overstate real control. In the desert only a 150 km radius around a tracked town is coloured.")
META={
 'main':(("L'armée tient le Nil, les RSF tiennent le Darfour","The army holds the Nile, the RSF holds Darfur"),
   ("Camp qui tient les villes de chaque localité du Soudan, mois par mois, avril 2023 à octobre 2026. Cercles : morts recensés dans le mois. RSF : Forces de soutien rapide","Side holding the towns of each Sudanese locality, month by month, April 2023 to October 2026. Circles: deaths recorded in the month. RSF: Rapid Support Forces"),
   (SRC['ctrl'][0]+" Morts : ACLED. Déplacés : OIM DTM.",SRC['ctrl'][1]+" Deaths: ACLED. Displaced: IOM DTM."),
   (LIMCTRL[0]+" Après le 17 août 2026, seuls deux ajouts manuels apparaissent.",LIMCTRL[1]+" After 17 August 2026 only two manual additions appear.")),
 'ch-flip':(("Depuis septembre 2024, l'armée reprend plus de villes qu'elle n'en perd","Since September 2024 the army retakes more towns than it loses"),
   ("Villes suivies qui changent de camp chaque mois. Au-dessus de l'axe, passées à l'armée. En dessous, passées aux RSF ou à leurs alliés","Tracked towns changing hands each month. Above the axis, to the army. Below, to the RSF or its allies"),
   SRC['ctrl'],
   ("Le compte dépend du rythme des bénévoles : un mois sans mise à jour reste vide, et le suivant cumule. Seules les villes déjà suivies le mois précédent sont comptées. De septembre 2024 à décembre 2025, 29 villes passent à l'armée et 16 aux RSF.","The count depends on the volunteers' pace: a month with no update stays empty and the next one accumulates. Only towns already tracked the previous month are counted. From September 2024 to December 2025, 29 towns go to the army and 16 to the RSF.")),
 'ch-reg':(("La guerre a quitté Khartoum pour le Darfour, puis le Kordofan","The war left Khartoum for Darfur, then Kordofan"),
   ("Morts recensés par mois dans cinq régions, même échelle sur les cinq lignes. Centre : Gezira, Sennar et Nil Blanc","Deaths recorded per month in five regions, same scale on all five rows. Centre: Gezira, Sennar and White Nile"),
   SRC['acled'],
   ("Les morts recensés sont un minimum et dépendent de ce que les médias et les réseaux locaux peuvent rapporter. Les zones coupées du réseau sont sous-comptées. Sur les douze derniers mois, les trois Kordofan comptent 52 % des morts recensés.","Recorded deaths are a minimum and depend on what media and local networks can report. Areas cut off from the network are undercounted. Over the last twelve months the three Kordofan states account for 52% of recorded deaths.")),
 'ch-price':(("À El Fasher assiégée, le sorgho coûte cent fois plus cher","In besieged El Fasher sorghum costs a hundred times more"),
   ("Prix de détail de 3 kg de sorgho, divisé par le prix de Port-Soudan le même mois. Une barre à 1 vaut le prix de Port-Soudan. Chaque ligne a sa propre échelle","Retail price of 3 kg of sorghum, divided by the Port Sudan price in the same month. A bar at 1 equals the Port Sudan price. Each row has its own scale"),
   (f"Programme alimentaire mondial (PAM), relevés de marché via {a('hapi','HDX HAPI')}, janvier 2023 à septembre 2026.",f"World Food Programme (WFP), market monitoring via {a('hapi','HDX HAPI')}, January 2023 to September 2026."),
   ("Les mois sans barre n'ont pas de relevé. À El Fasher la série s'arrête en octobre 2025, mois où les RSF prennent la ville. Un prix relevé ne dit pas si la denrée est disponible.","Months with no bar have no reading. The El Fasher series stops in October 2025, the month the RSF took the city. A recorded price does not say whether the food is available.")),
 'ch-top':(("Bara et Dilling ont changé cinq fois de statut","Bara and Dilling changed status five times"),
   ("Nombre de changements de couleur sur la carte source depuis le début du suivi de chaque ville. La couleur est celle du camp qui tient la ville en octobre 2026","Number of colour changes on the source map since each town started being tracked. The colour is that of the side holding the town in October 2026"),
   SRC['ctrl'],
   ("Un changement de couleur reflète une modification faite par un bénévole, pas toujours un combat. Une ville prise et reperdue entre deux relevés mensuels n'est pas comptée.","A colour change reflects an edit by a volunteer, not always a battle. A town taken and lost again between two monthly snapshots is not counted.")),
 'ch-drone':(("En 2026, le drone lance quatre attaques explosives sur cinq","In 2026 drones launch four explosive attacks in five"),
   ("Incidents avec armes explosives touchant la santé, l'éducation, l'aide, l'eau ou l'alimentation, par an. En couleur, l'arme a été lancée par drone","Explosive-weapon incidents affecting health, education, aid, water or food, by year. In colour, the weapon was launched by drone"),
   (f"{a('ii','Insecurity Insight')}, via HDX, avril 2023 à octobre 2026.",f"{a('ii','Insecurity Insight')}, via HDX, April 2023 to October 2026."),
   ("Ce relevé ne couvre pas toutes les frappes, seulement celles qui touchent des services civils. L'année 2026 s'arrête en octobre.","This record does not cover all strikes, only those affecting civilian services. The year 2026 stops in October.")),
 'ch-ref':(("Le nombre de réfugiés soudanais a quadruplé depuis 2022","The number of Sudanese refugees has quadrupled since 2022"),
   ("Réfugiés et demandeurs d'asile originaires du Soudan, en millions, en fin d'année. 2021 et 2022 donnent le niveau d'avant-guerre","Refugees and asylum seekers from Sudan, in millions, at year end. 2021 and 2022 give the pre-war level"),
   (f"Haut-Commissariat des Nations unies pour les réfugiés ({a('unhcr','HCR')}), statistiques de population, fin 2025.",f"UN Refugee Agency ({a('unhcr','UNHCR')}), population statistics, end 2025."),
   ("Pas de chiffre consolidé pour 2026. Le total ne dit pas dans quel pays vivent ces personnes.","No consolidated figure for 2026. The total does not say which country these people live in.")),
 'ch-fund':(("Les bailleurs financent la moitié du plan de réponse 2026","Donors fund half of the 2026 response plan"),
   ("Plan de réponse humanitaire pour le Soudan, en milliards de dollars. Aplat : reçu. Hachures : demandé et non reçu","Humanitarian response plan for Sudan, in billions of dollars. Solid: received. Hatched: requested and not received"),
   (f"{a('fts','FTS')}, Bureau de la coordination des affaires humanitaires (OCHA), relevé le 11 novembre 2026.",f"{a('fts','FTS')}, UN Office for the Coordination of Humanitarian Affairs (OCHA), read on 11 November 2026."),
   ("L'année 2026 n'est pas close. Le montant demandé a baissé d'un tiers entre 2025 et 2026 : un taux de financement plus élevé ne signifie pas plus d'argent.","The year 2026 is not closed. The amount requested fell by a third between 2025 and 2026: a higher funding rate does not mean more money.")),
 'tbl':(("La faim est la plus forte au Darfour et au Kordofan","Hunger is worst in Darfur and Kordofan"),
   ("Par État : contrôle en octobre 2026 en part des localités, part de la population en insécurité alimentaire aiguë (IPC phase 3 ou plus, février à mai 2026), déplacés accueillis au 31 août 2026, morts recensés de novembre 2025 à octobre 2026, organisations déclarant une activité de janvier à juillet 2026","By state: control in October 2026 as a share of localities, share of the population acutely food insecure (IPC phase 3 or above, February to May 2026), displaced people hosted on 31 August 2026, deaths recorded from November 2025 to October 2026, organisations reporting activity from January to July 2026"),
   (f"Wikipedia, {a('ipc','IPC')}, {a('dtm','OIM DTM')}, {a('acled_hdx','ACLED')}, 3W d'OCHA via {a('hapi','HDX HAPI')}.",f"Wikipedia, {a('ipc','IPC')}, {a('dtm','IOM DTM')}, {a('acled_hdx','ACLED')}, OCHA 3W via {a('hapi','HDX HAPI')}."),
   ("Une organisation présente ne signifie pas un besoin couvert. ACAPS estime que les données venant des zones tenues par les RSF sont minces et que les besoins y sont sans doute sous-estimés.","An organisation present does not mean a need met. ACAPS assesses that data from RSF-held areas are thin and that needs there are probably underestimated.")),
 'nums':(None,None,
   (f"{a('dtm','OIM DTM')}, {a('unhcr','HCR')}, {a('ipc','IPC')}, plan de réponse 2026 via {a('hapi','HDX HAPI')}, {a('acled_hdx','ACLED')}.",f"{a('dtm','IOM DTM')}, {a('unhcr','UNHCR')}, {a('ipc','IPC')}, 2026 response plan via {a('hapi','HDX HAPI')}, {a('acled_hdx','ACLED')}."),
   ("Chaque chiffre a sa date et sa méthode. Ils ne s'additionnent pas.","Each figure has its own date and method. They do not add up.")),
}
MAPMETA={
 "Khartoum et la Gezira, décembre 2023":(("En décembre 2023, les RSF atteignent Wad Madani","In December 2023 the RSF reaches Wad Madani"),("Contrôle des localités autour de Khartoum et de la Gezira, décembre 2023. Cercles : morts recensés dans le mois","Control of localities around Khartoum and Gezira, December 2023. Circles: deaths recorded in the month")),
 "Le Darfour après El Fasher":(("Après El Fasher, les RSF tiennent les cinq capitales du Darfour","After El Fasher the RSF holds all five Darfur capitals"),("Contrôle des localités du Darfour, novembre 2025. Violet : mouvement d'Abdelwahid al-Nur. Tirets : axes de ravitaillement schématiques","Control of Darfur localities, November 2025. Purple: Abdelwahid al-Nur's movement. Dashes: schematic supply routes")),
 "La reconquête du centre, mars 2025":(("En mars 2025, l'armée a repris le centre du pays","By March 2025 the army had retaken the centre"),("La même zone que la carte de décembre 2023, quinze mois plus tard","The same area as the December 2023 map, fifteen months later")),
 "Axes et points d'entrée":(("Les RSF se ravitaillent par l'ouest, l'armée par la mer Rouge","The RSF is supplied from the west, the army from the Red Sea"),("Axes routiers et points d'entrée, tracés schématiques, sur le contrôle d'octobre 2026","Road axes and entry points, drawn schematically, over control in October 2026")),
 "Le front du Kordofan":(("Au Kordofan, l'armée avance vers l'ouest depuis El Obeid","In Kordofan the army advances west from El Obeid"),("Contrôle des localités du Kordofan, octobre 2026. Cercle en tirets : ville assiégée. Cercle en pointillé : pression d'un seul côté","Control of Kordofan localities, October 2026. Dashed ring: besieged town. Dotted ring: pressure from one side")),
 "Où sont les déplacés":(("Le Darfour accueille deux déplacés internes sur trois","Darfur hosts two in three internally displaced people"),("Personnes déplacées accueillies dans chaque État, en millions, 31 août 2026, sur la carte du contrôle","Displaced people hosted in each state, in millions, 31 August 2026, over the control map")),
}
UIW=dict(src=("Source.","Source."),lim=("Limite.","Limit."))
def cartel(src,lim):
    return "".join(f"<p class='cartel L {lg}' lang='{lg}'><span><b>{UIW['src'][i]}</b> {src[i]}</span><span><b>{UIW['lim'][i]}</b> {lim[i]}</span></p>" for i,lg in enumerate(('fr','en')))
def bi(tag,pair,cls=''):
    c=(' '+cls) if cls else ''
    return f'<{tag} class="L fr{c}" lang="fr">{pair[0]}</{tag}><{tag} class="L en{c}" lang="en">{pair[1]}</{tag}>'
def head(m): return (bi('p',m[0],'pt') if m[0] else '')+(bi('p',m[1],'sub') if m[1] else '')
def chap(t,tag='h3'): return '<div class="chap">'+bi(tag,t)+'</div>'
o=[]
o.append('<header>'+bi('span',HEAD['eyebrow'],'eyebrow')+bi('h1',HEAD['h1'])+bi('p',HEAD['src'],'src')+bi('p',HEAD['note'],'src')+'</header>')
o.append('<section class="warn">'+bi('h2',WARN[0])+'<ul>'+''.join(bi('li',w) for w in WARN[1])+'</ul></section>')
o.append('<section>'+chap(("Les belligérants","The belligerents"),'h2')+'<div class="sides">'+''.join(f'<div class="side s-{k}">'+bi('h3',t)+bi('p',p1)+bi('p',p2)+'</div>' for k,t,p1,p2 in SIDES)+'</div></section>')
o.append('<section>'+chap(("Points clés","Key points"),'h2')+'<ol class="key">'+''.join(bi('li',k) for k in KEY)+'</ol></section>')
MAIN="""<figure class="piece">"""+head(META['main'])+"""
  <div class="map" id="main">
    <div class="map-h"><span class="map-d" id="m-date"></span></div>
    <div id="m-svg"></div>
    <div class="map-l" id="m-leg"></div>
    <div class="player">
      <div class="ctl">
        <button type="button" id="play"></button>
        <input type="range" id="slider" min="0" value="0" aria-label="Mois / Month">
        <label><input type="checkbox" id="c-fight" checked> <span data-t="cFight"></span></label>
        <label><input type="checkbox" id="c-idp"> <span data-t="cIdp"></span></label>
        <label><input type="checkbox" id="c-road"> <span data-t="cRoad"></span></label>
      </div>
      <p class="ev" id="m-ev"></p>
      <div class="mini">
        <div><span><span data-t="miniFat"></span> · <b id="m-fat"></b></span><div id="ch-fat"></div></div>
        <div><span><span data-t="miniIdp"></span> · <b id="m-idp"></b></span><div id="ch-idp"></div></div>
      </div>
    </div>
  </div>"""+cartel(META['main'][2],META['main'][3])+'</figure>'
for n,(title,blocks) in enumerate(S):
    o.append('<section>'+chap(title))
    for b in blocks:
        if b[0]=='p': o.append(bi('p',(b[1],b[2])))
        elif b[0]=='tl': o.append('<div class="tl">'+''.join(f'<div class="tl-y"><b>{y}</b><div>'+bi('p',t)+'</div></div>' for y,t in ORIG[1])+'</div>')
        elif b[0]=='ol': o.append('<ol class="key">'+''.join(bi('li',k) for k in b[1])+'</ol>')
        elif b[0]=='r': o.append('<div class="piece">'+b[1]+cartel(META['nums'][2],META['nums'][3])+'</div>')
        elif b[0]=='m':
            kw=b[5]; d=' '.join(f'data-{k}="{v}"' for k,v in kw.items()); mm=MAPMETA[b[1]]
            o.append('<figure class="piece">'+head(mm)+f'<div class="map frame" data-tfr="{html.escape(mm[0][0],quote=True)}" data-ten="{html.escape(mm[0][1],quote=True)}" {d}></div>'+cartel(SRC['ctrl'],(b[3]+' '+LIMCTRL[0],b[4]+' '+LIMCTRL[1]))+'</figure>')
        elif b[0]=='c': m=META[b[1]]; o.append('<figure class="piece">'+head(m)+f'<div id="{b[1]}"></div>'+cartel(m[2],m[3])+'</figure>')
        elif b[0]=='c2': m=META[b[1]]; o.append('<figure class="piece">'+head(m)+f'<div class="tw"><table id="{b[1]}"></table></div>'+cartel(m[2],m[3])+'</figure>')
    o.append('</section>')
    if n==0: o.append('<section>'+MAIN+'</section>')
o.append('<section>'+chap(("Méthode et sources","Method and sources")))
for lg,i in (('fr',0),('en',1)):
    o.append(f'<ul class="L {lg} meth" lang="{lg}">')
    for m in METH:
        if m[0]=='MANUAL': o.append('<li style="list-style:none;margin-left:-1.1em">'+manual_list(i)+'</li>')
        else: o.append('<li>'+m[0][i]+'</li>')
    o.append('</ul>')
o.append('</section>')
o.append('<footer>'+bi('p',WARN[1][-1])+bi('p',FOOT)+'</footer>')

page=f'''<title>Soudan, la guerre en cartes</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="La guerre au Soudan de 2023 à 2026 : belligérants, façon de se battre, contrôle mois par mois, déplacement, faim, accès. Sources ouvertes. FR / EN.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,700;1,7..72,400&family=IBM+Plex+Sans+Condensed:wght@400;500;600&display=swap">
<style>
{open('page.css').read()}
</style>
<div class="wrap" id="root" data-l="fr">
<nav class="lang" aria-label="Langue / Language"><button type="button" id="b-fr" aria-pressed="true">Français</button><button type="button" id="b-en" aria-pressed="false">English</button></nav>
{chr(10).join(o)}
</div>
<script src="data.js"></script>
<script>
{open('page.js').read()}
</script>
'''
import re
page=re.sub(r'(\d) %',r'\1&nbsp;%',page).replace('« ','«&nbsp;').replace(' »','&nbsp;»')
open('index.html','w').write(page); print(len(page))
