import random
tomb=[]
cig=[]
for i in range(99):
    tomb.append(random.randint(0,1000))
print(tomb)

fele=int(len(tomb)/2)
print(fele)
for i in range(fele-1):
    for j in range(i+1,fele):
        if tomb[i]>tomb[j]:
            temp=tomb[j]
            tomb[j]=tomb[i]
            tomb[i]=temp

for i in range(fele+1, len(tomb)-1):
    for j in range(i+1,len(tomb)):
        if tomb[i]<tomb[j]:
            temp=tomb[j]
            tomb[j]=tomb[i]
            tomb[i]=temp
tomb[fele]=0
print(tomb)