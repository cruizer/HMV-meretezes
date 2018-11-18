Számítások
##########

Szakaszokra végzett számítások
******************************

Minden *m* szakaszra számítandó az adott szakasz hővesztesége a következő egyenletekkel:

Hőátbocsátási tényező [W/mK]
============================

.. math::

   k_{m} = \frac{\pi}{\frac{1}{2 \cdot \lambda_{m}} \cdot \ln\frac{D_{m}}{d_{m}} + \frac{1}{\alpha_{k;m} \cdot \frac{d_{m}}{1000}}}

kᵥ = π / ( ( 1 / ( 2 · λₘ ) ) · ln( Dₘ - dₘ ) + ( 1 / ( αₖₘ · Dₘ / 1000 ) ) )

Hőleadás [W/m]
==============

q̇ₘ = kₘ · ( Tₕₘᵥ - Tₕ )

Szakasz hővesztesége [W]
========================

Q̇ₘ = q̇ₘ · Lₘ

Előremenő hálózatra végzett számitások
**************************************

Miután a szakaszokra kiszámitásra kerültek az értékek, kiszámíthatóak ezekből a rendszer vonatkozó értékek.

Teljes előremenő hálózat hővesztesége [W]
=========================================

Az összes szakasz hőveszteségét összeadva kapjuk meg a teljes előremenő hálózat hőveszteségét.

Q̇ = ∑Q̇ₘ

Szükséges tömegáram [m³/s] · 3,6 · 10⁶ = [dm³/h]
================================================

Ez a szivattyú által biztosítandó cirkulációs térfogatáram. Kiszámítható a teljes előremenő hálózat hőveszteség, a közeg sűrűség és fajhő, illetve a tárolótól a csapig tervezett hőmérséklet csökkenés függvényéből.

V̇       = Q̇ / ( ρ · c · Δϑ )

Csomópontokra végzett számítások
********************************

Csomópontokban hátralévő hőveszteségek
======================================

A csomópontból kiágazó ágak összes hővesztesége a cirkulációs vezetékek lecsatlakozásáig. A hőveszteséget a hálózaton a cirkulációs vezeték lecsatlakozásától indulva az ágra vonatkozó addigi hőveszteség értékét görgetve számítjuk ki minden következő csomópontra, amire a csomópontból leágazó összes ágból összegeztük a hőveszteségek, tehát megkaptuk a végeredményt az adott csomópontra. Majd haladunk tovább visszafelé az előremenő hálózaton, egészen a HMV tárolóig.

Továbbhaladó és leágazó hőveszteségek
=====================================

Egy adott csomópontból egy kiválasztott szakaszon kiindulva, mennyi a cirkulációs lecsatlakozásig hátralévő szakaszok összes hővesztesége.

Ezt a következőképp számítjuk:

* A kiválasztott szakasz másik végződésének (a cirkulációs leágazás felé eső) csomópontjára számított összes hátralévő hőveszteségek
  és
* A kiválasztott szakasz hőveszteségének
    összege.

Szakaszok térfogatáramának meghatározása
========================================

  A hálózaton a HMV tároló berendezéstől indulva az előremenő hálózaton számítjuk. A csomópontba bejövő összes csőszakasz térfogatáramát szorozzuk a számolt vezeték leágazó hőveszteségével, osztva a csomópontban hátralévő összes hőveszteséggel.

Visszatero oldal csoatmerok meghatarozasa
*****************************************

  A eloremeno halozat szakaszoknak megfelelo visszatero oldali csoszakaszok atmeroit az eloremeno oldal terforgataramok, es a rendelkezesre allo csomeretek (konfiguracioban modosithato) szerint szamoljuk, a kovetkezo keplet szerint:

  wₘ = 4 · (V̇ₘ / 3,6 · 10⁶) / ((dₘ / 1000)² · π)

  Ezt a szamitast sorban elvegezzuk a rendelkezesre allo csomeretekkel, egeszen addig, amig a csosebesseg 0,2 m/s es 1 m/s koze nem esik, ha ez megtortenik, akkor az adott csoatmero a megfelelo.

Csosurlodasi tenyezo meghatarozasa
**********************************

  A csosurlodasi tenyezo szamitasanak modja fugg az aramlas termeszetetol, amit a Reynolds szam hataroz meg. Tehat eloszor ezt szamitjuk, ennek modja:

  Rₑ = wₘ · (dₘ / 1000) / vₘ

  Ahol vₘ a kinematikai viszkozitas, allando erteke 5 · 10⁻⁷ esetunkben.

  Ezutan:

* A csosurlodasi tenyezo szamitasa Rₑ <= 2300 eseten: λ = 64 / Rₑ
* A csosurlodasi tenyezo szamitase Rₑ > 2300 eseten: λ = 1 / (-2 · lg(2,51 / (Rₑ √λ)))²
