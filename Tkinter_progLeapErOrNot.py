from tkinter import*
from tkinter import messagebox

m=Tk()
m.title("Mandar kelkar")
m.geometry("400x400")
m.configure(background="pink")
y1=IntVar()

def Year():
    if y1.get()%4==0 and y1.get()%100!=0:
        
         messagebox.showinfo("This is message box","This is leap year")
    else:
        messagebox.showinfo("This is message box","This is not leap year")

n1=Label(m,text="Enter the year ",activebackground="red",font="Arial 15 bold").grid(row=1,column=0)
e1=Entry(m,font="Arial 15 bold",textvariable=y1).grid(row=1,column=1)

b1=Button(m,text="Click to check Leap year or not",activebackground="blue",command=Year).place(x=100,y=50)
m.mainloop()