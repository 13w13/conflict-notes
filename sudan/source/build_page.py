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
U.update(
 burhan_dignity="https://www.newarab.com/news/sudan-army-chief-rules-out-compromise-rsf-paramilitaries",
 hemedti_gov="https://www.dabangasudan.org/en/all-news/article/hemedti-sudan-government-of-peace-and-unity-to-issue-new-currency-and-ids",
 treasury23="https://home.treasury.gov/news/press-releases/jy1514",
 ifri="https://www.ifri.org/sites/default/files/2025-05/ifri_hogendoorn_revenue_sources_sudan_civil_war_2025.pdf",
 ap_powers="https://www.pbs.org/newshour/world/the-role-outside-powers-are-playing-in-sudans-continued-brutal-war",
 us_genocide="https://2021-2025.state.gov/genocide-determination-in-sudan-and-imposing-accountability-measures/",
 icc_fasher="https://www.icc-cpi.int/news/statement-icc-office-prosecutor-situation-el-fasher-north-darfur",
 icc_2026="https://www.dabangasudan.org/en?p=20134836",
 icj="https://www.icj-cij.org/case/197",
 ffm24="https://www.globalsecurity.org/military/library/news/2024/10/mil-241029-unhrc01.htm",
 ffm25="https://sudan.un.org/en/node/301357",
 turk_khartoum="https://www.ungeneva.org/en/news-media/news/2025/04/105021/sudan-crisis-turk-condemns-extrajudicial-killings-khartoum",
 tora="https://news.un.org/en/story/2025/03/1161571",
 treasury_burhan="https://home.treasury.gov/news/press-releases/jy2789",
 lshtm="https://www.voanews.com/a/death-toll-from-sudan-s-brutal-civil-war-far-exceeds-previous-estimates-study-suggests/7877242.html",
 unhcr_sit="https://data.unhcr.org/en/situations/sudansituation",
 embargo="https://www.thenationalnews.com/news/us/2026/10/08/un-sudan-arms-embargo/",
 quad_state="https://www.state.gov/releases/office-of-the-spokesperson/2025/09/joint-statement-on-restoring-peace-and-security-in-sudan/",
 rsf_truce="https://www.thenationalnews.com/news/2025/11/06/sudans-rsf-agrees-to-us-proposal-for-humanitarian-ceasefire",
 jeddah="https://2021-2025.state.gov/jeddah-declaration-of-commitment-to-protect-the-civilians-of-sudan/",
 somoud="https://www.aljazeera.com/features/2025/2/20/after-splinter-can-sudans-anti-war-coalition-reinvent-itself",
 pop="https://data.humdata.org/dataset/cod-ps-sdn",
 acled_eula="https://acleddata.com/eula",
)
REP=('<span class="tag">rapporté</span>','<span class="tag">reported</span>')
CON=('<span class="tag">contesté</span>','<span class="tag">contested</span>')

HEAD=dict(
 eyebrow=("Note d'analyse à partir de sources ouvertes · 11 novembre 2026","Analytical note from open sources · 11 November 2026"),
 h1=("La guerre au Soudan, 2023 à 2026","The war in Sudan, 2023 to 2026"),
 lede=("Cette note pose deux questions. Pourquoi l'armée soudanaise et les Forces de soutien rapide se battent-elles depuis avril 2023 ? Pourquoi cette guerre tue-t-elle autant de civils ?",
       "This note asks two questions. Why have the Sudanese army and the Rapid Support Forces been fighting since April 2023? Why does this war kill so many civilians?"),
 src=(f"Sources : carte de contrôle tenue par des contributeurs de Wikipédia, arrêtée au 17 août 2026 ; données d'{a('acled_hdx','ACLED')}, de l'Organisation internationale pour les migrations, du cadre de classification de la sécurité alimentaire (IPC) et des Nations unies ; analyses d'ACLED, d'ACAPS et de Small Arms Survey. Chaque fait porte un lien. La liste complète est en fin de page.",
      f"Sources: a control map kept by Wikipedia contributors, last updated on 17 August 2026; data from {a('acled_hdx','ACLED')}, the International Organization for Migration, the Integrated Food Security Phase Classification (IPC) and the United Nations; analysis by ACLED, ACAPS and Small Arms Survey. Each fact carries a link. The full list is at the bottom of the page."),
)
WARN=(("Avertissement","Disclaimer"),[
 ("Les cartes colorent des zones à partir d'environ 200 villes suivies par des bénévoles. C'est une interprétation, qui ne vaut reconnaissance d'aucune autorité.",
  "The maps colour areas on the basis of about 200 towns tracked by volunteers. This is an interpretation and does not imply recognition of any authority."),
 ("Trois degrés de certitude sont employés. Un fait sans marque est établi par des sources indépendantes. Un fait <span class='tag'>rapporté</span> repose sur l'annonce d'un camp ou sur une seule source. Un fait <span class='tag'>contesté</span> est un fait sur lequel les sources divergent.",
  "Three degrees of certainty are used. A fact with no mark is established by independent sources. A <span class='tag'>reported</span> fact rests on one side's announcement or on a single source. A <span class='tag'>contested</span> fact is one on which sources disagree."),
 ("Cette note a été rédigée avec l'appui d'un modèle de langage, Claude (Anthropic, modèles Opus 5.5 et Fable 5.2). Le modèle a collecté les données, cherché et lu les sources, et écrit le code. La section Méthode précise ce qui a été vérifié et par qui.",
  "This note was written with the support of a large language model, Claude (Anthropic, Opus 5.5 and Fable 5.2 models). The model collected the data, searched for and read the sources, and wrote the code. The Method section states what was checked and by whom."),
])
KEY=[
 (f"<b>Pourquoi ils se battent.</b> L'armée et les Forces de soutien rapide (RSF, sigle anglais) ont pris le pouvoir ensemble en 2021. Elles sont entrées en guerre en avril 2023 sur les conditions de leur fusion. Chacune tire des revenus de sa position : l'or pour les RSF, les entreprises militaires et les douanes pour l'armée.",
  f"<b>Why they fight.</b> The army and the Rapid Support Forces (RSF) took power together in 2021. They went to war in April 2023 over the terms of their merger. Each draws income from its position: gold for the RSF, military companies and customs for the army."),
 (f"<b>Pourquoi autant de civils sont tués.</b> Les combats ont eu lieu dans les villes. Les RSF ont assiégé des villes et, selon Small Arms Survey, paient en partie leurs combattants par le pillage. Les deux camps frappent des marchés par drone. Plus d'une personne tuée sur trois, parmi celles qu'ACLED recense, l'a été dans une violence visant des civils.",
  f"<b>Why so many civilians are killed.</b> The fighting took place in towns. The RSF besieged towns and, according to Small Arms Survey, pays its fighters partly through looting. Both sides strike markets with drones. More than one in three of the deaths ACLED records came from violence targeting civilians."),
 ("<b>Deux zones.</b> L'armée tient la vallée du Nil, l'est et le centre. Les RSF tiennent presque tout le Darfour, à l'ouest. Le Kordofan se trouve entre les deux. En 2026, près d'une personne tuée sur deux l'a été au Kordofan.",
  "<b>Two zones.</b> The army holds the Nile valley, the east and the centre. The RSF holds almost all of Darfur, in the west. Kordofan lies between them. In 2026 nearly one in two of the people killed were killed in Kordofan."),
 ("<b>Une évolution par régions.</b> Au centre, l'armée avance depuis son offensive de septembre 2024. À l'ouest, les RSF ont pris El Fasher en octobre 2025. Au Kordofan-Nord, aucun camp n'a avancé avant juillet 2026.",
  "<b>A course that differs by region.</b> In the centre the army has advanced since its offensive of September 2024. In the west the RSF took El Fasher in October 2025. In North Kordofan neither side advanced before July 2026."),
 ("<b>Des annonces souvent non confirmées.</b> Sur une quinzaine de prises de villes annoncées de septembre à novembre 2026, une seule a pu être confirmée par deux sources indépendantes.",
  "<b>Announcements often unconfirmed.</b> Of some fifteen captures of towns announced between September and November 2026, only one could be confirmed by two independent sources."),
 ("<b>Pas de trêve.</b> Les RSF ont dit accepter en novembre 2025 la trêve proposée par les médiateurs. L'armée ne l'a pas acceptée. Le plan de réponse humanitaire de 2026 était financé à 50 % le 11 novembre.",
  "<b>No truce.</b> In November 2025 the RSF said it accepted the truce proposed by the mediators. The army has not accepted it. The 2026 humanitarian response plan was 50% funded on 11 November."),
]
SIDES=[
 ("saf",("L'armée soudanaise","The Sudanese army"),
  (f"En anglais Sudanese Armed Forces, SAF. Elle est commandée par le général Abdel Fattah al-Burhan, qui préside aussi le Conseil de souveraineté, l'organe qui tient lieu de chef de l'État. Ses effectifs étaient estimés entre 120 000 et 200 000 hommes en avril 2023, selon {a('euaa','l’Agence de l’Union européenne pour l’asile')}. Elle dispose d'une aviation.",
   f"The Sudanese Armed Forces, SAF. It is commanded by General Abdel Fattah al-Burhan, who also chairs the Sovereignty Council, the body that acts as head of state. Its strength was estimated at between 120,000 and 200,000 in April 2023, according to the {a('euaa','EU Agency for Asylum')}. It has an air force."),
  (f"Le gouvernement qu'elle dirige a siégé à Port-Soudan, sur la mer Rouge, à partir d'août 2023. Il {a('aj_gov','a annoncé son retour à Khartoum le 11 janvier 2026')}. Combattent à ses côtés une partie des anciens rebelles du Darfour, des brigades islamistes, des volontaires civils et, depuis {a('st_kikil','octobre 2024')}, la milice d'Abu Aqla Kikil, auparavant alliée aux RSF.",
   f"The government it leads sat in Port Sudan, on the Red Sea, from August 2023. It {a('aj_gov','announced its return to Khartoum on 11 January 2026')}. Fighting alongside it are some of the former Darfur rebels, Islamist brigades, civilian volunteers and, since {a('st_kikil','October 2024')}, the militia of Abu Aqla Kikil, previously allied to the RSF.")),
 ("rsf",("Les Forces de soutien rapide","The Rapid Support Forces"),
  (f"En anglais Rapid Support Forces, RSF. Elles sont commandées par Mohamed Hamdan Dagalo, dit Hemedti. Elles sont issues des janjawids, des milices recrutées dans des communautés arabes du Darfour, que l'État a armées à partir de 2003 puis intégrées en 2013. Leurs effectifs étaient estimés entre 70 000 et 100 000 hommes en avril 2023, selon la même source.",
   f"The RSF is commanded by Mohamed Hamdan Dagalo, known as Hemedti. It grew out of the Janjaweed, militias recruited from Arab communities in Darfur, which the state armed from 2003 and absorbed in 2013. Its strength was estimated at between 70,000 and 100,000 in April 2023, according to the same source."),
  (f"{a('acled_2y','ACLED')}, un organisme qui recense les violences politiques, les décrit comme une coalition de milices locales. Elles sont alliées au Mouvement populaire de libération du Soudan-Nord (SPLM-N) d'Abdelaziz al-Hilu, qui tient les monts Nouba, au Kordofan-Sud. Ensemble, ils ont formé un gouvernement parallèle, appelé Tasis. {a('tasis','Hemedti a prêté serment à sa tête le 30 août 2025')} à Nyala, au Darfour-Sud.",
   f"{a('acled_2y','ACLED')}, an organisation that records political violence, describes it as a coalition of local militias. It is allied to the Sudan People's Liberation Movement-North (SPLM-N) of Abdelaziz al-Hilu, which holds the Nuba Mountains in South Kordofan. Together they formed a parallel government, known as Tasis. {a('tasis','Hemedti was sworn in as its head on 30 August 2025')} at Nyala, in South Darfur.")),
 ("slm",("Les civils et les groupes non alignés","Civilians and non-aligned groups"),
  (f"Un gouvernement de transition dirigé par un civil, Abdalla Hamdok, a suivi la chute d'Omar el-Béchir en 2019. L'armée et les RSF l'ont renversé le 25 octobre 2021. La coalition civile opposée à la guerre s'est divisée en {a('somoud','février 2025')} sur la question d'un gouvernement avec les RSF. Ceux qui ont refusé, dont Hamdok, ont fondé Somoud. Ce mouvement ne reconnaît aucun des deux gouvernements.",
   f"A transitional government led by a civilian, Abdalla Hamdok, followed the fall of Omar al-Bashir in 2019. The army and the RSF overthrew it on 25 October 2021. The civilian coalition opposed to the war split in {a('somoud','February 2025')} over forming a government with the RSF. Those who refused, including Hamdok, founded Somoud. It recognises neither of the two governments."),
  ("Le Mouvement de libération du Soudan d'Abdelwahid al-Nur (SLM-AW) tient le massif du Jebel Marra, au Darfour. Il se déclare neutre. Ces acteurs ne tiennent pas de territoire au sens des cartes de cette note, à l'exception du Jebel Marra.",
   "The Sudan Liberation Movement of Abdelwahid al-Nur (SLM-AW) holds the Jebel Marra massif in Darfur. It declares itself neutral. These actors hold no territory on the maps in this note, apart from Jebel Marra.")),
 ("oth",("Les soutiens extérieurs","Outside backers"),
  (f"Le {a('panel','groupe d’experts de l’ONU sur le Soudan')} a jugé crédibles, en janvier 2024, les accusations selon lesquelles les Émirats arabes unis arment les RSF en passant par le Tchad. Les Émirats démentent. D'après {a('ap_powers','l’agence Associated Press')}, ils offrent un débouché à l'or des RSF, et un analyste cité explique leur soutien par la volonté d'écarter du pouvoir les groupes islamistes alliés à l'armée.",
   f"In January 2024 the {a('panel','UN Panel of Experts on Sudan')} found credible the accusations that the United Arab Emirates arms the RSF through Chad. The UAE denies it. According to the {a('ap_powers','Associated Press')}, it provides an outlet for RSF gold, and an analyst it quotes explains its support by a wish to keep the Islamist groups allied to the army out of power."),
  (f"L'Égypte soutient l'armée. La même source cite les liens anciens entre les deux armées, le Nil et la mer Rouge. L'Égypte dément fournir des armes. L'armée a acheté des {a('tb2','drones à la Turquie')} et en a reçu d'Iran selon {a('nbc_iran','Reuters et Bloomberg')}, ce que le gouvernement a nié. L'embargo de l'ONU sur les armes ne couvre que le Darfour. Le Conseil de sécurité {a('embargo','l’a prolongé jusqu’au 11 décembre 2026')}.",
   f"Egypt supports the army. The same source cites long-standing ties between the two armies, the Nile and the Red Sea. Egypt denies supplying arms. The army has bought {a('tb2','drones from Turkey')} and received some from Iran according to {a('nbc_iran','Reuters and Bloomberg')}, which the government denied. The UN arms embargo covers Darfur only. The Security Council {a('embargo','extended it to 11 December 2026')}.")),
]
ORIG=[
 ("2003",("Guerre au Darfour. Le gouvernement d'Omar el-Béchir a armé des milices recrutées dans des communautés arabes, les janjawids, contre des rébellions issues de communautés non arabes. Hemedti était l'un de leurs chefs.","War in Darfur. The government of Omar al-Bashir armed militias recruited from Arab communities, the Janjaweed, against rebellions drawn from non-Arab communities. Hemedti was one of their commanders.")),
 ("2013",("Les janjawids sont devenus les Forces de soutien rapide, une force distincte de l'armée.","The Janjaweed became the Rapid Support Forces, a force separate from the army.")),
 ("2019",("Après des mois de manifestations, l'armée et les RSF ont écarté Omar el-Béchir. Un gouvernement de transition a associé civils et militaires.","After months of protests, the army and the RSF removed Omar al-Bashir. A transitional government brought civilians and the military together.")),
 ("2021",("Le 25 octobre, Burhan et Hemedti ont renversé ce gouvernement. Burhan a pris la tête du Conseil de souveraineté, Hemedti en est devenu le numéro deux.","On 25 October Burhan and Hemedti overthrew that government. Burhan took the chair of the Sovereignty Council and Hemedti became his deputy.")),
 ("2022",("En décembre, un accord-cadre a prévu le retour à un pouvoir civil et l'intégration des RSF dans l'armée.","In December a framework agreement provided for a return to civilian rule and for merging the RSF into the army.")),
 ("2023",(f"Le 15 avril, les combats ont commencé à Khartoum. {a('reuters_expl','Chaque camp accuse l’autre d’avoir tiré le premier')}.",f"On 15 April fighting began in Khartoum. {a('reuters_expl','Each side accuses the other of firing first')}.")),
]

