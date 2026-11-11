# Charte « Presse » pour les notes et leurs graphiques

Version 1, 11 novembre 2026. Tirée des essais de style, de la charte d'écriture HI
(`/writing-style`), de la skill `dataviz` et des articles Datawrapper cités en bas.

## 1. Habillage

- Fond papier clair `#fbfbf8`, encre `#16181d`, gris de texte `#5b6170`, filets `#d9dbd6`, grille `#e6e7e2`.
- Une couleur d'accent, l'outremer `#1e3a8a` : filet au-dessus de chaque pièce, liens, courbe unique.
- Texte et titres en Literata. Chiffres, axes, légendes et cartels en IBM Plex Sans Condensed.
- Une colonne de 700 px au plus. Rien n'est centré.

## 2. Tailles (page web)

| Élément | Taille | Graisse |
|---|---|---|
| Titre de page | 24 px | 700 |
| Titre de chapitre | 19 px | 700 |
| Texte courant | 15 px, interligne 1,55 | 400 |
| Titre de graphique | 15 à 16 px | 700 |
| Description (sous le titre) | 13 px, gris | 400 |
| Étiquettes et annotations | 12 px gris, 13 px noir pour l'essentiel | 400 ou 600 |
| Cartel (source, limite) | 12 px, gris | 400 |

Rien sous 12 px (Datawrapper : « everything below 12px will likely be too small »).
Deux niveaux d'étiquettes au plus. Gras réservé au titre et à quelques mots d'annotation.

## 3. Titre et description d'un graphique

- Le titre dit le constat, en mots courants, en 10 mots au plus et sur une ligne en largeur bureau.
  Datawrapper : « Give the main statement first and the precise data explanation later ».
- La description porte la précision : ce qui est mesuré, l'unité, le lieu, la période, les sigles développés.
- Le titre nomme l'acteur. « L'armée tient le Nil, les RSF tiennent le Darfour », pas « Situation au Soudan ».
- Pas de chiffre dans le titre si le graphique le montre déjà, sauf quand le chiffre est le constat.

Exemples retenus :

| Titre | Description |
|---|---|
| La Russie annonce plus de terrain qu'elle n'en prend | Surface que l'état-major russe dit avoir prise en Ukraine, et surface mesurée par l'ISW, en km² |
| L'armée tient le Nil, les RSF tiennent le Darfour | Camp qui tient les villes de chaque localité du Soudan, 17 août 2026. RSF : Forces de soutien rapide |
| Le Soudan compte 3 millions de déplacés de moins qu'en 2025 | Personnes déplacées à l'intérieur du pays, en millions, avril 2023 à août 2026 |

## 4. Graphiques

- Étiqueter directement les séries et les points clés. Une légende seulement à partir de deux séries, et jamais seule.
- Annoter l'extrême, le dernier point et l'événement qui explique la courbe. Pas un chiffre sur chaque point.
- Gris pour le contexte, couleur pour ce dont parle le titre.
- Un seul axe. Grille en filets fins, sans tirets. Barres de 24 px au plus, ligne de 2 px, points de 4 px de rayon.
- Le texte reste en encre ou en gris. Il ne prend jamais la couleur de la série.
- Hachures pour ce qui est annoncé, déclaré ou disputé. Aplat pour ce qui est mesuré ou tenu.

## 5. Cartes

- Couleurs des acteurs, vérifiées pour les daltoniens avec `validate_palette.js` (tous les tests passent sur fond clair) :
  armée soudanaise `#2c4a9e`, Forces de soutien rapide `#c47a2c`, SPLM-N `#2a9d8f`, SLM d'al-Nur `#8a5fb0`.
  Disputé : hachures des deux couleurs. Non suivi : gris clair `#e9eae5`.
- Les mêmes couleurs dans toutes les notes pour le même acteur.
- Annotations posées sur la carte, avec un trait de rappel : nom de la ville en 13 px gras, fait daté en 12 px.
  Contour de la couleur du fond sous le texte.
- Pays voisins en petites capitales grises, interlettrées.
- Sur téléphone, garder trois ou quatre annotations au plus et renvoyer le reste au texte.

## 6. Cartel

Deux lignes sous chaque pièce, toujours dans cet ordre :

- **Source.** Producteur de la donnée, lien, date de la donnée.
- **Limite.** Ce que la pièce ne montre pas, ou ce qui n'a pas été vérifié.

## 7. Texte

- L'acteur est le sujet de la phrase et fait l'action. « Les Forces de soutien rapide ont pris El Fasher », pas « El Fasher est tombée ».
- Chaque fait porte sa source en lien, dans la phrase ou juste après. Chaque chiffre a sa date.
- Trois degrés de certitude, toujours les mêmes mots : établi, rapporté, contesté.
- Sigles développés à la première mention. Dates au format « 26 octobre 2025 ».
- Ni première personne, ni adjectif de jugement, ni tiret long. Phrases courtes, de longueur variée.
- Un détail concret par chapitre, pas plus.
- Ordre d'une note : source, avertissement, points clés, chapitres, méthode.

## Références lues

- Datawrapper, « What to consider when using text in data visualizations » : https://www.datawrapper.de/blog/text-in-data-visualizations/
- Datawrapper, « Which fonts to use for your charts and tables » : https://www.datawrapper.de/blog/fonts-for-data-visualization/
- Datawrapper, « What to consider when choosing colors for data visualization » : https://www.datawrapper.de/blog/colors/
- Datawrapper, « What to consider when creating choropleth maps » : https://www.datawrapper.de/blog/choroplethmaps/
- Datawrapper, « How to create better charts » : https://www.datawrapper.de/blog/better-charts/
- Datawrapper Academy, onglet Annotate : https://www.datawrapper.de/academy/annotate-tab

Les articles Datawrapper ne donnent pas de longueur chiffrée pour un titre. La limite de 10 mots est une règle maison.
Le guide de style de The Economist n'a pas pu être lu (accès bloqué).
