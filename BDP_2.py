'''
Olvass be a billentyűzetről egy max 20 karakter hosszú mondatot, 
amely csak az angol ABC betűit tartalmazhatja. Végezd el a szükséges input ellenőrzést, 
majd a beolvasott mondatot előbb fordítsd meg, és utána változtasd mindegyik második betűjét 
nagybetűvé!
'''

x=input("Adj meg egy max. 20 karakter hosszú szöveget, csak az angol abc betűit használhatod!")
asd=['ö', 'ü', 'ó', 'ő', 'ú', 'é', 'á', 'ű', 'í']
forditott=x[::-1]
caps=[]

while len(x)>20:
    print("Túl hosszú a szöveged!")
    x=input("Adj meg egy max. 20 karakter hosszú szöveget, csak az angol abc betűit használhatod!")

for i in x:
    if i in asd:
        print("Csak angol betűket")
        x=input("Adj meg egy max. 20 karakter hosszú szöveget, csak az angol abc betűit használhatod!")
print(x)

for i in range(len(forditott)):
    if not i%2:
        caps.append(forditott[i])
    else:
        caps.append(forditott[i].upper())

forditott="".join(caps)

print(forditott)