try:
    hind=float(input("Hind:"))
    if hind>=700:
        hind*=0.7
    print(hind)
except :
    print("Viga")





try:
    pikkus=float(input("Pikkus:"))
    try:
        laius=float(input("Laius:"))
        S=pikkus*laius
        print("Pindala võrdub",S)
        soov=input("Kas tahad remondi teha?").lower() #jah, Jah ,JAH ->jah upper()->JAH
        if soov=="jah" or soov=="да":
            try:
                hind=float(input("Ruutmeetri hind: "))
                summa=hind*S
                print("Remondi summa on ", summa)
            except :
                print("Viga")            
        else:
            print("Head aega")
    except :
        print("Viga")
except:
    print("Viga")






eesnimi1=input("Mis on 1. nimi?").capitalize()    # "Eldar" "Artur"
eesnimi2=input("Mis on 2. nimi?").capitalize()
if (eesnimi1=="Eldar" and eesnimi2=="Artur") or (eesnimi1=="Artur" and eesnimi2=="Eldar"):
    print("Need on pinginaabrid")
else:
    print("Rühmakaaslased")

if (eesnimi1!=eesnimi2) and (eesnimi1 and eesnimi2 in ["Eldar", "Artur"] or eesnimi1 and eesnimi2 in ["Anna", "Inna"]):
    print("Need on pinginaabrid")
else:
    print("Rühmakaaslased")





eesnimi=input("Mis on sinu nimi?").capitalize() #"Juku"
if eesnimi=="Juku":
    try:
        vanus=int(input("Kui vana sa oled?"))
        print("Jukule ostame ", end="")
        if 0<vanus<6:
            print("tasuta pilet")
        elif 6<=vanus<14:
            print("lastepilet")
        elif 14<=vanus<65:
            print("täispilet")
        elif 65<=vanus<=100:
            print("sooduspilet")
        else:
            print("mitte midagi. Viga andmetega!")
    except :
        print("Int andmetüüp on vaja kasutada!")
        
else:
    print("Mine ise kinno!")



