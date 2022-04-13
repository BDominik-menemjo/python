'''
   Tölts fel egy 100 elemű tömböt random egész számokkal [10-50] intervallumból. 
    Írass ki a képernyőre egy fele akkora tömböt, amelynek az elemeit úgy kapod meg, 
    hogy összeadod az eredeti tömb egymás melletti elemeit. 
    Tehát pl: 
    uj_tomb[0]=eredeti_tomb[0]+eredeti_tomb[1]; uj_tomb[1]=eredeti_tomb[2]+eredeti_tomb[3]; 
    uj_tomb[2]=eredeti_tomb[4]+eredeti_tomb[5]...
'''

import random
tomb=[]
uj=[]

for i in range(100):
    tomb.append(random.randint(10,50))
print(tomb)

