# HMV-meretezes

Használati melegvíz csőrendszer méretező plugin QGIS-hez.

## Telepítés

## Használat

### Plugin indítása

A telepítés után a plugin-nek meg kell jelennie a QGIS alkalmazás Plugins menüje alatt:

Plugins - HMV Méretezés - HMV Méretezés

Erre kattintva lehet a plugin-t indítani, amely a munkaterülettől jobbra jelenik meg egy beépülő panelban.

### Munkarétegek létrehozása

A csőhálózat elemzéséhez kétféle vektor réteget kell létrehoznunk a QGIS-ben:

- Egy csomópont réteget a csőhálózat kötőelemek, végpontok és a szivattyú részére. (Point layer)
- Egy szakasz réteget az ezeket összekötő csőszakaszok részére. (Line Layer)

Ezt a következőképp tehetjük meg:

- Válasszuk a Beállítások fület.
- Az Új HMV réteg szekcióban:
  - Adjuk meg a létrehozandó réteg nevét a Réteg név mezőben.
  - Az Adatbázis file név mező automatikusan kitöltődik, ha a File név réteg név szerint? opció ki van pipálva.
  - Ha saját magunk adnánk meg az adatbázis file nevét (például azért mert több réteggel is dolgozunk és szeretnénk mindet egy file-ban tárolni), kapcsoljuk ki a File név réteg név szerint? opciót és adjuk meg a választott file nevet. (A file minden esetben a Réteg munkakönytár mezőben megadott helyen lesz létrehozva.
  - Válassza ki, hogy elemek vagy szakaszok típusú réteget szeretne létrehozni, egy HMV hálózat elemzéséhez egy-egy összetartozó elemek és szakaszok rétegre van szükség.
  - A réteg QGIS projekthez való automatikus hozzáadásához a Hozzáadás réteg listához? opciót be kell kapcsolni.
  - Nyomja meg a Létrehoz gombot.
  
A rendszer ezután létrehoz egy SpatiaLite adatbázist a megadott file névvel, ha még nem létezik. Ha már van ilyen nevű adatbázis file a réteg munkakönyvtárban, akkor megkérdezi, hogy az új réteget a már létező file-ba mentheti-e. Ezután a választott réteg típus létrehozásra kerül az adatbázisban, fontos, hogy ilyenkor a plugin által végzendő kalkulációkhoz szükséges feature attribútumok is létrehozásra kerülnek. Ebből kifolyólag nem javasolt a rétegek manuális létrehozása a QGIS eszközökkel (New SpatiaLite Layer, New Shapefile Layer), mert így elkerülhető az attribútumok manuális létrehozásával járó plusz munka és esetleges esetleges konfigurációs, vagy adatbeviteli hiba lehetősége.

Ha a létrehozáskor kiválasztotta a Hozzzáadás réteglistához? opciót, akkor az újonnan létrehozott réteg automatikusan hozzáadásra kerül a Rétegek Panel-hez (Layers Panel). Ellenkező esetben, ha szeretné hozzáadni az adott rétegeket a QGIS projektjéhez, kövesse a Már meglévő rétegek megnyitása részt.

### Már meglévő rétegek megnyitása

Ha a rétegek, amelyekkel dolgozni szeretne szerepelnek a Rétegek Panel-ben (Layers Panel), például, mert a réteg létrehozásakor kiválasztotta a Hozzáadás réteglistához? opciót, vagy egy korábban elmentett QGIS projektet nyitott meg, amelyben a rétegek amikkel dolgozni szeretne meg voltak nyitva, akkor nincs szükség erre a lépésre.

Ha egy adatbázisban már meglévő, de a QGIS projektben nem szereplő réteget meg szeretne nyitni (hozzáadni a Rétegek Panel-hez), akkor kövesse az alábbiakat.

Megjegyzés: A QGIS-ben a rétegek létrehozása a legkülönbözőbb adatforrásokból lehetséges, azonban mivel a plugin SpatiaLite adatbázisban hozza létre a HMV analízishez megfelelően konfigurált régeteket, így a rétegek SpatiaLite adatbázisból való megnyitását tárgyaljuk.

- A Böngésző Panel-ben (Browser Panel) kattintson jobb egérgombbal a SpatiaLite elemre.
- Válassza az Új Kapcsolat (New Connection) menüpontot.
- Keresse meg az adatbázis file-t.
- Nyissa meg.
- Az adatbázis most megjelenik a Böngésző Panel-ban (Browser Panel), a SpatiaLite elem alatti hierarchiában.
- Nyissa ki az adatbázis elem alatti hierarchiát a Böngésző Panel-ban (Browser Panel).
- Az adatbázisban tárolt rétegek megjelennek az adatbázis alatti hierarchiában.
- Kattintson jobb egérgombbal a projekthez hozzáadni kívánt rétegre és válassza a Réteg Hozzáadása (Add Layer) menüpontot.
- A Koordináta Referencia Rendszer Kiválasztó-ban (Coordinate Reference System Selector) ne módosítsa az alapbeállítást (WGS84) és kattintson az OK gombra.
- A réteg hozzáadásra kerül a Rétegek Panel-hez (Layers Panel).

### Analízis munkarétegek kiválasztása

Az méretezési számítások elvégzéséhez a HMV hálózatot két összefüggő vektor rétegre kell felrajzolni és az elemek paramétereit megadni. Ha az értékelendő HMV hálózat meghatározásához szükséges elem és csőhálózat réteg be van töltve a Rétegek panel-ba (Layers Panel):

- A Beállítások fülön, nyomja meg a Réteg választás felirat melletti frissítés gombot.
- A plugin betölti az Elemek QGIS réteg és Csőhálózat QGIS réteg legördülő menübe a megfelelő típusú rétegeket (pont és szakasz) a Rétegek panel-ból (Layers Panel).
- Válassza ki a munkához használni kívánt rétegeket az Elemek QGIS réteg és Csőhálózat QGIS réteg legördülő menüben.
- A plugin funkciói mostantól a kiválasztott rétegekre kerülnek alkalmazásra.

### Használatban lévő munkarétegek formázása

A hálózat ábrázolásának áttekinhetőbbé és informatívabbá tétele érdekében a kiválasztott munkarétegekeket egy gombnyomással formázhatjuk, ezzel a különböző objektumtípusok kiemelésre a kulcsadatok pedig megjelenítésre kerülnek a rajzon.

### Kiindulási adatok megadása

A Beállítások fül alatt lehetőség van a számításokhoz használt rendszerszintű kiindulási adatok megadására. Ezek:

- Sűrűség: közeg (víz) sűrűsége, mértékegysége kg/m³
- Fajhő: közeg (víz) fajhője, mértékegysége J/kgK
- Δϑ: tervezett hőmérséklet csökkenés a tárolótól a csapig, mértékegysége K
- Csősebesség: közeg tervezett csősebessége, mértékegysége m/s

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
