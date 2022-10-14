from tkinter import Toplevel,Button,Tk,Menu, messagebox

top=Tk()

menubar=Menu(top)
file = Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")
file.add_separator()

def show():
    messagebox.showinfo("mk","Mandar kelkar")

menubar.add_cascade(label="File",menu=file)
edit=Menu(menubar,tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select all")

menubar.add_cascade(label="Edit",menu=edit)
help=Menu(menubar,tearoff=0)
help.add_command(label="About",command=show)
menubar.add_cascade(label="Help",menu=help)

top.config(menu=menubar)
top.mainloop()