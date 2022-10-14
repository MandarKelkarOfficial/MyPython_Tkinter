from cProfile import label

from tkinter import*

'''def select():
    sel ="Value ="+str(v.get())
    label.config(text = sel)
    
top = Tk()
top.geometry("200x100")
top.config(background="pink")
v=DoubleVar()
scale=Scale(top,background="aqua",variable=v,from_=1,to=50,orient=HORIZONTAL).pack(anchor=CENTER)
top.mainloop()'''
top=Tk()
top.title("MK")
top.configure(background="aqua",borderwidth=10)
sb=Scrollbar(top)
sb.pack(side= RIGHT,fill= Y)
mylist=Listbox(top,yscrollcommand=sb.set)
for line in range(30):
    mylist.insert(END,"Number "+str(line))
mylist.pack(side=LEFT)
sb.config(command=mylist.yview)
mainloop()