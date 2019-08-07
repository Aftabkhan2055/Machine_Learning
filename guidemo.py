from tkinter import *
from tkinter.messagebox import *

def test():
    p=int(textbox1.get())
    n = int(textbox2.get())
    s=p+n
    showinfo("",(s))


root=Tk()
root.title("aftab")
root.geometry("400x300")
textbox1=Entry(root)
textbox1.pack()
textbox2=Entry(root)
textbox2.pack()

bt1=Button(root,text="click",command=test)
bt1.pack()

root.mainloop()
