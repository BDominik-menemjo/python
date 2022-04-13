eredmeny=[[],[],[],[]]

for i in range(3):
    eredmeny[0].append(input("Név:"))
    eredmeny[1].append(input("Születési Hely:"))
    eredmeny[2].append(input("Anja neve:"))
    eredmeny[3].append(input("Születési év:"))

for i in range(len(eredmeny[3]),1,-1):
    for j in range (i-1):
        if eredmeny[3][j]>eredmeny[3][j+1]:
            temp=eredmeny[3][j+1]
            eredmeny[3][j+1]=eredmeny[3][j]
            eredmeny[3][j]=temp

            temp=eredmeny[0][j+1]
            eredmeny[0][j+1]=eredmeny[0][j]
            eredmeny[0][j]=temp

            temp=eredmeny[1][j+1]
            eredmeny[1][j+1]=eredmeny[1][j]
            eredmeny[1][j]=temp

            temp=eredmeny[2][j+1]
            eredmeny[2][j+1]=eredmeny[2][j]
            eredmeny[2][j]=temp

print(eredmeny)