tomb=[]
tomb.append(int(input("HJ")))
for i in range(1,10):
    szam=int(input("fdfadkjslhé"))
    while szam in tomb:
        szam=int(input("dlhkjsbvg"))
    tomb.append(szam)

print(tomb)
#buborék rendezés
'''
Az egymás utáni elemeket összehasonlítjuk. Ha a nagyobb értékű elem alacsonyabb indexű helyen van akkor kicseréljük őket.
A tömbön először végighaladva a legnagyobb elem a legnagyobb sorszámú helyen lesz.
A külső ciklus (n-1)-től haéad 1-ig, visszafelé. A belső ciklus 0-tól iterál (i-1)-ig.
'''
for i in range(len(tomb),1,-1):
    for j in range(i-1):
        if tomb[j]>tomb[j+1]:
            temp=tomb[j+1]
            tomb[j+1]=tomb[j]
            tomb[j]=temp

print(tomb)

#cserés rendezés
'''
A tömb 1...n eleme közül kiválasztja a legkisebbet, majd a legelső elem heylére teszi.
A tömb 2...n eleme közül kiválasztja a legkisebbet, majd a legelső elem heylére teszi.
És így tovább
'''
for i in range(len(tomb)-1):
    for j in range(i+1,len(tomb)):
        if tomb[i]>tomb[j]:
            temp=tomb[j]
            tomb[j]=tomb[i]
            tomb[i]=temp
print(tomb)

#beszúrásos rendezés
'''
Sorra egymás után kiemeljük a tömb elemeit. Ha a kiemelt elem előtt nála nayobb elemet találunk, akkor azokat egyel hátrább másoljuk.
'''

for i in range(1,len(tomb)):
    kulcs=tomb[i]
    j=i-1
    while j>=0 and tomb[j]>kulcs:
        tomb[j+1]=tomb[j]
        j-=1
    tomb[j+1]=kulcs

print(tomb)