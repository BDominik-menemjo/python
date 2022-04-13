"""
        Osztályok és objektumok
    
    A pythonban szinte minden objektum, a tulajdonségokkal és metódusokkal együtt.

    Osztályt létrehozni a 'class' kulcsszóval lehet.
"""

class en_osztalyom:
    x=5

osztaly=en_osztalyom()

#print(osztaly.x)

"""
    Hogy jobban megértsük az osztályokat, meg kell előbb érteni az __init()__ függvényt.
    Minden osztálynak van egy __init()__ függvénye, amely minden alkalommal lefut, amikor inicializáljuk.

    Hogy megértsük, hozzunk létre egy osztálya és használjuk az __init()__ figgvényt,
    hogy értékeket rendeljünk a névhez és a korhoz.
"""

'''
            class Szemely:
                def __init__(self, name, age):
                    self.name=name
                    self.age=age

            szemely1=Szemely("Pista", 21)

            print(szemely1.name)
            print(szemely1.age)
'''

"""
    Az __init()__ függvény automatikusan meghívódik minden egyes alkalommal, amikor használjuk az
    osztályt, egy új objektum létrehozására.
    A self paraméter a pillanatnyi osztály állapotra hivatkozik és ezzel tudjuk elérni az osztályhoz
    tartozó változókat. Nem kötelező self-nek nevvezni, elnevezhetjük bárminek, de az osztályon belüli
    függvények első paramétere kell hogy legyen.
    
    Nézzünk egy újabb példát erre
"""

'''
class Szemely:
    def __init__(osztaly_neve, nev, eletkor):
        osztaly_neve.nev=nev
        osztaly_neve.eletkor=eletkor
    
    def az_en_nevem(ez_lehet_barmi):
        print("Az én nevem " + ez_lehet_barmi.nev)
    
    def az_en_korom(megint_lehez_barmi_a_neve):
        print("Az én korom " + str(megint_lehez_barmi_a_neve.eletkor))

szemely1=Szemely("Jóska", 55)
szemely1.az_en_nevem()
szemely1.az_en_korom()
# meg is tudom változtatni az objektum valamelyik értékét
szemely1.eletkor=34
szemely1.az_en_korom()
'''

# Törölni is tudunk objektum tulajdonságokat, vagy egész objektumot is

'''
del szemely1.eletkor
szemely1.az_en_korom()
'''
'''
del szemely1
szemely1.az_en_nevem()
'''
