
from tkinter import*
from tkinter import messagebox

Avg=Tk()
Avg.title("Student Average")
Avg.geometry("400x400")
Avg.minsize(400,400)
Avg.maxsize(400,400)
Avg.configure(background="aqua",borderwidth=10)

name=StringVar()
m=IntVar()
s=IntVar()
c=IntVar()
h=IntVar()

def avge():
    
    total=200

    tot=m.get()+s.get()+h.get()+c.get()
    tot_mrk=tot/200*100
    if tot>total:
        messagebox.showwarning("Error","Please enter proper marks\nEach subject have 50 marks")
    else:
        if tot_mrk>80:
            messagebox.showinfo( "Distintion",tot_mrk)
        elif tot_mrk>60:
            messagebox.showinfo("First class",tot_mrk)
        elif tot_mrk>30:
            messagebox.showinfo("Passed",tot_mrk) 
        else :
            messagebox.showinfo("Failed",tot_mrk)


stu=Label(Avg,text="Enter your Name ",font="Arial 15 bold",foreground="blue",background="aqua").grid(row=1,column=0)
e1=Entry(Avg,textvariable=name).grid(row=1,column=1,ipadx=40,ipady=3)

L1=Label(Avg,text="Enter your marks of following subjects \n mentioned below",font="Arial 15 bold",foreground="red",background="aqua").place(x=5,y=50)
l2=Label(Avg,text="Maths ",background="aqua",foreground="blue",font="Arial 10 bold").place(x=10,y=100)
e2=Entry(Avg,textvariable=m).place(x=80,y=100)
l3=Label(Avg,text="Science ",background="aqua",foreground="blue",font="Arial 10 bold").place(x=10,y=120)
e3=Entry(Avg,textvariable=s).place(x=80,y=120)
l4=Label(Avg,text="Computer",background="aqua",foreground="blue",font="Arial 10 bold").place(x=10,y=140)
e4=Entry(Avg,textvariable=c).place(x=80,y=140)
l5=Label(Avg,text="History ",background="aqua",foreground="blue",font="Arial 10 bold").place(x=10,y=160)
e5=Entry(Avg,textvariable=h).place(x=80,y=160)

B1=Button(Avg,text="Check",activebackground="red",background="blue",foreground="red",command=avge).place(x=100,y=200)


Avg.mainloop()

