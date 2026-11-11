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
 note=("Chaque horodatage ouvre la vidéo au passage qui fonde la phrase. Un clic agrandit les images. Les noms de lieux ukrainiens suivent la graphie des cartes de l'épisode, les noms russes l'usage français.",
       "Each timestamp opens the video at the passage the sentence draws on. Click an image to enlarge it. Ukrainian place names follow the spelling on the episode's maps, Russian names common English usage."),
)
WARN=(("Avertissement","Disclaimer"),[
 ("Ces notes reflètent la position des deux invités, pas celle de l'auteur ni de son employeur.",
  "These notes reflect the position of the two guests, not that of the author or the author's employer."),
 ("Le sujet de la vidéo est militaire. Elle ne traite pas des conséquences humanitaires de la guerre.",
  "The subject of the video is military. It does not deal with the humanitarian consequences of the war."),
 ("Les captures d'écran appartiennent au Lex Fridman Podcast. Elles sont reprises à seule fin de commentaire, chacune avec sa source et un lien vers le passage de la vidéo.",
  "The stills belong to the Lex Fridman Podcast. They are reproduced for commentary only, each with its source and a link to the passage in the video."),
 ("Transparence : notes rédigées avec l'appui d'un modèle de langage, Claude (Anthropic, modèles Opus 5.5 et Fable 5.2), à partir de la transcription officielle et de la vidéo.",
  "Transparency: notes written with the help of a large language model, Claude (Anthropic, Opus 5.5 and Fable 5.2 models), from the official transcript and the video."),
])
GUESTS=[
 ("kofman.jpg","Michael Kofman",
  "Chercheur principal à la Fondation Carnegie pour la paix internationale, spécialiste des armées russe et ukrainienne. Il anime le podcast <em>Russia Contingency</em> et se rend auprès de brigades ukrainiennes. L'essentiel de l'analyse vient de lui.",
  "Senior fellow at the Carnegie Endowment, specialist in the Russian and Ukrainian armed forces. He hosts the <em>Russia Contingency</em> podcast and visits Ukrainian brigades. Most of the analysis is his."),
 ("stewart.jpg","Preston Stewart",
  "Diplômé de West Point, l'académie militaire de l'armée de terre américaine, il a servi en Afghanistan. Il couvre la guerre sur sa chaîne YouTube et dans le podcast <em>War and Conflict</em>.",
  "A graduate of West Point, the US Military Academy, he served in Afghanistan. He covers the war on his YouTube channel and the <em>War and Conflict</em> podcast."),
]
KEY=[
 (78,"En 2026, l'armée ukrainienne connaît sa situation la plus favorable sur le terrain depuis l'été 2023, et l'armée russe sa plus difficile depuis l'hiver 2022-2023. La tendance s'est inversée à l'été ou à l'automne 2025.",
  "In 2026 the Ukrainian army is in its most favourable position on the ground since summer 2023, and the Russian army in its most difficult since the winter of 2022-23. The trend reversed in the summer or autumn of 2025."),
 (146,"L'armée russe s'appuie de plus en plus sur le bombardement stratégique : des frappes sur les villes, l'énergie et les infrastructures civiles loin du front. Cette méthode a rarement suffi à atteindre des buts politiques étendus, surtout sans succès au sol.",
  "The Russian army relies more and more on strategic bombardment: strikes on cities, energy and civilian infrastructure far from the front. The method has rarely been enough to achieve far-reaching political aims, least of all without success on the ground."),
 (792,"Les drones causent 80 % des pertes, mais ne suffiraient pas seuls à tenir le terrain. Ils s'ajoutent aux défenses préparées, aux champs de mines et à l'artillerie.",
  "Drones cause 80% of casualties, but would not be enough on their own to hold ground. They come on top of prepared defences, minefields and artillery."),
 (717,"Le front ne forme plus une ligne continue. Les drones frappent jusqu'à une quinzaine de kilomètres de part et d'autre, et une zone grise que personne ne tient sépare les deux armées.",
  "The front no longer forms a continuous line. Drones strike up to about 15 km either side of it, and a grey zone that nobody holds separates the two armies."),
 (5883,"Sur ses cartes, l'armée russe se place 10 à 15 km en avant de ses positions réelles. Elle planifie ensuite d'après cette ligne, ce qui lui coûte des hommes.",
  "On its maps the Russian army places itself 10 to 15 km ahead of its real positions. It then plans from that line, which costs it men."),
 (8387,"Les demandes du gouvernement russe n'ont presque pas changé depuis 2022 et dépassent ce que son armée peut prendre. Celles du gouvernement ukrainien s'alignent sur la ligne de front actuelle.",
  "The Russian government's demands have barely changed since 2022 and exceed what its army can take. The Ukrainian government's are tied to the current front line."),
 (9386,"Aucune paix n'est attendue à court terme. Des trêves partielles sont possibles. Un cessez-le-feu sans garanties de sécurité serait dangereux pour l'Ukraine.",
  "No peace is expected in the short term. Partial truces are possible. A ceasefire without security guarantees would be dangerous for Ukraine."),
]
POD=("Lex Fridman Podcast #504, YouTube, 10 novembre 2026","Lex Fridman Podcast #504, YouTube, 10 November 2026")
S=[
 (60,("Où en est la guerre","Where the war stands"),[
  Q("Sur le front, l'armée ukrainienne connaît sa situation la plus favorable depuis 2023. Loin du front, la campagne de frappes russe s'étend à de nouvelles cibles.",
    "At the front, the Ukrainian army is in its most favourable position since 2023. Away from the front, Russia's strike campaign is extending to new targets."),
  P(517,"La guerre est dans sa cinquième année. Les combats ont lieu dans l'est et le sud-est du pays. Kyiv n'est pas menacée au sol, mais des drones et des missiles la visent chaque jour.",
    "The war is in its fifth year. The fighting is in the east and south-east of the country. Kyiv is not threatened on the ground, but it comes under drone and missile attack every day."),
  F("carte-ensemble.jpg",72,("Le territoire tenu par l'armée russe, carte d'ouverture","Territory held by the Russian army, opening map"),
    ("Territoire tenu par l'armée russe, en rouge. En orange, les villes du front citées dans ces notes, de Kupiansk au nord à Huliaipole au sud.","Territory held by the Russian army, in red. In orange, the front-line towns named in these notes, from Kupiansk in the north to Huliaipole in the south."),
    ("L'écran cite DeepState et l'ISW et ne date pas la carte. Dans la zone grise, toute ligne est approximative.","The screen credits DeepState and ISW and gives the map no date. In the grey zone any line is approximate.")),
  P(595,"L'effort russe porte sur le reste du Donbas, la région que forment les oblasts (provinces) de Luhansk et de Donetsk. Quatre villes de l'oblast de Donetsk restent sous contrôle ukrainien : Sloviansk, Kramatorsk, Druzhkivka et Kostiantynivka, que les soldats appellent « Kostya » parce que le nom est trop long. Au nord, vers Sumy et Kharkiv, l'armée russe mène des incursions limitées pour établir une zone tampon.",
    "Russia's effort is aimed at the rest of the Donbas, the region formed by Luhansk and Donetsk oblasts (provinces). Four cities in Donetsk oblast remain under Ukrainian control: Sloviansk, Kramatorsk, Druzhkivka and Kostiantynivka, which soldiers call \"Kostya\" because the name is too long. In the north, near Sumy and Kharkiv, the Russian army conducts limited incursions to establish a buffer zone."),
  P(686,"Fait nouveau en 2026, l'armée ukrainienne reprend du terrain. Elle mène deux offensives locales, l'une près de Lyman, l'autre dans la région de Zaporizhzhia. Certaines opérations récentes ont repris plus de terrain que la contre-offensive de l'été 2023. Celle-ci, préparée avec des unités formées et équipées par les pays occidentaux, avait échoué.",
    "What is new in 2026 is that the Ukrainian army is retaking ground. It is running two local offensives, one near Lyman, the other in the Zaporizhzhia region. Some recent operations have regained more ground than the summer 2023 counter-offensive. That offensive, prepared with units trained and equipped by Western countries, had failed."),
  F("front-2026.jpg",633,("En 2026, l'armée ukrainienne reprend du terrain au nord de Lyman","In 2026 the Ukrainian army retakes ground north of Lyman"),
    ("Gains de 2026, russes en rouge vif, ukrainiens en bleu. Le contour blanc entoure la « ceinture de forteresses », les quatre villes du Donbas que l'armée russe n'a pas prises.","2026 gains, Russian in bright red, Ukrainian in blue. The white outline is the \"Fortress Belt\", the four Donbas cities the Russian army has not taken."),
    ("Carte de l'équipe du podcast, sans date précise ni source à l'écran.","Map by the podcast team, with no precise date or source on screen.")),
  P(293,"L'armée russe a gardé l'initiative pendant l'essentiel de 2024 et de 2025, en menant une offensive d'usure sur un front très large. La tendance s'est inversée à l'automne 2025. Le graphique de l'épisode représente cette évolution mois par mois.",
    "The Russian army held the initiative for most of 2024 and 2025, through a grinding offensive on a very broad front. The trend reversed in the autumn of 2025. The episode's chart represents that change month by month."),
  F("initiative.jpg",348,("Terrain gagné et perdu chaque mois par l'armée russe","Ground gained and lost each month by the Russian army"),
    ("Terrain gagné (rouge) et perdu (turquoise), janvier 2023 à octobre 2026. Les pertes incluent le terrain passé en zone grise. L'épisode date l'inversion de l'automne 2025.","Ground gained (red) and lost (teal), January 2023 to October 2026. Losses include ground that fell into the grey zone. The episode dates the reversal to the autumn of 2025."),
    ("L'écran ne donne ni unité, ni échelle, ni source.","The screen gives no unit, scale or source.")),
  P(379,"Loin du front, la campagne de frappes russe a commencé à l'automne 2022 contre les centrales, les postes électriques et les chaufferies. En 2026, elle vise aussi des entrepôts, des centres de données, des écoles, des établissements médicaux, des centres commerciaux et des trains. Des drones à réaction ont remplacé les drones à hélice, plus faciles à abattre. C'est un bombardement stratégique : il vise ce qui fait vivre l'économie et la population plutôt que les forces du front. Michael Kofman souligne que cette méthode a rarement suffi à atteindre des buts politiques étendus. L'issue de l'hiver reste incertaine pour les villes ukrainiennes. L'hiver est le plus dur pour la population civile, pas pour les troupes du front [[9461]].",
    "Away from the front, Russia's strike campaign began in autumn 2022 against power stations, substations and heating plants. In 2026 it also targets warehouses, data centres, schools, medical facilities, shopping centres and trains. Jet-powered drones have replaced propeller drones, which were easier to shoot down. This is strategic bombardment: it aims at what sustains the economy and the population rather than at forces at the front. Michael Kofman stresses that the method has rarely been enough to achieve far-reaching political aims. The outcome of the winter remains uncertain for Ukrainian cities. The winter is hardest for the civilian population, not for troops at the front [[9461]]."),
  F("bombardement.jpg",160,("L'armée russe lance des milliers de drones chaque mois","The Russian army launches thousands of drones every month"),
    ("Drones (rouge) et missiles (rose) lancés sur l'Ukraine chaque mois, janvier 2025 à octobre 2026, soit 120 300 au total selon l'écran. Carte : attaques ayant touché chaque oblast, janvier 2025 à juillet 2026.","Drones (red) and missiles (pink) launched at Ukraine each month, January 2025 to October 2026, 120,300 in all according to the screen. Map: attacks with recorded hits per oblast, January 2025 to July 2026."),
    ("Lancements rapportés, sans source nommée. La dernière barre, hachurée, porte la mention « Air Force monthly count ». Non vérifié ici.","Reported launches, no source named. The last, hatched bar is labelled \"Air Force monthly count\". Not verified here.")),
 ]),
 (879,("Drones et zone grise","Drones and the grey zone"),[
  Q("Des postes isolés et des drones tiennent le front. Pour y avancer, l'armée russe envoie des hommes par petits groupes, au prix de pertes très lourdes.",
    "Isolated posts and drones hold the front. To advance across it, the Russian army sends men in small groups, at the cost of very heavy losses."),
  P(717,"L'armée ukrainienne ne tient pas une ligne continue. Elle tient souvent des postes de trois soldats, séparés de plusieurs centaines de mètres [[1889]]. Les drones peuvent frapper jusqu'à une quinzaine de kilomètres de part et d'autre, distance variable selon les secteurs, dans une bande que les soldats appellent la <em>kill zone</em>. Entre les deux armées s'étend une zone grise que personne ne contrôle.",
    "The Ukrainian army does not hold a continuous line. It often holds three-man posts several hundred metres apart [[1889]]. Drones can strike up to about 15 km either side, a distance that varies by sector, in a band soldiers call the kill zone. Between the two armies lies a grey zone that nobody controls."),
  F("defense-zonale.jpg",724,("Le front : des postes de trois soldats, sans ligne continue","The front: three-man posts, no continuous line"),
    ("Postes d'infanterie (cercles) de part et d'autre d'une zone grise (hachures), sous la surveillance des drones.","Infantry posts (circles) on either side of a grey zone (hatched), watched by drones."),
    ("Schéma simplifié de l'équipe du podcast. Il illustre un propos des invités et ne mesure rien.","Simplified diagram by the podcast team. It illustrates a point made by the guests and measures nothing.")),
  P(792,"Les drones causent 80 % des pertes, d'après les statistiques citées dans l'épisode. Ils ne suffiraient pas seuls : les champs de mines arrêtent les assauts, et l'artillerie oblige l'adversaire à se disperser et prend le relais par mauvais temps, quand les drones volent mal.",
    "Drones cause 80% of casualties, according to the statistics cited in the episode. They would not be enough on their own: minefields stop assaults, and artillery forces the enemy to disperse and takes over in bad weather, when drones fly poorly."),
  P(1057,"Le drone le plus visible dans les vidéos est le FPV (<em>first-person view</em>), un petit quadricoptère chargé d'explosif que son pilote dirige par la caméra embarquée jusqu'à l'impact. Chaque camp en emploie 8 000 à 10 000 par jour. Sauf rares cas de guidage automatique en fin de trajectoire, ils sont pilotés à distance par une équipe de deux ou trois personnes : un pilote, un navigateur et souvent un technicien.",
    "The drone seen most often in videos is the FPV (first-person view), a small quadcopter carrying an explosive charge, steered by its pilot via an on-board camera until impact. Each side uses 8,000 to 10,000 a day. Apart from rare cases of automatic guidance in the final approach, they are flown remotely by a team of two or three people: a pilot, a navigator and often a technician."),
  P(1375,"Les vidéos publiées ne montrent que les frappes réussies. Une partie des drones est brouillée, tombe en panne ou n'explose pas. Une compagnie mécanisée ukrainienne qui part à l'assaut s'attend à recevoir près de 300 impacts.",
    "Published videos show only the successful strikes. Some drones are jammed, fail or do not detonate. A Ukrainian mechanised company going into an assault expects to take close to 300 hits."),
  C('drones'),
  P(1518,"Une colonne blindée est repérée à 10, 20 ou 30 km du front et détruite avant d'y arriver. L'armée russe envoie donc des hommes seuls ou par petits groupes, à pied, à moto, en quad, parfois en voiture civile.",
    "An armoured column is spotted 10, 20 or 30 km from the front and destroyed before it arrives. So the Russian army sends men alone or in small groups, on foot, by motorbike or quad bike, sometimes in civilian cars."),
  P(1932,"Kofman parle d'un calcul sinistre. Dans son exemple, sept hommes sur dix n'atteignent pas les positions ukrainiennes, mais les trois autres ont trouvé un passage entre deux postes, que le groupe suivant emprunte. Trois à cinq kilomètres plus loin, ils atteignent les équipes de drones, qui pilotent et ne sont pas préparées à recevoir un assaut. Un volontaire américain engagé du côté ukrainien, cité par Preston Stewart, résume la méthode : elle fait gagner du terrain au prix de 90 à 95 % des hommes envoyés [[1561]].",
    "Kofman calls it a grim calculus. In his example, seven men in ten do not reach the Ukrainian positions, but the other three have found a gap between two posts, which the next group uses. Three to five kilometres further on they reach the drone teams, who are flying drones and are not prepared to receive an assault. An American volunteer serving on the Ukrainian side, quoted by Preston Stewart, sums up the method: it gains ground at the cost of 90 to 95% of the men sent [[1561]]."),
  P(1629,"L'armée ukrainienne n'a pas ces effectifs et n'accepterait pas de telles pertes. Depuis 2025, la guerre est une lutte pour la supériorité dans la zone d'engagement des drones. Certaines unités d'assaut ukrainiennes, parmi les mieux équipées en drones, localisent d'abord les équipes de drones russes, les frappent, coupent leur ravitaillement, puis attaquent. Les unes emploient des blindés pour avancer vite, les autres progressent par équipes de trois, une rangée d'arbres après l'autre.",
    "The Ukrainian army does not have the manpower and would not accept such losses. Since 2025 the war has been a contest for superiority in the drone engagement zone. Some of the best-equipped Ukrainian assault units first locate the Russian drone teams, strike them, cut their supplies, then attack. Some use armour to move fast, others advance in three-man teams, one tree line after another."),
  P(2206,"Chaque camp s'adapte aux innovations de l'autre en trois à quatre mois. Contre le brouillage, l'armée russe a déployé à grande échelle le drone à fibre optique. Un fil aussi fin qu'un fil de pêche le relie au pilote, jusqu'à 50 km, et le brouillage est sans effet sur lui. Ces drones resteraient minoritaires : 15 % ou moins, un chiffre donné au jugé. L'armée ukrainienne innove plus vite, l'armée russe généralise plus vite.",
    "Each side adapts to the other's innovations within three to four months. Against jamming, the Russian army deployed the fibre-optic drone at scale. A thread as thin as fishing line links it to the pilot, up to 50 km away, and jamming has no effect on it. These drones appear to remain a minority: 15% or less, a figure offered as a guess. The Ukrainian army innovates faster, the Russian army scales up faster."),
  P(2465,"Presque tout le monde sur le front possède un détecteur qui ressemble à une vieille Game Boy. Quand l'appareil sonne, son écran affiche ce que filme le drone ennemi. Les passagers d'une voiture regardent l'écran, puis par la vitre, pour savoir si la voiture à l'image est la leur. Contre un drone à fibre optique, l'appareil ne détecte rien.",
    "Almost everyone at the front has a detector that looks like an old Game Boy. When it beeps, its screen shows what the enemy drone is filming. The passengers in a car look at the screen, then out of the window, to work out whether the car in the picture is theirs. Against a fibre-optic drone it detects nothing."),
  P(2574,"Cette guerre ne préfigure pas forcément les suivantes. Elle doit une grande part de sa forme à une particularité : aucun camp n'a la maîtrise du ciel, et aucun ne fait voler ses avions au-dessus du territoire tenu par l'autre.",
    "This war is not necessarily a guide to future ones. It owes much of its shape to one particular feature: neither side controls the air, and neither flies its aircraft over territory held by the other."),
 ]),
 (3109,("Qui a l'avantage","Who has the advantage"),[
  Q("Aucun des deux invités ne désigne de vainqueur. L'armée ukrainienne a l'avantage sur le terrain en 2026, sans garantie qu'il dure.",
    "Neither guest names a winner. The Ukrainian army has the advantage on the ground in 2026, with no guarantee that it will last."),
  P(3131,"Les deux États ne poursuivent pas les mêmes objectifs, et une guerre ne se lit pas comme un décompte de points : l'Allemagne et le Japon avaient l'avantage pendant une grande partie de la Seconde Guerre mondiale. L'Ukraine existe toujours comme État souverain, mais elle a perdu des territoires qu'elle ne semble pas près de reprendre [[3171]].",
    "The two states are pursuing different objectives, and a war cannot be read off a scoreboard: Germany and Japan had the upper hand for much of the Second World War. Ukraine still exists as a sovereign state, but it has lost territory it does not appear close to regaining [[3171]]."),
  P(3312,"Kofman préfère parler d'avantage. L'armée ukrainienne l'a sur le terrain en 2026 ; il ignore s'il est durable ou passager. Aucun effondrement n'est en vue dans l'un ou l'autre camp, et beaucoup dépendra de l'hiver et de la campagne de frappes.",
    "Kofman prefers to speak of advantage. The Ukrainian army has it on the ground in 2026; he does not know whether it is lasting or temporary. No collapse is in sight on either side, and much will depend on the winter and the strike campaign."),
  L(3451,("La guerre se lit à trois niveaux :","The war can be read at three levels:"),
    [("la tactique : comment on se bat sur le terrain ;","tactics: how the fighting is done on the ground;"),
     ("les opérations : comment on coordonne des unités, leur appui-feu et leur ravitaillement vers un objectif ;","operations: how units, their fire support and their supplies are coordinated towards an objective;"),
     ("la stratégie : en quoi tout cela sert le but politique.","strategy: how all of that serves the political aim.")],
    ("Une avancée de cinq ou dix kilomètres ne décide pas de la guerre, mais la carte indique quel camp aborde une négociation en position de force. Une stratégie dépend aussi de ses hypothèses de départ.","An advance of five or ten kilometres does not decide the war, but the map shows which side enters a negotiation with leverage. A strategy also depends on its starting assumptions.")),
 ]),
 (3806,("L'invasion de février 2022","The February 2022 invasion"),[
  Q("Le plan russe reposait sur une hypothèse politique : la résistance serait brève. La défense ukrainienne a souvent été improvisée.",
    "The Russian plan rested on a political assumption: resistance would be brief. Ukraine's defence was often improvised."),
  P(3946,"Kofman dit avoir prévu l'invasion, mais pas sa forme. Le commandement russe préparait une prise de contrôle rapide : avancer vite, encercler la capitale, capturer ou isoler les dirigeants. Le plan supposait une résistance brève et un bon accueil de la population. Il ne prévoyait aucune solution de repli.",
    "Kofman says he predicted the invasion, but not its form. Russian command was preparing a rapid takeover: advance fast, encircle the capital, capture or isolate the leadership. The plan assumed brief resistance and a welcome from the population. It had no fallback."),
  F("invasion.jpg",3811,("Axes de l'offensive russe, 24 février 2022","Axes of the Russian offensive, 24 February 2022"),
    ("En rouge, ce que l'armée russe tenait déjà : la Crimée et une partie du Donbas. L'axe venu du Bélarus vise Kyiv.","In red, what the Russian army already held: Crimea and part of the Donbas. The axis from Belarus aims at Kyiv."),
    ("L'écran cite l'ISW et VIINA. Les flèches schématisent des mouvements, elles ne tracent pas un front.","The screen credits ISW and VIINA. The arrows sketch movements, they do not trace a front.")),
  P(4388,"Du côté ukrainien, la défense a souvent été improvisée. L'état-major attendait l'attaque dans le Donbas et y avait placé une grande partie de ses unités. Au nord de la capitale, il n'y avait presque aucune troupe régulière, et des volontaires ont rejoint les rangs. Les analystes en savaient plus sur le plan russe d'attaque que sur le plan ukrainien de défense.",
    "On the Ukrainian side, the defence was often improvised. The general staff expected the attack in the Donbas and had put many of its units there. North of the capital there were almost no regular troops, and volunteers joined the ranks. Analysts knew more about Russia's plan of attack than about Ukraine's plan of defence."),
  P(4499,"Stewart explique d'abord l'échec russe par le commandement. Une armée occidentale délègue la décision à un sergent de vingt ans ; l'armée russe attend l'ordre d'en haut. Quand les colonnes se sont immobilisées sur la route de Kyiv, des officiers supérieurs ont dû s'avancer pour rétablir la circulation, et beaucoup ont été tués dans les premières semaines.",
    "Stewart attributes the Russian failure primarily to command. A Western army delegates decisions to a twenty-year-old sergeant; the Russian army waits for orders from above. When the columns stalled on the road to Kyiv, senior officers had to go forward to get the traffic moving, and many were killed in the first weeks."),
 ]),
 (4754,("Bakhmut","Bakhmut"),[
  Q("La bataille a duré dix mois et détruit la ville. Sa perte a peu pesé sur la suite, et le choix de la défendre aussi longtemps reste débattu.",
    "The battle lasted ten months and destroyed the city. Its loss weighed little on what followed, and the choice to defend it for so long is still debated."),
  P(4890,"La bataille a duré d'août 2022 à mai 2023. C'était un siège classique, mené à deux échelles. Dans la ville, les combats se livraient d'immeuble en immeuble. Autour, ils portaient sur les routes d'accès, et ce second combat était le plus important.",
    "The battle lasted from August 2022 to May 2023. It was a classic siege fought at two scales. Inside the city, the fighting went building to building. Around it, the fight was for the access roads, and that second fight was the more important."),
  F("bakhmut.jpg",4861,("Bakhmut et ses flancs au début de la bataille","Bakhmut and its flanks as the battle began"),
    ("En rouge, le territoire tenu par l'armée russe. La ville est en contrebas, dominée à l'est et à l'ouest, et les flancs comptaient le plus : Soledar au nord, la route de Chasiv Yar à l'ouest.","In red, territory held by the Russian army. The city lies on low ground, overlooked from east and west, and the flanks mattered most: Soledar to the north, the Chasiv Yar road to the west."),
    ("Carte de l'équipe du podcast, sans source à l'écran.","Map by the podcast team, no source on screen.")),
  P(5057,"Du côté russe, l'assaut a été confié à Wagner, une société militaire privée dirigée par Evgueni Prigojine et autorisée à recruter dans les prisons. Elle a envoyé les détenus par groupes successifs, jusqu'à ce que les défenseurs soient épuisés et à court de munitions, puis ses soldats expérimentés. Pendant ce temps, l'artillerie russe a détruit la ville. À la fin de la bataille, il n'en restait presque rien. Prigojine a déclaré 20 000 tués dans ses rangs [[7698]].",
    "On the Russian side the assault was given to Wagner, a private military company headed by Yevgeny Prigozhin and allowed to recruit in prisons. It sent the convicts in successive groups until the defenders were exhausted and short of ammunition, then its experienced soldiers. Meanwhile Russian artillery destroyed the city. By the end of the battle almost nothing of it was left. Prigozhin reported 20,000 killed in his ranks [[7698]]."),
  P(5407,"Le « syndrome de Bakhmut » désigne la défense d'une ville au-delà du point où elle se justifie. Le gouvernement ukrainien craignait qu'une perte visible n'affaiblisse le soutien occidental, et a déclaré la ville « forteresse ». Pour les soldats, ce mot signifie qu'aucun repli ne sera autorisé à temps. La bataille a peut-être usé des troupes aguerries qui auraient pu mener la contre-offensive de l'été 2023, confiée à des unités neuves. Le débat reste ouvert.",
    "\"Bakhmut syndrome\" means defending a city beyond the point where it makes sense. The Ukrainian government feared a visible loss would weaken Western support, and declared the city a \"fortress\". To soldiers the word means no timely withdrawal will be allowed. The battle may have used up seasoned troops who could have led the summer 2023 counter-offensive, which was assigned to newly formed units. The debate remains open."),
  P(5215,"Avec le recul, la perte de Bakhmut a peu compté : l'armée russe a mis un an à atteindre la ville suivante, Chasiv Yar.",
    "With hindsight the loss of Bakhmut mattered little: the Russian army took a year to reach the next town, Chasiv Yar."),
  F("chasiv-yar.jpg",5249,("Bakhmut et Chasiv Yar, distantes d'environ 11 km","Bakhmut and Chasiv Yar, about 11 km apart"),
    ("Distance lue à l'écran (« about 7 miles »). L'armée russe a mis un an à atteindre Chasiv Yar, puis un an à en prendre une grande partie. En rouge, le territoire qu'elle tient en août 2025.","Distance read off the screen (\"about 7 miles\"). The Russian army took a year to reach Chasiv Yar, then another year to take much of it. In red, the territory it holds in August 2025."),
    ("Carte de l'équipe du podcast, sans source à l'écran.","Map by the podcast team, no source on screen.")),
  P(5585,"D'après Stewart, la situation de Kostiantynivka commence à ressembler à celle d'autres villes encerclées.",
    "Stewart thinks the situation at Kostiantynivka is beginning to resemble that of other towns that were encircled."),
  L(5622,("Trois signes indiquent qu'une position n'est plus tenable :","Three signs show that a position can no longer be held:"),
    [("l'encerclement menace ;","encirclement threatens;"),
     ("ravitailler la position coûte des hommes et du matériel ;","resupplying the position costs men and equipment;"),
     ("il faut contre-attaquer pour seulement conserver la position.","counter-attacks are needed merely to keep the position.")],
    ("La décision de tenir une ville relève alors souvent du pouvoir politique.","The decision to hold a city is then often a political one.")),
 ]),
 (5696,("Terrain déclaré, terrain tenu","Ground claimed, ground held"),[
  Q("L'armée russe déclare tenir plus de terrain qu'elle n'en tient. Cet écart fausse ses propres opérations.",
    "The Russian army claims to hold more ground than it does. The gap distorts its own operations."),
  P(5990,"Contrôler un terrain, c'est pouvoir l'utiliser. Être présent ne suffit pas si l'on ne peut pas y circuler librement. Ce contrôle réel commence à 20 km ou plus derrière le front. Avant cela, à l'approche du front, les habitants partent, les commerces ferment, et la ville ne compte bientôt plus que des militaires [[5730]].",
    "Controlling ground means being able to use it. Presence is not enough without freedom to move around. That real control begins 20 km or more behind the front. Before that, as the front approaches, residents leave, businesses close, and soon only the military remains in the town [[5730]]."),
  P(5730,"L'armée russe procède autrement. Un soldat atteint un village et agite un drapeau devant un drone. La position est portée sur la carte, et tout le terrain situé en arrière est déclaré tenu. La semaine de l'enregistrement, une de ces vidéos avait été produite par intelligence artificielle, ce que des commentateurs russes ont eux-mêmes signalé.",
    "The Russian army does it differently. A soldier reaches a village and waves a flag in front of a drone. The position goes on the map, and all the ground behind it is declared held. In the week of the recording, one such video had been produced with artificial intelligence, as Russian commentators themselves pointed out."),
  C('claimed'),
  P(5921,"Les cartes russes placent les troupes 10 à 15 km en avant de leurs positions réelles. L'artillerie et l'aviation règlent leur appui sur cette ligne. Une unité de relève reçoit une carte inexacte et rencontre l'adversaire là où elle attendait ses propres troupes. Souvent, en octobre et en novembre, le commandement demande à voir le terrain déclaré depuis des mois, et les assauts s'intensifient pour le prendre.",
    "Russian maps place the troops 10 to 15 km ahead of their real positions. Artillery and air support are planned around that line. A relieving unit is handed an inaccurate map and meets the enemy where it expected its own troops. Often, in October and November, the command asks to see the ground reported for months as taken, and the assaults intensify to take it."),
  F("ligne-revendiquee.jpg",5956,("L'armée russe planifie sur une ligne qu'elle ne tient pas","The Russian army plans from a line it does not hold"),
    ("La ligne déclarée (tirets, à gauche) précède de 10 à 15 km la ligne tenue (trait plein, à droite). Les drapeaux marquent les positions déclarées. Zone quadrillée : les assauts d'octobre et de novembre.","The claimed line (dashed, left) runs 10 to 15 km ahead of the held line (solid, right). Flags mark claimed positions. Cross-hatched area: the October and November assaults."),
    ("Schéma simplifié de l'équipe du podcast. Il illustre un propos des invités et ne mesure rien.","Simplified diagram by the podcast team. It illustrates a point made by the guests and measures nothing.")),
  P(6142,"Kupiansk en est un exemple. Fin 2025, le chef d'état-major, Valeri Guerassimov, a annoncé à Vladimir Poutine que les unités ukrainiennes y étaient encerclées. Kofman se trouvait alors à l'ouest de la ville avec un collègue d'une brigade ukrainienne : ce n'était pas le cas.",
    "Kupiansk is one example. In late 2025 the chief of the general staff, Valery Gerasimov, told Vladimir Putin that the Ukrainian units there were encircled. Kofman was then west of the city with a colleague from a Ukrainian brigade: this was not the case."),
  F("kupiansk.jpg",6105,("Kupiansk, déclarée prise, n'était pas tenue par l'armée russe","Kupiansk was declared captured but not held by the Russian army"),
    ("Kupiansk, décembre 2025. Tirets roses : zone déclarée prise en novembre 2025. Rouge : ce que l'armée russe tient. Hachures : zone grise. Point blanc : lieu de la vidéo de Volodymyr Zelensky à l'entrée de la ville.","Kupiansk, December 2025. Pink dashes: area declared captured in November 2025. Red: what the Russian army holds. Hatching: grey zone. White dot: where Volodymyr Zelensky filmed his video at the city's entrance."),
    ("Carte de l'équipe du podcast, sans source à l'écran. Ici les hachures désignent la zone grise, pas le terrain déclaré.","Map by the podcast team, no source on screen. Here the hatching marks the grey zone, not the claimed ground.")),
  P(6248,"Ces faux rapports tiennent à la culture militaire russe. Toute erreur y est punie, ce qui incite à mentir ; soldats et officiers se font peu confiance ; les décisions se prennent en haut, d'après ce qui remonte d'en bas. L'armée ukrainienne a connu de faux rapports elle aussi, surtout sous son précédent commandant en chef, quand des commandants ne pouvaient pas se replier sans l'accord de l'état-major général. Certains ont été relevés.",
    "These false reports stem from Russian military culture. Every mistake is punished, which is an incentive to lie; soldiers and officers do not trust each other; decisions are made at the top on what comes up from below. The Ukrainian army has had false reports too, especially under its previous commander-in-chief, when commanders could not withdraw without approval from the general staff. Some were relieved."),
  F("cultures-militaires.jpg",6253,("Niveaux de décision dans les deux armées, schéma de l'épisode","Decision levels in the two armies, the episode's diagram"),
    ("Cercles jaunes : les échelons qui décident. Sous le schéma, les trois effets cités côté russe : peu de confiance, sanction de toute erreur, centralisation.","Yellow rings: the levels that decide. Under the diagram, the three effects cited on the Russian side: little trust, punishment for any mistake, centralisation."),
    ("Schéma de l'équipe du podcast, capturé en cours d'animation : une seule des trois lignes est éclairée.","Diagram by the podcast team, captured mid-animation: only one of the three lines is lit.")),
  P(6545,"Le même défaut existe au niveau politique. Les dirigeants qui engagent une guerre la croient souvent courte et écartent les avis contraires. L'épisode cite l'invasion de 2022 et la guerre des États-Unis contre l'Iran en 2026.",
    "The same flaw exists at the political level. Leaders who start a war often expect it to be short and set aside contrary advice. The episode cites the 2022 invasion and the United States' war with Iran in 2026."),
 ]),
 (6905,("La mutinerie de Prigojine","Prigozhin's mutiny"),[
  Q("Wagner a été démantelée après sa mutinerie de juin 2023. L'armée russe a repris ses méthodes.",
    "Wagner was dismantled after its mutiny of June 2023. The Russian army adopted its methods."),
  P(7023,"Prigojine critiquait publiquement le ministre de la Défense de l'époque, Sergueï Choïgou, et le chef d'état-major. Après Bakhmut, le ministère a exigé que tous les hommes de Wagner signent un contrat avec l'armée, ce qui aurait retiré à Prigojine le commandement de ses troupes.",
    "Prigozhin publicly criticised the then defence minister, Sergei Shoigu, and the chief of the general staff. After Bakhmut the ministry required all of Wagner's men to sign contracts with the army, which would have taken command of his troops away from Prigozhin."),
  P(7132,"Les 23 et 24 juin 2023, Wagner a occupé le quartier général de Rostov, et deux colonnes ont pris la route de Moscou. Elles disposaient de chars et de moyens de défense antiaérienne, et ont abattu des appareils russes. Kofman parle d'une mutinerie en temps de guerre ; d'autres analystes y voient plutôt une forme de pétition. Aucun membre de l'élite ne s'est rallié à Prigojine, qui a négocié une amnistie. Il est mort le 23 août 2023 dans l'explosion en vol de son avion. Pour Kofman, il a été tué.",
    "On 23 and 24 June 2023 Wagner occupied the Rostov headquarters, and two columns took the road to Moscow. They had tanks and air defence, and shot down Russian aircraft. Kofman calls it a mutiny in wartime; other analysts see it more as a kind of petition. No member of the elite rallied to Prigozhin, who negotiated an amnesty. He died on 23 August 2023 when his plane exploded in mid-air. Kofman says he was killed."),
  P(7590,"Wagner a été démantelée, même si une partie de son encadrement sert encore dans l'Africa Corps, qui opère en Afrique. L'armée russe a repris ses méthodes : le recrutement de détenus et les compagnies d'assaut réparties dans les unités régulières. Elle s'est ainsi spécialisée à l'excès. Elle sait mener de petits assauts et peine à conduire des opérations plus vastes.",
    "Wagner was dismantled, though part of its leadership still serves in the Africa Corps, which operates in Africa. The Russian army adopted its methods: recruiting convicts and spreading assault companies across regular units. It has over-specialised as a result. It can run small assaults and struggles to conduct larger operations."),
 ]),
 (7760,("Buts de guerre et moyens","War aims and means"),[
  Q("Les buts politiques du gouvernement russe dépassent les moyens de son armée. Les deux pays peuvent pourtant poursuivre la guerre en 2027.",
    "The Russian government's political aims exceed its army's means. Both countries can nonetheless continue the war into 2027."),
  P(7867,"Aucun des deux présidents ne dirige le détail des combats, même si Vladimir Poutine semble un peu plus impliqué. Volodymyr Zelensky reçoit une image plus exacte du front.",
    "Neither president directs the fighting in detail, though Vladimir Putin appears a little more involved. Volodymyr Zelensky gets a more accurate picture of the front."),
  P(7951,"La guerre se divise en deux périodes : les trente premiers jours, qui ont réglé la question de l'indépendance de l'Ukraine, et la suite, qui porte sur ses frontières, son économie et ses alliances. Les demandes russes sont pourtant restées celles du début, alors que celles du gouvernement ukrainien se sont rapprochées de ce que son armée peut tenir.",
    "The war falls into two periods: the first thirty days, which settled the question of Ukraine's independence, and what followed, which concerns its borders, economy and alliances. Russia's demands nonetheless remain what they were at the outset, while the Ukrainian government's have moved close to what its army can hold."),
  D(8087),
  F("negociations.jpg",8124,("Le reste du Donbas, demandé par le gouvernement russe","The rest of the Donbas, demanded by the Russian government"),
    ("Hachures : le reste du Donbas, autour de Sloviansk et de Kramatorsk, un peu plus de 20 % de la région.","Hatching: the rest of the Donbas, around Sloviansk and Kramatorsk, just over 20% of the region."),
    ("Carte de l'équipe du podcast, sans source à l'écran. Ici les hachures désignent le terrain demandé.","Map by the podcast team, no source on screen. Here the hatching marks the ground demanded.")),
  P(8431,"Vladimir Poutine a qualifié de terres russes historiques les oblasts de Zaporizhzhia, de Kherson, de Donetsk et de Luhansk. Prendre le reste de Kherson supposerait de franchir le Dniepr, ce dont l'armée russe ne paraît pas capable à ce jour.",
    "Vladimir Putin has called Zaporizhzhia, Kherson, Donetsk and Luhansk oblasts historic Russian lands. Taking the rest of Kherson would mean crossing the Dnipro, which the Russian army does not appear capable of at present."),
  P(8644,"Les deux pays ont les ressources pour poursuivre la guerre en 2027, chacun grâce à des soutiens extérieurs : les pays occidentaux pour l'Ukraine, qui n'aurait pas tenu sans eux ; la Chine, la Corée du Nord et, dans une moindre mesure, l'Iran pour la Russie. L'avantage russe en effectifs est net [[8484]]. Les sanctions ont eu moins d'effet que Stewart ne l'attendait, et la société russe a peu réagi aux pertes. La guerre continue d'endommager l'économie ukrainienne et de pousser des habitants à quitter le pays [[8755]].",
    "Both countries have the resources to continue the war into 2027, each thanks to outside backers: Western countries for Ukraine, which could not have held out without them; China, North Korea and, to a lesser extent, Iran for Russia. Russia's advantage in manpower is clear [[8484]]. Sanctions have had less effect than Stewart expected, and Russian society has reacted little to the losses. The war continues to damage Ukraine's economy and to drive people from the country [[8755]]."),
  N(8715,("Trois chiffres cités de mémoire par les invités","Three figures the guests cite from memory"),
    [("44 %","du budget de l'État russe, soit 9 à 10 % du PIB","44%","of Russia's state budget, or 9 to 10% of GDP"),
     ("Plus de 30 000","soldats russes tués ou blessés par mois","Over 30,000","Russian soldiers killed or wounded each month"),
     ("40 %","des obus russes fournis par la Corée du Nord, à un moment de la guerre","40%","of Russian shells supplied by North Korea, at one point in the war")],
    ("Chiffres donnés de mémoire par les invités, sans source citée. Non vérifiés ici.","Figures given from memory by the guests, with no source cited. Not verified here.")),
 ]),
 (8838,("Le rôle des États-Unis","The role of the United States"),[
  Q("Les États-Unis fournissent encore des armes et du renseignement, mais ne dirigent plus la coalition de soutien à l'Ukraine.",
    "The United States still supplies weapons and intelligence, but no longer leads the coalition supporting Ukraine."),
  P(8855,"Les États-Unis ne versent plus d'aide financière directe. Ils fournissent encore des armes et des munitions, que les pays européens paient, ainsi que du renseignement.",
    "The United States no longer gives direct financial aid. It still supplies weapons and ammunition, which European countries pay for, as well as intelligence."),
  P(9281,"Les deux invités critiquent l'approche de l'administration Trump. Les États-Unis dirigeaient la coalition de soutien à l'Ukraine et se sont présentés en arbitre neutre. Ils y ont perdu leur influence sur le gouvernement ukrainien et la confiance des Européens, sans que le gouvernement russe les tienne pour neutres.",
    "Both guests criticise the Trump administration's approach. The United States led the coalition supporting Ukraine and then presented itself as a neutral arbiter. It lost its influence over the Ukrainian government and the trust of Europeans, without the Russian government ever regarding it as neutral."),
  P(9076,"Cette administration a pourtant eu un effet : elle a poussé chaque partie à formuler ses conditions, même si c'était probablement pour de mauvaises raisons. La précédente n'avait pas de plan pour terminer la guerre, les Européens non plus. « Aussi longtemps qu'il le faudra » était un slogan.",
    "This administration has nonetheless had one effect: it pushed each party to state its conditions, even if probably for the wrong reasons. The previous one had no plan to end the war, nor did the Europeans. \"As long as it takes\" was a slogan."),
 ]),
 (9373,("Perspectives de paix","Prospects for peace"),[
  Q("Le gouvernement russe ne montre pas de volonté de négocier. Le risque principal est un cessez-le-feu sans garanties de sécurité.",
    "The Russian government shows no willingness to negotiate. The main risk is a ceasefire without security guarantees."),
  P(9386,"Le gouvernement russe demande que toutes les questions de fond soient réglées avant un cessez-le-feu. Vladimir Poutine attendrait l'issue de l'hiver et celle des élections du printemps en Europe, dont l'élection française. Kofman se dit pessimiste à court terme, et ajoute qu'il peut se tromper.",
    "The Russian government asks for every substantive issue to be settled before a ceasefire. Vladimir Putin is probably waiting for the outcome of the winter and of Europe's spring elections, France's among them. Kofman says he is pessimistic in the short term, and adds that he may be wrong."),
  P(9671,"Une avancée serait limitée. Les deux camps cesseraient de frapper les infrastructures essentielles et les navires en mer Noire. Un cessez-le-feu de quelques jours ou de quelques semaines pourrait suivre.",
    "Any progress would be limited. Both sides would stop striking critical infrastructure and shipping in the Black Sea. A ceasefire of a few days or weeks might follow."),
  P(9587,"Le risque est un cessez-le-feu sans garanties de sécurité, une feuille de papier portant ce seul mot. L'armée ukrainienne devrait démobiliser des hommes qui veulent rentrer chez eux. L'armée russe, composée en grande partie de soldats sous contrat, pourrait rester en place et se réarmer. Six à huit mois plus tard, l'Ukraine serait très vulnérable. Les deux accords de Minsk, après 2014, n'ont pas abouti à un règlement.",
    "The risk is a ceasefire without security guarantees, a piece of paper bearing that one word. The Ukrainian army would have to demobilise men who want to go home. The Russian army, made up largely of contract soldiers, could stay in place and rearm. Six to eight months later Ukraine would be highly exposed. The two Minsk agreements, after 2014, did not lead to a settlement."),
  P(9871,"Après la guerre, l'Ukraine restera un État viable si les pays européens la considèrent comme l'un des leurs. La guerre n'est pas celle du seul Vladimir Poutine : des centaines de milliers de Russes ont signé un contrat pour combattre.",
    "After the war, Ukraine will remain a viable state if European countries regard it as one of their own. The war is not Vladimir Putin's alone: hundreds of thousands of Russians signed a contract to fight."),
 ]),
 (10013,("Évacuations de blessés","Evacuating the wounded"),[
  Q("L'épisode se termine sur deux évacuations de blessés, que les invités citent quand on leur demande ce qui leur donne de l'espoir.",
    "The episode ends with two evacuations of wounded soldiers, which the guests cite when asked what gives them hope."),
  P(10129,"Deux soldats ukrainiens ont été transportés chacun sur 30 km dans une nacelle fixée sous un drone, pendant que l'équipe leur parlait. Deux autres blessés, dont le robot d'évacuation avait été touché par un drone russe, ont été récupérés en pick-up par leur commandant de compagnie.",
    "Two Ukrainian soldiers were each carried 30 km in a pod fixed under a drone while the crew talked to them. Two other wounded men, whose evacuation robot had been hit by a Russian drone, were fetched in a pickup by their company commander."),
 ]),
]
METHOD=(("Méthode","Method"),[
 ("Ces notes suivent l'ordre des chapitres de l'épisode. Chaque chapitre s'ouvre sur la question posée par Lex Fridman, ou sur le lien que font les invités avec ce qui précède. Les faits et les jugements sont ceux des invités, deux analystes américains favorables à l'Ukraine. Aucun point de vue russe n'est représenté. Chaque paragraphe renvoie au passage de la vidéo qui le fonde.",
  "These notes follow the order of the episode's chapters. Each chapter opens with the question Lex Fridman asked, or with the link the guests make to what came before. The facts and judgements are those of the guests, two American analysts sympathetic to Ukraine. No Russian point of view is represented. Each paragraph links to the passage of the video it draws on."),
 ("Le texte a été relu contre la transcription officielle, qui attribue mal certaines répliques, puis soumis à trois relectures automatiques distinctes : langue et fil, graphiques, registre et fidélité. Les chiffres n'ont pas été vérifiés. Ceux qui ne figurent qu'à l'écran sont signalés dans la ligne « Limite » de la pièce concernée. Ces notes décrivent la situation de novembre 2026 et devront être relues après l'hiver.",
  "The text was checked against the official transcript, which misattributes some lines, then put through three separate automated reviews: language and flow, graphics, register and accuracy. The figures have not been verified. Those that appear only on screen are flagged in the \"Caveat\" line of the piece concerned. These notes describe the situation in November 2026 and should be revisited after the winter."),
 ("Trois faits ont été recoupés auprès d'une seconde source (Wikipédia, Meduza) : la mutinerie des 23 et 24 juin 2023, la mort de Prigojine le 23 août 2023 et la vidéo de Volodymyr Zelensky à Kupiansk en décembre 2025. Les événements de 2026 n'ont pas pu l'être.",
  "Three facts were cross-checked against a second source (Wikipedia, Meduza): the mutiny of 23 and 24 June 2023, Prigozhin's death on 23 August 2023 and Volodymyr Zelensky's video in Kupiansk in December 2025. The events of 2026 could not be."),
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
def rf(x): return re.sub(r' ?\[\[(\d+)\]\]([.,;]?)', lambda m: m.group(2)+' '+yt(int(m.group(1)),' class="ref"'), x)
def cartel(src,lim,i): return f"<p class='cartel'><span><b>{UI['src'][i]}</b> {src}</span><span><b>{UI['lim'][i]}</b> {nb(lim,i)}</span></p>"

def chart(k,i):
    if k=='claimed':
        t=("L'état-major russe déclare plus de terrain que l'ISW n'en mesure","Russia's General Staff claims more ground than ISW measures")[i]
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
        d=("Nombre de drones FPV employés par cible, estimations données par les deux invités. Un carré représente un drone, un carré vide le haut de la fourchette","Number of FPV drones used per target, rough figures given by the two guests. One square is one drone, an empty square the upper end of the range")[i]
        rows=[(("Un soldat","One soldier")[i],5,5,("environ 5 ; 12 dans un cas extrême","about 5; 12 in one extreme case")[i]),(("Un blindé d'infanterie","An infantry fighting vehicle")[i],15,20,("15 à 20","15 to 20")[i]),(("Un char","A tank")[i],30,40,("30 à 40 ; 79 pour un char surblindé, cas extrême","30 to 40; 79 for one heavily up-armoured tank, an extreme case")[i])]
        h=f"<div class='piece'><p class='pt'>{nb(t,i)}</p><p class='sub'>{nb(d,i)}</p>"
        for name,lo,hi,txt in rows:
            h+=f"<div class='dot-g'><span class='bar-n'>{name}<small>{nb(txt,i)}</small></span><div class='dots'>"+"".join(f"<i class='{'d' if j<lo else 'd lo'}'></i>" for j in range(hi))+"</div></div>"
        src=f"{POD[i]}, {UI['atp'][i]} {yt(1375)}."
        lim=("Estimations tirées de ce que les invités ont vu ou entendu auprès d'unités ukrainiennes. Aucune série de données.","Rough figures drawn from what the guests saw or heard from Ukrainian units. No data series.")[i]
        return h+cartel(src,lim,i)+"</div>"
    if k=='timeline':
        t=("Chronologie retenue par l'épisode, 2022 à 2026","Timeline used in the episode, 2022 to 2026")[i]
        d=("Principaux événements militaires retenus par l'épisode, février 2022 à octobre 2026","Main military events picked out by the episode, February 2022 to October 2026")[i]
        ev=[("2022",[("r","Fév. à mai","Feb to May","L'armée russe envahit l'Ukraine, prend Kherson et Mariupol","The Russian army invades Ukraine, takes Kherson and Mariupol"),("u","Avril","April","L'armée ukrainienne reprend la région de Kyiv","The Ukrainian army retakes the Kyiv region"),("u","Sept. à nov.","Sep to Nov","L'armée ukrainienne reprend Izium, puis Kherson","The Ukrainian army retakes Izium, then Kherson"),("r","Octobre","October","L'armée russe commence ses frappes massives sur le réseau électrique","The Russian army begins mass strikes on the power grid")]),
            ("2023",[("r","Mai","May","L'armée russe prend Bakhmut","The Russian army takes Bakhmut"),("u","Juin","June","L'armée ukrainienne lance sa contre-offensive d'été, qui échoue","The Ukrainian army launches its summer counter-offensive, which fails")]),
            ("2024",[("r","Février","February","L'armée russe prend Avdiivka","The Russian army takes Avdiivka"),("u","Août","August","L'armée ukrainienne entre dans la région russe de Koursk","The Ukrainian army enters Russia's Kursk region")]),
            ("2025",[("r","Mars","March","L'armée russe reprend l'essentiel du terrain perdu à Koursk","The Russian army retakes most of the ground it lost in Kursk"),("u","Juin","June","Des drones ukrainiens frappent des bases de bombardiers russes","Ukrainian drones hit Russian bomber bases"),("u","Août","August","L'armée ukrainienne frappe les raffineries, le carburant manque dans une partie de la Russie","The Ukrainian army strikes refineries, parts of Russia run short of fuel"),("r","Hiver","Winter","Les frappes russes privent de chauffage une grande partie de Kyiv","Russian strikes leave much of Kyiv without heating")]),
            ("2026",[("r","Début d'année","Early in the year","L'armée russe prend Pokrovsk et Huliaipole","The Russian army takes Pokrovsk and Huliaipole"),("u","Février","February","L'armée ukrainienne reprend du terrain au sud","The Ukrainian army retakes ground in the south"),("u","Mai à oct.","May to Oct","L'armée ukrainienne reprend du terrain au nord de Lyman","The Ukrainian army retakes ground north of Lyman")])]
        h=f"<div class='piece'><p class='pt'>{t}</p><p class='sub'>{nb(d,i)}</p><div class='legend'><span><i style='background:var(--ru)'></i>{('Action russe','Russian action')[i]}</span><span><i style='background:var(--ua)'></i>{('Action ukrainienne','Ukrainian action')[i]}</span></div><div class='tl'>"
        for y,es in ev:
            h+=f"<div class='tl-y'><b>{y}</b><ul>"+"".join(f"<li class='{e[0]}'><span>{e[1+i]}</span>{e[3+i]}</li>" for e in es)+"</ul></div>"
        src=(f"Frise de l'épisode, {POD[i]}, {UI['at'][i]} {yt(80)}.",f"Timeline in the episode, {POD[i]}, {UI['at'][i]} {yt(80)}.")[i]
        lim=("Sélection faite par l'équipe du podcast, lue à l'écran. Les pertes civiles et les déplacements de population n'y figurent pas.","Selection made by the podcast team, read off the screen. Civilian losses and displacement do not appear.")[i]
        return h+"</div>"+cartel(src,lim,i)+"</div>"

def demands(t,i):
    ti=("Positions de négociation des deux gouvernements","Negotiating positions of the two governments")[i]
    a=(("Le gouvernement ukrainien demande","The Ukrainian government asks for")[i],[("un cessez-le-feu sur la ligne actuelle","a ceasefire along the current line"),("le retour des prisonniers, des disparus et des enfants enlevés","the return of prisoners, the missing and abducted children")])
    b=(("Le gouvernement russe demande","The Russian government asks for")[i],[("le reste du Donbas, que son armée ne tient pas","the rest of the Donbas, which its army does not hold"),("des limites à la taille et aux capacités de l'armée ukrainienne","limits on the size and capabilities of Ukraine's army"),("le renoncement à l'OTAN et l'absence de troupes occidentales","no NATO membership and no Western troops"),("la reconnaissance des annexions","recognition of the annexations")])
    h=f"<div class='piece'><p class='pt'>{ti}</p><div class='two'>"+"".join(f"<div><b>{c[0]}</b><ul>"+"".join(f"<li>{x[i]}</li>" for x in c[1])+"</ul></div>" for c in (a,b))+"</div>"
    lim=("Positions rapportées par les invités, complétées par l'encadré de la carte ci-dessous. Aucun texte officiel n'a été consulté.","Positions as reported by the guests, completed from the box on the map below. No official text was consulted.")[i]
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
            elif b[0]=='p': o.append(f"<p>{rf(nb(b[2+i],i))} {yt(b[1],' class=\"ref\"')}</p>")
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