def P(fr,en): return ('p',fr,en)
def H3(fr,en): return ('h3',fr,en)
def PIECE(pid,title,sub,src,lim,**kw): return ('piece',pid,title,sub,src,lim,kw)
SRC_CTRL=(f"{a('wiki','carte détaillée de Wikipédia')} (CC BY-SA 4.0), relevés mensuels jusqu'au 17 août 2026, corrections manuelles décrites en méthode. Limites administratives : {a('cod','OCHA')}.",
          f"{a('wiki','Wikipedia detailed map')} (CC BY-SA 4.0), monthly snapshots to 17 August 2026, manual corrections described under method. Administrative boundaries: {a('cod','OCHA')}.")
SRC_ACLED=(f"{a('acled_hdx','ACLED (Armed Conflict Location & Event Data)')}, acleddata.com, agrégats par localité et par mois, Soudan, avril 2023 à octobre 2026, téléchargés le 11 novembre 2026. Les calculs sont ceux de l'auteur.",
           f"{a('acled_hdx','ACLED (Armed Conflict Location & Event Data)')}, acleddata.com, aggregates by locality and month, Sudan, April 2023 to October 2026, downloaded on 11 November 2026. The calculations are the author's.")
LIM_CTRL=("Les surfaces sont une interprétation et surestiment le contrôle réel. Voir la limite de la première carte.","The areas are an interpretation and overstate real control. See the limitations under the first map.")

