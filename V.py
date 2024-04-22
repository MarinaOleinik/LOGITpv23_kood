from tkinter import *
from tkinter import simpledialog as sd

kasutajad=[]
salasõna=[]
def registreerimine():
    s=sal.get()
    k=texbox.get()
    ümber_kirjuta_fail("kasutajad.txt",k)
    ümber_kirjuta_fail("salasõna.txt",s)
def ümber_kirjuta_fail(fail:str,text:str):
    """
    """
    f=open(fail,'a')
    f.write(text+"\n")
    f.close()
def autoriseerimine():
    k=texbox.get()
    s=sal.get()
    kasutajad=loe_failist("kasutajad.txt")
    salasõna=loe_failist("salasõna.txt")
    if k in kasutajad:           
        try:
            if kasutajad.index(k)==salasõna.index(s):
                pealkiri.configure(text=k+", Tere tulemast!")
        except:
            pealkiri.configure(text=k+", Sina ei ole süsteemis!")
    else:
        print("Kasutajad pole")
def loe_failist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,'r',encoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend


def Muutmine(kfail:str,sfail:str,klist_:list,slist_:list):
    """
    """
    s=sal.get()
    k=texbox.get()
    if k != "" and s !="":
        if k in klist_ and s in slist_:
            uusk=sd.askstring("Uus kasutajanimi","Sisesta teie uus kasutajanimi ")
            uuss=sd.askstring("Uus kasutajanimi","Sisesta teie uus parool")
            kindeks=klist_.index(k)
            sindeks=slist_.index(s)
            klist_[kindeks]=uusk
            slist_[sindeks]=uuss
            f=open(kfail,"w",encoding="utf-8")
            for el in klist_:
                f.write(el+"\n")
            f.close()
            f=open(sfail,"w",encoding="utf-8")
            for el in slist_:
                f.write(el+"\n")
            f.close()

def rparoolsk(var):
    f=var.get()
    if f:
        texbox.configure(show="")
        vk.configure(image=pilt1)

    else:
        texbox.configure(show="*")
        vs.configure(image=pilt2)
def salasõna():
    f=var.get()
    if f:
        texbox.configure(show="")
        vk.configure(image=pilt1)

    else:
        texbox.configure(show="*")
        vs.configure(image=pilt2)
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(5,END)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#DCDCDC")
aken.iconbitmap("icon.ico")
pealkiri=Label(aken,
               text="Kasutajanimi",
               bg="#FFFFFF",
               fg="#0000FF",
               cursor="star",
               font="Britannic_Bold 16",
               justify=CENTER,
               height=3,width=26)
raam=Frame(aken)
# r=Frame(reg_1)
texbox=Entry(raam,
             bg="#FFFFFF",
             fg="#7B68EE",
             font="Britannic_Bold 16",
             width=16,
             show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="closed.png")
var=BooleanVar() #IntVar(), StringVar()
vk=Checkbutton(raam,
                   image=pilt1, #text="Punkt1"
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:salasõna())
vs=Checkbutton(raam,
                   image=pilt2, #text="Punkt1"
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:salasõna())
#valik.deselect()
sal=Entry(raam,
             bg="#FFFFFF",
             fg="#7B68EE",
             font="Britannic_Bold 16",
             width=16,
             show="*")
nupp=Button(raam,
            text="Kuva ekraanile",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=salasõna)
reg=Button(raam,
            text="Registreerimine",
            bg="#11FF11",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=registreerimine)
kin=Button(raam,
            text="Kinnitada",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=salasõna)
aut=Button(raam,
            text="Autoriseerimine",
            bg="#44FFFF",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=autoriseerimine)
nmut=Button(raam,
            text="Nimi Muutmine",
            bg="#999999",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=lambda:Muutmine("kasutajad.txt","salasõna.txt",kasutajad,salasõna))
tas=Button(raam,
            text="Taastamine",
            bg="#FF8000",
            fg="white",
            font="Britannic_Bold 16",
            width=16)
pealkiri.grid()
raam.grid()
texbox.grid(row=0, column=0)
kin.grid(row=1,column=2)
vk.grid(row=0, column=1)
vs.grid(row=1, column=1)
sal.grid(row=1,column=0)
nupp.grid(row=0,column=2)
reg.grid(row=3, column=0)
aut.grid(row=3,column=2)
nmut.grid(row=4, column=0)
tas.grid(row=4, column=2)
# lup.grid(row=5, column=0)
aken.mainloop()

