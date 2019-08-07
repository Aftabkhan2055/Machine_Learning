from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from  pymysql import *
from connection import *

class addparking:
    def test(self):
        if self.cb1.get() == "" or self.cb2.get() == "" or self.textbox.get() == "":
            showinfo("", "ALL field are Mandatory ")

        elif self.cb1.get()!="":
            query="select * from rates where Vehicletype='"+self.cb1.get()+"'and Parkingtype='"+self.cb2.get()+"'"
            db=connection()
            cr=db.conn.cursor()      
            cr.execute(query)

            p=cr.fetchone()

            if p==None:

                query ="insert into rates values('null','"+self.cb1.get()+"','"+self.cb2.get()+"','"+self.textbox.get()+"')"

                db = connection()
                cr = db.conn.cursor()

                cr.execute(query)

                db.conn.commit()

                showinfo("", "parking Added Sucessfully")
            else:
                showinfo("","Parking booked")


    def __init__(self):

        self.root=Tk()
        self.root.title("Add parking Window")
        self.root.config(bg='light gray')
        self.root.geometry("300x230")
        self.root.resizable(0,0)
        self.lb_heading = Label(self.root, text='RATES')
        labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='brown', background='light gray', font=labelfont)

        self.lb1 = Label(self.root, text="Select vehicle type ", background="light gray", foreground="brown")
        self.lb2 = Label(self.root, text="Select parking type ", background="light gray", foreground="brown")
        self.lb3 = Label(self.root, text="Enter Price", background="light gray", foreground="brown")

        self.cb1 = Combobox(self.root, state="readonly", values=("Two Wheeler", "Four Wheeler", "Truck"))
        self.cb2 = Combobox(self.root, state="readonly", values=("3 Hours", "Half day", "Full day"))
        self.textbox = Entry(self.root)

        self.lb_heading.grid(row=0, column=0, columnspan=2)
        self.lb1.grid(row=1, column=0, sticky=(W))
        self.lb2.grid(row=2, column=0, sticky=(W))
        self.lb3.grid(row=3, column=0, sticky=(W))

        self.cb1.grid(row=1, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.cb2.grid(row=2, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox.grid(row=3, column=1, padx=5, pady=5, sticky=(N, E, W))


        self.bt1=Button(self.root,text="Submit",width=15,command=self.test)
        self.bt1.grid(row=6,column=1)
        self.root.mainloop()

#-------------------------------------------------
#x=addparking()