S=[
 ('h2',("Pourquoi l'armée et les RSF se battent","Why the army and the RSF are fighting"),[
  H3("Repères","Bearings"),
  P(f"Le Soudan compte environ 47,5 millions d'habitants, selon la {a('pop','projection publiée par l’OCHA')}, le bureau de coordination humanitaire de l'ONU. Trois ensembles reviennent dans cette note. La vallée du Nil et l'est regroupent la capitale, formée de trois villes (Khartoum, Omdurman et Bahri), et Port-Soudan, le port sur la mer Rouge. Le Kordofan, au centre-sud, compte trois États. Le Darfour, à l'ouest, compte cinq États et borde le Tchad. Avant la guerre, le Darfour abritait environ un habitant sur quatre et le Kordofan un sur six.",
    f"Sudan has about 47.5 million inhabitants, according to the {a('pop','projection published by OCHA')}, the UN humanitarian coordination office. Three areas recur in this note. The Nile valley and the east contain the capital, made up of three cities (Khartoum, Omdurman and Bahri), and Port Sudan, the port on the Red Sea. Kordofan, in the centre-south, has three states. Darfur, in the west, has five states and borders Chad. Before the war Darfur was home to about one inhabitant in four and Kordofan to one in six."),
  H3("Les belligérants","The belligerents"),
  ('sides',),
  H3("De l'alliance à la guerre","From alliance to war"),
  ('tl',),
  P(f"La cause immédiate a été un désaccord sur le calendrier de la fusion. L'armée voulait intégrer les RSF en deux ans. Les RSF demandaient dix ans. La question du commandement n'était pas réglée. {a('acled_2y','ACLED')} ajoute que des réseaux islamistes liés au gouvernement d'Omar el-Béchir, qui avaient soutenu le coup d'État de 2021, rejetaient l'accord-cadre.",
    f"The immediate cause was a disagreement over the timetable for the merger. The army wanted to absorb the RSF within two years. The RSF asked for ten. The question of command was not settled. {a('acled_2y','ACLED')} adds that Islamist networks linked to the government of Omar al-Bashir, which had backed the 2021 coup, rejected the framework agreement."),
  P(f"Chaque force tire des revenus de sa position. Le {a('treasury23','Trésor américain')} écrit que la société Al Junaid est contrôlée par Hemedti et son frère, et que l'extraction et l'exportation d'or sont une source de revenus essentielle pour sa famille et pour les RSF depuis qu'elles ont pris la mine du Jebel Amer en 2017. Il décrit aussi le Système des industries de défense, lié à l'armée, comme la première entreprise de défense du pays, avec environ 2 milliards de dollars de revenus. Selon une {a('ifri','note de l’Institut français des relations internationales')}, l'armée, qui contrôle le gouvernement reconnu, taxe le commerce officiel par la mer Rouge, et les RSF taxent le commerce avec la Libye, le Tchad et la Centrafrique.",
    f"Each force draws income from its position. The {a('treasury23','US Treasury')} writes that the company Al Junaid is controlled by Hemedti and his brother, and that gold mining and export have been a vital source of revenue for his family and the RSF since it took the Jebel Amer mine in 2017. It also describes the Defense Industries System, linked to the army, as the country's largest defence enterprise, with about 2 billion dollars in revenue. According to a {a('ifri','note by the French Institute of International Relations')}, the army, which controls the recognised government, taxes official trade through the Red Sea, and the RSF taxes trade with Libya, Chad and the Central African Republic."),
  P(f"Chaque camp présente autrement ce qu'il défend. Le 14 août 2025, lors de l'anniversaire de l'armée, le général Burhan a parlé d'une « bataille pour la dignité » destinée à « vaincre la rébellion », sans compromis ni réconciliation « quel qu'en soit le coût », selon {a('burhan_dignity','The New Arab')}. Hemedti a déclaré le 15 avril 2025 que son gouvernement n'était pas « un État parallèle » et qu'il s'adressait à « chaque Soudanais qui se sent oublié, marginalisé et privé de ses droits ». Il a dit vouloir un Soudan « libre, démocratique, pluraliste et pacifique ». Selon {a('hemedti_gov','Radio Dabanga')}, qui rapporte ces propos, la charte signée à Nairobi en février 2025 par les RSF, le SPLM-N et d'autres groupes prévoit un État décentralisé et la séparation de la religion et de l'État. Ces citations sont traduites de l'anglais. Elles disent ce que chaque camp affirme. La suite de la note rapporte ce que des sources indépendantes disent de leurs actes.",
    f"Each side presents what it defends differently. On 14 August 2025, on the army's anniversary, General Burhan spoke of a 'battle for dignity' to 'defeat the rebellion', with no compromise or reconciliation 'whatever the cost', according to {a('burhan_dignity','The New Arab')}. Hemedti said on 15 April 2025 that his government was not 'a parallel state' and that it was for 'every Sudanese person who feels forgotten, marginalised, and disenfranchised'. He said he wanted a 'free, democratic, pluralistic, and peaceful Sudan'. According to {a('hemedti_gov','Radio Dabanga')}, which reports these remarks, the charter signed in Nairobi in February 2025 by the RSF, the SPLM-N and other groups provides for a decentralised state and the separation of religion and state. These quotations say what each side claims. The rest of the note reports what independent sources say about their acts."),
  P(f"Les raisons pour lesquelles la guerre continue ne sont pas seulement celles qui l'ont déclenchée. {a('sas','Small Arms Survey')}, un centre de recherche sur les armes légères, décrit des communautés mobilisées par leurs propres chefs et rémunérées par le butin et par des prélèvements aux barrages routiers. ACLED parle d'une {a('acled_infight','alliance transactionnelle')}. Au Darfour, la guerre a ravivé le conflit de 2003 entre des milices issues de communautés arabes et des communautés non arabes, dont les Massalit, les Four et les Zaghawa. Les deux camps reçoivent des armes de l'étranger.",
    f"The reasons the war continues are not only those that started it. {a('sas','Small Arms Survey')}, a research centre on small arms, describes communities mobilised by their own leaders and paid through loot and levies at road checkpoints. ACLED speaks of a {a('acled_infight','transactional alliance')}. In Darfur the war has revived the 2003 conflict between militias drawn from Arab communities and non-Arab communities, among them the Masalit, the Fur and the Zaghawa. Both sides receive weapons from abroad."),
  PIECE('routes',("Les RSF se ravitaillent par l'ouest, l'armée par l'est","The RSF is supplied from the west, the army from the east"),
    ("Points d'entrée et axes routiers, tracés schématiques, sur le contrôle d'octobre 2026. Trait à la couleur du camp desservi. Tirets : route fermée ou seulement rapportée","Entry points and road axes, drawn schematically, over control in October 2026. Line in the colour of the side supplied. Dashes: route closed or only reported"),
    (f"{a('panel','groupe d’experts de l’ONU')}, janvier 2024 ; {a('amdjarass','Reuters')}, décembre 2024 et {a('kufra','décembre 2025')} ; {a('chad','The National')}, février 2026. Fond : Wikipédia.",f"{a('panel','UN Panel of Experts')}, January 2024; {a('amdjarass','Reuters')}, December 2024 and {a('kufra','December 2025')}; {a('chad','The National')}, February 2026. Base map: Wikipedia."),
    ("Les tracés ne sont pas des routes réelles. Les Émirats arabes unis démentent armer les RSF. L'Éthiopie et la Centrafrique, citées par ACLED comme nouvelles voies en 2026, ne sont pas représentées.","The lines are not real roads. The UAE denies arming the RSF. Ethiopia and the Central African Republic, cited by ACLED as new routes in 2026, are not shown."),
    map=dict(m="2026-10",road="1",fade="1",nb="1",nodots="1",names="Port Sudan,Khartoum,El Fasher,Nyala,El-Obeid")),
  P(f"Reuters a {a('amdjarass','vérifié 86 vols')} vers Amdjarass, au Tchad. Les Émirats parlent d'aide humanitaire. Après que les RSF ont occupé le triangle frontalier avec la Libye et l'Égypte, en juin 2025, des livraisons sont passées par {a('kufra','Koufra, en Libye')}, selon Reuters. Amnesty International a identifié chez les RSF des bombes guidées et des obusiers de fabrication chinoise, et {a('amnesty25','conclut qu’ils ont très probablement été réexportés par les Émirats')}. Le Tchad a {a('chad','fermé sa frontière le 23 février 2026')}. ACLED note que les livraisons aux RSF {a('acled_drone','passent davantage par l’Éthiopie et la Centrafrique')} depuis.",
    f"Reuters {a('amdjarass','verified 86 flights')} to Amdjarass in Chad. The UAE speaks of humanitarian aid. After the RSF occupied the border triangle with Libya and Egypt in June 2025, deliveries came through {a('kufra','Kufra in Libya')}, according to Reuters. Amnesty International identified Chinese-made guided bombs and howitzers in RSF hands and {a('amnesty25','concluded that the UAE had almost certainly re-exported them')}. Chad {a('chad','closed its border on 23 February 2026')}. ACLED notes that deliveries to the RSF have {a('acled_drone','come more through Ethiopia and the Central African Republic')} since."),
 ]),
 ('h2',("Comment la guerre s'est déroulée","How the war unfolded"),[
  PIECE('ch-share',("L'armée tient plus de la moitié des localités depuis 2025","The army has held more than half of localities since 2025"),
    ("Part des localités du Soudan tenue par chaque camp, mois par mois, avril 2023 à août 2026. Une localité est l'échelon administratif situé sous l'État","Share of Sudan's localities held by each side, month by month, April 2023 to August 2026. A locality is the administrative level below the state"),
    SRC_CTRL,
    ("La carte source ne suivait qu'une vingtaine de villes en avril 2023, environ 70 à l'été 2023 et 200 en 2026 : la part « disputée » du début tient en partie à ce manque de relevés. Une localité compte pour une, quelle que soit sa population. La partie grisée, après le 17 août 2026, n'a pas de relevé.","The source map tracked only about twenty towns in April 2023, about 70 in summer 2023 and 200 in 2026: the early 'disputed' share partly reflects that lack of readings. Each locality counts as one, whatever its population. The greyed part, after 17 August 2026, has no reading.")),
  ('main',),
  P(f"<b>2023.</b> Les combats ont commencé à Khartoum et se sont étendus au Darfour. À El Geneina, capitale du Darfour-Ouest, les RSF et des milices alliées ont tué des milliers de civils massalit, selon {a('hrw_geneina','Human Rights Watch')}. Le général Burhan a {a('dab_burhan','quitté son quartier général assiégé le 24 août')}. D'octobre à novembre, les RSF ont pris {a('dab_darfur','quatre garnisons de l’armée au Darfour')}, dont Nyala. Le 18 décembre, elles sont entrées dans {a('aawsat_madani','Wad Madani')}, capitale de la Gezira, au sud-est de Khartoum.",
    f"<b>2023.</b> Fighting began in Khartoum and spread to Darfur. In El Geneina, the capital of West Darfur, the RSF and allied militias killed thousands of Masalit civilians, according to {a('hrw_geneina','Human Rights Watch')}. General Burhan {a('dab_burhan','left his besieged headquarters on 24 August')}. From October to November the RSF took {a('dab_darfur','four army garrisons in Darfur')}, including Nyala. On 18 December it entered {a('aawsat_madani','Wad Madani')}, the capital of Gezira, south-east of Khartoum."),
  P(f"<b>2024.</b> Au printemps, les RSF ont encerclé El Fasher, capitale du Darfour-Nord et dernière capitale du Darfour tenue par l'armée et ses alliés. En juin, elles ont pris {a('sw_sennar','Sinja')}, dans l'État de Sennar. Le 26 septembre, l'armée a lancé une offensive au centre. {a('acled_2y','ACLED')} date de cette offensive le moment où l'armée a repris l'avantage dans cette région.",
    f"<b>2024.</b> In the spring the RSF encircled El Fasher, the capital of North Darfur and the last Darfur capital held by the army and its allies. In June it took {a('sw_sennar','Sinja')}, in Sennar state. On 26 September the army launched an offensive in the centre. {a('acled_2y','ACLED')} dates the army's regained advantage in that region to this offensive."),
  P(f"<b>2025.</b> L'armée a repris Wad Madani le 11 janvier, puis, à Khartoum, {a('palace','le palais présidentiel le 21 mars')}. À l'ouest, les RSF ont attaqué le camp de personnes déplacées de Zamzam, près d'El Fasher, du 11 au 13 avril. Elles ont pris El Fasher le 26 octobre, puis {a('swm_babanusa','Babanusa et le champ pétrolier de Heglig')}, au Kordofan-Ouest, en décembre.",
    f"<b>2025.</b> The army retook Wad Madani on 11 January and then, in Khartoum, {a('palace','the presidential palace on 21 March')}. In the west the RSF attacked Zamzam, a camp for displaced people near El Fasher, from 11 to 13 April. It took El Fasher on 26 October, then {a('swm_babanusa','Babanusa and the Heglig oil field')}, in West Kordofan, in December."),
  PIECE('pair',("L'armée a repris en 2025 le centre perdu en 2023","In 2025 the army retook the centre it lost in 2023"),
    ("Contrôle des localités autour de Khartoum et de la Gezira, en décembre 2023 et en mars 2025","Control of localities around Khartoum and Gezira, in December 2023 and in March 2025"),
    SRC_CTRL,LIM_CTRL,
    pair=[dict(m="2023-12",box="31.2,12.6,35.2,16.6",names="Wad Madani,Khartoum,Sennar",facts="1",nolegend="1",maxsmall="3"),dict(m="2025-03",box="31.2,12.6,35.2,16.6",names="Wad Madani,Khartoum,Sennar",facts="1",maxsmall="3")]),
  PIECE('ch-net',("L'armée regagne des villes depuis l'automne 2024","The army has been regaining towns since autumn 2024"),
    ("Villes suivies passées à l'armée, moins villes passées aux RSF ou à leurs alliés, en cumul depuis avril 2023","Tracked towns that went to the army, minus towns that went to the RSF or its allies, cumulative since April 2023"),
    SRC_CTRL,
    ("La courbe dépend du rythme de mise à jour des bénévoles. Seules les villes déjà suivies le mois précédent sont comptées. Une ville prise et perdue entre deux relevés n'apparaît pas. Pas de relevé après le 17 août 2026.","The line depends on how often the volunteers update. Only towns already tracked the previous month are counted. A town taken and lost between two snapshots does not appear. No reading after 17 August 2026.")),
  P(f"<b>2026.</b> Les combats se sont concentrés au Kordofan. L'armée a annoncé avoir rouvert la route de {a('aj_dilling','Dilling le 26 janvier')} et levé le siège de {a('aj_kadugli','Kadugli le 3 février')}, deux villes du Kordofan-Sud {REP[0]}. À Bara, au nord d'El Obeid, {a('dab_bara','l’armée est entrée le 5 mars, les RSF sont revenues le 16, l’armée a repris la ville le 25 juillet')}. Le 13 août, {a('acled_saf','ACLED')} a écrit que l'encerclement d'El Obeid par les RSF avait cédé après plus de dix-huit mois, et que les RSF auraient des difficultés à tenir trois fronts.",
    f"<b>2026.</b> Fighting concentrated in Kordofan. The army announced that it had reopened the road to {a('aj_dilling','Dilling on 26 January')} and lifted the siege of {a('aj_kadugli','Kadugli on 3 February')}, two towns in South Kordofan {REP[1]}. At Bara, north of El Obeid, {a('dab_bara','the army entered on 5 March, the RSF returned on the 16th, and the army retook the town on 25 July')}. On 13 August {a('acled_saf','ACLED')} wrote that the RSF's encirclement of El Obeid had given way after more than eighteen months, and that the RSF would have difficulty holding three fronts."),
  PIECE('kordofan',("Au Kordofan, l'armée a repris Bara et Sodari en 2026","In Kordofan the army retook Bara and Sodari in 2026"),
    ("Contrôle des localités du Kordofan, octobre 2026. Cercle en tirets : ville assiégée. Cercle en pointillé : pression d'un seul côté, d'après la carte source","Control of Kordofan localities, October 2026. Dashed ring: besieged town. Dotted ring: pressure from one side, according to the source map"),
    SRC_CTRL,
    ("Contrôle du 17 août 2026, avec deux ajouts manuels : Sodari, dont la confirmation est faible, et Kazgeil, disputée début novembre. "+LIM_CTRL[0],"Control as of 17 August 2026, with two manual additions: Sodari, whose confirmation is weak, and Kazgeil, disputed in early November. "+LIM_CTRL[1]),
    map=dict(m="2026-10",box="26.6,9.4,32.4,15.2",names="El-Obeid,Barah,Sodari,Kazgeil,En Nahud,Dilling,Kadugli,Babanusa",facts="1",siege="1",spl="1",road="1",maxsmall="5")),
  P(f"Dans l'État du Nil Bleu, à la frontière éthiopienne, les RSF et le SPLM-N ont pris Kurmuk le 23 mars 2026. L'armée l'a reprise le 8 juillet. Les RSF et le SPLM-N {a('aj_kurmuk','l’ont reprise le 13 août')}. {a('acled_bn','ACLED')} y voit un front secondaire, ouvert pour ralentir l'armée au Kordofan-Nord. ACLED tient le soutien de l'Éthiopie aux RSF pour établi depuis novembre 2025. {a('acaps_risk','ACAPS')}, un organisme d'analyse humanitaire, est plus prudent et rappelle le démenti éthiopien.",
    f"In Blue Nile state, on the Ethiopian border, the RSF and the SPLM-N took Kurmuk on 23 March 2026. The army retook it on 8 July. The RSF and the SPLM-N {a('aj_kurmuk','took it again on 13 August')}. {a('acled_bn','ACLED')} sees a secondary front, opened to slow the army in North Kordofan. ACLED treats Ethiopian support for the RSF as established since November 2025. {a('acaps_risk','ACAPS')}, a humanitarian analysis organisation, is more cautious and recalls Ethiopia's denial."),
  P(f"De septembre à novembre 2026, l'armée et ses alliés ont poursuivi leur avancée au Kordofan-Nord. Ils sont entrés à {a('swm_sodari','Sodari le 25 septembre')} et ont annoncé la prise d'{a('aj_mazroub','Al-Mazroub le 2 octobre')} {REP[0]}. Au sud d'El Obeid, selon {a('swm_nov','Sudan War Monitor')}, un site de suivi du conflit, l'armée est entrée à Kazgeil le 5 novembre et les RSF y sont revenues le soir même. Au Darfour, aucune ville n'a changé de camp dans les sources consultées.",
    f"From September to November 2026 the army and its allies continued to advance in North Kordofan. They entered {a('swm_sodari','Sodari on 25 September')} and announced the capture of {a('aj_mazroub','Al-Mazroub on 2 October')} {REP[1]}. South of El Obeid, according to {a('swm_nov','Sudan War Monitor')}, a conflict-monitoring site, the army entered Kazgeil on 5 November and the RSF returned the same evening. In Darfur no town changed sides in the sources consulted."),
  P("Les annonces de prise de ville sont souvent impossibles à confirmer. Pour cette note, un changement postérieur au 17 août 2026 n'a été retenu que si deux sources indépendantes le rapportaient comme un fait. Sur une quinzaine d'annonces, seule celle de Sodari a satisfait ce critère, avec une confirmation faible. Les cartes de cette note donnent donc une image approximative.",
    "Announcements of captured towns often cannot be confirmed. For this note, a change later than 17 August 2026 was accepted only if two independent sources reported it as fact. Of some fifteen announcements, only Sodari met that test, with weak confirmation. The maps in this note therefore give an approximate picture."),
 ]),
 ('h2',("Pourquoi la guerre tue autant de civils","Why the war kills so many civilians"),[
  P(f"{a('acled_hdx','ACLED')} a recensé plus de 57 000 personnes tuées d'avril 2023 à octobre 2026. Plus de 20 000 d'entre elles l'ont été dans des violences qui visaient des civils, soit plus d'une sur trois. Les autres ont été tuées dans des combats ou des frappes, et comprennent des combattants et des civils. Ces chiffres sont un minimum : ACLED ne compte que les morts rapportées par des sources qu'il peut recouper.",
    f"{a('acled_hdx','ACLED')} recorded more than 57,000 people killed from April 2023 to October 2026. More than 20,000 of them were killed in violence that targeted civilians, more than one in three. The others were killed in fighting or strikes, and include both combatants and civilians. These figures are a minimum: ACLED counts only deaths reported by sources it can cross-check."),
  PIECE('ch-deaths',("Les violences visant des civils causent un tiers des morts recensés","Violence targeting civilians accounts for a third of recorded deaths"),
    ("Personnes tuées recensées par mois au Soudan, avril 2023 à octobre 2026. En noir, celles tuées dans des violences visant des civils. Les cinq mois nommés renvoient à des événements décrits dans le texte","People recorded killed per month in Sudan, April 2023 to October 2026. In black, those killed in violence targeting civilians. The five months named refer to events described in the text"),
    SRC_ACLED,
    ("Minimum. Les zones privées de réseau sont sous-comptées. La catégorie « violences visant des civils » est celle d'ACLED. Le Haut-Commissariat des Nations unies aux droits de l'homme compte autrement, et ses chiffres, cités plus bas, ne s'additionnent pas à ceux-ci.","A minimum. Areas without network coverage are undercounted. The category 'violence targeting civilians' is ACLED's. The UN human rights office counts differently, and its figures, cited below, cannot be added to these.")),
  P(f"Le nombre réel de morts n'est pas connu. Une {a('lshtm','étude de la London School of Hygiene and Tropical Medicine')} a estimé à plus de 61 000 les décès de toutes causes dans le seul État de Khartoum entre avril 2023 et juin 2024, dont plus de 26 000 morts violentes. Selon ses auteurs, plus de 90 % de ces décès n'avaient pas été enregistrés. Cinq mécanismes, décrits ci-dessous, rendent compte d'une grande partie des morts de civils.",
    f"The real number of deaths is not known. A {a('lshtm','study by the London School of Hygiene and Tropical Medicine')} estimated more than 61,000 deaths from all causes in Khartoum state alone between April 2023 and June 2024, including more than 26,000 violent deaths. According to its authors, more than 90% of these deaths had not been recorded. Five mechanisms, described below, account for a large part of civilian deaths."),
  H3("1. Les combats ont eu lieu dans les villes","1. The fighting took place in towns"),
  P("La guerre a commencé dans la capitale, entre deux forces installées au milieu des habitants. En 2023, Khartoum et le Darfour ont concentré plus de huit personnes tuées sur dix. La part du centre a augmenté en 2024, quand les RSF tenaient la Gezira. En 2026, près d'une personne tuée sur deux l'a été au Kordofan.",
    "The war began in the capital, between two forces stationed among the residents. In 2023 Khartoum and Darfur accounted for more than eight in ten of the people killed. The centre's share rose in 2024, when the RSF held Gezira. In 2026 nearly one in two of the people killed were killed in Kordofan."),
  PIECE('ch-reg',("En 2026, une personne tuée sur deux l'a été au Kordofan","In 2026 one in two of the people killed were in Kordofan"),
    ("Part de chaque région dans les personnes tuées recensées, par trimestre, avril 2023 à octobre 2026. Centre : Gezira, Sennar et Nil Blanc","Each region's share of the people recorded killed, by quarter, April 2023 to October 2026. Centre: Gezira, Sennar and White Nile"),
    SRC_ACLED,
    ("Des parts, pas des effectifs : le graphique précédent donne le niveau. Le dernier trimestre ne compte qu'un mois. De janvier à octobre 2026, le Kordofan représente 49 % des personnes tuées recensées.","Shares, not counts: the previous chart gives the level. The last quarter has one month only. From January to October 2026 Kordofan accounts for 49% of the people recorded killed.")),
  H3("2. Des civils sont visés pour leur communauté, et pillés","2. Civilians are targeted for their community, and looted"),
  P(f"Selon {a('sas','Small Arms Survey')}, les RSF ont réduit les soldes après 2023, et le pillage est devenu une part nécessaire de la rémunération des combattants. Les RSF répondent que leurs hommes sont payés et que les pillards sont des éléments incontrôlés. Dans la Gezira, {a('reuters_gezira','Reuters')} a recueilli les témoignages de 43 personnes sur des pillages commis par des combattants des RSF. {a('acled_2y','ACLED')} a attribué aux RSF 68 % des violences contre des civils recensées d'avril 2023 à avril 2025.",
    f"According to {a('sas','Small Arms Survey')}, the RSF cut salaries after 2023 and looting became a necessary part of fighters' pay. The RSF replies that its men are salaried and that looters are rogue elements. In Gezira, {a('reuters_gezira','Reuters')} gathered accounts from 43 people of looting by RSF fighters. {a('acled_2y','ACLED')} attributed to the RSF 68% of the violence against civilians recorded from April 2023 to April 2025."),
  P(f"Au Darfour, des civils ont été tués en raison de leur communauté. À El Geneina en 2023, les RSF et des milices alliées ont tué des milliers de Massalit, une communauté non arabe, selon {a('hrw_geneina','Human Rights Watch')}. Le groupe d'experts de l'ONU a cité une estimation de 10 000 à 15 000 morts. Dans le camp de Zamzam, en avril 2025, le Haut-Commissariat aux droits de l'homme a compté {a('zamzam','au moins 1 013 civils tués par les RSF')}. À El Fasher, il a documenté {a('un_fasher','plus de 6 000 personnes tuées en trois jours')} lors de la prise de la ville par les RSF, en octobre 2025, et juge le bilan réel bien supérieur.",
    f"In Darfur civilians were killed because of their community. In El Geneina in 2023 the RSF and allied militias killed thousands of Masalit, a non-Arab community, according to {a('hrw_geneina','Human Rights Watch')}. The UN Panel of Experts cited an estimate of 10,000 to 15,000 dead. In Zamzam camp in April 2025 the UN human rights office counted {a('zamzam','at least 1,013 civilians killed by the RSF')}. In El Fasher it documented {a('un_fasher','more than 6,000 people killed in three days')} when the RSF took the city in October 2025, and considers the real toll much higher."),
  P(f"Des instances ont qualifié ces faits. Le 7 janvier 2025, le secrétaire d'État américain a {a('us_genocide','conclu que des membres des RSF et de milices alliées avaient commis un génocide')}. Le bureau du procureur de la Cour pénale internationale {a('icc_fasher','enquête sur les crimes commis au Darfour depuis avril 2023')}. Il n'avait pas rendu public de mandat d'arrêt pour ces faits en {a('icc_2026','juillet 2026')}. La Cour internationale de justice a {a('icj','rejeté le 5 mai 2025')} la requête du Soudan contre les Émirats arabes unis, faute de compétence.",
    f"Official bodies have characterised these acts. On 7 January 2025 the US Secretary of State {a('us_genocide','concluded that members of the RSF and allied militias had committed genocide')}. The Office of the Prosecutor of the International Criminal Court {a('icc_fasher','is investigating crimes committed in Darfur since April 2023')}. It had made public no arrest warrant for these acts as of {a('icc_2026','July 2026')}. On 5 May 2025 the International Court of Justice {a('icj','dismissed')} Sudan's case against the United Arab Emirates for lack of jurisdiction."),
  P(f"La mission d'établissement des faits de l'ONU a conclu en {a('ffm24','octobre 2024')} que les RSF étaient responsables de violences sexuelles à grande échelle dans les zones qu'elles contrôlent, dont des viols collectifs et des enlèvements. En {a('ffm25','septembre 2025')}, elle a écrit que des femmes et des filles de communautés non arabes étaient particulièrement visées, et que des membres de l'armée et de forces alliées étaient impliqués dans des tortures à caractère sexuel en détention.",
    f"The UN Fact-Finding Mission concluded in {a('ffm24','October 2024')} that the RSF was responsible for sexual violence on a large scale in areas under its control, including gang rapes and abductions. In {a('ffm25','September 2025')} it wrote that women and girls from non-Arab communities were particularly targeted, and that members of the army and allied forces were implicated in sexualised torture in detention."),
  P(f"L'armée et ses alliés sont mis en cause pour d'autres faits. Selon la même mission, ils ont visé la communauté des Kanabi après la reprise de Wad Madani en janvier 2025 et tué des dizaines de personnes. Après la reprise de Khartoum, le Haut-Commissaire aux droits de l'homme s'est dit {a('turk_khartoum','consterné par des informations faisant état d’exécutions extrajudiciaires')}. Le 24 mars 2025, des frappes aériennes de l'armée sur le marché de Tora, au Darfour-Nord, ont tué des centaines de civils selon des informations {a('tora','rapportées par le Haut-Commissaire')}. Le {a('treasury_burhan','Trésor américain a sanctionné le général Burhan')} le 16 janvier 2025, en citant des bombardements indiscriminés et des exécutions.",
    f"The army and its allies are implicated in other acts. According to the same mission, they targeted the Kanabi community after retaking Wad Madani in January 2025 and killed dozens of people. After the recapture of Khartoum, the UN High Commissioner for Human Rights said he was {a('turk_khartoum','appalled by reports of extrajudicial killings')}. On 24 March 2025 army air strikes on Tora market, in North Darfur, killed hundreds of civilians according to reports {a('tora','relayed by the High Commissioner')}. The {a('treasury_burhan','US Treasury sanctioned General Burhan')} on 16 January 2025, citing indiscriminate bombing and executions."),
  H3("3. Les RSF assiègent des villes","3. The RSF besieges towns"),
  P(f"À El Fasher, les RSF ont commencé le 9 mai 2025 à élever une levée de terre autour de la ville. Le laboratoire de recherche humanitaire de l'université Yale, qui suivait les travaux par satellite, a mesuré {a('berm1','plus de 31 km fin août')} et {a('berm2','38 km à la mi-septembre')}. Selon le {a('ohchr_fasher','rapport du Haut-Commissariat aux droits de l’homme')}, les RSF avaient bloqué toutes les routes principales en août 2025. Aux sorties restantes, leurs combattants contrôlaient les personnes et exigeaient de l'argent. Ils ont arrêté des personnes qui tentaient d'apporter de la nourriture, et en ont exécuté certaines. Les habitants ont mangé de l'ambaz, {a('aj_ambaz','un résidu d’arachide destiné au bétail')}.",
    f"In El Fasher the RSF began building an earthen berm around the city on 9 May 2025. Yale University's Humanitarian Research Lab, which followed the work by satellite, measured {a('berm1','more than 31 km in late August')} and {a('berm2','38 km by mid-September')}. According to the {a('ohchr_fasher','report of the UN human rights office')}, the RSF had blocked all main roads by August 2025. At the remaining exits its fighters screened people and demanded money. They detained people who tried to bring food in, and executed some of them. Residents ate ambaz, {a('aj_ambaz','a groundnut residue meant for livestock')}."),
  PIECE('ch-price',("À El Fasher assiégée, le sorgho a coûté 96 fois plus","In besieged El Fasher sorghum cost 96 times more"),
    ("Prix de détail de 3 kg de sorgho dans quatre villes, divisé par le prix à Port-Soudan le même mois. Échelle logarithmique. Janvier 2023 à septembre 2026","Retail price of 3 kg of sorghum in four towns, divided by the Port Sudan price in the same month. Logarithmic scale. January 2023 to September 2026"),
    (f"Programme alimentaire mondial (PAM), relevés de marché, via {a('hapi','HDX HAPI')}, la base de données humanitaires de l'OCHA.",f"World Food Programme (WFP), market monitoring, via {a('hapi','HDX HAPI')}, OCHA's humanitarian data service."),
    ("Les interruptions de ligne sont des mois sans relevé. À El Fasher, la série s'arrête en octobre 2025, mois où les RSF ont pris la ville. Kadugli a été assiégée jusqu'en février 2026, El Obeid encerclée jusqu'en juillet 2026. El Geneina, non assiégée, sert de comparaison. Un prix relevé ne dit pas si la denrée est disponible.","Breaks in a line are months with no reading. In El Fasher the series stops in October 2025, the month the RSF took the city. Kadugli was besieged until February 2026 and El Obeid encircled until July 2026. El Geneina, not besieged, serves as a comparison. A recorded price does not say whether the food is available.")),
  PIECE('darfur',("Les RSF tiennent les cinq capitales du Darfour depuis octobre 2025","The RSF has held all five Darfur capitals since October 2025"),
    ("Contrôle des localités du Darfour, novembre 2025, et date à laquelle les RSF ont pris chaque capitale d'État. Violet : mouvement d'Abdelwahid al-Nur","Control of Darfur localities, November 2025, and the date the RSF took each state capital. Purple: Abdelwahid al-Nur's movement"),
    SRC_CTRL,
    (f"À El Geneina, la date est celle de la prise de la garnison d'Ardamata, en novembre 2023. L'armée et ses alliés tenaient encore Tina, à la frontière tchadienne. Le chiffre de Tawila vient de {a('tawila','l’Organisation internationale pour les migrations')}, septembre 2026. "+LIM_CTRL[0],f"For El Geneina the date is that of the capture of the Ardamata garrison, in November 2023. The army and its allies still held Tina, on the Chadian border. The Tawila figure is from the {a('tawila','International Organization for Migration')}, September 2026. "+LIM_CTRL[1]),
    map=dict(m="2025-11",box="21.6,9.4,28.2,16.4",names="El Fasher,Nyala,Geneina,Zalingei,Ed Daein,Tawila,Tine",facts="1",slm="1",nodots="1",maxsmall="5")),
  P(f"Les RSF ont assiégé d'autres villes : Babanusa pendant près de deux ans, Kadugli et Dilling avec le SPLM-N, El Obeid sur trois côtés jusqu'en juillet 2026. Le comité d'examen de la famine, l'instance d'experts qui valide les classements de l'IPC, a confirmé la famine dans le camp de Zamzam en août 2024, puis {a('fao_famine','à El Fasher et à Kadugli en novembre 2025')}. Ces trois lieux étaient alors assiégés. Dans les sources lues, l'armée n'assiège pas de villes. {a('acaps_access','ACAPS')} décrit de sa part un autre moyen : l'interdiction, fin 2025, de faire entrer des marchandises dans les zones tenues par les RSF.",
    f"The RSF besieged other towns: Babanusa for nearly two years, Kadugli and Dilling together with the SPLM-N, El Obeid on three sides until July 2026. The Famine Review Committee, the expert body that validates IPC classifications, confirmed famine in Zamzam camp in August 2024, then {a('fao_famine','in El Fasher and Kadugli in November 2025')}. All three were under siege at the time. In the sources read, the army does not besiege towns. {a('acaps_access','ACAPS')} describes a different means on its part: the ban, in late 2025, on bringing goods into RSF-held areas."),
  H3("4. Les deux camps frappent par drone","4. Both sides strike with drones"),
  P(f"Du 4 au 9 mai 2025, des drones ont frappé {a('portsudan','Port-Soudan')} six jours de suite, à environ 650 km des positions connues des RSF les plus proches. Les RSF n'ont pas revendiqué ces frappes. Pour 2025, ACLED a compté {a('newlines','environ 500 frappes de drones')}, dont environ 280 de l'armée et 200 des RSF, près de la moitié sur des cibles civiles. Peu de drones sont interceptés : selon {a('acled_drone','ACLED')}, l'armée intercepte environ 13 % de ceux des RSF, et les RSF 2,3 % de ceux de l'armée.",
    f"From 4 to 9 May 2025 drones struck {a('portsudan','Port Sudan')} on six consecutive days, about 650 km from the nearest known RSF positions. The RSF did not claim the strikes. For 2025 ACLED counted {a('newlines','about 500 drone strikes')}, roughly 280 by the army and 200 by the RSF, nearly half on civilian targets. Few drones are intercepted: according to {a('acled_drone','ACLED')}, the army intercepts about 13% of the RSF's, and the RSF 2.3% of the army's."),
  PIECE('ch-drone',("Contre les services civils, quatre frappes sur cinq par drone","Against civilian services, four strikes in five are by drone"),
    ("Part des incidents avec armes explosives où l'arme a été lancée par drone, par an. Seuls sont comptés les incidents touchant la santé, l'éducation, l'aide, l'eau ou l'alimentation","Share of explosive-weapon incidents in which the weapon was launched by drone, by year. Only incidents affecting health, education, aid, water or food are counted"),
    (f"{a('ii','Insecurity Insight')}, une organisation qui recense les attaques contre l'aide et les soins, via HDX, avril 2023 à octobre 2026.",f"{a('ii','Insecurity Insight')}, an organisation that records attacks on aid and health care, via HDX, April 2023 to October 2026."),
    ("Le relevé ne couvre pas toutes les frappes et ne dit pas quel camp a frappé. L'année 2023 commence en avril, l'année 2026 s'arrête en octobre.","The record does not cover all strikes and does not say which side struck. The year 2023 starts in April and 2026 stops in October.")),
  P(f"Le Haut-Commissariat aux droits de l'homme a recensé {a('ohchr_may','au moins 880 civils tués par drone de janvier à avril 2026')}, soit plus de 80 % des civils tués qu'il a recensés sur cette période. En octobre 2026, des drones ont frappé trois marchés en neuf jours. Des sources locales ou des organisations de défense des droits attribuent les trois frappes à l'armée. Aucune réponse de l'armée n'a été trouvée dans les sources consultées. À Dibab, au Kordofan-Ouest, le 18 octobre, le Haut-Commissariat a compté {a('ohchr_oct','au moins 139 personnes tuées')}. À Amiet, dans la zone d'Abyei, le 19 octobre, la mission de l'ONU sur place a parlé de plus de 80 morts et {a('acled_amiet','ACLED')} de 150 à 220. À Nyala, le 26 octobre, les sources donnent entre 21 et plus de 100 morts {CON[0]}.",
    f"The UN human rights office recorded {a('ohchr_may','at least 880 civilians killed by drones from January to April 2026')}, more than 80% of the civilians it recorded killed in that period. In October 2026 drones struck three markets in nine days. Local sources or rights organisations attribute all three strikes to the army. No response from the army was found in the sources consulted. At Dibab, in West Kordofan, on 18 October, the human rights office counted {a('ohchr_oct','at least 139 people killed')}. At Amiet, in the Abyei area, on 19 October, the UN mission there spoke of more than 80 dead and {a('acled_amiet','ACLED')} of 150 to 220. At Nyala, on 26 October, sources give between 21 and more than 100 dead {CON[1]}."),
  P(f"Des drones ont aussi frappé le réseau électrique du nord. L'{a('ap_grid','agence Associated Press')} a compté quinze sous-stations touchées depuis début octobre 2026. La production est passée de 4 400 mégawatts avant la guerre à 1 100. Le gouvernement et une organisation de juristes attribuent ces frappes aux RSF, ce que retient aussi {a('acled_eth','ACLED')} {REP[0]}. L'aviation de l'armée largue par ailleurs des bombes non guidées sur des villes tenues par les RSF. {a('hrw_nyala','Human Rights Watch')} a documenté une frappe de ce type à Nyala le 3 février 2025. L'armée dément viser des civils.",
    f"Drones have also struck the power grid in the north. The {a('ap_grid','Associated Press')} counted fifteen substations hit since early October 2026. Output has fallen from 4,400 megawatts before the war to 1,100. The government and a lawyers' organisation attribute these strikes to the RSF, an attribution {a('acled_eth','ACLED')} shares {REP[1]}. The army's air force also drops unguided bombs on RSF-held towns. {a('hrw_nyala','Human Rights Watch')} documented one such strike on Nyala on 3 February 2025. The army denies targeting civilians."),
  H3("5. L'aide atteint peu les zones où l'on compte le plus de morts","5. Little aid reaches the areas with the most deaths"),
  P(f"Chaque camp contrôle les autorisations de passage vers la zone de l'autre. Le poste frontière d'Adré, entre le Tchad et le Darfour, fonctionne par {a('adre','autorisations de trois mois')} délivrées par le gouvernement dirigé par l'armée. Dans les zones des RSF, une agence créée par elles, la SARHO, exige depuis fin 2024 que les organisations s'enregistrent auprès d'elle. D'après {a('sarho','Reuters')}, la part des organisations signalant des retards de permis vers ces zones est passée de 20 à 30 % à 60 % en janvier 2025. Selon {a('acaps_access','ACAPS')}, le gouvernement a menacé de poursuites, le 28 janvier 2026, les organisations qui coopéreraient avec la SARHO.",
    f"Each side controls permits for crossing into the other's area. The Adré border post, between Chad and Darfur, operates on {a('adre','three-month authorisations')} issued by the army-led government. In RSF areas an agency it created, SARHO, has required organisations to register with it since late 2024. According to {a('sarho','Reuters')}, the share of organisations reporting permit delays into those areas rose from between 20% and 30% to 60% in January 2025. According to {a('acaps_access','ACAPS')}, on 28 January 2026 the government threatened legal action against organisations cooperating with SARHO."),
  P(f"Des convois ont été attaqués. Dans la nuit du 2 juin 2025, une attaque contre {a('alkoma','un convoi de quinze camions du PAM et de l’UNICEF')} à Al Koma, au Darfour-Nord, a tué cinq personnes. Aucun camp ne l'a revendiquée. En 2026, trois attaques ont eu lieu au Kordofan : sur {a('aj_feb','la route d’El Obeid à Kosti le 6 février')}, près de Dilling {a('un_convoy','le 30 août')}, où une frappe aérienne a détruit deux camions du PAM et 50 tonnes de vivres, et près de Dilling encore {a('aj_driver','le 3 octobre')}, où un chauffeur a été tué. Les sources consultées n'attribuent pas les deux dernières. Insecurity Insight a compté 187 travailleurs humanitaires tués au Soudan de 2023 à octobre 2026.",
    f"Convoys have been attacked. On the night of 2 June 2025 an attack on {a('alkoma','a fifteen-truck WFP and UNICEF convoy')} at Al Koma, in North Darfur, killed five people. No side claimed it. In 2026 three attacks took place in Kordofan: on {a('aj_feb','the El Obeid to Kosti road on 6 February')}, near Dilling {a('un_convoy','on 30 August')}, where an air strike destroyed two WFP trucks and 50 tonnes of food, and near Dilling again {a('aj_driver','on 3 October')}, where a driver was killed. The sources consulted do not attribute the last two. Insecurity Insight counted 187 aid workers killed in Sudan from 2023 to October 2026."),
  PIECE('ch-fund',("Le plan de réponse 2026 est financé à moitié","The 2026 response plan is half funded"),
    ("Plan de réponse humanitaire pour le Soudan, en milliards de dollars, par an. Aplat : reçu. Hachures : demandé et non reçu","Humanitarian response plan for Sudan, in billions of dollars, by year. Solid: received. Hatched: requested and not received"),
    (f"{a('fts','Service de suivi financier (FTS)')} de l'OCHA, relevé le 11 novembre 2026.",f"OCHA {a('fts','Financial Tracking Service (FTS)')}, read on 11 November 2026."),
    ("L'année 2026 n'est pas close. Le montant demandé a baissé d'un tiers entre 2025 et 2026 : le taux de financement monte alors que la somme reçue, 1,45 milliard, reste inférieure à celle de 2024, 1,89 milliard.","The year 2026 is not closed. The amount requested fell by a third between 2025 and 2026: the funding rate rises while the sum received, 1.45 billion, remains below that of 2024, 1.89 billion.")),
  P("Le plan de 2026 vise 20,4 millions de personnes sur 33,7 millions dans le besoin. En 2025, le nombre de personnes dans le besoin était de 30,4 millions.",
    "The 2026 plan targets 20.4 million people out of 33.7 million in need. In 2025 the number of people in need was 30.4 million."),
  H3("Déplacement et faim","Displacement and hunger"),
  ('nums',),
  PIECE('ch-idp',("Le Darfour accueille deux personnes déplacées sur trois","Darfur hosts two in three displaced people"),
    ("Personnes déplacées à l'intérieur du Soudan, par région d'accueil, en millions, de l'été 2023 au 31 août 2026","People displaced within Sudan, by host region, in millions, from summer 2023 to 31 August 2026"),
    (f"{a('dtm','Matrice de suivi des déplacements')} de l'Organisation internationale pour les migrations (OIM), via HDX.",f"International Organization for Migration (IOM) {a('dtm','Displacement Tracking Matrix')}, via HDX."),
    ("Le total inclut les personnes déjà déplacées avant avril 2023. Les mois sans nouveau relevé reprennent le précédent. La baisse depuis janvier 2025 vient des retours vers Khartoum et le centre. Elle ne décrit pas les conditions dans les lieux de retour.","The total includes people already displaced before April 2023. Months with no new reading repeat the previous one. The fall since January 2025 comes from returns to Khartoum and the centre. It does not describe conditions in the places of return.")),
  P(f"L'OIM comptait {a('iom_sep','8,6 millions de personnes déplacées et 5,1 millions de retours')} fin août 2026, après un maximum d'environ 11,6 millions en janvier 2025. Tawila, dans le Jebel Marra, {a('tawila','abritait environ 665 000 personnes déplacées')} en septembre 2026. Hors du Soudan, le Haut-Commissariat des Nations unies pour les réfugiés {a('unhcr_sit','comptait 3,7 millions de réfugiés et demandeurs d’asile')} arrivés depuis avril 2023, dont 1,5 million en Égypte, près d'un million au Tchad, 570 000 en Libye et 475 000 au Soudan du Sud.",
    f"IOM counted {a('iom_sep','8.6 million displaced people and 5.1 million returns')} at the end of August 2026, after a peak of about 11.6 million in January 2025. Tawila, in Jebel Marra, {a('tawila','sheltered about 665,000 displaced people')} in September 2026. Outside Sudan, the UN Refugee Agency {a('unhcr_sit','counted 3.7 million refugees and asylum seekers')} who had arrived since April 2023, including 1.5 million in Egypt, nearly a million in Chad, 570,000 in Libya and 475,000 in South Sudan."),
  P(f"Pour la période de février à mai 2026, l'IPC a classé {a('unicef_ipc','près de 19,5 millions de personnes en insécurité alimentaire aiguë')}, c'est-à-dire en phase 3 ou plus sur une échelle de 5, dont environ 135 000 en phase 5. Il ne classait alors aucune zone en famine et signalait un risque de famine dans quatorze zones.",
    f"For February to May 2026 the IPC classified {a('unicef_ipc','nearly 19.5 million people as acutely food insecure')}, that is, in phase 3 or above on a scale of 5, including about 135,000 in phase 5. It classified no area as in famine at that point and flagged a risk of famine in fourteen areas."),
  ('table',),
 ]),
 ('h2',("Où en est la médiation","Where mediation stands"),[
  P(f"Le 11 mai 2023, à Djeddah, l'armée et les RSF ont signé une {a('jeddah','déclaration')} par laquelle elles s'engageaient à protéger les civils et à faciliter l'aide. Ce texte n'était pas un cessez-le-feu. Le {a('quad_state','12 septembre 2025')}, les États-Unis, l'Arabie saoudite, les Émirats arabes unis et l'Égypte, réunis dans un groupe appelé le Quad, ont proposé une trêve humanitaire de trois mois, puis un cessez-le-feu permanent, puis une transition de neuf mois vers un gouvernement civil. Deux de ces quatre médiateurs sont accusés de soutenir un belligérant : les Émirats les RSF, l'Égypte l'armée.",
    f"On 11 May 2023, in Jeddah, the army and the RSF signed a {a('jeddah','declaration')} committing them to protect civilians and facilitate aid. The text was not a ceasefire. On {a('quad_state','12 September 2025')} the United States, Saudi Arabia, the United Arab Emirates and Egypt, meeting as a group known as the Quad, proposed a three-month humanitarian truce, then a permanent ceasefire, then a nine-month transition to a civilian government. Two of these four mediators are accused of backing a belligerent: the UAE the RSF, Egypt the army."),
  P(f"Les RSF ont {a('rsf_truce','annoncé le 6 novembre 2025')} qu'elles acceptaient la trêve humanitaire. L'armée ne l'a pas acceptée. D'après {a('dab_quad','Radio Dabanga')}, un média soudanais indépendant, elle a donné en juillet 2026 un accord de principe assorti de conditions, dont le retrait des RSF des villes. Le 6 octobre 2026, le général Burhan a déclaré qu'il n'y aurait pas de négociation.",
    f"The RSF {a('rsf_truce','announced on 6 November 2025')} that it accepted the humanitarian truce. The army has not accepted it. According to {a('dab_quad','Radio Dabanga')}, an independent Sudanese outlet, in July 2026 it agreed in principle, with conditions that included an RSF withdrawal from towns. On 6 October 2026 General Burhan said there would be no negotiation."),
  P("En novembre 2026, aucune trêve n'est en vigueur. L'armée tient la capitale et le centre, et avance au Kordofan-Nord. Les RSF tiennent les cinq capitales du Darfour et le Kordofan-Ouest. Les deux camps continuent de recevoir des armes de l'étranger. Les personnes tuées recensées chaque mois sont moins nombreuses qu'en 2025. De janvier à avril 2026, selon le Haut-Commissariat aux droits de l'homme, la plupart des civils tués l'ont été par des drones.",
    "In November 2026 no truce is in force. The army holds the capital and the centre and is advancing in North Kordofan. The RSF holds all five Darfur capitals and West Kordofan. Both sides continue to receive weapons from abroad. Fewer people are recorded killed each month than in 2025. From January to April 2026, according to the UN human rights office, most of the civilians killed were killed by drones."),
 ]),
]
NUMS=[("8,6 M","8.6 M",f"personnes déplacées dans le pays, 31 août 2026 (OIM)","people displaced within the country, 31 August 2026 (IOM)"),
      ("3,7 M","3.7 M","réfugiés et demandeurs d'asile arrivés à l'étranger depuis avril 2023 (HCR, 2 novembre 2026)","refugees and asylum seekers who have arrived abroad since April 2023 (UNHCR, 2 November 2026)"),
      ("19,5 M","19.5 M","personnes en insécurité alimentaire aiguë, soit 41 % de la population (IPC, février à mai 2026)","people acutely food insecure, 41% of the population (IPC, February to May 2026)"),
      ("33,7 M","33.7 M","personnes dans le besoin en 2026 (plan de réponse humanitaire)","people in need in 2026 (humanitarian response plan)")]
