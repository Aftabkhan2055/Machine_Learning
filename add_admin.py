from tkinter import*
from tkinter.messagebox import *
from tkinter.ttk import *
from pymysql import *
from connection import *
class admin:
    def test(self):
        if self.textbox1.get() == "" or self.textbox2.get() == "" or self.textbox3.get() == "" or self.textbox4.get() == "":
            showinfo("", "ALL field are Mendatory ")
        elif  str(self.textbox1.get().count("@"))!="1" and str(self.textbox1.get().count("."))<="1":
            showinfo("","email is not valid")
        elif  self.textbox2.get()!=self.textbox3.get():
            showinfo("","password does not match")
        else:
            query ="insert into admin values('"+self.textbox1.get()+"','"+self.textbox3.get()+"','"+self.textbox4.get()+"','"+self.cb1.get()+"')"

            db = connection()
            cr = db.conn.cursor()

            cr.execute(query)

            db.conn.commit()

            showinfo("", "Admin Added Sucessfully")


    def __init__(self):

        self.root=Tk()
        self.root.title("Add Admin Window")
        self.root.config(bg='light gray')
        self.root.geometry("300x230")
        self.root.resizable(0,0)
        self.lb_heading = Label(self.root, text='ADD ADMIN')
        labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='brown', background='light gray', font=labelfont)


        self.lb1=Label(self.root,text="Email",background="light gray",foreground="brown")
        self.lb2=Label(self.root,text="Password",background="light gray",foreground="brown")
        self.lb3=Label(self.root,text="Confirm password",background="light gray",foreground="brown")
        self.lb4=Label(self.root,text="Mobile",background="light gray",foreground="brown")
        self.lb5 = Label(self.root, text="Type", background="light gray", foreground="brown")

        self.cb1 =Combobox(self.root,state="readonly", values=("admin"," user"))


        self.textbox1=Entry(self.root)
        self.textbox2=Entry(self.root,show="*")
        self.textbox3=Entry(self.root,show="*")
        self.textbox4=Entry(self.root)

        self.lb_heading.grid(row=0, column=0,columnspan=2)
        self.lb1.grid(row=1,column=0,sticky=(W))
        self.lb2.grid(row=2,column=0,sticky=(W))
        self.lb3.grid(row=3,column=0,sticky=(W))
        self.lb4.grid(row=4,column=0,sticky=(W))
        self.lb5.grid(row=5, column=0,sticky=(W))

        self.textbox1.grid(row=1,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.textbox2.grid(row=2,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.textbox3.grid(row=3,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.textbox4.grid(row=4,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.cb1.grid(row=5, column=1,padx=5,pady=5,sticky=(N,E,W))
        bt1=Button(self.root,text="Submit",width=15,command=self.test)
        bt1.grid(row=6,column=1)
        self.root.mainloop()

#-------------------------------------------------
#x=admin()