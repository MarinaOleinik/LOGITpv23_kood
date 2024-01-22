from math import *
v=input("Kas tahad 1-7 numbrist saada päeva nimetus?")
if v.lower()=="jah":
    try:
        nr=int(input("Päeva number: "))
        if nr==1:
            p="esmaspäev"
        elif nr==2:
            p="teisipäev"
        elif nr==3:
            p="kolmapäev"
        elif nr==4:
            p="neljapäev"
        elif nr==5:
            p="reede"
        elif nr==6:
            p="laupäev"
        elif nr==7:
            p="pühapäev"
        else:
            p="on vaja 1-7"
        print(p)
    except :
        print("viga")
    



a,b,c=map(float,input("a,b,c:").split())
if a>0 and b>0 and c>0:
    if a+b+c==180:
        print("Kolmnurk")
        if a==b==c:
            print("võrdkülgne")
        elif a==b or b==c or a==c:
            print("võrdhaarne")
        else:
            print("erikülgne")
    else:
        print("Nurgad")
else:
    print("<0")


vastus=input("Kas lahendame ruutvõrrand?").lower()
if vastus=="jah":
    print("Ruutvõrrandi lahendamine:")
    try:
        #a,b,c=map(float,input("a,b,c:")).split( ",")
        a=float(input("a: "))
        b=float(input("b: "))
        c=float(input("c: "))
        D=b**2-4*a*c
        if D>0:
            x1=(-b+sqrt(D))/2*a
            x2=(-b-sqrt(D))/2*a
            print("2 lahendust 1:{0:.2f},2:{1:.2f} ".format(x1,x2))
        elif D==0:
            x1=(-b)/2*a
            print("1 lahendus: {0:.2f} ".format(x1))
        else:
            print("Lahendused puuduvad")
    except :
        print("Viga andmetüübiga")
else:
    print("Head aega!")
