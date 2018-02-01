QGIS projekt konfiguracio a plugin hasznalatahoz
################################################

Snapping options
****************

Lehetove teszi az geometria objektumok konnyebb illeszthetoseget es csokkenti a hibasan illesztett csovek / csomopontok szamat.

* Snapping mode: Advanced
* Minden layerhez:

  * Mode: **to vertex and segment**
  * Tolerance: **20**
  * Units: **pixels**
                  
Formazasi beallitasok
*********************

A jobb attekinthetoseg es bizonyos adatok egyszeru leolvasasa erdekeben, a geometriai objektumokat kulonbozoen formazzuk, cimkeket jelenitunk meg.

Formazas reszei
===============

*Style:*

Elemek:

* Rule-based

  * Szivattyu, SVG kep, ``tipus=Szivattyu``
  * Halozat nem ellenorzott, kis pont kek, ``assoc_err=0``
  * Halozat OK, kis pont zold, ``assoc_err=2``
  * Halozati hiba, nagyobb pont piros, ``assoc_err=1``

Szakaszok:

* Rule-based

  * Halozat hiba, piros, ``assoc_err=1``
  * Halozat OK, zold, ``accoc_err=2``
  * Halozat nem ellenorzott, sarga, ``assoc_err=0``

*Cimkek:*

* Beallitas: Show labels for this layer
* Megjelenitendo cimke adat
* Font (tipus, meret, szin)
* Line direction symbol (above)

*Mezok:*

* Mezok szerkesztesi beallitasa: Provide ui-file, ``szakaszok_form.ui``

