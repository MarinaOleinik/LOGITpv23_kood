from tkinter import *
import matplotlib.pyplot as plt #Y funktsiooni loomiseks
import numpy as np #X vahemik X[nim,max]
def Vaal():
    """Joonestatakse vaal paraabolite abil matplotlib mooduli kasutades
    """
    x1=np.arange(0,9,0.5)
    y1=(2/27)*x1**2-3
    x2=np.arange(-10,0,0.5)
    y2=0.04*x2**2-3
    #...
    x9 = np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    plt.figure()
    #plt.plot(x1,y1,"r:*",x2,y2,"m-s") #1.Variant
    for i in range(1,3):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),"b--x") #2.Variant
    plt.title("Vaal")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    plt.show()

def valik(event):
    n=loetelu.get(loetelu.curselection())
    
    print(n)
    if n=="Vaal":
        Vaal()
    
aken=Tk()
aken.geometry("400x500")
aken.title("Akna pealkiri")
aken.configure(bg="#13e0eb")
l=["Vaal","Vihmavari","Liblikas","Prillid","Kilpkonn"]
loetelu=Listbox(aken,font="Arial 30",fg="green",bg="gold",selectborderwidth=3)
for i in range(len(l)):
    loetelu.insert(i,l[i])

loetelu.grid()
loetelu.bind("<Double-1>",valik)

aken.mainloop()
