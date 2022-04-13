# listák

lista=['alma', 'körte', 'bicska', 'pálinka', 'kerítésszaggató']
print(lista)
ujlista=[2, 'pitypang', 3.18, 'Freddy', 'Hey Google', True, ]
print(ujlista)
print(lista[2])

# Slice roatation vagy szeletelő jelölés (slicing):
print(lista[:3])        # A másodiktól a 3-ig. A 3. már nincs benne.
print(lista[1:4])       # a másodiktól a 4-ig. A 5. már nincs benne.
print(lista[-1])        # az utolsó elem indexe -1.
print(list[-4])         # Hárultól a 4. elem
print(lista[1:-1])      # A másodiktól az urolsó elemig.
print(lista[-2][:3])    # Az utolsó előtti elem első 3 elemét.
print(ujlista[::2])     # A teljes listából minden második elemet listáz.
szamok=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(szamok[1:-1:3])   # Násodiktól az utolsó előtti elemig, minden harmadik.
print(szamok[-1::-1])   # Háruljától az elejéig, visszafelé
#ugyanez:
print(szamok[::-1])

lista.append('barack')  # Hozzáfűz a lista végére
print(lista[-1])
lista.append('alma')
print(lista)
lista.remove('alma')
print(lista)

lista.sort()            # ABC szerint sorba rendezi. ASCII kódtábla alapján rendez.
print(lista)
#ujlista.sort()         Különböző típusukat nem tud sorba rendezni.

lista.reverse()         # Lista megfordítása
print(lista)

lista.count('a')        # Megszámolja az 'a' betű előfordulását
print(lista)

print(lista[2].count('a')) # Megszámolja az 'a' betű előfordulását a 3. elemben.
print(szamok.count(1))  # Meszámolja az 1-es előfordulásokat.

print(lista.index('bicska')) # Vissza adja a keresett elem index számát.

mondat = """A kocskázatok és mellékhatások tekintetében
            olvassa el a betegtájékoztatót.""" #többsoros sztring írása 
szavak = mondat.split() # Szóközök mentén feldarabolja a sztringet.
print(szavak)
print(" ".join(szavak))

# LISTA BEJÁRÁSA (List comprehension):

ujlista2 = [x for x in lista]
print(ujlista2)

# ujlista = [kifejezés for elem in lista]

ujlista3 = [elem for elem in lista if elem!='alma'] #not-tal is működik
print(ujlista3)

szamok2 = [x for x in range(5,50,3)] # Belerakja a listába a számokat 5-50 között, hármasával.

print(szamok2)
