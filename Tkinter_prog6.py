#Button widget
'''import tkinter as tk
from tkinter import messagebox
r=tk.Tk()
r.geometry("300x200")
r.title('Counting Seconds')
def sayhello():
    print("Welcome to Tkinter")
    messagebox.showinfo("Welcome","My first tkinter program")
button=tk.Button(r,text='Stop',width=35,command=sayhello,activebackground="blue",bg="red",fg="aqua",activeforeground="yellow").pack()
r.mainloop()

#Canvas widget
from tkinter import*

top=Tk()
top.geometry("200x200")
  #creating a canvas
c=Canvas(top,bg="pink",height="200",width="200")
arc=c.create_arc((5,10,150,200),start=0,extent=150,fill="white")
c.pack()
top.mainloop()

#checkbutton widget
from tkinter import*
m=Tk()
m.geometry("400x200")
var1=IntVar()
Checkbutton(m,text="Male",variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(m,text="Female",variable=var2).grid(row=1,sticky=W)
m.mainloop()

#Entry widget
from tkinter import*
root=Tk()
root.geometry("500x500")
e1=Entry(root,bg="pink",font="Arial 35 bold",bd=5,relief=GROOVE).pack()
root.mainloop()'''


