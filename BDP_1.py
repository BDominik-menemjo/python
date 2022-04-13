"""
Írj programot, amely bekér a bementről két számot. Hozz létre egy listát, amelyet feltöltesz számokkal. 
Az első beolvasott szám mondja meg, hogy hány eleme legyen a listának 1-n-ig, a második szám pedig a 
hatvány kitevő lesz. 
Pl.: 
Első szám: n=5; 
Második szám: m=4, 
akkor az eredmény ezt adja: [1**4, 2**4, 3**4, 4**4, 5**4]
"""

a=[]

n=int(input("Adj meg egy számot! Ez megszabja hány számnak szeretnéd a hatványát: "))
m=int(input("Ezzel pedig megadod hányadik hatványig szeretnéd:"))

a=[i**m for i in range(1, n+1)]

print(a)
