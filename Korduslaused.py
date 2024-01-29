from datetime import *
from random import *
#15 

#14 Korrutustabel
for j in range(1,11):
    for i in range(1,11):
        print(f"{j*i:4}",end=" ")
    print()

#12 Pank

algsumma=float(input("Mis summa paneme panka?"))
alg=lõppsumma=algsumma
intress=randint(1,10)
print(f"Paned panka summa, mis võrdub {algsumma}. Intress on {intress}")
aastad=int(input("Mitmeks aastaks?"))
print("Aasta Algsumma Intress Aasta_lõpuks")
for i in range(1,aastad+1):
    intsumma=(algsumma*intress)/100
    lõppsumma=algsumma+intsumma
    print(f"{i} {algsumma} {intsumma} {lõppsumma}")
    algsumma=lõppsumma
print(f"Summa kokku: {lõppsumma} Eur")
print(f"Kasum: {lõppsumma-alg} Eur")


print()
k=0
while True:
    k+=1
    a=randint(1,50)
    b=randint(1,50)
    p=0
    while p!=3:
        p+=1
        v=int(input("Millega võrdub {0}+{1}= ".format(a,b)))
        if v==a+b:
            print("Tubli!")
            break
        else:
            print("Mõtle veel!")
    print("{0}+{1}={2}".format(a,b,a+b))
    
    if k==5:break





#2 summa 10 arvud
summa=0
for i in range(10):
    arv=float(input("Sisesta arv: "))
    summa+=arv
print(summa)

summa=0
i=0
while True:
    i+=1
    arv=float(input("Sisesta arv: "))
    summa+=arv
    if i==10: break
print(summa)



#1 Siim
nimi=input("Mis on sinu nimi?")
mitu=int(input("Mitu korda tervitada?"))
for i in range(1,mitu+1):
    print("Ole tervitatud, "+nimi+", "+str(i)+". korda.")


#Komm
print("1. variant -while True-")
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. variant -while tingimusega-")
v=""
while v!="komm":
    v=input("Tahan komme!").lower()

#Nädala päevad
paevad=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede","Laupäev","Pühapäev"]
tunnid=["8 tundi","9 tundi","5 tundi","8 tundi","6 tundi","tunde pole","tunde pole"]
for i in range(7):
    print(paevad[i]+"-"+tunnid[i])

#8 Poes korduslausega
arve_nr=datetime.now() # date.today()
print(arve_nr)
tsekk="Arve: "+str(arve_nr)+"\nToode  Hind  Kogus  Summa\n"
summa=0
tooded=["Piim","Leib","Komm"] #index 0-1-2
for i in range(3): #i=0,i=1,i=2
    toode=tooded[i]
    hind=randint(50,150)/100
    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
        mitu=int(input("Mitu?"))
        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
        summa+=mitu*hind

tsekk+="Kokku maksta: "+str(summa)
print(tsekk)
