from tkinter import*
from tkinter import messagebox

m=Tk()
m.title("Mandar kelkar")
m.geometry("400x400")
m.configure(background="yellow")
t1=IntVar()

def PosNeg():
    if t1.get()>=0:
         messagebox.showinfo("This is message box","is positive")
    else:
         messagebox.showinfo("This is message box","is negative")

n1=Label(m,text="Enter the number ",activebackground="red",font="Arial 15 bold").grid(row=1,column=0)
e1=Entry(m,font="Arial 15 bold",textvariable=t1).grid(row=1,column=1)

b1=Button(m,text="Click to check positive or negative",activebackground="blue",command=PosNeg).place(x=100,y=50)
m.mainloop()