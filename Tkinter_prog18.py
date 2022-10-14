
from tkinter import*

t=Tk()
t.title("<Mandar>")
t.geometry("300x400")
t.minsize(300,400)
t.configure(background="beige",borderwidth=10)

def open():
    top=Toplevel()
    top.geometry("200x200")
    top.configure(background="pink")
    l2=Label(top,text="Second window").pack()
    top.mainloop()
btn=Button(t,text="open",command=open).place(x=75,y=50)

t.mainloop()