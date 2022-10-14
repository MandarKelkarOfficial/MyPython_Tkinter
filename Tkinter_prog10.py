from tkinter import*
from tkinter import messagebox

m=Tk()
m.title("Mandar kelkar")
m.geometry("400x400")
m.configure(background="aqua")

t1=IntVar()
t2=IntVar()

def GreLesTan():
    if t1.get()>t2.get():
        messagebox.showinfo("First num is great",t1.get())

    else:
        messagebox.showinfo("Second num is great",t2.get())


n1=Label(m,text="Enter first number ").grid(row=1,column=0)
e1=Entry(m,textvariable=t1).grid(row=1,column=1)

n2=Label(m,text="Enter second number ").grid(row=2,column=0)
e2=Entry(m,textvariable=t2).grid(row=2,column=1)

k=Button(m,text="Check",activeforeground="orange",command=GreLesTan).grid(row=4,column=1)
m.mainloop()