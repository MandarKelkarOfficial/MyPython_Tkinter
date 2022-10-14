#Grid method

from cProfile import label
from tkinter import*

T=Tk()
T.title("Welcome")
T.geometry("400x300")
T.minsize(400,400)#To set the minimum size of window
T.maxsize(400,400)#To set the maximum size of window

#name button
name=Label(T,text="Name").grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10)
e1=Entry(T).grid(row=0 ,column=1)

#Email button
email=Label(T,text="Email").grid(row=1,column=0,padx=5,pady=5,ipadx=10,ipady=10)
e3=Entry(T).grid(row=1,column=1)

#Password button
password=Label(T,text="Password").grid(row=2,column=0,padx=5,pady=5,ipadx=10,ipady=10)
e2=Entry(T).grid(row=2,column=1)

#submit button
submit=Button(T,text="Submit").grid(row=4,column=0)
T.mainloop()