lista=[]
magan=['a', 'e', 'i', 'u', 'o', 'ö', 'ü', 'ó', 'ő', 'ú', 'é', 'á', 'ű', 'í']
mgh=[]

x=input("Írj le egy maximum 20 karakteres szöveget!")
while len(x)>20:
    print("Túl hosszú a szöveged!")
    x=input("Írj le egy maximum 20 karakteres szöveget!")

for i in x:
    lista.append(i)

print(lista)

for i in lista:
    if i in mgh:
        mgh.append(i)

print(mgh)