NUMS_SRC=((f"{a('dtm','OIM')}, {a('unhcr_sit','HCR')}, {a('ipc','IPC')}, plan de réponse 2026 via {a('hapi','HDX HAPI')}.",f"{a('dtm','IOM')}, {a('unhcr_sit','UNHCR')}, {a('ipc','IPC')}, 2026 response plan via {a('hapi','HDX HAPI')}."),
          ("Estimations arrondies. Chaque chiffre a sa date et sa méthode. Ils ne s'additionnent pas.","Rounded estimates. Each figure has its own date and method. They cannot be added together."))
TBL=(("Dans quatre États, plus d'un habitant sur deux a faim","In four states more than one inhabitant in two is hungry"),
     ("Tableau par État : contrôle en octobre 2026 en part des localités, part de la population en phase IPC 3 ou plus (février à mai 2026), personnes déplacées accueillies (31 août 2026, arrondi au millier), personnes tuées recensées (novembre 2025 à octobre 2026, arrondi à la dizaine), organisations déclarant une activité (janvier à juillet 2026)","Table by state: control in October 2026 as a share of localities, share of the population in IPC phase 3 or above (February to May 2026), displaced people hosted (31 August 2026, rounded to the thousand), people recorded killed (November 2025 to October 2026, rounded to ten), organisations reporting activity (January to July 2026)"),
     (f"Wikipédia, {a('ipc','IPC')}, {a('dtm','OIM')}, {a('acled_hdx','ACLED')}, relevé des présences opérationnelles de l'OCHA via {a('hapi','HDX HAPI')}.",f"Wikipedia, {a('ipc','IPC')}, {a('dtm','IOM')}, {a('acled_hdx','ACLED')}, OCHA operational presence via {a('hapi','HDX HAPI')}."),
     ("Les quatre États sont le Darfour-Nord, le Darfour-Sud, le Kordofan-Sud et le Darfour-Central. Une organisation présente ne signifie pas un besoin couvert. ACAPS estime que les données venant des zones tenues par les RSF sont minces et que les besoins y sont probablement sous-estimés.","The four states are North Darfur, South Darfur, South Kordofan and Central Darfur. An organisation present does not mean a need met. ACAPS assesses that data from RSF-held areas are thin and that needs there are probably underestimated."),
     ("Voir le tableau par État","Show the table by state"))
