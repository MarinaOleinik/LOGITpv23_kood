from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd

def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
        valik.configure(image=pilt2)
    else:
        texbox.configure(show="*")
        valik.configure(image=pilt1)
def textpealkirjasse():
    vastus=mb.askquestion("Küsimus","Kas tõesti tahad info kopeerida?")
    if vastus=='yes':
        mb.showwarning("Tähelepanu","Kohe teiseldatakse info!")
        t=texbox.get()
        pealkiri.configure(text=t)
        texbox.delete(0,END)
    else:
        mb.showinfo("Valik oli tehtud","Info jääb omal kohal")
        nimi=sd.askstring("Saame tuttavaks!","Mis on sinu nimi?") #askinteger(),askfloat()
        pealkiri.configure(text=nimi)
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#13e0eb")
aken.iconbitmap("icon.ico")
pealkiri=Label(aken,
               text="Põhielemendid",
               bg="#9edb8f",
               fg="#18420d",
               cursor="star",
               font="Britannic_Bold 16",
               justify=CENTER,
               height=3,width=26)
raam=Frame(aken)
texbox=Entry(raam,
             bg="#18420d",
             fg="#9edb8f",
             font="Britannic_Bold 16",
             width=16,
             show="*")
pilt1=PhotoImage(file="eye.png")
pilt2=PhotoImage(file="closed.png")
var=BooleanVar() #IntVar(), StringVar()
valik=Checkbutton(raam,
                  image=pilt1, #text="Punkt1"
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda:tehtudvalik(var))
#valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#9edb8f",
            fg="#18420d",
            font="Britannic_Bold 16",
            width=16,
            command=textpealkirjasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0) #raami sees
valik.grid(row=0,column=1) #raami sees
nupp.grid(row=0,column=2) #raami sees
aken.mainloop()
