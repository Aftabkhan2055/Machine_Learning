from tkinter import  *
from pymysql import *
from tkinter.ttk import *

root=Tk()

t=Treeview(root,column=("dname","loc","head"))

t.heading("dname",text="department")
t.heading("loc",text="location")
t.heading("head",text="head name")


conn=connect("127.0.0.1","root",'',"testfile")
query="select * from course"
cr=conn.cursor()

cr.execute(query)

p=cr.fetchall()

for i in range (0,len(p)):
    t.insert("",values=p[i],index=i)



t.pack()
root.mainloop()



