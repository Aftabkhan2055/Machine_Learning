from tkinter import *
from tkinter.ttk import *
from pymysql import *
from tkinter.messagebox import *

class demo4:

    def insert(self):


        query="insert into employ values(NULL,'"+self.textbox1.get()+"',"+self.textbox2.get()+",'"+self.textbox3.get()+"','"+self.cb1.get()+"')"

        self.conn = Connect("127.0.0.1", "root", '', "testfile")

        cr=self.conn.cursor()

        cr.execute(query)
        self.conn.commit()
        showinfo("","Employee Added Sucessfully")



    def __init__(self):
        self.root=Tk()

        self.lb1=Label(self.root,text="Employee Name").grid(row=0,column=0)
        self.lb2=Label(self.root,text="Employee Age").grid(row=1,column=0)
        self.lb3=Label(self.root,text="Employee Email").grid(row=2,column=0)
        self.lb4=Label(self.root,text="Employee Department Name").grid(row=3,column=0)

        self.textbox1=Entry(self.root)
        self.textbox1.grid(row=0,column=1)
        self.textbox2=Entry(self.root)
        self.textbox2.grid(row=1,column=1)
        self.textbox3=Entry(self.root)
        self.textbox3.grid(row=2,column=1)

        self.conn=Connect("127.0.0.1","root",'',"testfile")

        query="select depatname from employ"

        cr=self.conn.cursor()
        cr.execute(query)

        p=cr.fetchall()



        self.cb1=Combobox(self.root,values=p)
        self.cb1.grid(row=3,column=1)



        self.bt1=Button(self.root,text="Add New Employee",command=self.insert).grid(row=4,column=1)
        self.root.mainloop()

#------------------------
