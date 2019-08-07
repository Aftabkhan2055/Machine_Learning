from tkinter import *
from add_admin import*
from update_admin import *
from view_admin import *
from connection import *

def test1():
    obj=admin()
def test2():
    obj=update()
def test3():
    obj2=view()


x=Tk()

x.geometry("1024x768")
mymenu=Menu(x)
x.config(menu=mymenu)

option1=Menu(mymenu)
mymenu.add_cascade(label="admin  Management",menu=option1)

option1.add_command(label="Add admin",command=test1)
option1.add_command(label="Update/Delete admin",command=test2)
option1.add_command(label="View admin",command=test3)



x.mainloop()