MAINMETA=(("L'armée tient le Nil, les RSF tiennent le Darfour","The army holds the Nile, the RSF holds Darfur"),
  ("Camp qui tient les villes de chaque localité, mois par mois, avril 2023 à octobre 2026. Cercles : personnes tuées recensées dans le mois. Le curseur fait défiler les mois","Side holding the towns of each locality, month by month, April 2023 to October 2026. Circles: people recorded killed in the month. The slider moves through the months"),
  (SRC_CTRL[0]+" Personnes tuées : ACLED.",SRC_CTRL[1]+" People killed: ACLED."),
  ("Chaque localité prend la couleur du camp qui tient ses villes : les surfaces sont une interprétation et surestiment le contrôle réel. Dans le désert, les zones en teinte claire couvrent un rayon de 150 km autour d'une ville suivie, et le reste est sans relevé. Après le 17 août 2026, seuls deux ajouts manuels apparaissent.","Each locality takes the colour of the side holding its towns: the areas are an interpretation and overstate real control. In the desert the lighter areas cover a 150 km radius around a tracked town, and the rest has no reading. After 17 August 2026 only two manual additions appear."))

MAN=json.load(open('manual_updates.json'))
def srcs(u): return ' '.join(f'<a href="{s}">[{i+1}]</a>' for i,s in enumerate(u['sources']))
KIND={'fix':("correction","correction"),'update':("mise à jour","update"),'contested':("contesté","contested")}
ST={'saf':("armée","army"),'rsf':("RSF","RSF"),'x':("disputé","disputed")}
MO_FR=['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre']
MO_EN=['January','February','March','April','May','June','July','August','September','October','November','December']
def mo(m,i): y,k=m.split('-'); return ((MO_FR,MO_EN)[i])[int(k)-1]+' '+y
NOTE=dict(
 fr={'Nyala':"La carte source donne Nyala aux RSF d'avril à juin 2023. La ville était disputée : l'armée tenait la base de la 16e division, que les RSF ont prise le 26 octobre 2023.",
  'Ed Daein':"La carte source donne Ed Daein aux RSF dès avril 2023. La garnison de l'armée est restée en place jusqu'au 21 novembre 2023, sans combats, par arrangement local.",
  'Al Muthalathu':"Triangle frontalier avec la Libye et l'Égypte. L'armée s'en est retirée le 11 juin 2025 et les RSF l'ont occupé. La carte source ne l'affiche qu'à partir de janvier 2026.",
  'Sodari':"L'armée et ses alliés sont entrés dans la ville le 25 septembre 2026. Sudan War Monitor a géolocalisé leur présence. Radio Tamazuj et Sudan Tribune ont rapporté l'annonce. La confirmation est faible. La ville est absente de la carte source et n'a pas de couleur avant cette date.",
  'Kazgeil':"La carte source la donne à l'armée. Sudan War Monitor rapporte que l'armée y est entrée le 5 novembre 2026 et que les RSF y sont revenues le soir même. La carte affiche cette situation de début novembre sur son dernier mois, octobre."},
 en={'Nyala':"The source map gives Nyala to the RSF from April to June 2023. The city was disputed: the army held the 16th Division base, which the RSF took on 26 October 2023.",
  'Ed Daein':"The source map gives Ed Daein to the RSF from April 2023. The army garrison stayed in place until 21 November 2023, without fighting, under a local arrangement.",
  'Al Muthalathu':"Border triangle with Libya and Egypt. The army withdrew on 11 June 2025 and the RSF occupied it. The source map only shows it from January 2026.",
  'Sodari':"The army and its allies entered the town on 25 September 2026. Sudan War Monitor geolocated their presence. Radio Tamazuj and Sudan Tribune reported the announcement. The confirmation is weak. The town is absent from the source map and has no colour before that date.",
  'Kazgeil':"The source map gives it to the army. Sudan War Monitor reports that the army entered on 5 November 2026 and the RSF returned the same evening. The map shows this early-November situation on its last month, October."})
