# írj egy programot két járékos játszik és dobókockát kell dobálni
# először az első játékos dob x gomb megnyomásával, majd a második játékos dob az y gomb megnyomásával.
# A számokat random generátorral kell előállítani. Majd írja ki a progran, hogy melyik játékos nyert.
# Az nyer, aki nagyobbat dob. Valósítsd meg függvény segítségével a programot!
# A program fusson addig, amíg meg nem nyomjuk a "q" gombot
import random
def jatek():
    jatekosok = ["x","y"]

    while (input("Kezd el a játékot! Kilépéshez nyomd meg a 'q' gombot"))!='q':
        x=input("Az első játékos dob, nyomd meg az 'x' gombot!")
        while x!=jatekosok[0]:
            print("Rossz gombot nyomtál meg!")
            x=input("Az első játékos dob, nyomd meg az 'x' gombot!")
        szam1=random.randint(1,6)
        y=input("A 2. játékos dob, nyomd meg az 'y' gombot!")
        while y!=jatekosok[1]:
            print("Rossz gombot nyomtál meg!")
            y=input("Az első játékos dob, nyomd meg az 'x' gombot!")
        szam2=random.randint(1,6)
        if szam1>szam2:
            print("Az első játékos nyert!")
        elif szam2>szam1:
            print("A második játékos nyert!")
        else:
            print("Döntetlen!")
jatek()