from tkinter import *
from tkinter.messagebox import *
def find():
    a=int(textbox1.get())
    b=int(textbox2.get())
    c=int(textbox3.get())
    if a>b and a>c:
        showinfo("","largest no is"+str(a))
    elif b>a and b>c:
        showinfo("","largest n o is"+str(b))
    else:
        c>a and c>b
        showinfo("","largest no is"+str(c))
root=Tk()

root.geometry("400x300")
root.title("aftab")
textbox1=Entry(root)
textbox2=Entry(root)
textbox3=Entry(root)

lb1=Label(root,text="enter the first no")
lb2=Label(root,text="enter the second no")
lb3=Label(root,text="enter the third no")

bt1=Button(root,text="find largest no",command=find)
lb1.grid(row=0,column=0)
lb2.grid(row=1, column=0)
lb3.grid(row=2, column=0)

textbox1.grid(row=0,column=1)
textbox2.grid(row=1,column=1)
textbox3.grid(row=2,column=1)

bt1.grid(row=3,column=1)
root.mainloop()