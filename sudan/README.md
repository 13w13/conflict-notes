# Soudan, la guerre en cartes / Sudan, the war in maps

Note bilingue (FR/EN) sur la guerre au Soudan, avril 2023 à novembre 2026 : belligérants, façon de se battre, contrôle territorial mois par mois, déplacement, faim, accès humanitaire. Page statique, sans serveur.

Bilingual note (FR/EN) on the war in Sudan, April 2023 to November 2026: belligerents, how the war is fought, month-by-month territorial control, displacement, hunger, humanitarian access. Static page, no server.

## Avertissement / Disclaimer

L'auteur n'est pas analyste militaire. La note n'exprime la position d'aucune organisation. Les zones colorées sont une interprétation. Rédigée avec l'appui de Claude (Anthropic, modèles Opus 5.5 et Fable 5.2), qui a aussi collecté les données, vérifié les sources et écrit le code.

The author is not a military analyst. The note expresses no organisation's position. The coloured areas are an interpretation. Written with the support of Claude (Anthropic, Opus 5.5 and Fable 5.2 models), which also collected the data, checked the sources and wrote the code.

## Fichiers / Files

| Fichier | Rôle |
|---|---|
| `index.html` | page générée, charge `data.js` / generated page, loads `data.js` |
| `build_page.py`, `page.js`, `page.css` | texte FR/EN, script et style de la page / FR/EN text, page script and style |
| `build_data.py` | construit `data.js` à partir de `raw/` / builds `data.js` from `raw/` |
| `manual_updates.json` | corrections et ajouts faits à la main, avec sources / manual fixes and additions, with sources |
| `wiki_hist.py` | relève l'historique mensuel du module Wikipedia / fetches the monthly history of the Wikipedia module |
| `fetch_extra.py` | financement, réfugiés, prix, besoins, 3W / funding, refugees, prices, needs, 3W |

## Sources et licences / Sources and licences

