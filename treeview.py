from tkinter import  *
from pymysql import *
from tkinter.ttk import *


root=Tk()
t=Treeview(root,columns=("rollno","name","age","course"))

t.heading("rollno",text="roll number")
t.heading("name",text="student name")
t.heading("age",text="student age")
t.heading("course",text="student course")

t.insert ("",values=(1,"aftab",20,"btech"),index=0)
t.insert ("",values=(2,"rahul",22,"mca"),index=1)
t.insert ("",values=(3,"samim",21,"bca"),index=2)
t.insert ("",values=(4,"sufyan",23,"mtech"),index=3)
t.insert ("",values=(5,"nasim",19,"hm"),index=4)
t.insert ("",values=(6,"perwez",24,"diploma"),index=5)

t.pack()

root.mainloop()










































