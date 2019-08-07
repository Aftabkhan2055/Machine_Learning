from tkinter import *
from tkinter.messagebox import *
    def demo():
        f=int(textbox1.get())
        t=(f-32)/1.8
        showinfo("",t)
obj=Tk()
obj.title("aftab")
textbox1=Entry(obj)
textbox1.pack()
bt1=Button(obj,text="click",command=demo)
bt1.pack()
obj.mainloop()