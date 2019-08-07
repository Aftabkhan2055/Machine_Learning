from pymysql import *
from tkinter.ttk import *
from tkinter import *
class demo5:

    def __init__(self):
        self.root = Tk()



        self.t = Treeview(self.root,columns=( "empid""ename", "age","email","department"))
        self.t.heading("empid", text="Employee Id")
        self.t.heading("ename", text="Employee Name")
        self.t.heading("age", text="Employee Age")
        self.t.heading("email", text="Employee Email")
        self.t.heading("department", text="Employee Department")

        conn = Connect("127.0.0.1", "root", '', "testfile")

        query = "select * from employ"

        cr = conn.cursor()

        cr.execute(query)

        p = cr.fetchall()

        for i in range(0, len(p)):
            self.t.insert("", values=p[i], index=i)
        self.t.pack()

        self.root.mainloop()

#-------------------------------------------------------------------------------

