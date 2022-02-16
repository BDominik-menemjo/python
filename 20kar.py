lista=[]
magan=['a', 'e', 'i', 'u', 'o', 'ö', 'ü', 'ó', 'ő', 'ú', 'é', 'á', 'ű', 'í']
mgh=[]
msh=[]

x=input("Írj le egy maximum 20 karakteres szöveget!")
while len(x)>20:
    print("Túl hosszú a szöveged!")
    x=input("Írj le egy maximum 20 karakteres szöveget!")

for i in x:
    lista.append(i)

print(lista)

for i in magan:
    for i in lista:
        mgh.append(i)

print(mgh)
