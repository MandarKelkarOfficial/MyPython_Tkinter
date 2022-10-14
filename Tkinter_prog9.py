import tkinter as tk
win=tk.Tk()
win.configure(background="pink")
win.title("ListBoxProg")
win.geometry("500x500")

def additem():
      listbox.insert(tk.END,content.get())
def deletitem():
      listbox.delete(0,tk.END)
def delselitem():
      listbox.delete(tk.ANCHOR)
    
content=tk.StringVar()
e1=tk.Entry(win,textvariable=content).pack()

b1=tk.Button(win,text="Add item",command=additem).pack()
b2=tk.Button(win,text="Delet item",command=deletitem).pack()
b3=tk.Button(win,text="Deletselect item",command=delselitem).pack()
listbox = tk.Listbox(win)
listbox.pack()
win.mainloop()