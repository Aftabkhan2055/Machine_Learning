from tkinter import  *
from pymysql import *
from tkinter.ttk import *

root=Tk()

t=Treeview(root,column=("empid","ename","age","email","departname"))

t.heading("empid",text="Employ id")
t.heading("ename",text=" Employ name")
t.heading("age",text="Employ age")
t.heading("email",text="Employ email")
t.heading("departname",text="Employ department")



conn=connect("127.0.0.1","root",'',"aftab")
query="select * from employ"
cr=conn.cursor()

cr.execute(query)

p=cr.fetchall()

for i in range (0,len(p)):
    t.insert("",values=p[i],index=i)



t.pack()
root.mainloop()



