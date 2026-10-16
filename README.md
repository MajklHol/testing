# Slepá mapa Slovenska

Kvíz na slepej mape Slovenska. Nad mapou sa zobrazí názov mesta, ty klikneš, kde si myslíš, že leží, a aplikácia ukáže skutočnú polohu a o koľko km si sa minul. Za trafu sa počíta klik do 15 km.

Obsahuje 68 miest nad 10 000 obyvateľov a tri režimy: všetky mestá, mestá nad 20 000 obyvateľov a rýchle kolo s 10 mestami.

## Spustenie

Otvor `index.html` v prehliadači. Nepotrebuje server ani inštaláciu.

## Štruktúra

| Súbor | Obsah |
| --- | --- |
| `index.html` | Hotová stránka (vygenerovaná, needitovať ručne) |
| `src/template.html` | Zdroj stránky: vzhľad, zoznam miest a logika kvízu |
| `data/map-paths.json` | Hranica a rieky ako SVG cesty v kilometroch |
| `data/slovakia-border.geojson` | Hranica Slovenska z Natural Earth (1:10m) |
| `tools/build.py` | Zostaví `index.html` zo šablóny a dát |
| `tools/geo.py` | Vyrobí `map-paths.json` z dát Natural Earth |

Po úprave šablóny spusti `python3 tools/build.py`.

## Dáta

- Hranica a rieky: [Natural Earth](https://www.naturalearthdata.com/) (public domain).
- Zoznam miest, počty obyvateľov a súradnice sú zostavené bez prístupu k online zdrojom a sú približné. Mestá okolo hranice 10 000 obyvateľov treba ešte overiť podľa sčítania 2021.