def manual_list(i):
    lg=('fr','en')[i]; o=[]
    for u in MAN['updates']:
        per=mo(u['from'],i)+((' à ',' to ')[i]+mo(u['to'],i) if u.get('to') else (' et après',' onward')[i])
        o.append(f"<li><b>{u['town']}</b>, {per}, {ST[u['status']][i]} <span class='tag'>{KIND[u['kind']][i]}</span>. {NOTE[lg][u['town']]} {srcs(u)}</li>")
    return "<ul class='small'>"+"".join(o)+"</ul>"
METH=[
 (f"<b>Qui a vérifié quoi.</b> Le modèle de langage a cherché, ouvert et lu les sources en ligne le 11 novembre 2026. Certains articles, dont ceux du Sudan Tribune, n'ont pu être lus qu'en extrait. Les faits marqués « rapporté » ou « contesté » n'ont pas pu être établis. Quatre relectures automatiques indépendantes ont porté sur la lisibilité, le ton, l'équilibre entre les camps et les graphiques. Aucune personne connaissant le Soudan n'a encore relu cette note.",
  f"<b>Who checked what.</b> The language model searched for, opened and read the online sources on 11 November 2026. Some articles, including Sudan Tribune's, could only be read as excerpts. Facts marked 'reported' or 'contested' could not be established. Four independent automated reviews covered readability, tone, balance between the sides and the charts. No person who knows Sudan has yet reviewed this note."),
 (f"<b>Contrôle territorial.</b> {a('wiki','Carte détaillée de Wikipédia')}, un relevé par mois d'avril 2023 au 17 août 2026, licence CC BY-SA 4.0. Le module n'a pas été modifié depuis cette date, vérification faite le 11 novembre 2026. Les mois sans modification reprennent le mois précédent.",
  f"<b>Territorial control.</b> {a('wiki','Wikipedia detailed map')}, one snapshot a month from April 2023 to 17 August 2026, CC BY-SA 4.0. The module has not been edited since, as checked on 11 November 2026. Months with no edit repeat the previous month."),
 ("<b>Des villes aux zones.</b> Une localité prend la couleur majoritaire de ses villes suivies, pondérée par leur taille. Sans ville suivie, elle prend celle des trois villes les plus proches à moins de 250 km. Au-delà, elle reste sans couleur. Une ville n'a pas de couleur avant d'apparaître sur la carte source. Les localités désertiques de plus de 40 000 km² sont découpées autour de leurs villes, dans un rayon de 150 km.",
  "<b>From towns to areas.</b> A locality takes the majority colour of its tracked towns, weighted by size. With no tracked town, it takes that of the three nearest towns within 250 km. Beyond that it stays uncoloured. A town has no colour before it appears on the source map. Desert localities larger than 40,000 km² are split around their towns, within a 150 km radius."),
 ('MANUAL',("Corrections et ajouts faits à la main","Manual corrections and additions")),
 ("<b>Annonces non retenues.</b> Al-Mazroub (armée, 2 octobre 2026), Umm Sumayma (5 novembre), Iyal Bakhit (7 et 8 novembre) et plusieurs garnisons du Nil Bleu reposent sur l'annonce d'un camp ou sur une seule source indépendante. Elles ne figurent pas sur la carte.",
  "<b>Announcements not applied.</b> Al-Mazroub (army, 2 October 2026), Umm Sumayma (5 November), Iyal Bakhit (7 and 8 November) and several Blue Nile garrisons rest on one side's announcement or on a single independent source. They are not on the map."),
 (f"<b>Données ACLED.</b> ACLED (Armed Conflict Location & Event Data), acleddata.com, consulté le 11 novembre 2026 via HDX. Filtres : Soudan, violence politique et violences visant des civils, avril 2023 à octobre 2026. Transformation : agrégation par localité, par région et par mois. Les analyses tirées de ces données sont celles de l'auteur et non celles d'ACLED. Conditions d'usage : {a('acled_eula','EULA d’ACLED')}.",
  f"<b>ACLED data.</b> ACLED (Armed Conflict Location & Event Data), acleddata.com, accessed on 11 November 2026 via HDX. Filters: Sudan, political violence and violence targeting civilians, April 2023 to October 2026. Transformation: aggregation by locality, region and month. The analysis drawn from these data is the author's, not ACLED's. Terms of use: {a('acled_eula','ACLED EULA')}."),
 (f"<b>Autres données.</b> {a('cod','Limites administratives')} et {a('pop','population')} de l'OCHA. {a('dtm','OIM')} pour le déplacement. {a('ipc','IPC')} pour la sécurité alimentaire. {a('ii','Insecurity Insight')} pour les armes explosives et les travailleurs humanitaires. {a('hapi','HDX HAPI')} pour les prix du PAM, les besoins et les présences opérationnelles. {a('fts','FTS')} pour le financement. {a('unhcr_sit','HCR')} pour les réfugiés. Collecte par les scripts du dépôt {a('repo','humanitarian-secondary-data')}.",
  f"<b>Other data.</b> OCHA {a('cod','administrative boundaries')} and {a('pop','population')}. {a('dtm','IOM')} for displacement. {a('ipc','IPC')} for food security. {a('ii','Insecurity Insight')} for explosive weapons and aid workers. {a('hapi','HDX HAPI')} for WFP prices, needs and operational presence. {a('fts','FTS')} for funding. {a('unhcr_sit','UNHCR')} for refugees. Collected with the scripts of the {a('repo','humanitarian-secondary-data')} repository."),
 ("<b>Sources qui n'ont pas répondu.</b> ReliefWeb a refusé l'identifiant de l'application. Les données ACLED par événement, l'interface d'ACAPS et celle de l'Observatoire des situations de déplacement interne demandent une clé qui n'était pas configurée. Le PAM ne publie pas le Soudan sur HungerMap. Les rapports d'ACAPS et d'ACLED ont été lus sur leurs sites.",
  "<b>Sources that did not respond.</b> ReliefWeb refused the application identifier. ACLED event-level data, the ACAPS interface and that of the Internal Displacement Monitoring Centre require a key that was not configured. WFP does not publish Sudan on HungerMap. ACAPS and ACLED reports were read on their websites."),
 ("<b>Ce que la note ne couvre pas.</b> Les lignes de front réelles, le tracé exact des routes, le contrôle après le 17 août 2026, la mortalité indirecte liée à la faim et aux maladies à l'échelle du pays, la situation des personnes handicapées et des personnes âgées, les restes explosifs de guerre.",
  "<b>What the note does not cover.</b> Real front lines, the exact course of roads, control after 17 August 2026, indirect mortality from hunger and disease at national level, the situation of persons with disabilities and of older people, explosive remnants of war."),
]
FOOT=("Les désignations employées et la présentation des cartes n'impliquent aucune prise de position sur le statut d'un territoire ou le tracé d'une frontière. La frontière entre le Soudan et le Soudan du Sud n'est pas définitivement fixée, et le statut d'Abyei n'est pas déterminé. Données dérivées de Wikipédia sous licence CC BY-SA 4.0.",
      "The designations used and the presentation of the maps imply no position on the status of any territory or the course of any border. The border between Sudan and South Sudan is not finally settled, and the status of Abyei is not determined. Data derived from Wikipedia under CC BY-SA 4.0.")

