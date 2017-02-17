# HMV-meretezes

Használati melegvíz csőrendszer méretező plugin QGIS-hez.

## Telepítés

## Használat

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
