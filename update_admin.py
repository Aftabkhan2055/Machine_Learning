from pymysql import *
from tkinter import *
from tkinter.ttk import*
from tkinter.messagebox import *
from connection import *
class update:
    def search(self):
        query ="select * from admin where email='"+self.textbox1.get()+"'"
        db = connection()
        cr = db.conn.cursor()
        cr.execute(query)

        p = cr.fetchone()

        self.textbox2.insert(0, p[1])
        self.textbox3.insert(0, p[2])
        self.cb1.set( p[3])

    def remove(self):
        query2="delete  from admin where email='"+self.textbox1.get()+"'"
        db = connection()
        cr = db.conn.cursor()
        cr.execute(query2)
        db.conn.commit()
        showinfo("","Admin Delete Successfully")

    def save(self):
        query3 = "update admin set password ='"+self.textbox2.get() +"',mobile='"+self.textbox3.get()+"',type='"+self.cb1.get()+"' where email='"+self.textbox1.get()+"'"
        db = connection()
        cr = db.conn.cursor()
        cr.execute(query3)

        showinfo("","Admin update Successfully")


    def __init__(self):

        self.root=Tk()
        self.root.title("Update Admin Window")
        self.root.config(bg='light gray')
        self.root.geometry("350x230")
        self.lb_heading = Label(self.root, text='UPDATE ADMIN')
        labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='brown', background='light gray', font=labelfont)
        self.lb_heading.grid(row=0, column=1, columnspan=3)

        self.lb1=Label(self.root,text="Enter Email",background='light gray',foreground='brown')
        self.lb1.grid(row=1,column=0,sticky=(W))

        self.lb2=Label(self.root,text="Enter Password",background='light gray',foreground='brown')
        self.lb2.grid(row=2,column=0,sticky=(W))

        self.lb3=Label(self.root,text="Enter Mobile",background='light gray',foreground='brown')
        self.lb3.grid(row=3,column=0,sticky=(W))

        self.lb4=Label(self.root,text="Type",background='light gray',foreground='brown')
        self.lb4.grid(row=4,column=0,sticky=(W))

        self.textbox1=Entry(self.root)
        self.textbox1.grid(row=1,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.textbox2=Entry(self.root)
        self.textbox2.grid(row=2,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.textbox3=Entry(self.root)
        self.textbox3.grid(row=3,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.cb1=Combobox(self.root,state="readonly",values=("Admin","limited"))
        self.cb1.grid(row=4,column=1,padx=5,pady=5,sticky=(N,E,W))

        self.bt1=Button(self.root,text="find",command=self.search,)
        self.bt2=Button(self.root,text="delete",command=self.remove)
        self.bt3=Button(self.root,text="save",command=self.save)

        self.bt1.grid(row=1,column=3)
        self.bt2.grid(row=2,column=3)
        self.bt3.grid(row=3,column=3)


        self.root.mainloop()



#-------------------------------------------------------
#x=update()