UIW=dict(src=("Source.","Source."),lim=("Limite.","Limitations."))
def cartel(src,lim):
    return "".join(f"<p class='cartel L {lg}' lang='{lg}'><span><b>{UIW['src'][i]}</b> {src[i][0].upper()+src[i][1:] if not src[i].startswith('<') else src[i]}</span><span><b>{UIW['lim'][i]}</b> {lim[i]}</span></p>" for i,lg in enumerate(('fr','en')))
def bi(tag,pair,cls=''):
    c=(' '+cls) if cls else ''
    return f'<{tag} class="L fr{c}" lang="fr">{pair[0]}</{tag}><{tag} class="L en{c}" lang="en">{pair[1]}</{tag}>'
def head(t,s): return bi('p',t,'pt')+bi('p',s,'sub')
def frame(d,title): return f'<div class="map frame" data-tfr="{html.escape(title[0],quote=True)}" data-ten="{html.escape(title[1],quote=True)}" '+' '.join(f'data-{k}="{v}"' for k,v in d.items())+'></div>'
o=[]
o.append('<header>'+bi('span',HEAD['eyebrow'],'eyebrow')+bi('h1',HEAD['h1'])+bi('p',HEAD['src'],'src')+'</header>')
o.append('<section class="warn">'+bi('h2',WARN[0])+'<ul>'+''.join(bi('li',w) for w in WARN[1])+'</ul></section>')
o.append('<section><div class="chap">'+bi('h2',("Points clés","Key points"))+'</div><ol class="key">'+''.join(bi('li',k) for k in KEY)+'</ol></section>')
MAIN='<figure class="piece">'+head(MAINMETA[0],MAINMETA[1])+"""
  <div class="map" id="main">
    <div class="map-h"><span class="map-d" id="m-date"></span></div>
    <div id="m-svg"></div>
    <div class="map-l" id="m-leg"></div>
    <div class="player">
      <div class="ctl"><button type="button" id="play"></button><div class="sl"><input type="range" id="slider" min="0" value="0" aria-label="Mois / Month"><div class="sl-t" id="sl-ticks"></div></div></div>
      <p class="ev" id="m-ev"></p>
      <div class="mini"><span>"""+bi('span',("Personnes tuées, recensées par mois (ACLED)","People killed, recorded per month (ACLED)"))+""" · <b id="m-fat"></b></span><div id="ch-fat"></div></div>
    </div>
  </div>"""+cartel(MAINMETA[2],MAINMETA[3])+'</figure>'
