#tölts fel egy listát vegyesen egész számokkal és stringekkel,
#vagy irasd ki a listából csak az egész számokat. Az adatokat futási időben kell megadni.

lista=[]

for i in range(10):
    lista.append(input("Adj meg egy elemet:"))

ujlista=[x for x in lista if type(x)==int]
print(ujlista)