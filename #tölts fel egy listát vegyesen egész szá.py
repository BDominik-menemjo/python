#tölts fel egy listát vegyesen egész számokkal és stringekkel,
#vagy irasd ki a listából csak az egész számokat. Az adatokat futási időben kell megadni.

lista=[]
ujlista=[]

for i in range(5):
    lista.append(input("Adj meg egy értéket:"))

ujlista= [x for x in lista if x.isnumeric()==True]
print(ujlista)
