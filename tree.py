from tkinter import *
from pymysql import *
from tkinter.ttk import *

root=Tk()

t=Treeview(root,column=("id","username","password","email","course"))
t.heading("id",text="student id")
t.heading("username",text="student username")
t.heading("password",text="student password")
t.heading("email",text="student email")
t.heading("course",text="coursename")


conn=connect("127.0.0.1","root",'',"testfile")
query="select * from students "
cr=conn.cursor()
cr.execute(query)

p=cr.fetchall()

for i in range(0,len(p)):
    t.insert("",values= p[i],index=i)
t.pack()
root.mainloop()