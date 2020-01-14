# Autó Biztonsági Rendszer
## Felhasználói dokumentáció

#### Összefoglalás

Biztonági rendszerünk autókba behelyezve védelmet nyújt az esetleges balesetek megelőzése ellen. Kritikus dőlésszögeket beállítva, a Sense HAT-en elhelyezett LED-mátrix mutatja, merre dől az autó, és van lehetőség a jármű korrigálására, felborulva pedig egy segítségkérő Twitter üzenetet oszt meg. Az eszköz mindemellett képes arra, hogy hirtelen túl nagy G gyorsulást mérve azt feltételezze, hogy az autó ütközött, így ekkor az ütközésről fog tweetelni. A program elindítását követően folyamatosan gyűjti az adatokat az eszköz egy helyi adatbázisba, amit grafikusan is megjelenít.

#### Környezet

* Raspberry Pi, Sense HAT, .py futtatására alkalmas operációs rendszer (Linux).
* Egeret, billentyűzetet, monitort és internetet igényel.
	
#### Használat

Átlagos felhasználó számára az adatbázis lényegtelen, mivel ezt egy adatelemző fogja kiolvasni, aki ezáltal tudja modellezni a balesetet. A sofőrnek csupán elég az autóban elhelyezett Sense HAT LED-mátrixára figyelni, ami jelzi a dőlésirányt.

*A program indítása*
	
	A program	
		Main.py
	néven található, a /pi mappában.

*A program eredménye*

A program elindítja az adatok naplózását egy lokális adatbázisba a hozzájuk tartozó dátummal, és képes mindezt grafikus ábrán megjeleníteni.
Felborulás és ütközés esetén Twitter üzentet küld a problémáról.
Leállítása kézi beavatkozást igényel.
		
*Egy lehetséges kimenet*

![Kep1](https://i.imgur.com/hheDdPi.png)

Futás közben is kapunk visszajelzést az aktuális értékekről.



![Kep2](https://i.imgur.com/pwOY5SX.png)

Egy kommunikációs csatornán keresztül válik publikusság a baleset.


*Hibalehetőség*

A program leállítása nem automatikus, mert egyéni döntés, meddig akarjuk használni. Abban az esetben, ha a programot huzamosabb ideig használjuk, a memória képes betelni és az adatokat nem rögzíteni az adatbázisba.

## Fejlesztői dokumentáció

#### Tervezés

A projekt témájának kiválasztása során fontos tényező volt, hogy egy használható, és hasznos mikroprocesszor által vezérelt ötletet eszeljünk ki. Manapság folyamatosan közúti balesetek és az ezzel járó halálos áldozatok megdöbbentően nagy számú cikkekkeivel találkozunk szerte az interneten, újságokban és a televízióban is. Az általunk elkészített Autós Biztonsági Rendszer segítséget nyújt a balesetek megelőzésében és a gyorsabb reagálásban a segítség nyújtásához.

#### Hibák megoldása

A Twitter API-ja nem engedélyezi kétszer, egymás után ugyan annak a szövegnek a tweetelését, erre egy *Status is duplicate* nevű hibaüzentet hozott fel. A probléma megoldására egy kritikus gyorsulási vagy dőlési szöget írattunk ki (a balesetnek megfelelően) a segélykérés után, ami *float*-ként lett megadva, így szinte bekövetkezhetetlen, hogy egymás után kétszer mérje ugyan azt az értéket. Továbbfejlesztésként ezt GPS koordinátákra cserélnénk, hogy a segítséget pontos helyre lehessen irányítani. Elég valószínűtlen kétszer, egymás után, ugyan azok a helyen felborulni és/vagy ütközni, ezért a tweeteléssel csak a tesztfázisban lehet hiba, ha egy helyen végezzük a tesztelést.

#### Környezet

* Raspberry Pi, Sense HAT, .py futtatására alkalmas operációs rendszer (Linux).
* Python III fordítóprogram.
* Internetwebcímhelye a grafikai megjelenítésre.
* Internet és fejlesztői Twitter felhasználó az automatikus üzenetküldésre.

#### Forráskód
	/globals.py 		- a változók inicializálása
	/Database		- az adatbázis létrehozása
	/insertdatabase.py	- az adatbázis importálása, és a megfelelő 
						formátumok beállítása
	/Arrows.py		- a dőlés függvényében a nyilak megjelnítése a 
						LED-mátrixon.
	/tweet.py		- automatikus tweetelés
	/Main.py		- végleges futtatható kód, az előző kódokat meghívva

#### Megoldás

*Fontos programrészek*
	
*insertdatabase.py*
```python
	import mysql.connector
	from datetime import datetime
	from sense_hat import SenseHat
	import time
		
		
	def insert(pitch,roll,yaw,x,y,z):
    		mydb=mysql.connector.connect(host="localhost", user="Raspberry", password="root", database="exampledb4")
    		mycursor=mydb.cursor()
    		now=datetime.now()
    		formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')
    		sql="""INSERT INTO adatok (datum,pitch,roll,yaw,backwardforward,rightleft,updown)
    		VALUES(%s,%s,%s,%s,%s,%s,%s)"""
   		val=(formatted_date,pitch,roll,yaw,x,y,z)
    		mycursor.execute(sql,val)
    		mydb.commit()
    		time.sleep(0.2)
    		mycursor.close()
    		mydb.close()
```

A programban szükséges deklarálni a létrehozott adatbázis elérhetőségét és szükséges a jelszót megadni a *mysql.connector.connect()* függvényben. A *mycursor=mydb.cursor()* és a *now=datetime.now()* függvényekkel az adatbázisba való írást és az időt beállítottuk.
Ezek után *formatted_date=now.strftime('%Y-%m-%d %H:%M:%S')*-el a megfelelő formátumban kapjuk meg a dátumot. A mérések eredményeit és idejét be kell illeszteni a még eddig üres adatbázisunkba. A *sql="""INSERT INTO adatok (datum,pitch,roll,yaw,backwardforward,rightleft,updown)* sora ezt mutatja. A *time.sleep()* függvénnyel állítottunk be 0.2 másodpercenkénti újabb mérést.

*tweet.py*

A segítségkérő üzenet létrehozásához készíteni kellett egy Developer Twitter Accountot, amihez különböző *kulcsokat*, *secret külcsokat*, *tokeneket*, és *secret tokeneket* kaptunk. Mindemellett az operációs rendszerre (Linux) telepíteni kellet egy tweepy nevű modult amivel kapcsolatba tudunk lépni a Twitterel a posztoláshoz.
```python
	


```
*Main.py*

```python
	...
	if (pitch>90 and pitch <270) or (roll>90 and roll <270):
		s.set_pixels( Arrows.piros_x() )
		
	elif pitch >40 and pitch <90:
		s.set_pixels( Arrows.nyil_balra())
	...
```
Az arrows.py függvény meghívásával és a kritikus dőlésszögek 50 fokra beállításával, jelzi ki az eszköz a dölés irányát, illetve a borulást.


#### Jövőbeli továbbfejlesztés

A rendszer a probléma twittelése esetén egy értéket is visszaad a segítségkérő üzenet ütán, ezt egy GPS-modul segítségével koordinátákra lehet cserélni, hogy tudjuk, hol is történt a baleset.
Havi támogatás keretein belül, egy Cloud SQL előfizetést létrehozni, és az adatbázist automatikusan feltölteni, hogy ne csak a lokális szerveren legyen elérhető, hanem online bármilyen eszközről, ugyanis egy esetleges ütközés eseten a Raspberry Pi használhatatlanná válik.