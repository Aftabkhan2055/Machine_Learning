from tkinter import *
from update_deptt import *
from view_dept import *
from add_dept import*

def test7():
    obj3=demo7()
def test():
    obj=demo()
def test2():
    obj2=demo3()


x=Tk()

x.geometry("800x800")

bt1=Button(x,text="Add New dept",command=test7)
bt3=Button(x,text="Update/Delete Department",command=test)
bt2=Button(x,text="View All Department",command=test2)

bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)
bt3.grid(row=0,column=2)
x.mainloop()


