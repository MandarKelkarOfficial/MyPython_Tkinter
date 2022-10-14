
from tkinter import*
from tkinter import messagebox

t=Tk()
t.title("Mandar kelkar")
t.geometry("300x400")
t.minsize(300,400)
t.configure(background="bisque1",borderwidth=10)

k=IntVar()

def fib():
    i=0
    n=0
    n1=1
    while i < k.get():
        n2=n+n1
        n=n1
        n1=n2
        i+=1
    messagebox.showinfo("fib series",n2)
    
def fact():
    k.get()
    fact=1
    if k.get()<0:
        messagebox.showwarning("FAct","Factorial cant \nbe negative")
    elif k.get()==0:
        messagebox.showinfo("FAct","The factorial of 0 is always 0")
    else: 
        for i in range(1,k.get()+1):
            fact*i
    messagebox.showinfo("FAct",fact)
    
l1=Label(t,text="Enter the value ",background="beige",font="Arial 15 bold").place(x=70,y=10)
e1=Entry(t,textvariable=k).place(x=85,y=50)

rdb=Radiobutton(t,text="Fibbonasus series",value=1,variable=k,command=fib).place(x=80,y=80)
rbd1=Radiobutton(t,text="Factorial",variable=k,command=fact).place(x=80,y=100)

t.mainloop()