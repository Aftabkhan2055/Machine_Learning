from pymysql import *
from tkinter import *
from tkinter.messagebox import *
class demo2:
    def search(self):
        self.conn = connect("127.0.0.1", "root", '', "testfile")
        query="select * from course where coursename='" +self.textbox1.get() + "'"
        cr=self.conn.cursor()
        cr.execute(query)
        p=cr.fetchone()

        self.textbox2.insert(0,p[1])
        self.textbox3.insert(0, p[2])

    def remove(self):
        query2="delete * from course where coursename='" +self.textbox1.get() + "'"
        cr=self.conn.cursor()
        cr.execute(query2)
        self.conn.commit()
        showinfo("", "course Delete Successfully")

    def save(self):
        query3 = "update  course set location ='" + self.textbox2.get() + "',hod ='" + self.textbox3.get() + "'where coursename='"+self.textbox1.get()+"'"
        cr=self.conn.cursor()
        cr.execute(query3)
        self.conn.commit()
        showinfo("", "course upload Successfully")





    def __init__(self):



        self.root=Tk()


        self.lb1=Label(self.root,text="enter the name of department name")
        self.lb1.grid(row=0,column=0)

        self.lb2=Label(self.root,text="enter location")
        self.lb2.grid(row=1,column=0)

        self.lb3=Label(self.root,text="enter the head name of department")
        self.lb3.grid(row=2,column=0)

        self.textbox1=Entry(self.root)
        self.textbox1.grid(row=0,column=1)

        self.textbox2=Entry(self.root)
        self.textbox2.grid(row=1,column=1)

        self.textbox3=Entry(self.root)
        self.textbox3.grid(row=2,column=1)


        self.bt1=Button(self.root,text="find",command=self.search)
        self.bt2=Button(self.root,text="delete",command=self.remove)
        self.bt3=Button(self.root,text="save",command=self.save)

        self.bt1.grid(row=0,column=2)
        self.bt2.grid(row=3,column=1)
        self.bt3.grid(row=3,column=2)


        self.root.mainloop()



#------------------------------------------------------