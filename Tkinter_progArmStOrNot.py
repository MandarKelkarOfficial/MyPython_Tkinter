from tkinter import*
from tkinter import messagebox

m=Tk()
m.title("Mandar kelkar")
m.geometry("400x400")
m.configure(background="pink")
num=IntVar()
temp=num
na1=num
def Armst():
    temp=num.get()
    sum=0
    while temp>0:
        n=temp%10
        sum+=n*n*n
        temp//=10
    if na1==sum:
        messagebox.showinfo("Mk","Number is Armstrong")
    else:
        messagebox.showinfo("mk","Number is not Armstrong")

n1=Label(m,text="Enter the number ",activebackground="red",font="Arial 15 bold").grid(row=1,column=0)
e1=Entry(m,font="Arial 15 bold",textvariable=num).grid(row=1,column=1)

b1=Button(m,text="Click to check armstrong or not",activebackground="orange",command=Armst).place(x=100,y=50)
m.mainloop()