import random
tomb=[]
jebo=[]

for i in range(100):
    tomb.append(random.randint(-50,50))
print(tomb)

for i in range(0,len(tomb)):
    if tomb[i]<0:
        if tomb[i]%2!=0:
            print(tomb[i], end=" ")
tomb=[]
tomb.append(int(input("Adj meg egy számot: ")))
for i in range(1,10):
    szam=int(input("Adj meg egy számot: "))
    while szam in tomb:
        szam=int(input("Másikat, mertez már volt!"))
    tomb.append(szam)
print(tomb)

for x in range(len(tomb)):
    kicsi = 9999999999999999
    for i in tomb:
        if i<kicsi:
            kicsi=i
    jebo.append(kicsi)
    tomb.remove(kicsi)
print("Ugyanezek sorba rendezve:")
print(jebo)