'''
1   Kérj be a standard bemenetről egy jelszót. 
    Az elfogadható jelszó: alma, körte, szilva. 
    Ha helytelen jelszót gépel be a felhasználó, akkor figyelmeztesse a program egy hibaüzenettel. 
    Amennyiben helyes jelszót gépelt be, akkor üdvözölje gratulációval.
'''

x=str(input("Add meg a jelszót!"))
pw=['alma', 'körte', 'szilva']
while x not in pw:
    x=str(input("Helytelen jelszó, próbáld újra!"))

print("Üdv a rendszerben")