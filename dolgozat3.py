'''
   Olvass be pontosan 10 darab egész számot a standard bemenetről. 
    Írasd ki a képernyőre a megfelelő kísérőszöveggel a számok számtani átlagát, a megfelelő formában. 
    Ezen felül keresd meg és írasd ki melyik volt a számok közül a legkisebb. 
    A feladathoz nem használhatsz tömböt, kész függvényeket vagy metódusokat.
'''
eredmeny=0
j=0

for i in range(10):
    x=int(input("Adj meg egy számot!"))
    j+=1
    eredmeny+=x
print("A számok összege: %d" %eredmeny)
print("A számok számtani átlaga %.2f" %(eredmeny/j))