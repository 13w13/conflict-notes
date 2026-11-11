# Génère index.html (FR + EN), deux habillages au choix du lecteur (Presse, Sombre).  python3 build.py
import html,re
YT="https://www.youtube.com/watch?v=2hJkprFnzhY"
TR="https://lexfridman.com/preston-stewart-michael-kofman-transcript"
def Q(fr,en): return ('q',fr,en)
def P(t,fr,en): return ('p',t,fr,en)
def F(f,t,title,desc,lim): return ('f',f,t,title,desc,lim)
def L(t,intro,items,outro=None): return ('l',t,intro,items,outro)
def N(t,title,rows,lim): return ('n',t,title,rows,lim)
def D(t): return ('d',t)
def C(k): return ('c',k)

HEAD=dict(
 eyebrow=("Notes de visionnage","Viewing notes"),
 h1=("La guerre en Ukraine, 2026","The war in Ukraine, 2026"),
 src=(f"Source : <a href='{YT}'>Lex Fridman Podcast #504</a>, YouTube, mis en ligne le 10 novembre 2026. Durée 2 h 53. Invités : Michael Kofman et Preston Stewart. <a href='{TR}'>Transcription officielle</a>.",
      f"Source: <a href='{YT}'>Lex Fridman Podcast #504</a>, YouTube, published 10 November 2026. Running time 2hr 53min. Guests: Michael Kofman and Preston Stewart. <a href='{TR}'>Official transcript</a>."),
 note=("Chaque horodatage ouvre la vidéo au passage qui fonde la phrase. Un clic agrandit les images. Les noms de lieux ukrainiens suivent la graphie des cartes de l'épisode.",
       "Each timestamp opens the video at the passage behind the sentence. Click an image to enlarge it. Ukrainian place names follow the spelling on the episode's maps."),
)
WARN=(("Avertissement","Disclaimer"),[
 ("Ces notes résument ce que disent deux analystes américains favorables à l'Ukraine. Personne ne les contredit pendant l'épisode, et aucun point de vue russe n'y est représenté. Elles rapportent leur point de vue, pas celui de l'auteur de ces notes ni de son employeur.",
  "These notes summarise what two American analysts who support Ukraine say. Nobody challenges them during the episode, and no Russian point of view is represented. The notes report the guests' view, not that of their author or of the author's employer."),
 ("En près de trois heures, l'épisode ne dit presque rien des conséquences de la guerre pour les civils, qui en supportent l'essentiel, ni des déplacements de population. Le sujet est militaire.",
  "In almost three hours the episode says next to nothing about the consequences of the war for civilians, who bear the brunt of it, or about displacement. The subject is military."),
 ("Les cartes de l'épisode citent DeepState, un projet ukrainien de cartographie du front, et l'Institute for the Study of War (ISW), un institut de recherche américain. Les ratios de drones viennent de ce que les invités ont vu ou entendu auprès d'unités ukrainiennes. Aucun de ces chiffres n'a été vérifié ici.",
  "The episode's maps credit DeepState, a Ukrainian front-mapping project, and the Institute for the Study of War (ISW), an American research institute. The drone ratios come from what the guests saw or heard with Ukrainian units. None of these figures has been verified here."),
 ("Michael Kofman dit lui-même ignorer si l'avantage ukrainien de 2026 va durer. Ces notes décrivent la situation de novembre 2026 et devront être relues après l'hiver. Un résumé simplifie : pour toute citation, la vidéo et la transcription font foi.",
  "Michael Kofman himself says he does not know whether Ukraine's 2026 advantage will last. These notes describe the situation in November 2026 and should be reread after the winter. A summary simplifies: for any quotation, the video and the transcript are authoritative."),
 ("Les captures d'écran appartiennent au Lex Fridman Podcast. Elles sont reprises à seule fin de commentaire, chacune avec sa source et un lien vers le passage de la vidéo.",
  "The stills belong to the Lex Fridman Podcast. They are reproduced for commentary only, each with its source and a link to the passage in the video."),
 ("Transparence : notes rédigées avec l'appui d'un modèle de langage, Claude (Anthropic, modèles Opus 5.5 et Fable 5.2), à partir de la transcription officielle et de la vidéo.",
  "Transparency: notes written with the support of a large language model, Claude (Anthropic, Opus 5.5 and Fable 5.2 models), from the official transcript and the video."),
])
GUESTS=[
 ("kofman.jpg","Michael Kofman",
  "Chercheur au Carnegie Endowment, spécialiste des armées russe et ukrainienne. Il anime le podcast <em>Russia Contingency</em> et se rend régulièrement auprès de brigades ukrainiennes. L'essentiel de l'analyse vient de lui.",
  "Senior fellow at the Carnegie Endowment, specialist in the Russian and Ukrainian militaries. He hosts the <em>Russia Contingency</em> podcast and regularly visits Ukrainian brigades. Most of the analysis is his."),
 ("stewart.jpg","Preston Stewart",
  "Diplômé de West Point, vétéran d'Afghanistan. Il couvre la guerre sur sa chaîne YouTube et dans le podcast <em>War and Conflict</em>. Il apporte le point de vue du soldat.",
  "West Point graduate, Afghanistan veteran. He covers the war on his YouTube channel and the <em>War and Conflict</em> podcast. He brings the soldier's point of view."),
]
KEY=[
 (78,"Selon Kofman, l'armée ukrainienne n'avait pas été dans une situation aussi favorable sur le terrain depuis l'été 2023, date de l'échec de sa contre-offensive. L'armée russe traverse sa période la plus difficile depuis l'hiver 2022-2023, quand sa propre offensive avait échoué. Il situe le tournant à l'été ou à l'automne 2025.",
  "According to Kofman, the Ukrainian army has not been in so favourable a position on the ground since summer 2023, when its counteroffensive failed. The Russian army is going through its most difficult period since the winter of 2022-23, when its own offensive failed. He puts the turning point in the summer or autumn of 2025."),
 (146,"La Russie mise désormais sur le bombardement stratégique, c'est-à-dire des frappes sur les villes, l'énergie et les infrastructures civiles loin du front. Kofman rappelle que cette méthode a rarement fait céder un pays, surtout quand l'offensive au sol piétine.",
  "Russia now leans on strategic bombardment, meaning strikes on cities, energy and civilian infrastructure far from the front. Kofman points out that this method has rarely made a country yield, least of all when the ground campaign is floundering."),
 (792,"Les statistiques attribuent aux drones 80 % des pertes. Seuls, ils ne tiendraient pourtant pas le terrain. Ils s'ajoutent aux défenses préparées, aux champs de mines et à l'artillerie, avec peu d'infanterie en première ligne.",
  "Statistics attribute 80% of casualties to drones. On their own, though, they would not hold the ground. They sit on top of prepared defences, minefields and artillery, with few infantry in the forward positions."),
 (717,"Le front n'est plus une ligne. Les drones frappent jusqu'à une quinzaine de kilomètres de part et d'autre, et entre les deux armées s'étend une zone grise que personne ne tient.",
  "The front is no longer a line. Drones strike up to about 15 km either side of it, and between the two armies lies a grey zone that nobody holds."),
 (5883,"Sur ses cartes, l'armée russe se déclare 10 à 15 km en avant de ses positions réelles. Elle planifie ensuite sur cette ligne fictive, à ses dépens.",
  "On its maps the Russian army claims to be 10 to 15 km ahead of where it is. It then plans on that fictional line, to its own cost."),
 (8387,"Les exigences russes n'ont presque pas changé depuis 2022 et dépassent ce que l'armée russe peut prendre. Celles de l'Ukraine suivent la ligne de front.",
  "Russia's demands have barely changed since 2022 and exceed what its army can take. Ukraine's follow the front line."),
 (9386,"Kofman n'attend pas de paix prochaine. Il juge possibles des trêves partielles, et dangereux un cessez-le-feu sans garanties de sécurité.",
  "Kofman does not expect peace soon. He considers partial truces possible, and a ceasefire without security guarantees dangerous."),
]
POD=("Lex Fridman Podcast #504, YouTube, 10 novembre 2026","Lex Fridman Podcast #504, YouTube, 10 November 2026")
S=[
 (60,("Où en est la guerre","Where the war stands"),[
  Q("Où en est la guerre ? Kofman répond en deux temps. Sur le front, l'armée ukrainienne connaît sa situation la plus favorable depuis 2023. À l'arrière, la campagne de frappes russe s'étend à de nouvelles cibles.",
    "Where does the war stand? Kofman answers in two halves. At the front, the Ukrainian army is in its most favourable position since 2023. In the rear, Russia's strike campaign is extending to new targets."),
  P(517,"La guerre est dans sa cinquième année. Les combats ont lieu à l'est et au sud-est. Kyiv n'est pas menacée au sol, mais des drones et des missiles la visent chaque jour.",
    "The war is in its fifth year. The fighting is in the east and south-east. Kyiv is not threatened on the ground, but it comes under drone and missile attack every day."),
  F("carte-ensemble.jpg",72,("La Russie tient la Crimée, le Luhansk et le sud-est","Russia holds Crimea, Luhansk and the south-east"),
    ("Territoire tenu par la Russie, en rouge. En orange, les villes du front citées dans ces notes, de Kupiansk au nord à Huliaipole au sud.","Russian-held territory, in red. In orange, the front-line towns named in these notes, from Kupiansk in the north to Huliaipole in the south."),
    ("L'écran cite DeepState et l'ISW et ne date pas la carte. Dans la zone grise, toute ligne est approximative.","The screen credits DeepState and ISW and gives the map no date. In the grey zone any line is approximate.")),
  P(595,"L'effort russe porte sur le reste du Donbas, la région formée des oblasts (provinces) de Luhansk et de Donetsk. Quatre villes y font obstacle : Sloviansk, Kramatorsk, Druzhkivka et Kostiantynivka, que les soldats appellent « Kostya » parce que le nom est trop long. Au nord, vers Sumy et Kharkiv, la Russie mène des incursions limitées pour se ménager une zone tampon.",
    "Russia's effort is aimed at the rest of the Donbas, the region made up of Luhansk and Donetsk oblasts (provinces). Four cities stand in the way: Sloviansk, Kramatorsk, Druzhkivka and Kostiantynivka, which soldiers call \"Kostya\" because the name is too long. In the north, near Sumy and Kharkiv, Russia conducts limited incursions to carve out a buffer zone."),
  P(686,"Ce qui est nouveau en 2026, c'est que l'Ukraine reprend du terrain. Deux offensives locales ont abouti, l'une près de Lyman, l'autre dans la région de Zaporizhzhia. Certaines opérations récentes ont repris plus de terrain que la contre-offensive de l'été 2023, pourtant conçue à une tout autre échelle.",
    "What is new in 2026 is that Ukraine is retaking ground. Two local offensives have succeeded, one near Lyman, the other in the Zaporizhzhia region. Some recent operations regained more ground than the summer 2023 counteroffensive, which had been planned on quite another scale."),
  F("front-2026.jpg",633,("En 2026, l'Ukraine reprend du terrain au nord de Lyman","In 2026 Ukraine retakes ground north of Lyman"),
    ("Gains de 2026, russes en rouge vif, ukrainiens en bleu. Le contour blanc entoure la « ceinture de forteresses », les quatre villes du Donbas que la Russie n'a pas prises.","2026 gains, Russia's in bright red, Ukraine's in blue. The white outline is the \"Fortress Belt\", the four Donbas cities Russia has not taken."),
    ("Carte de l'équipe du podcast, sans date précise ni source à l'écran.","Map by the podcast team, with no precise date or source on screen.")),
  P(293,"La Russie a gardé l'initiative pendant l'essentiel de 2024 et de 2025, au prix d'une offensive d'usure sur un front très large. Kofman voit la tendance s'inverser à l'automne 2025. Le graphique de l'épisode le montre mois par mois.",
    "Russia held the initiative for most of 2024 and 2025, at the price of a grinding offensive on a very broad front. Kofman sees the trend turn in the autumn of 2025. The episode's chart shows it month by month."),
  F("initiative.jpg",348,("Depuis fin 2025, la Russie avance moins et recule davantage","Since late 2025 Russia gains less and loses more"),
    ("Terrain gagné (rouge) et perdu (turquoise) par la Russie chaque mois, janvier 2023 à octobre 2026. Les pertes incluent le terrain passé en zone grise.","Ground gained (red) and lost (teal) by Russia each month, January 2023 to October 2026. Losses include ground that fell into the grey zone."),
    ("L'écran ne donne ni unité, ni échelle, ni source. Le titre résume la forme des barres, pas un chiffre.","The screen gives no unit, scale or source. The title sums up the shape of the bars, not a figure.")),
  P(379,"Reste l'arrière. Depuis l'automne 2022, la Russie frappe les centrales, les postes électriques et les chaufferies. En 2026, la liste s'est allongée : entrepôts, centres de données, écoles, établissements médicaux, centres commerciaux, trains. Les drones à hélice ont cédé la place à des drones à réaction, lancés par milliers chaque mois. Kofman juge incertaine l'issue de l'hiver pour les villes ukrainiennes.",
    "That leaves the rear. Since autumn 2022 Russia has struck power plants, substations and heating plants. In 2026 the list has grown: warehouses, data centres, schools, medical facilities, shopping centres, trains. Propeller drones have given way to jet-powered ones, launched by the thousand every month. Kofman considers the outcome of the winter for Ukrainian cities uncertain."),
  F("bombardement.jpg",160,("La Russie lance des milliers de drones chaque mois","Russia launches thousands of drones every month"),
    ("Drones (rouge) et missiles (rose) lancés sur l'Ukraine chaque mois, janvier 2025 à octobre 2026, soit 120 300 au total selon l'écran. Carte : attaques ayant touché chaque oblast, janvier 2025 à juillet 2026.","Drones (red) and missiles (pink) launched at Ukraine each month, January 2025 to October 2026, 120,300 in all according to the screen. Map: attacks with recorded hits per oblast, January 2025 to July 2026."),
    ("Lancements rapportés, sans source nommée. La dernière barre, hachurée, porte la mention « Air Force monthly count ». Non vérifié ici.","Reported launches, no source named. The last, hatched bar is labelled \"Air Force monthly count\". Not verified here.")),
 ]),
 (879,("Drones et zone grise","Drones and the grey zone"),[
  Q("À quoi ressemble ce front, et comment y avance-t-on encore ?","What does this front look like, and how does anyone still advance across it?"),
  P(717,"L'Ukraine ne tient pas une ligne continue. Elle tient des postes de trois soldats, séparés de plusieurs centaines de mètres. Autour, les drones frappent tout ce qui bouge jusqu'à une quinzaine de kilomètres de part et d'autre : les soldats appellent cette bande la <em>kill zone</em>. Entre les deux armées reste une zone grise que personne ne contrôle.",
    "Ukraine does not hold a continuous line. It holds three-man posts several hundred metres apart. Around them drones strike anything that moves up to about 15 km either side: soldiers call that band the kill zone. Between the two armies lies a grey zone that nobody controls."),
  F("defense-zonale.jpg",724,("Des postes de trois soldats tiennent le front, pas une ligne","Three-man posts hold the front, not a line"),
    ("Postes d'infanterie (cercles) de part et d'autre d'une zone grise (hachures), sous la surveillance des drones.","Infantry posts (circles) on either side of a grey zone (hatched), watched by drones."),
    ("Schéma simplifié de l'équipe du podcast. Il illustre un propos des invités et ne mesure rien.","Simplified diagram by the podcast team. It illustrates a point made by the guests and measures nothing.")),
  P(1057,"L'arme la plus répandue est le drone FPV, un petit quadricoptère chargé d'explosif que son pilote dirige par la caméra embarquée jusqu'à l'impact. Chaque camp en emploie 8 000 à 10 000 par jour. Ces drones ne sont pas autonomes. Une équipe compte deux ou trois personnes : un pilote, un navigateur, souvent un technicien.",
    "The commonest weapon is the FPV drone, a small quadcopter carrying explosives which its pilot steers through the onboard camera until impact. Each side uses 8,000 to 10,000 a day. These drones are not autonomous. A team is two or three people: a pilot, a navigator, often a technician."),
  P(1375,"Les vidéos publiées ne montrent que les frappes réussies. Une partie des drones est brouillée, tombe en panne ou n'explose pas. Une compagnie mécanisée ukrainienne qui part à l'assaut s'attend à encaisser près de 300 impacts.",
    "Published videos show only the strikes that worked. A share of drones is jammed, breaks down or fails to detonate. A Ukrainian mechanised company going into an assault expects to take close to 300 hits."),
  C('drones'),
  P(1518,"Comment avancer dans une zone pareille ? Une colonne blindée est repérée à 10, 20 ou 30 km du front et détruite avant d'y arriver. La Russie envoie donc des hommes seuls ou par petits groupes, à pied, à moto, en quad. Kofman dit avoir vu passer des Lada.",
    "How does anyone advance through that? An armoured column is spotted 10, 20 or 30 km from the front and destroyed before it arrives. So Russia sends men alone or in small groups, on foot, on motorbikes, on quad bikes. Kofman says he has seen Ladas."),
  P(1932,"Kofman parle d'un calcul sinistre et donne un exemple. Sur dix hommes, sept n'arrivent pas. Les trois autres ont trouvé un passage entre deux postes, et le groupe suivant l'emprunte. Trois à cinq kilomètres plus loin, ils atteignent les équipes de drones, qui pilotent et ne sont pas préparées à recevoir un assaut. Selon un volontaire américain cité par Preston Stewart, la méthode permet d'avancer à qui accepte de perdre 90 à 95 % de ses hommes.",
    "Kofman calls it a grim calculus and gives an example. Of ten men, seven do not make it. The other three have found a gap between two posts, and the next group uses it. Three to five kilometres further on they reach the drone teams, who are flying drones and are not prepared to receive an assault. According to an American volunteer quoted by Preston Stewart, the method gains ground for anyone prepared to lose 90 to 95% of their men."),
  P(1629,"Selon Kofman, l'Ukraine n'a pas ces effectifs et n'accepterait pas de telles pertes. Il décrit la guerre depuis 2025 comme une lutte pour la supériorité dans la kill zone. Les unités ukrainiennes les plus avancées localisent d'abord les équipes de drones russes, les frappent, coupent leur ravitaillement, puis attaquent. Certaines emploient des blindés pour aller vite. D'autres avancent par équipes de trois, une rangée d'arbres après l'autre.",
    "According to Kofman, Ukraine does not have the manpower and would not accept such losses. He describes the war since 2025 as a contest for superiority in the kill zone. The most advanced Ukrainian units first locate the Russian drone teams, strike them, cut their supplies, then attack. Some use armour to move fast. Others advance in three-man teams, one tree line after another."),
  P(2206,"Kofman observe qu'une parade trouve sa réponse en trois ou quatre mois. Contre le brouillage, la Russie a généralisé le drone à fibre optique : un fil aussi fin qu'un fil de pêche le relie au pilote, sur une distance qui atteint 50 km, et le brouillage ne l'arrête pas. Ces drones resteraient minoritaires, 15 % ou moins, chiffre que Kofman dit donner au jugé. Selon lui, l'Ukraine innove plus vite et la Russie généralise plus vite.",
    "Kofman observes that a countermeasure meets its response within three or four months. Against jamming, Russia rolled out the fibre-optic drone: a thread as thin as fishing line links it to the pilot over a distance of up to 50 km, and jamming does not stop it. These drones are thought to remain a minority, 15% or less, a figure Kofman says he is guessing. In his view Ukraine innovates faster and Russia scales up faster."),
  P(2465,"Presque tout le monde sur le front possède un détecteur qui ressemble à une vieille Game Boy. Kofman en garde un dans la voiture. Quand l'appareil sonne, son écran affiche ce que filme le drone ennemi. Les passagers regardent l'écran, puis par la vitre, pour savoir si la voiture à l'image est la leur. Contre un drone à fibre optique, l'appareil reste muet.",
    "Almost everyone at the front has a detector that looks like an old Game Boy. Kofman keeps one in the car. When it beeps, its screen shows what the enemy drone is filming. The passengers look at the screen, then out of the window, to work out whether the car in the picture is theirs. Against a fibre-optic drone it stays silent."),
  P(2574,"Cette guerre annonce-t-elle les suivantes ? Les deux invités restent prudents. Elle doit une grande part de sa forme à une particularité : aucun camp n'a la maîtrise du ciel, et aucun ne fait voler ses avions au-dessus de l'autre.",
    "Does this war foreshadow the next ones? Both guests are cautious. It owes much of its shape to a peculiarity: neither side controls the air, and neither flies its aircraft over the other's territory."),
 ]),
 (3109,("Qui gagne ?","Who is winning?"),[
  Q("Fridman pose la question que tout le monde pose. Les invités refusent d'y répondre par un nom.","Fridman asks the question everyone asks. The guests decline to answer with a name."),
  P(3131,"Pour Preston Stewart, les deux pays ne poursuivent pas le même but, et aucun score ne permet de les départager comme dans un match. Il fait remarquer que l'Allemagne et le Japon gagnaient pendant une grande partie de la Seconde Guerre mondiale.",
    "For Preston Stewart the two countries are not after the same thing, and no score can settle it as in a match. He points out that Germany and Japan were winning for much of the Second World War."),
  P(3312,"Kofman préfère parler d'avantage. L'Ukraine l'a en 2026. Il ignore si cet avantage est durable ou passager. Il ne prévoit d'effondrement dans aucun camp et rappelle le poids de l'hiver et des frappes.",
    "Kofman prefers to speak of advantage. Ukraine has it in 2026. He does not know whether that advantage is lasting or temporary. He foresees no collapse on either side and stresses the weight of the winter and the strikes."),
  L(3451,("Kofman distingue trois niveaux d'analyse. Il précise que des officiers d'état-major contestent l'existence du deuxième.","Kofman distinguishes three levels of analysis. He notes that staff officers dispute the existence of the second."),
    [("la tactique : comment on se bat sur le terrain ;","tactics: how the fighting is done on the ground;"),
     ("les opérations : comment on coordonne des unités, leur feu et leur ravitaillement vers un objectif ;","operations: how units, their fire support and their supplies are coordinated towards an objective;"),
     ("la stratégie : en quoi tout cela sert le but politique.","strategy: how all of that serves the political aim.")],
    ("Les dix prochains kilomètres ne décideront pas de la guerre. La carte indique en revanche qui aborde une négociation en position de force. Kofman ajoute qu'une stratégie dépend de ses hypothèses de départ. L'invasion de février 2022 en fournit l'exemple.",
     "The next ten kilometres will not decide the war. The map does show who enters a negotiation with leverage. Kofman adds that a strategy depends on its starting assumptions. The February 2022 invasion is the example.")),
 ]),
 (3806,("Retour à février 2022","Back to February 2022"),[
  Q("Retour en arrière. Que vaut un plan quand ses hypothèses politiques sont fausses ?","A step back. What is a plan worth when its political assumptions are wrong?"),
  P(3946,"Kofman avait prévu l'invasion, mais pas sa forme. Moscou préparait une prise de contrôle rapide : avancer vite, encercler la capitale, capturer ou isoler les dirigeants. Le plan supposait une résistance brève et un accueil favorable de la population. Il ne prévoyait aucune solution de repli.",
    "Kofman had predicted the invasion, but not its form. Moscow was preparing a rapid takeover: advance fast, encircle the capital, capture or isolate the leadership. The plan assumed brief resistance and a favourable welcome from the population. It had no fallback."),
  F("invasion.jpg",3811,("La Russie attaque par le nord, l'est et le sud","Russia attacks from the north, east and south"),
    ("Axes d'attaque le 24 février 2022. En rouge, ce que la Russie tenait déjà : la Crimée et une partie du Donbas. L'axe venu du Bélarus vise Kyiv.","Axes of attack on 24 February 2022. In red, what Russia already held: Crimea and part of the Donbas. The axis from Belarus aims at Kyiv."),
    ("L'écran cite l'ISW et VIINA. Les flèches schématisent des mouvements, elles ne tracent pas un front.","The screen credits ISW and VIINA. The arrows sketch movements, they do not trace a front.")),
  P(4388,"En face, la défense a été en grande partie improvisée. Kyiv attendait l'attaque dans le Donbas et y avait placé ses unités. Au nord de la capitale, il n'y avait presque aucune troupe régulière, et des volontaires ont grossi les rangs. Les analystes, reconnaît Kofman, en savaient plus sur le plan russe d'attaque que sur le plan ukrainien de défense.",
    "On the other side the defence was largely improvised. Kyiv expected the attack in the Donbas and had put its units there. North of the capital there were almost no regular troops, and volunteers swelled the ranks. Analysts, Kofman admits, knew more about Russia's plan of attack than about Ukraine's plan of defence."),
  P(4499,"Preston Stewart y voit d'abord une affaire de commandement. Une armée occidentale laisse un sergent de vingt ans décider sur place. L'armée russe attend l'ordre. Quand les colonnes se sont immobilisées sur la route de Kyiv, des officiers supérieurs ont dû s'avancer pour débloquer la circulation, et beaucoup y ont été tués dans les premières semaines.",
    "Preston Stewart sees it first as a matter of command. A Western army lets a twenty-year-old sergeant decide on the spot. The Russian army waits for the order. When the columns stalled on the road to Kyiv, senior officers had to go forward to clear the traffic, and many were killed there in the first weeks."),
 ]),
 (4754,("Bakhmut","Bakhmut"),[
  Q("Pour comprendre la mutinerie de Wagner, Kofman revient à la bataille qui a fait connaître cette société militaire privée et son dirigeant, Evgueni Prigojine.",
    "To explain the Wagner mutiny, Kofman goes back to the battle that brought that private military company and its head, Yevgeny Prigozhin, to prominence."),
  P(4890,"La bataille dure d'août 2022 à mai 2023. C'est un siège classique, mené à deux échelles. Dans la ville, on se bat d'immeuble en immeuble. Autour, on se bat pour les routes d'accès, et c'est ce second combat qui décide.",
    "The battle lasts from August 2022 to May 2023. It is a classic siege fought at two scales. Inside the city, the fighting goes building to building. Around it, the fight is for the access roads, and that second fight is the one that decides."),
  F("bakhmut.jpg",4861,("Bakhmut est en cuvette, dominée à l'est et à l'ouest","Bakhmut sits in a bowl, overlooked from east and west"),
    ("En rouge, le territoire tenu par la Russie au début de la bataille. Tout se décide sur les flancs : Soledar au nord, la route de Chasiv Yar à l'ouest.","In red, Russian-held territory as the battle begins. It is decided on the flanks: Soledar to the north, the Chasiv Yar road to the west."),
    ("Carte de l'équipe du podcast, sans source à l'écran.","Map by the podcast team, no source on screen.")),
  P(5057,"Côté russe, l'assaut revient à Wagner, autorisée à recruter dans les prisons. Elle envoie les détenus par groupes successifs, jusqu'à ce que les défenseurs soient épuisés et à court de munitions, puis ses soldats expérimentés. Pendant ce temps, l'artillerie russe détruit la ville. À la fin, observe Kofman, les forces russes n'ont à peu près rien pris, puisqu'il ne restait à peu près rien. Prigojine a parlé de 20 000 tués dans ses rangs.",
    "On the Russian side the assault falls to Wagner, which has been allowed to recruit in prisons. It sends the convicts in successive groups until the defenders are exhausted and short of ammunition, then its experienced soldiers. Meanwhile Russian artillery destroys the city. By the end, Kofman observes, Russian forces had taken next to nothing, because next to nothing was left. Prigozhin put his dead at 20,000."),
  P(5407,"Le « syndrome de Bakhmut » consiste à défendre une ville au-delà du point où cela se justifie. Kyiv craignait qu'une perte visible n'affaiblisse le soutien occidental, et a déclaré la ville « forteresse ». Kofman dit que ce mot l'inquiète, comme il inquiète les soldats : il annonce qu'aucun repli ne sera autorisé à temps. Des troupes aguerries y ont été engagées, pendant que la contre-offensive de l'été 2023 revenait à des unités neuves. Le débat sur le prix payé reste ouvert.",
    "\"Bakhmut syndrome\" means defending a city beyond the point where it makes sense. Kyiv feared a visible loss would weaken Western support, and declared the city a \"fortress\". Kofman says the word worries him, as it worries the soldiers: it means no timely withdrawal will be allowed. Seasoned troops were committed there, while the summer 2023 counteroffensive went to new units. The debate about the price paid remains open."),
  P(5215,"Avec le recul, il juge que la perte de Bakhmut a peu compté : il a fallu un an à l'armée russe pour atteindre la ville suivante, Chasiv Yar.",
    "With hindsight he thinks losing Bakhmut mattered little: it took the Russian army a year to reach the next town, Chasiv Yar."),
  F("chasiv-yar.jpg",5249,("L'armée russe a mis un an pour atteindre Chasiv Yar","The Russian army took a year to reach Chasiv Yar"),
    ("Environ 11 km séparent les deux villes (« about 7 miles » à l'écran). En rouge, le territoire tenu par la Russie en août 2025, après une autre année passée à prendre une grande partie de Chasiv Yar.","The two towns are about 11 km apart (\"about 7 miles\" on screen). In red, Russian-held territory in August 2025, after another year spent taking much of Chasiv Yar."),
    ("Carte de l'équipe du podcast, sans source à l'écran.","Map by the podcast team, no source on screen.")),
  L(5622,("À quoi reconnaît-on qu'une position n'est plus tenable ? Kofman donne trois signes :","How do you know a position can no longer be held? Kofman gives three signs:"),
    [("l'encerclement menace ;","encirclement threatens;"),
     ("la ravitailler coûte des hommes et du matériel ;","resupplying it costs men and equipment;"),
     ("il faut contre-attaquer pour seulement rester sur place.","you have to counterattack merely to stay where you are.")],
    ("Pour Preston Stewart, Kostiantynivka commence à y ressembler.","To Preston Stewart, Kostiantynivka is starting to look like that.")),
 ]),
 (5696,("Déclarer et tenir","Claiming and holding"),[
  Q("Moscou avait déclaré Bakhmut prise bien avant de la tenir. D'où la question : que signifie contrôler un territoire ?",
    "Moscow declared Bakhmut taken well before it held it. Hence the question: what does controlling territory mean?"),
  P(5990,"Kofman retient un critère : pouvoir s'en servir. Être présent ne suffit pas si l'on ne peut pas y circuler librement. Preston Stewart situe ce contrôle réel à 20 km ou plus derrière le front.",
    "Kofman uses one test: being able to use it. Presence is not enough if you cannot move around freely. Preston Stewart places that real control 20 km or more behind the front."),
  P(5730,"L'armée russe fait autrement. Un soldat atteint un village et agite un drapeau devant un drone. La position est portée sur la carte, et tout ce qui se trouve derrière est déclaré tenu. La semaine de l'enregistrement, une de ces vidéos avait été fabriquée par intelligence artificielle. Des Russes l'ont signalé eux-mêmes.",
    "The Russian army does it differently. A soldier reaches a village and waves a flag in front of a drone. The position goes on the map, and everything behind it is declared held. In the week of the recording, one such video had been made with artificial intelligence. Russians pointed it out themselves."),
  C('claimed'),
  P(5921,"L'écart a un coût. L'artillerie et l'aviation règlent leur appui sur une ligne fausse. Une unité de relève reçoit une carte inexacte et rencontre l'adversaire là où elle attendait les siens. En octobre et en novembre, le commandement demande à voir le terrain déclaré depuis des mois, et les assauts s'intensifient pour prendre le terrain déjà déclaré.",
    "The gap has a cost. Artillery and aircraft set their support on a false line. A relieving unit is handed an inaccurate map and meets the enemy where it expected its own side. In October and November the command asks to see the ground reported as taken for months, and the assaults intensify to take the ground already claimed."),
  F("ligne-revendiquee.jpg",5956,("L'armée russe planifie sur une ligne qu'elle ne tient pas","The Russian army plans on a line it does not hold"),
    ("La ligne déclarée (tirets, à gauche) précède de 10 à 15 km la ligne tenue (trait plein, à droite). Les drapeaux marquent les positions déclarées. Zone quadrillée : les assauts d'octobre et de novembre.","The claimed line (dashed, left) runs 10 to 15 km ahead of the held line (solid, right). Flags mark claimed positions. Cross-hatched area: the October and November assaults."),
    ("Schéma simplifié de l'équipe du podcast. Il illustre le propos de Kofman et ne mesure rien.","Simplified diagram by the podcast team. It illustrates Kofman's point and measures nothing.")),
  P(6142,"Kupiansk en est l'exemple. Il y a un an, le chef d'état-major Valeri Guerassimov annonçait à Vladimir Poutine que les unités ukrainiennes y étaient encerclées. Kofman se trouvait alors juste à l'ouest de la ville, avec un collègue d'une brigade ukrainienne, et y lisait la nouvelle.",
    "Kupiansk is the example. A year ago the chief of the general staff, Valery Gerasimov, told Vladimir Putin that the Ukrainian units there were encircled. Kofman was just west of the city at the time, with a colleague from a Ukrainian brigade, reading the news."),
  F("kupiansk.jpg",6105,("Moscou a déclaré prise une ville qu'elle ne tenait pas","Moscow declared captured a city it did not hold"),
    ("Kupiansk, décembre 2025. Tirets roses : zone déclarée prise en novembre 2025. Rouge : ce que la Russie tient. Hachures : zone grise. Point blanc : lieu de la vidéo de Volodymyr Zelensky à l'entrée de la ville.","Kupiansk, December 2025. Pink dashes: area declared captured in November 2025. Red: what Russia holds. Hatching: grey zone. White dot: where Volodymyr Zelensky filmed his video at the city's entrance."),
    ("Carte de l'équipe du podcast, sans source à l'écran. Ici les hachures désignent la zone grise, pas le terrain déclaré.","Map by the podcast team, no source on screen. Here the hatching marks the grey zone, not the claimed ground.")),
  P(6248,"Pourquoi ces faux rapports ? Kofman y voit un effet de la culture militaire russe. Toute erreur y est punie, ce qui incite à mentir ; soldats et officiers se font peu confiance ; les décisions se prennent en haut, sur ce qui remonte d'en bas. L'armée ukrainienne a connu de faux rapports elle aussi, précise-t-il, et des commandants ont été relevés pour cela.",
    "Why the false reports? Kofman puts them down to Russian military culture. Every mistake is punished, which is an incentive to lie; soldiers and officers do not trust each other; decisions are made at the top on what filters up from below. The Ukrainian army has had false reports too, he adds, and commanders have been relieved over them."),
  F("cultures-militaires.jpg",6253,("L'armée russe décide en haut, l'armée ukrainienne délègue","Russia's army decides at the top, Ukraine's delegates"),
    ("Cercles jaunes : les échelons qui décident. Sous le schéma, les trois effets cités côté russe : peu de confiance, sanction de toute erreur, centralisation.","Yellow rings: the levels that decide. Under the diagram, the three effects cited on the Russian side: little trust, punishment for any mistake, centralisation."),
    ("Schéma de l'équipe du podcast, capturé en cours d'animation : une seule des trois lignes est éclairée.","Diagram by the podcast team, captured mid-animation: only one of the three lines is lit.")),
  P(6545,"La conversation remonte alors d'un cran, vers ceux qui décident des guerres. Ils les croient courtes et écartent les avis contraires. Kofman cite l'invasion de 2022 et la guerre des États-Unis contre l'Iran en 2026.",
    "The conversation then moves up a level, to those who decide on wars. They believe they will be short and set aside contrary advice. Kofman cites the 2022 invasion and the United States' war with Iran in 2026."),
 ]),
 (6905,("La mutinerie de Prigojine","Prigozhin's mutiny"),[
  Q("Fridman revient à la question posée une demi-heure plus tôt : que dit la mutinerie de l'armée russe ?","Fridman returns to the question he asked half an hour earlier: what does the mutiny say about the Russian army?"),
  P(7023,"Prigojine attaquait publiquement le ministre de la Défense, Sergueï Choïgou, et le chef d'état-major. Après Bakhmut, le ministère exige que tous les hommes de Wagner signent un contrat avec l'armée. Prigojine y perd le commandement de ses troupes.",
    "Prigozhin publicly attacked the defence minister, Sergei Shoigu, and the chief of the general staff. After Bakhmut the ministry requires all Wagner's men to sign contracts with the army. Prigozhin stands to lose command of his troops."),
  P(7132,"Les 23 et 24 juin 2023, Wagner occupe le quartier général de Rostov, et deux colonnes prennent la route de Moscou. Elles ont des chars et de la défense aérienne, et abattent des appareils russes. Kofman parle d'une mutinerie en temps de guerre ; des analystes qu'il cite y voient plutôt une forme de pétition. Personne, dans l'élite, ne s'est rallié. Prigojine négocie une amnistie. Son avion explose en vol le 23 août 2023.",
    "On 23 and 24 June 2023 Wagner occupies the Rostov headquarters, and two columns take the road to Moscow. They have tanks and air defence, and shoot down Russian aircraft. Kofman calls it a mutiny in wartime; analysts he cites see it more as a kind of petition. Nobody in the elite rallied to him. Prigozhin negotiates an amnesty. His plane explodes in mid-air on 23 August 2023."),
  P(7590,"Wagner a été démantelée, même si une partie de son encadrement sert encore dans l'Africa Corps. L'armée a repris ses méthodes : le recrutement de détenus et les compagnies d'assaut réparties dans les unités régulières. Kofman y voit une spécialisation excessive. L'armée russe sait mener de petits assauts et peine à conduire des opérations plus vastes.",
    "Wagner was dismantled, though part of its leadership still serves in the Africa Corps. The army took up its methods: recruiting convicts and spreading assault companies across regular units. Kofman sees over-specialisation. The Russian army can run small assaults and struggles to conduct larger operations."),
 ]),
 (7760,("Buts de guerre et moyens","War aims and means"),[
  Q("Ce que Moscou exige correspond-il à ce que son armée peut prendre ? Kofman répond que non.","Does what Moscow demands match what its army can take? Kofman's answer is no."),
  P(7951,"Il découpe la guerre en deux. Les trente premiers jours ont tranché la question de l'indépendance de l'Ukraine. La suite porte sur ses frontières, son économie et ses alliances. Les exigences russes sont pourtant restées celles du début, alors que celles de Kyiv se sont rapprochées de ce que son armée peut tenir.",
    "He cuts the war in two. The first thirty days settled the question of Ukraine's independence. What followed concerns its borders, economy and alliances. Yet Russia's demands have stayed those of the start, while Kyiv's have moved close to what its army can hold."),
  D(8087),
  F("negociations.jpg",8124,("La Russie exige le Donbas qu'elle n'a pas pris","Russia demands the Donbas it has not taken"),
    ("Hachures : le reste du Donbas, autour de Sloviansk et de Kramatorsk, un peu plus de 20 % de la région selon Kofman.","Hatching: the rest of the Donbas, around Sloviansk and Kramatorsk, just over 20% of the region according to Kofman."),
    ("Carte de l'équipe du podcast, sans source à l'écran. Ici les hachures désignent le terrain exigé.","Map by the podcast team, no source on screen. Here the hatching marks the ground demanded.")),
  P(8431,"Moscou réclame aussi la totalité des oblasts de Zaporizhzhia et de Kherson. Preston Stewart note que prendre le reste de Kherson supposerait de franchir le Dniepr, ce dont il ne juge pas l'armée russe capable aujourd'hui.",
    "Moscow also demands all of Zaporizhzhia and Kherson oblasts. Preston Stewart notes that taking the rest of Kherson would mean crossing the Dnipro, which he does not think the Russian army capable of today."),
  P(7867,"Aucun des deux présidents ne règle le détail des combats, même si Stewart juge Poutine un peu plus impliqué. Kofman estime que Volodymyr Zelensky reçoit une image plus exacte du front.",
    "Neither president runs the detail of the fighting, though Stewart thinks Putin a little more involved. Kofman reckons Volodymyr Zelensky gets a more accurate picture of the front."),
  P(8715,"Combien de temps cela peut-il durer ? Selon Kofman, les deux pays ont de quoi poursuivre en 2027, chacun grâce à des soutiens extérieurs. Preston Stewart reconnaît avoir attendu davantage des sanctions, et une réaction plus vive de la société russe aux pertes.",
    "How long can it last? According to Kofman, both countries have the means to continue into 2027, each thanks to outside backers. Preston Stewart admits he expected more from sanctions, and a sharper reaction from Russian society to the losses."),
  N(8715,("La Russie consacre près de la moitié de son budget à la guerre","Russia spends almost half its budget on the war"),
    [("44 %","du budget de l'État russe, soit 9 à 10 % du PIB","44%","of Russia's state budget, or 9 to 10% of GDP"),
     ("Plus de 30 000","soldats russes tués ou blessés par mois, selon Preston Stewart","Over 30,000","Russian soldiers killed or wounded each month, according to Preston Stewart"),
     ("40 %","des obus russes fournis par la Corée du Nord, à un moment de la guerre","40%","of Russian shells supplied by North Korea, at one point in the war")],
    ("Chiffres donnés de mémoire par les invités, sans source citée. Non vérifiés ici.","Figures given from memory by the guests, with no source cited. Not verified here.")),
 ]),
 (8838,("Le rôle des États-Unis","The role of the United States"),[
  Q("Que pèsent encore les États-Unis ?","How much does the United States still count?"),
  P(8855,"Ils ne versent plus d'aide financière directe. Ils fournissent des armes et des munitions que les Européens paient, ainsi que du renseignement.",
    "It no longer gives direct financial aid. It supplies weapons and ammunition that Europeans pay for, as well as intelligence."),
  P(9281,"Les deux invités critiquent l'approche de l'administration Trump. Washington dirigeait la coalition et s'est présenté en arbitre neutre. Selon eux, il y a perdu son influence sur Kyiv et la confiance des Européens, sans que Moscou le tienne pour neutre.",
    "Both guests criticise the Trump administration's approach. Washington led the coalition and then cast itself as a neutral arbiter. In their view it lost its influence over Kyiv and the trust of Europeans, without Moscow ever regarding it as neutral."),
  P(9076,"Kofman reconnaît pourtant un effet à la nouvelle administration : elle a obligé chaque partie à formuler ses conditions. La précédente n'avait pas de plan pour terminer la guerre, les Européens non plus. « Aussi longtemps qu'il le faudra », dit-il, est un slogan, pas un plan.",
    "Kofman does credit the new administration with one effect: it made each party state its conditions. The previous one had no plan to end the war, nor did the Europeans. \"As long as it takes\", he says, is a slogan, not a plan."),
 ]),
 (9373,("Perspectives de paix","Prospects for peace"),[
  Q("À quoi ressemblerait une sortie, et pourquoi Kofman n'y croit-il pas pour l'instant ?","What would a way out look like, and why does Kofman not believe in one yet?"),
  P(9386,"Il ne voit pas la Russie disposée à négocier. Elle demande que toutes les questions de fond soient réglées avant un cessez-le-feu. Poutine, pense-t-il, attend l'issue de l'hiver et celle des élections du printemps en Europe, dont l'élection française.",
    "He does not see Russia willing to negotiate. It asks for every underlying issue to be settled before a ceasefire. Putin, he thinks, is waiting for the outcome of the winter and of Europe's spring elections, France's among them."),
  P(9671,"Une avancée, si elle vient, serait limitée. Les deux camps cesseraient de frapper les infrastructures essentielles et les navires en mer Noire. Un cessez-le-feu de quelques jours ou de quelques semaines pourrait suivre.",
    "Progress, if it comes, would be limited. Both sides would stop striking critical infrastructure and shipping in the Black Sea. A ceasefire of a few days or weeks might follow."),
  P(9587,"Ce que Kofman redoute, c'est un cessez-le-feu qui ne serait qu'une feuille de papier portant ce mot, sans garant extérieur. L'Ukraine finirait par démobiliser des hommes qui veulent rentrer chez eux. L'armée russe, faite de soldats sous contrat, pourrait rester en place et se réarmer. Six à huit mois plus tard, l'Ukraine serait très vulnérable. Il rappelle un précédent : les deux accords de Minsk, après 2014, n'ont jamais débouché sur un règlement.",
    "What Kofman fears is a ceasefire that is only a piece of paper with that word on it, with no outside guarantor. Ukraine would eventually have to demobilise men who want to go home. The Russian army, made up of contract soldiers, could stay put and rearm. Six to eight months on, Ukraine would be highly exposed. He recalls a precedent: the two Minsk agreements, after 2014, never led to a settlement."),
  P(9871,"Et après ? Kofman pense que l'Ukraine restera un État viable si les pays européens la considèrent comme l'un des leurs. Il ajoute que la guerre n'est pas celle du seul Poutine : des centaines de milliers de Russes ont signé un contrat pour combattre.",
    "And afterwards? Kofman thinks Ukraine will remain a viable state if European countries regard it as one of their own. He adds that the war is not Putin's alone: hundreds of thousands of Russians signed a contract to fight."),
 ]),
 (10013,("La dernière question","The last question"),[
  Q("Dernière question de Fridman : qu'est-ce qui vous donne de l'espoir ? Chacun répond par une évacuation.","Fridman's last question: what gives you hope? Each guest answers with an evacuation."),
  P(10129,"Stewart raconte celle de deux soldats ukrainiens, ramenés l'un après l'autre sur 30 km dans une nacelle accrochée sous un drone. L'équipe parle au blessé pendant tout le vol. Kofman raconte celle d'un commandant de compagnie qui part en pick-up, sans gilet pare-balles, chercher deux blessés immobilisés dans un robot d'évacuation qu'un drone russe vient de toucher. Il les charge l'un après l'autre et repart. Sur le front, dit Kofman, on voit le pire et le meilleur, parfois le même jour.",
    "Stewart tells of two Ukrainian soldiers flown out one after the other over 30 km in a pod slung under a drone. The crew talks to the wounded man throughout the flight. Kofman tells of a company commander who sets off in a pickup, without body armour, to fetch two wounded men stranded in an evacuation robot a Russian drone has just hit. He loads them one after the other and drives away. At the front, Kofman says, you see the worst and the best, sometimes on the same day."),
 ]),
]
METHOD=(("Méthode","Method"),[
 ("Ces notes suivent l'ordre de la conversation. Chaque chapitre s'ouvre sur la question posée par Lex Fridman, ou sur le lien que font les invités avec ce qui précède.",
  "These notes follow the order of the conversation. Each chapter opens with the question Lex Fridman asked, or with the link the guests make to what came before."),
 ("Le texte a été comparé ligne à ligne à la transcription officielle, puis relu par deux relecteurs automatiques indépendants, l'un pour la langue et le fil, l'autre pour les graphiques. Les chiffres qui ne figurent qu'à l'écran sont signalés dans la ligne « Limite » de la pièce concernée.",
  "The text was compared line by line with the official transcript, then reread by two independent automated reviewers, one for language and flow, the other for the graphics. Figures that appear only on screen are flagged in the \"Caveat\" line of the piece concerned."),
 ("Trois faits ont été recoupés auprès d'une seconde source : la mutinerie des 23 et 24 juin 2023, la mort de Prigojine le 23 août 2023 et la vidéo de Volodymyr Zelensky à Kupiansk en décembre 2025. Les événements de 2026 n'ont pas pu l'être.",
  "Three facts were cross-checked against a second source: the mutiny of 23 and 24 June 2023, Prigozhin's death on 23 August 2023 and Volodymyr Zelensky's video in Kupiansk in December 2025. The events of 2026 could not be."),
])
UI=dict(guests=("Les invités","The guests"),key=("Points clés","Key points"),zoom=("Agrandir","Enlarge"),
 src=("Source.","Source."),lim=("Limite.","Caveat."),
 at=("capture à","still at"),atp=("passage à","passage at"),
 portraits=("Portraits : captures du Lex Fridman Podcast #504, YouTube.","Portraits: stills from Lex Fridman Podcast #504, YouTube."),
 foot=("Texte : notes personnelles, sans lien avec l'employeur de l'auteur. Images : captures du Lex Fridman Podcast #504, © Lex Fridman, reprises à seule fin de commentaire.",
       "Text: personal notes, unrelated to the author's employer. Images: stills from Lex Fridman Podcast #504, © Lex Fridman, reproduced for commentary only."))
