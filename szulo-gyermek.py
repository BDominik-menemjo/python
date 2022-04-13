"""
                                        Öröklődés

    Olyan tulajdonság, mely lehetővé teszi, hogy osztályok örökölhessék egymás tul.ait.

    Szülőosztályból adjuk tovább a tulajdonságokat. 
    Gyermekosztály örökli ezt.
"""

# Hozzunk létre egy új szülő fájlt

class Szemely:
    def __init__(self, vnev, knev):
        self.vezeteknev=vnev
        self.keresztnev=knev

    def printnev(self):
        print(self.vezeteknev, self.keresztnev)

szemely=Szemely("Kiss", "Pista")
szemely.printnev()

# Most létre hozunk egy gyermek osztályt, amely örökli a Szemely osztály minden tulajdonságát
class Diak(Szemely):
    pass # Nem lehet üres, ezért egy pass parancsot használunk

diak=Diak("Vicc", "Elek")
diak.printnev()

"""
    Ha a gyermek osztályban létrehoznék egy __init__() függvényt, az felülítna a szülőosztályét, és nem örökölné tovább a szülő osztály
    __init__() függvényének tulajdonságait, a köv. módon kell rá hivatkozni:
"""

class Diak(Szemely):
    def __init__(self, vnev, knev):
        Szemely.__init__(vnev, knev)
        # ugyan ezt meg lehet tenni a super() függvénnyel, amely hivatkozik a szülő osztály nevére:
        # super().__init__(self, vnev, knev)
        # a super()-nál nem kell self
        # Továbbá új tul.-t is tudunk létrehozni
        self.eretsegi_eve=2022

diak=Diak("Kiss", "Pista")
print(diak.eretsegi_eve)