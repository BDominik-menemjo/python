'''
    Írass ki minden harmadik számot [1-50] intervallumban for ciklus segítségével. A számokat egymás mellé, vesszővel elválasztva kell kiíratni. Az utolsó szám után már ne kerüljön vessző! Ezután írasd ki ugyanezeket a számokat csökkenő sorrendben is!
'''

for i in range(1,50,3):
    if i!=49:
        print(i, end=",")
    else:
        print(i)

for i in range(1,50,-3):
    if i!=1:
        print(i, end=",")
    else:
        print(i)