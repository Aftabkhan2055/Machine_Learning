from tkinter.ttk import *
from tkinter import *
from pymysql import *
class demo3:
    def __init__(self):

        self.root = Tk()

        self.t = Treeview(self.root, columns=("dname", "loc", "head"))
        self.t.heading("dname", text="Department Name")
        self.t.heading("loc", text="Location")
        self.t.heading("head", text="Head Name")

        conn = Connect("127.0.0.1", "root", '', "testfile")

        query = "select * from course"

        cr = conn.cursor()

        cr.execute(query)

        p = cr.fetchall()

        for i in range(0, len(p)):
            self.t.insert("", values=p[i], index=i)
        self.t.pack()

        self.root.mainloop()
#---------------------------------------------------------------------------------

