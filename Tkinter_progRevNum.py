
from tkinter import*
from tkinter import messagebox

R=Tk()
R.title("Reverse number")
R.geometry("400x400")
R.configure(bg="#00FFFF")
Revnum=IntVar()
def Rev():
    sum=0
    rev=0
    Revnum1=Revnum.get()
    while Revnum1>0:
        n= Revnum1%10
        rev=(rev*10)+n
        Revnum1=Revnum1//10
    
    messagebox.showinfo("reverse number",rev)

n1=Label(R,text="Enter the number ",activebackground="red",font="Arial 15 bold").grid(row=1,column=0)
e1=Entry(R,font="Arial 15 bold",textvariable=Revnum).grid(row=1,column=1)

b1=Button(R,text="Click to reverse number",activebackground="#B23AEE",command=Rev).place(x=100,y=50)
R.mainloop()