| Donnée / Data | Source | Licence, conditions |
|---|---|---|
| Contrôle territorial / territorial control | Wikipedia, [Module:2023 Sudanese Clashes detailed map](https://en.wikipedia.org/wiki/Module:2023_Sudanese_Clashes_detailed_map), relevés mensuels jusqu'au 17 août 2026 | CC BY-SA 4.0. Les séries de contrôle de `data.js` et `manual_updates.json` en sont dérivées et restent sous CC BY-SA 4.0, avec attribution aux contributeurs de Wikipedia. / The control series in `data.js` and `manual_updates.json` are derived from it and remain under CC BY-SA 4.0, with attribution to Wikipedia contributors. |
| Violence | [ACLED](https://data.humdata.org/dataset/sudan-acled-conflict-data), agrégats mensuels par admin2 publiés sur HDX | [EULA](https://acleddata.com/eula) (mise à jour du 1er novembre 2026) et [politique d'attribution](https://acleddata.com/attributionpolicy) (5 novembre 2026). Voir la section ACLED ci-dessous avant toute mise en ligne publique. / See the ACLED section below before any public release. |
| Limites / boundaries | [COD-AB Soudan](https://data.humdata.org/dataset/cod-ab-sdn), OCHA | voir la fiche HDX / see the HDX page |
| Déplacement / displacement | [OIM DTM](https://data.humdata.org/dataset/sdn-iom-dtm-from-api) | voir la fiche HDX |
| Faim / hunger | [IPC](https://data.humdata.org/dataset/sudan-acute-food-insecurity-country-data) | voir la fiche HDX |
| Armes explosives, travailleurs humanitaires / explosive weapons, aid workers | [Insecurity Insight](https://data.humdata.org/dataset/sudan-violence-against-civilians-and-vital-civilian-facilities) | voir la fiche HDX |
| Prix, besoins, 3W / prices, needs, 3W | [HDX HAPI](https://hapi.humdata.org/) (PAM, OCHA) | voir HDX HAPI |
| Financement / funding | [FTS](https://fts.unocha.org/), OCHA | données ouvertes OCHA |
| Réfugiés / refugees | [HCR / UNHCR](https://www.unhcr.org/refugee-statistics/) | conditions du HCR |

Téléchargements du 11 novembre 2026. Le texte de la note cite ses sources par des liens. / Downloads dated 11 November 2026. The text cites its sources by links.

## ACLED : à régler avant publication / to settle before publishing

Relu le 11 novembre 2026. L'EULA n'autorise la publication que de travaux dérivés « transformatifs », qui ne permettent pas de reconstituer le jeu de données. Elle précise que réorganiser les données ou les présenter dans son propre tableau de bord ne suffit pas. Elle interdit aussi de laisser des robots ou des agents d'IA accéder aux données hors de l'API d'ACLED. `data.js` contient aujourd'hui les morts et événements par localité et par mois, ce qui est un cas limite que le texte ne tranche pas. Trois options : demander un accord écrit à ACLED, réduire `data.js` à des agrégats par région et par mois, ou retirer les cercles de la carte et ne garder que les graphiques. La politique d'attribution demande : la mention « ACLED (Armed Conflict Location & Event Data) » sur chaque visuel, un lien vers acleddata.com, la date d'accès, les filtres utilisés et ce qui a été modifié (ici : Soudan, avril 2023 à octobre 2026, violence politique, agrégation par localité et par mois, téléchargé de HDX le 11 novembre 2026). La licence affichée sur la page HDX n'a pas pu être lue automatiquement.

Reread on 11 November 2026. The EULA only allows publishing derivative work that is "transformative" and cannot be used to reconstruct the dataset. It states that reorganising the data or showing it in one's own dashboard is not enough. It also forbids letting bots or AI agents access the data other than through ACLED's API. `data.js` currently holds deaths and events per locality per month, a borderline case the text does not settle. Three options: ask ACLED for written permission, reduce `data.js` to aggregates by region and month, or remove the circles from the map and keep only the charts. The attribution policy requires: "ACLED (Armed Conflict Location & Event Data)" on each visual, a link to acleddata.com, the access date, the filters used and what was changed (here: Sudan, April 2023 to October 2026, political violence, aggregated by locality and month, downloaded from HDX on 11 November 2026). The licence shown on the HDX page could not be read automatically.

## Méthode / Method

1. Un relevé du module Wikipedia par mois. Les mois sans modification reprennent le précédent. / One snapshot of the Wikipedia module per month. Months with no edit repeat the previous one.
2. Une localité (admin2) prend la couleur majoritaire de ses villes suivies, pondérée par leur taille. Sans ville suivie, celle des trois villes les plus proches à moins de 250 km. Sinon, pas de couleur. / A locality (admin2) takes the majority colour of its tracked towns, weighted by size. With none, that of the three nearest towns within 250 km. Otherwise no colour.
3. Une ville n'a pas de couleur avant d'apparaître sur la carte source. / A town has no colour before it appears on the source map.
4. Les localités de plus de 40 000 km² sont découpées autour de leurs villes, dans un rayon de 150 km. Le reste est sans relevé. / Localities above 40,000 km² are split around their towns within 150 km. The rest has no reading.
5. `manual_updates.json` corrige la carte source là où elle se trompe (Nyala et Ed Daein en 2023, triangle frontalier en 2025) et ajoute les changements postérieurs au 17 août 2026 confirmés par deux sources indépendantes (Sodari). Une annonce d'un seul camp n'est pas appliquée. / `manual_updates.json` corrects the source map where it is wrong (Nyala and Ed Daein in 2023, border triangle in 2025) and adds changes after 17 August 2026 confirmed by two independent sources (Sodari). A one-sided announcement is not applied.

## Limites / Limits

- La carte suit des villes et non des lignes de front. Les surfaces surestiment le contrôle réel. / The map tracks towns, not front lines. Areas overstate real control.
- Avril à octobre 2023 repose sur 20 à 70 villes. / April to October 2023 rests on 20 to 70 towns.
- Aucun relevé de contrôle après le 17 août 2026, sauf deux ajouts manuels. / No control snapshot after 17 August 2026, except two manual additions.
- Les morts ACLED sont un minimum. / ACLED deaths are a minimum.
- Les routes sont schématiques. / Roads are schematic.
- Sources non disponibles sur ce poste : ReliefWeb (identifiant refusé), ACLED par événement, ACAPS et IDMC (clés absentes), WFP HungerMap (Soudan non publié), Liveuamap (accès refusé). / Sources unavailable on this machine: ReliefWeb (app name refused), ACLED event data, ACAPS and IDMC (no keys), WFP HungerMap (Sudan withheld), Liveuamap (access refused).

## Régénérer / Rebuild

```bash
python3 -m venv .venv && .venv/bin/pip install shapely openpyxl
```

```bash
python3 wiki_hist.py raw/wiki
```

```bash
python3 -X utf8 fetch_extra.py
```

```bash
.venv/bin/python build_data.py
```

```bash
python3 build_page.py
```

`wiki_hist.py` ne retélécharge pas un mois déjà présent : supprimer le fichier du mois en cours pour le rafraîchir. L'API Wikipedia limite le débit. `fetch_extra.py` attend le dépôt [humanitarian-secondary-data](https://github.com/13w13/humanitarian-secondary-data) cloné dans `../hsd`. Les fichiers HDX de `raw/` se téléchargent depuis les fiches liées plus haut.

`wiki_hist.py` does not re-download a month already present: delete the current month's file to refresh it. The Wikipedia API is rate-limited. `fetch_extra.py` expects the [humanitarian-secondary-data](https://github.com/13w13/humanitarian-secondary-data) repository cloned in `../hsd`. The HDX files in `raw/` are downloaded from the pages linked above.
