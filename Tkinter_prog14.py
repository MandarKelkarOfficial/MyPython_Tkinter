from cProfile import label
from cgitb import text
from tkinter import*
def selection():
    selection="You selected the option "+str(radio.get())
    label.config(text= selection)
top=Tk()
top.geometry("300x150")
radio=IntVar()
lbl=Label(top,text="Favourite programming language :").pack()
r1=Radiobutton(top,text="C",variable=radio,value=1,command=selection).pack(anchor=W)
r2=Radiobutton(top,text="Java",variable=radio,value=2,command=selection).pack(anchor=W)
r3=Radiobutton(top,text="C++",variable=radio,value=3,command=selection).pack(anchor=W)
label=Label(top)
label.pack()
top.mainloop()