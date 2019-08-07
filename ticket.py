from tkinter.ttk import *
from tkinter import *
from tkinter.messagebox import *
from  pymysql import *
from connection import *

class parking:
    def ticket(self):
        if  self.textbox2.get() == "" or self.cb1.get() == "" or self.cb2.get() == "" or self.textbox3.get() == "" or self.textbox4.get() == "" or self.textbox5.get() == "" or self.textbox6.get() == "" or self.textbox7.get() == "" or self.textbox8.get() == "":
            showinfo("", "ALL field are Mandatory ")


        else:
            query = "insert into ticket values('null','"+self.textbox2.get()+"','" + self.cb1.get() + "','" + self.cb2.get() + "','" + self.textbox3.get() + "','" + self.textbox4.get() + "','" + self.textbox5.get() + "','" + self.textbox6.get() + "','" + self.textbox7.get() + "','" + self.textbox8.get() + "')"
            db = connection()
            cr = db.conn.cursor()

            cr.execute(query)

            db.conn.commit()

            showinfo("", "Ticket Added Sucessfully")

    def __init__(self):
        self.root = Tk()
        self.root.title("Ticket parking Window")
        self.root.config(bg='light gray')
        self.root.geometry("400x430")
        self.root.resizable(0, 0)
        self.lb_heading = Label(self.root, text='TICKET')
        labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='brown', background='light gray', font=labelfont)

        #self.lb1=Label(self.root,text="Tid")
        self.lb2=Label(self.root, text="vehicle number")
        self.lb3=Label(self.root, text="vehicle type ")
        self.lb4=Label(self.root, text="parking type")
        self.lb5 = Label(self.root, text="Price")
        self.lb6=Label(self.root, text="Date of entry")
        self.lb7=Label(self.root, text="Time of entry")
        self.lb8=Label(self.root, text="Date of exit")
        self.lb9=Label(self.root, text="Time of exit")
        self.lb10=Label(self.root,text="Remarksifany")

        #self.textbox1=Entry(self.root)
        self.textbox2 = Entry(self.root)
        self.cb1 = Combobox(self.root, state="readonly", values=("Two Wheeler", "Four Wheeler", "Truck"))
        self.cb2 = Combobox(self.root, state="readonly", values=("3 Hours", "Half day", "Full day"))
        self.textbox3 = Entry(self.root)
        self.textbox4 = Entry(self.root)
        self.textbox5 = Entry(self.root)
        self.textbox6 = Entry(self.root)
        self.textbox7 = Entry(self.root)
        self.textbox8 = Entry(self.root)

        self.lb_heading.grid(row=0, column=0, columnspan=2)
        #self.lb1.grid(row=1, column=0, sticky=(W))
        self.lb2.grid(row=2, column=0, sticky=(W))
        self.lb3.grid(row=3, column=0, sticky=(W))
        self.lb4.grid(row=4, column=0, sticky=(W))
        self.lb5.grid(row=5,column=0, sticky=(W))
        self.lb6.grid(row=6, column=0, sticky=(W))
        self.lb7.grid(row=7, column=0, sticky=(W))
        self.lb8.grid(row=8, column=0, sticky=(W))
        self.lb9.grid(row=9, column=0, sticky=(W))
        self.lb10.grid(row=10,column=0, sticky=(W))


        #self.textbox1.grid(row=1, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox2.grid(row=2, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.cb1.grid(row=3, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.cb2.grid(row=4, column=1, padx=5, pady=5, sticky=(N, E, W))

        self.textbox3.grid(row=5, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox4.grid(row=6, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox5.grid(row=7, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox6.grid(row=8, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox7.grid(row=9, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.textbox8.grid(row=10, column=1, padx=5, pady=5, sticky=(N, E, W))

        self.bt1 = Button(self.root, text="Submit", width=15, command=self.ticket)
        self.bt1.grid(row=11, column=1)

        self.root.mainloop()


#--------------------------------------------------------
x=parking()