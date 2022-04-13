"""
    Feladat: Hozz létre ehy Auto osztályt, amely a köv. tulajdonságokat tartalmazza:
    Márka, modell, típus, tankméret, üzemanyagszint
    Hozz létre benne egy függvényt, amely kiírja, hogyí hány százalékos a pillanatnyi üzemanyag szint
    és figyelmeztessen a tankolásra.
    Minden adatot inputról
"""
"""
    Egészítsd ki, hogy három adatot kérjen be és írd bele egy csv fájlba
"""

f=open("C:\\Users\\diak\\Documents\\Bélai Dominik Péter 10.i\\python\\autok.csv", "w")

f.writelines("Márka;Modell;Típus;Tank mérete;Üzemanyagszint""\n")

class Auto:
    def __init__(self, marka, modell, tipus, tank, uzem):
        self.marka=marka
        self.modell=modell
        self.tipus=tipus
        self.tank=tank
        self.uzem=uzem     

    def szint(self):
        asd=int(self.uzem/self.tank*100)
        if asd<=10:
            print("A tank szintje %d%% szinten van, menj tankolni!" %asd)
        else:
            print("A tank szintje egyelőre rendben van!")

    def tipus_kiir(self):
        print("Az autó: %s %s %s" %(self.marka, self.modell, self.tipus))

    def fajliras(self):
        f.writelines(self.marka+";"+self.modell+";"+self.tipus+";"+str(self.tank)+";"+str(self.uzem)+"\n")

marka=input("Add meg a kocsi márkáját: ")
modell=input("Add meg a kocsi modelljét: ")
tipus=input("Add meg a kocsi típusát: ")
tank=int(input("Add meg a kocsi tankjának a méretét: "))
uzem=int(input("Add meg a kocsi uzemanyag szintjét: "))  

auto=Auto(marka, modell, tipus, tank, uzem)

auto.szint()
auto.tipus_kiir()
auto.fajliras()
