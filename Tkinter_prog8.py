#************Frame widget***************
'''from tkinter import*

top=Tk()
top.geometry("300x300")
top.configure(background="pink")
frame=Frame(top)
frame.pack()
leftframe=Frame(top)
leftframe.pack(side= LEFT)
rightframe=Frame(top)
rightframe.pack(side=RIGHT)
b1=Button(frame,text="Submit",fg="red",activebackground="red").pack(side=LEFT)
b2=Button(frame,text="Remove",fg="brown",activebackground="brown").pack(side=RIGHT)
b3=Button(frame,text="Add",fg="blue",activebackground="blue").pack(side=LEFT)
b4=Button(frame,text="Modify",fg="black",activebackground="white").pack(side=RIGHT)
top.mainloop()

#ListBox widget
from tkinter import*
top=Tk()
top.geometry("300x400")
lb=Listbox(top)
lb.insert(1,'Python')
lb.insert(2,'Java')
lb.insert(3,'C')
lb.insert(4,'Any other')
lb.pack()
#lb.delete()
top.mainloop()'''


import tkinter as tk

win = tk.Tk()


def additem():
    listbox.insert(tk.END, content.get())


def deleteAll():
    listbox.delete(0, tk.END)


def deleteselected():
    listbox.delete(tk.ANCHOR)


content = tk.StringVar()
entry = tk.Entry(win, textvariable=content)
entry.pack()

button = tk.Button(win, text="Add Item", command=additem)
button.pack()

button2 = tk.Button(win, text="Delete list", command=deleteAll)
button2.pack()

button3 = tk.Button(win, text="Delete selected", command=deleteselected)
button3.pack()

listbox = tk.Listbox(win)
listbox.pack()

win.mainloop()