for kind,title,blocks in S:
    o.append('<section><div class="chap">'+bi('h2',title)+'</div>')
    for b in blocks:
        if b[0]=='p': o.append(bi('p',(b[1],b[2])))
        elif b[0]=='h3': o.append(bi('h3',(b[1],b[2])))
        elif b[0]=='sides': o.append('<div class="sides">'+''.join(f'<div class="side s-{k}">'+bi('h4',t)+bi('p',p1)+bi('p',p2)+'</div>' for k,t,p1,p2 in SIDES)+'</div>')
        elif b[0]=='tl': o.append('<div class="tl">'+''.join(f'<div class="tl-y"><b>{y}</b><div>'+bi('p',t)+'</div></div>' for y,t in ORIG)+'</div>')
        elif b[0]=='main': o.append(MAIN)
        elif b[0]=='nums': o.append('<div class="piece"><div class="nums">'+''.join(f'<div><b class="L fr" lang="fr">{n[0]}</b><b class="L en" lang="en">{n[1]}</b>'+bi('span',(n[2],n[3]))+'</div>' for n in NUMS)+'</div>'+cartel(*NUMS_SRC)+'</div>')
        elif b[0]=='table': o.append('<figure class="piece">'+head(TBL[0],TBL[1])+'<details><summary>'+bi('span',TBL[4])+'</summary><div class="tw"><table id="tbl"></table></div></details>'+cartel(TBL[2],TBL[3])+'</figure>')
        elif b[0]=='piece':
            _,pid,t,s,src,lim,kw=b
            if 'map' in kw: inner=frame(kw['map'],t)
            elif 'pair' in kw: inner='<div class="pair">'+''.join(frame(d,t) for d in kw['pair'])+'</div>'
            else: inner=f'<div id="{pid}" class="chartbox"></div>'
            o.append('<figure class="piece">'+head(t,s)+inner+cartel(src,lim)+'</figure>')
    o.append('</section>')
o.append('<section><div class="chap">'+bi('h2',("Méthode et sources","Method and sources"))+'</div>')
for lg,i in (('fr','0'),('en','1')):
    i=int(i); o.append(f'<ul class="L {lg} meth" lang="{lg}">')
    for m in METH:
        if m[0]=='MANUAL': o.append(f'<li><details><summary><b>{m[1][i]}</b></summary>'+manual_list(i)+'</details></li>')
        else: o.append('<li>'+m[i]+'</li>')
    o.append('</ul>')
o.append('</section>')
o.append('<footer>'+bi('p',FOOT)+'</footer>')

page=f'''<title>Soudan, la guerre en cartes</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="La guerre au Soudan de 2023 à 2026 : pourquoi l’armée et les Forces de soutien rapide se battent, pourquoi tant de civils sont tués. Sources ouvertes. FR / EN.">
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
