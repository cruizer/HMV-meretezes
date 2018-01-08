# HMV-meretezes

Használati melegvíz csőrendszer méretező plugin QGIS-hez.

## Telepítés

## Használat

### Munkarétegek létrehozása

A csőhálózat elemzéséhez kétféle vektor réteget kell létrehoznunk a QGIS-ben:


## Plugin komponensek

A plugin telepítéséhez a következő file-okat kell a QGIS plugin könyvtárába másolni, pl. az én esetemben a plugin file-ok itt vannak: ``~/.qgis2/python/plugins/hmv/``.

- ``__init__.py``: Plugin inicializációs szkriptje.
- ``chart.py``: Térfogatáram grafikon rajzolás.
- ``hmv_chart.py``: Térfogatáram grafikont megjelenítő widget. (Qt generált file)
- ``hmv_meretezes.py``: The main plugin program, containing most of the logic.
- ``hmv_meretezes_models.py``: Qt komponens modellek.
- ``hmv_meretezes_plugin.py``: A fő HmvPlugin objektum, ami összerakja a widget komponenseket és elindítja a plugint.
- ``hmv_results.py``: Az eredmény nézet. (Qt generált file)
- ``hmv_widget.py``: A fő widget nézet. (Qt generált file)
- ``metadata.txt``: Plugin metadata a QGIS-nek.
- ``pipesys_objects.py``: A csőhálózat objektumok.
- ``qt_utility.py``: Qt helper a megfelelő címke encodinghoz?
- ``ui_refresh.py``: A refresh ikont biztosító Qt resource file.
- ``refresh_rc``: Valamilyen refresh ikon resource file?

## QGIS projekt komponensek

### Projekt

A projekt file (``.qgs``) tarolja a projekt reszet kepezo retegek listajat, azok allapotat (pl. aktiv, meg van jelenitve, vagy nincs), tovabba a megjelenites formazasat, pl. hogy neznek ki az objektumok, milyen cimkezes van.

### Retegek

A reteg adatok az objektumok geometriajat, a felvett objektum mezoket, illetve az ezekben tarolt adatokat tartalmazzak (SpatialLite).

## QGIS projekt konfiguracio a plugin hasznalatahoz

### Snapping options

Lehetove teszi az geometria objektumok konnyebb illeszthetoseget es csokkenti a hibasan illesztett csovek / csomopontok szamat.

- Snapping mode: Advanced
- Minden layerhez:
  - Mode: **to vertex and segment**
  - Tolerance: **20**
  - Units: **pixels**
  
### Formazasi beallitasok

A jobb attekinthetoseg es bizonyos adatok egyszeru leolvasasa erdekeben, a geometriai objektumokat kulonbozoen formazzuk, cimkeket jelenitunk meg.

#### Formazas reszei

***Style:***

Elemek:

- Rule-based
  - Szivattyu, SVG kep, ``tipus=Szivattyu``
  - Halozat nem ellenorzott, kis pont kek, ``assoc_err=0``
  - Halozat OK, kis pont zold, ``assoc_err=2``
  - Halozati hiba, nagyobb pont piros, ``assoc_err=1``

Szakaszok:

- Rule-based
  - Halozat hiba, piros, ``assoc_err=1``
  - Halozat OK, zold, ``accoc_err=2``
  - Halozat nem ellenorzott, sarga, ``assoc_err=0``

***Cimkek:***

- Beallitas: Show labels for this layer
- Megjelenitendo cimke adat
- Font (tipus, meret, szin)
- Line direction symbol (above)

***Mezok:***

- Mezok szerkesztesi beallitasa: Provide ui-file, ``szakaszok_form.ui``