NB=" "; NNB=" "
def nb(s,i):
    """Espaces insécables, français seulement, hors balises."""
    if i: return s
    out=[]
    for part in re.split(r'(<[^>]+>)',s):
        if not part.startswith('<'):
            part=re.sub(r'(\d) (\d{3})\b',r'\1'+NNB+r'\2',part)
            part=re.sub(r'(\d) (%|km²|km|h|PIB)',r'\1'+NB+r'\2',part)
            part=re.sub(r' ([:;?!»])',NB+r'\1',part)
            part=part.replace('« ','«'+NB)
            part=re.sub(r'(\d) (à|ou) (\d)',r'\1'+NB+r'\2 \3',part)
        out.append(part)
    return ''.join(out)
def hms(t): return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}" if t>=3600 else f"{t//60}:{t%60:02d}"
def yt(t,cls=''): return f"<a{cls} href='{YT}&amp;t={max(t-2,0)}s' target='_blank' rel='noopener'>{hms(t)}</a>"
def cartel(src,lim,i): return f"<p class='cartel'><span><b>{UI['src'][i]}</b> {src}</span><span><b>{UI['lim'][i]}</b> {nb(lim,i)}</span></p>"

def chart(k,i):
    if k=='claimed':
        t=("La Russie déclare plus de terrain qu'elle n'en prend","Russia claims more ground than it takes")[i]
        d=("Surface que l'état-major russe déclare avoir prise en Ukraine, et surface mesurée par l'Institute for the Study of War (ISW), en km²","Area Russia's General Staff claims to have taken in Ukraine, and area measured by the Institute for the Study of War (ISW), in km²")[i]
        rows=[(("Janvier à mi-décembre 2025","January to mid-December 2025")[i],6300,4700),(("Janvier à avril 2026","January to April 2026")[i],1700,382)]
        lab=(("déclaré","mesuré"),("claimed","measured"))[i]
        nf=(lambda v:f"{v:,}".replace(",",NNB)) if i==0 else (lambda v:f"{v:,}")
        h=f"<div class='piece'><p class='pt'>{nb(t,i)}</p><p class='sub'>{nb(d,i)}</p><div class='bars'>"
        for name,a,b in rows:
            h+=f"<div class='bar-g'><span class='bar-n'>{name}</span><div class='bar-r'><b>{nf(a)} <em>{lab[0]}</em></b><span class='bar-t'><i class='bar hatch' style='width:{a/63:.1f}%'></i></span></div><div class='bar-r'><b>{nf(b)} <em>{lab[1]}</em></b><span class='bar-t'><i class='bar full' style='width:{b/63:.1f}%'></i></span></div></div>"
        src=(f"État-major russe et ISW, cités sur un graphique de l'épisode à {yt(5728)}.",f"Russian General Staff and ISW, credited on a chart in the episode at {yt(5728)}.")[i]
        lim=("Chiffres lus à l'écran, absents de la transcription et non recoupés avec les publications de l'ISW.","Figures read off the screen, absent from the transcript and not cross-checked against ISW publications.")[i]
        return h+"</div>"+cartel(src,lim,i)+"</div>"
    if k=='drones':
        t=("Il faut plusieurs drones par cible","It takes several drones per target")[i]
        d=("Nombre de drones FPV employés par cible, ordres de grandeur donnés par Michael Kofman et Preston Stewart. Un carré représente un drone, un carré vide la fourchette haute","Number of FPV drones used per target, orders of magnitude given by Michael Kofman and Preston Stewart. One square is one drone, an empty square the upper range")[i]
        rows=[(("Un soldat","One soldier")[i],5,5,("environ 5 ; 12 dans un cas vu par Kofman","about 5; 12 in one case Kofman saw")[i]),(("Un blindé d'infanterie","An infantry fighting vehicle")[i],15,20,("15 à 20","15 to 20")[i]),(("Un char","A tank")[i],30,40,("30 à 40 ; 79 pour un char surblindé, cas extrême","30 to 40; 79 for one heavily up-armoured tank, an extreme case")[i])]
        h=f"<div class='piece'><p class='pt'>{nb(t,i)}</p><p class='sub'>{nb(d,i)}</p>"
        for name,lo,hi,txt in rows:
            h+=f"<div class='dot-g'><span class='bar-n'>{name}<small>{nb(txt,i)}</small></span><div class='dots'>"+"".join(f"<i class='{'d' if j<lo else 'd lo'}'></i>" for j in range(hi))+"</div></div>"
        src=f"{POD[i]}, {UI['atp'][i]} {yt(1375)}."
        lim=("Ordres de grandeur tirés de ce que les invités ont vu ou entendu auprès d'unités ukrainiennes. Aucune série de données.","Orders of magnitude drawn from what the guests saw or heard with Ukrainian units. No data series.")[i]
        return h+cartel(src,lim,i)+"</div>"
    if k=='timeline':
        t=("Quatre ans de guerre en quinze dates","Four years of war in fifteen dates")[i]
        d=("Principaux événements militaires retenus par l'épisode, février 2022 à octobre 2026","Main military events picked out by the episode, February 2022 to October 2026")[i]
        ev=[("2022",[("r","Fév. à mai","Feb to May","La Russie envahit l'Ukraine, prend Kherson et Mariupol","Russia invades Ukraine, takes Kherson and Mariupol"),("u","Avril","April","L'Ukraine reprend la région de Kyiv","Ukraine regains the Kyiv region"),("u","Sept. à nov.","Sep to Nov","L'Ukraine reprend Izium, puis Kherson","Ukraine retakes Izium, then Kherson"),("r","Octobre","October","La Russie commence ses frappes massives sur le réseau électrique","Russia begins mass strikes on the power grid")]),
            ("2023",[("r","Mai","May","La Russie prend Bakhmut","Russia takes Bakhmut"),("u","Juin","June","L'Ukraine lance sa contre-offensive d'été, qui échoue","Ukraine launches its summer counteroffensive, which fails")]),
            ("2024",[("r","Février","February","La Russie prend Avdiivka","Russia takes Avdiivka"),("u","Août","August","L'Ukraine entre dans la région russe de Koursk","Ukraine enters Russia's Kursk region")]),
            ("2025",[("r","Mars","March","La Russie reprend l'essentiel du terrain perdu à Koursk","Russia retakes most ground lost in Kursk"),("u","Juin","June","Des drones ukrainiens frappent des bases de bombardiers russes","Ukrainian drones hit Russian bomber bases"),("u","Août","August","L'Ukraine frappe les raffineries, le carburant manque dans une partie de la Russie","Ukraine strikes refineries, parts of Russia run short of fuel"),("r","Hiver","Winter","Les frappes russes privent de chauffage une grande partie de Kyiv","Russian strikes leave much of Kyiv without heat")]),
            ("2026",[("r","Début d'année","Early in the year","La Russie prend Pokrovsk et Huliaipole","Russia takes Pokrovsk and Huliaipole"),("u","Février","February","L'Ukraine reprend du terrain au sud","Ukraine retakes ground in the south"),("u","Mai à oct.","May to Oct","L'Ukraine reprend du terrain au nord de Lyman","Ukraine retakes ground north of Lyman")])]
        h=f"<div class='piece'><p class='pt'>{t}</p><p class='sub'>{nb(d,i)}</p><div class='legend'><span><i style='background:var(--ru)'></i>{('Action russe','Russian action')[i]}</span><span><i style='background:var(--ua)'></i>{('Action ukrainienne','Ukrainian action')[i]}</span></div><div class='tl'>"
        for y,es in ev:
            h+=f"<div class='tl-y'><b>{y}</b><ul>"+"".join(f"<li class='{e[0]}'><span>{e[1+i]}</span>{e[3+i]}</li>" for e in es)+"</ul></div>"
        src=(f"Frise de l'épisode, {POD[i]}, {UI['at'][i]} {yt(80)}.",f"Timeline in the episode, {POD[i]}, {UI['at'][i]} {yt(80)}.")[i]
        lim=("Sélection faite par l'équipe du podcast, lue à l'écran. Les pertes civiles et les déplacements de population n'y figurent pas.","Selection made by the podcast team, read off the screen. Civilian losses and displacement do not appear.")[i]
        return h+"</div>"+cartel(src,lim,i)+"</div>"

def demands(t,i):
    ti=("Kyiv demande une trêve, Moscou exige des concessions","Kyiv asks for a truce, Moscow demands concessions")[i]
    a=(("Kyiv demande","Kyiv asks for")[i],[("un cessez-le-feu sur la ligne actuelle","a ceasefire along the current line"),("le retour des prisonniers, des disparus et des enfants enlevés","the return of prisoners, the missing and abducted children")])
    b=(("Moscou exige","Moscow demands")[i],[("le reste du Donbas, qu'elle ne tient pas","the rest of the Donbas, which it does not hold"),("des limites à l'armée ukrainienne","limits on Ukraine's army"),("le renoncement à l'OTAN et l'absence de troupes occidentales","no NATO membership and no Western troops"),("la reconnaissance des annexions","recognition of the annexations")])
    h=f"<div class='piece'><p class='pt'>{ti}</p><div class='two'>"+"".join(f"<div><b>{c[0]}</b><ul>"+"".join(f"<li>{x[i]}</li>" for x in c[1])+"</ul></div>" for c in (a,b))+"</div>"
    lim=("Positions rapportées par Kofman, complétées par l'encadré de la carte ci-dessous. Aucun texte officiel n'a été consulté.","Positions as reported by Kofman, completed from the box on the map below. No official text was consulted.")[i]
    return h+cartel(f"{POD[i]}, {UI['atp'][i]} {yt(t)} {('et','and')[i]} {yt(8251)}.",lim,i)+"</div>"

def art(i):
    lg='fr' if i==0 else 'en'; o=[f"<article class='L {lg}' lang='{lg}'>"]
    o.append(f"<header><span class='eyebrow'>{HEAD['eyebrow'][i]}</span><h1>{HEAD['h1'][i]}</h1><p class='src'>{nb(HEAD['src'][i],i)}</p></header>")
    o.append(f"<section class='warn'><h2>{WARN[0][i]}</h2><ul>"+"".join(f"<li>{nb(x[i],i)}</li>" for x in WARN[1])+"</ul></section>")
    o.append(f"<section><div class='chap'><h2>{UI['guests'][i]}</h2></div><div class='guests'>"+"".join(f"<div class='guest'><img src='img/{g[0]}' alt='{g[1]}'><div><h3>{g[1]}</h3><p>{g[2+i]}</p></div></div>" for g in GUESTS)+f"</div><p class='cr'>{nb(UI['portraits'][i],i)}</p></section>")
    o.append(f"<section><div class='chap'><h2>{UI['key'][i]}</h2></div><ol class='key'>"+"".join(f"<li>{nb(k[1+i],i)} {yt(k[0],' class=\"ref\"')}</li>" for k in KEY)+f"</ol><p class='note'>{nb(HEAD['note'][i],i)}</p>{chart('timeline',i)}</section>")
    for sec,title,blocks in S:
        o.append(f"<section><div class='chap'><h3>{nb(title[i],i)}</h3>{yt(sec+2,' class=\"ts\"')}</div>")
        for b in blocks:
            if b[0]=='q': o.append(f"<p class='lead'>{nb(b[1+i],i)}</p>")
            elif b[0]=='p': o.append(f"<p>{nb(b[2+i],i)} {yt(b[1],' class=\"ref\"')}</p>")
            elif b[0]=='l':
                o.append(f"<div class='lst'><p>{nb(b[2][i],i)}</p><ul>"+"".join(f"<li>{nb(x[i],i)}</li>" for x in b[3])+"</ul>"+(f"<p>{nb(b[4][i],i)} {yt(b[1],' class=\"ref\"')}</p>" if b[4] else "")+"</div>")
            elif b[0]=='f':
                _,f,t,title_,desc,lim=b
                o.append(f"<figure><p class='pt'>{nb(title_[i],i)}</p><p class='sub'>{nb(desc[i],i)}</p><button class='zoom' type='button' data-z='{UI['zoom'][i]}'><img src='img/{f}' alt='{html.escape(title_[i]+'. '+desc[i],quote=True)}' loading='lazy'></button>"+cartel(f"{POD[i]}, {UI['at'][i]} {yt(t)}.",lim[i],i)+"</figure>")
            elif b[0]=='n':
                _,t,title_,rows,lim=b
                o.append(f"<div class='piece'><p class='pt'>{nb(title_[i],i)}</p><div class='nums'>"+"".join(f"<div><b>{nb(r[2*i],i)}</b><span>{nb(r[2*i+1],i)}</span></div>" for r in rows)+"</div>"+cartel(f"{POD[i]}, {UI['atp'][i]} {yt(t)}.",lim[i],i)+"</div>")
            elif b[0]=='d': o.append(demands(b[1],i))
            elif b[0]=='c': o.append(chart(b[1],i))
        o.append("</section>")
    o.append(f"<section><div class='chap'><h2>{METHOD[0][i]}</h2></div>"+"".join(f"<p class='note'>{nb(x[i],i)}</p>" for x in METHOD[1])+"</section>")
    o.append(f"<footer><p>{nb(UI['foot'][i],i)}</p></footer></article>")
    return "\n".join(o)

CSS=open('style.css').read()
page=f"""<title>Lex Fridman #504, notes (Presse)</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Viewing notes on Lex Fridman Podcast #504 with Michael Kofman and Preston Stewart on the war in Ukraine. French and English. Press layout.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,700;1,7..72,400&family=IBM+Plex+Sans+Condensed:wght@400;500;600&family=Barlow+Condensed:wght@600&family=Source+Sans+3:ital,wght@0,400;0,600;1,400&display=swap">
<style>{CSS}</style>
<div class="wrap" id="root" data-l="fr">
<nav class="lang" aria-label="Langue et habillage / Language and style"><div><button type="button" id="b-fr" aria-pressed="true">Français</button><button type="button" id="b-en" aria-pressed="false">English</button></div><div><button type="button" id="s-presse" aria-pressed="true">Presse</button><button type="button" id="s-sombre" aria-pressed="false">Sombre</button></div></nav>
{art(0)}
{art(1)}
</div>
<dialog id="lightbox" aria-label="Image"><img id="lightbox-img" alt=""><button type="button" id="lightbox-close">Fermer / Close</button></dialog>
<script>
(function(){{
  var r=document.getElementById('root'),bf=document.getElementById('b-fr'),be=document.getElementById('b-en');
  function set(l,keep){{r.setAttribute('data-l',l);bf.setAttribute('aria-pressed',l==='fr');be.setAttribute('aria-pressed',l==='en');document.documentElement.lang=l;if(keep){{try{{localStorage.setItem('lang',l)}}catch(e){{}}}}}}
  var l='fr';try{{l=localStorage.getItem('lang')||l}}catch(e){{}}
  if(location.hash==='#en')l='en';if(location.hash==='#fr')l='fr';set(l,false);
  bf.addEventListener('click',function(){{set('fr',true);location.hash='fr'}});be.addEventListener('click',function(){{set('en',true);location.hash='en'}});
  window.addEventListener('hashchange',function(){{if(location.hash==='#en')set('en',false);if(location.hash==='#fr')set('fr',false)}});
  var sp=document.getElementById('s-presse'),ss=document.getElementById('s-sombre');
  function sty(s,keep){{if(s==='sombre')document.documentElement.setAttribute('data-style','sombre');else document.documentElement.removeAttribute('data-style');sp.setAttribute('aria-pressed',s!=='sombre');ss.setAttribute('aria-pressed',s==='sombre');if(keep){{try{{localStorage.setItem('style',s)}}catch(e){{}}}}}}
  var s0='presse';try{{s0=localStorage.getItem('style')||s0}}catch(e){{}}sty(s0,false);
  sp.addEventListener('click',function(){{sty('presse',true)}});ss.addEventListener('click',function(){{sty('sombre',true)}});
  var d=document.getElementById('lightbox'),i=document.getElementById('lightbox-img');
  document.querySelectorAll('.zoom').forEach(function(b){{b.addEventListener('click',function(){{var s=b.querySelector('img');i.src=s.src;i.alt=s.alt;if(d.showModal)d.showModal()}})}});
  document.getElementById('lightbox-close').addEventListener('click',function(){{d.close()}});
  d.addEventListener('click',function(e){{if(e.target===d||e.target===i)d.close()}});
}})();
</script>
"""
open('index.html','w').write(page); print(len(page))
# Copie autonome pour un aperçu local ou GitHub Pages (dossier docs/).
import os,shutil
os.makedirs('docs',exist_ok=True)
open('docs/index.html','w').write('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<meta name="robots" content="noindex">\n</head>\n<body>\n'+page+'</body>\n</html>\n')
shutil.copytree('img','docs/img',dirs_exist_ok=True)
