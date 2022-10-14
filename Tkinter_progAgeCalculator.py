from tkinter import*
from turtle import title

a=Tk()
a.geometry("250x300")
a.minsize(250,300)
a.title("Age calculator...by MK")
a.configure(bg="beige",borderwidth=10)

l=Spinbox(a,from_=1,to=31).place(x=40,y=40)
m=Listbox(a)
a.mainloop()