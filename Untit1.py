'''

'''
mondat=input("Adj megy egy max 50 karakter hosszú mondatot: ")
while len(mondat)>50:
    print("A mondat hosszabb mont 50 karakter!")
    mondat=input("Adj megy egy max 50 karakter hosszú mondatot: ")
while len(mondat)<=50:
    for i in mondat:
        if not ((i>='A' and i<='Z') or (i>='a' and i<='z') or i=='.'):
            print("A mondatban csak ékezet nélküli betűk lehetnek!")
            mondat=input("Adj megy egy max 50 karakter hosszú mondatot: ")
szoDarab=mondat.split(' ')
print("A mondatban szereplő szavak száma: %d" %len(szoDarab))
for i in range(len(szoDarab)):
    szoDarab[i].capitalize()
mondat=' '.join(szoDarab)
print("A szavak kezdőbetűje nagybetűre változtatva: \n%s" %mondat)