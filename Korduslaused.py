from datetime import *
from random import *
#Komm
print("1. variandt -while True-")
while True:
    v=input("Tahan komme!").lower()
    if v=="komm": break

print("2. variandt -while tingimusega-")
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
