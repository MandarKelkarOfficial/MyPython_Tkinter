# Pack method
from tkinter import*
top=Tk()
top.title("Welcome")
top.geometry("300x200")
redbutton=Button(top,text="Red",fg="red")
redbutton.pack(side=LEFT)
greenbutton=Button(top,text="Green",fg="green")
greenbutton.pack(side=RIGHT)
bluebutton=Button(top,text="Blue",fg="blue")
bluebutton.pack(side=TOP)
blackbutton=Button(top,text="Black",fg="black")
blackbutton.pack(side=BOTTOM)
top.mainloop()