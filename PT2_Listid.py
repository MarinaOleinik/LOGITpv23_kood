from string import *
from random import *
#6
list_=[]
m=randint(1,30)
for i in range(m):
    list_.insert(i,randint(1,1000))
print(list_)
max_=max(list_)
print("maximum:", max_,", Kokku:", m)
arv=max_//m
indeks=list_.index(max_)
list_[indeks]=arv
print(list_)




#4 Index

Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]

while True:
    indeks=input("Indeks: ")
    if len(indeks)==5 and indeks.isdigit():
        break
    else:
        print("Ainult 5 numbriline arv saab kontrollida!")

print(indeks,"kasutatakse",Indeksid[int(indeks[0])-1],"piirkonnas")
if int(indeks[0]) in [1,2,3]:
    pass
else:
    pass




#3
while True:
    sym=input("Mis sümbol kasutame?")
    if sym in punctuation: 
        break
    else:
        print("Saab kasutada ainult: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")
while True:
    try:
        N=int(input("Ridade arv: "))
        break
    except TypeError:
        print("Ainult täisarvud")
for i in range(N):
    #print(randint(1,50)*sym)
    print(sym.ljust(randint(1,50),sym))

#2.3

vanused=[]
N=int(input("Mitu elemendi? "))
for i in range(N):
    vanus=randint(10,97)
    vanused.append(vanus)
print(vanused)
min_=min(vanused)
max_=max(vanused)
sum_=sum(vanused)
avg_=sum_/N
print("Minimum:",min_)
print("Maksimum:",max_)
print("Kogusumma:",sum_)
print("Keskmine:",avg_)

#2.2
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus=[]
for nimi in opilased:
    if nimi not in uus:
        uus.append(nimi)
print(uus)


#2.1
nimed=[]
for i in range(5):
    nimi=input(f"Sisestage {i+1}. nimi: ").capitalize()
    nimed.append(nimi)
#vim_nimi=nimi
print("Oli: ",nimed)
nimed.sort()
print("Sortimise pärast: ",nimed)
print("Viimasena oli lisatud:",nimi)

vananimi=input("Mis nimi on vaja asendada? ").capitalize()
if nimed.count(vananimi)>0:
    uusnimi=input("Mis on uus nimi?").capitalize()
    i=0
    for nimi in nimed:        
        if nimi==vananimi:
            nimed[i]=uusnimi
        i+=1
else:
    print(f"{vananimi} ei ole")
print(nimed)