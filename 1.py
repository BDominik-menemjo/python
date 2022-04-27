"""
Tölts fel egy listát pontosan 5 db egész véletlen egyjegyű számmal.
Értékeld ki a listát, hogy halmaz-e. Ezt végezd el egy függvénnyel.
Akkor tekinthető halmaznak a lista, ha nincs benne ismétlődő elem.
Ismételd meg a folyamatot 10x és minden alkalommal írd ki a vizsgálat 
eredményét!
"""

import random

def egesz():
    tomb=[]
    for i in range(5):
        tomb.append(random.randint(0, 9))
    print(tomb)
    
    for i in tomb:
        if tomb.count(i)>1:
            return "Nem halmaz"
    return "Halmaz"

for i in range(10):
    print(egesz())