"""
    20 db random elem, [1-100]
    prímek-e
    duplumokat kiszedni
"""

import random

tomb=[random.randint(1,100) for i in range(20)]
tomb2=list(set(tomb))
    
print(tomb)
print(tomb2)
    
def prim(szam):
    if szam==1:
        return False
    elif szam==2:
        return True
    else:
        for x in range(2, szam):
            if szam%x==0:
                return False
        return True
    
for szam in tomb2:
    if prim(szam):
        print("A %d prím szám!" %szam)
    else:
        print("A %d szám nem prímszám!" %szam)