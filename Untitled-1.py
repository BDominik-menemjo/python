x=input("Adj meg egy 10 karakter hosszú szöveget csupa kis betűkkel:")

x=x.lower()
print(x)

while len(x)>10:
    print("Túl hosszú a szöveged!")
    x=input("Adj meg egy 10 karakter hosszú szöveget csupa kis betűkkel:")

szoveg=[]