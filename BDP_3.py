'''
Olvass be a billentyűzetről egy max 20 karakter hosszú szöveget, amely csak az angol ABC betűit 
tartalmazhatja, majd számold meg, hogy az egyes betűkből hány darab érkezett. 
Ha valamely betű nem jelenik meg a szövegben, akkor azt ne írd ki, csak azokat amelyek megjelennek. 
Végezd el a szükséges input ellenőrzést is!
'''

import abc

asd=[]
x=input("Adj meg egy max. 20 karakter hosszú szöveget, csak az angol abc betűit használhatod!")

while len(x)>20:
    print("Túl hosszú a szöveged!")
    x=input("Adj meg egy max. 20 karakter hosszú szöveget, csak az angol abc betűit használhatod!")

print(x)
for i in x:
    asd.append(i)
for i in asd:
    i.lower()

for i in x:
    if 'a' in x:
        a=x.count("a")
        print("Ennyi van 'A'-ból", a)
    elif 'b' in x:
        b=x.count("b")
        print("Ennyi van 'b'-ból", b)
    elif 'c' in x:
        c=x.count("c")
        print("Ennyi van 'c'-ból", c)
    elif 'd' in x:
        d=x.count("d")
        print("Ennyi van 'd'-ból", d)
    elif 'e' in x:
        e=x.count("e")
        print("Ennyi van 'e'-ból", e)
    elif 'f' in x:
        f=x.count("f")
        print("Ennyi van 'f'-ból", f)
    elif 'g' in x:
        g=x.count("g")
        print("Ennyi van 'g'-ból", g)
    elif 'h' in x:
        h=x.count("h")
        print("Ennyi van 'h'-ból", h)
    elif 'i' in x:
        i=x.count("i")
        print("Ennyi van 'i'-ból", i)
    elif 'j' in x:
        j=x.count("j")
        print("Ennyi van 'j'-ból", j)
    elif 'k' in x:
        k=x.count("k")
        print("Ennyi van 'k'-ból", k)
    elif 'l' in x:
        l=x.count("l")
        print("Ennyi van 'l'-ból", l)
    elif 'm' in x:
        m=x.count("m")
        print("Ennyi van 'm'-ból", m)
    elif 'n' in x:
        n=x.count("n")
        print("Ennyi van 'n'-ból", n)
    elif 'o' in x:
        o=x.count("o")
        print("Ennyi van 'o'-ból", o)
    elif 'p' in x:
        p=x.count("p")
        print("Ennyi van 'p'-ból", p)
    elif 'q' in x:
        q=x.count("q")
        print("Ennyi van 'q'-ból", q)
    elif 'r' in x:
        r=x.count("r")
        print("Ennyi van 'r'-ból", r)
    elif 's' in x:
        s=x.count("s")
        print("Ennyi van 's'-ból", s)
    elif 't' in x:
        t=x.count("t")
        print("Ennyi van 't'-ból", t)
    elif 'u' in x:
        u=x.count("u")
        print("Ennyi van 'u'-ból", u)
    elif 'v' in x:
        v=x.count("v")
        print("Ennyi van 'v'-ból", v)
    elif 'w' in x:
        w=x.count("w")
        print("Ennyi van 'w'-ból", w)
    elif 'x' in x:
        x=x.count("x")
        print("Ennyi van 'x'-ból", x)
    elif 'y' in x:
        y=x.count("y")
        print("Ennyi van 'y'-ból", y)
    elif 'z' in x:
        z=x.count("z")
        print("Ennyi van 'z'-ból", z)
