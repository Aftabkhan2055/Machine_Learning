from tkinter import *
import tkinter.ttk as ttk
from connection import *
from datetime import *

class sellr:
    def date(self):
        dr = connection()

        query = "select * from booking where Vehicle_number='" + self.vnumber.get() + "'"

        # print(query)
        cr = dr.conn.cursor()
        cr.execute(query)
        p = cr.fetchall()

        for i in range(0, len(p)):
            self.tree.insert("", value=p[i], index=i)

        query1="SELECT price from booking where  Vehicle_number='" + self.vnumber.get() + "'"
        cd=dr.conn.cursor()
        cd.execute(query1)
        q=cd.fetchall()
        s=0
        for i in q:
            for j in range(0,1):
                s=s+int(i[j])
        self.total.insert(0,s)
        self.total.config(state="readonly")




    def __init__(self):
        self.root=Tk()
        self.root.configure(bg="dark green")
        # -=================================
        top=Frame(self.root,bg="dark green")
        top.pack()
        down=Frame(self.root,bg="dark green")
        down.pack()
        # -==========================================

        lb=Label(top,text="Today Earning",font=("arial",20,"bold"),bg="dark green",fg="blue").pack()
        self.tree = ttk.Treeview(down, column=("tid", "vnumber", "vtype","vparking", "price",  "dentry", "tentry", "plocation","mobile", "dexit", "texit","remark"))
        self.tree.heading("tid", text="Tid")
        self.tree.heading("vnumber", text="Vechicle_Number")
        self.tree.heading("vtype", text="Vechicle_type")
        self.tree.heading("vparking", text="Parking_type")
        self.tree.heading("price", text="Price")
        self.tree.heading("dentry", text="Date_of_Entry")
        self.tree.heading("tentry", text="Time_of_Entry")
        self.tree.heading("plocation", text="Parking_location")
        self.tree.heading("mobile", text="Mobile")
        self.tree.heading("dexit", text="Date_of_Exit")
        self.tree.heading("texit", text="Time_of_Exit")
        self.tree.heading("remark", text="remark")
        self.tree.column("#0",width=0)
        self.tree.column("price", width=90)
        self.tree.column("dentry", width=100)
        self.tree.column("plocation", width=100)
        self.tree.column("tentry", width=90)
        self.tree.column("tid", width=70)
        self.tree.column("mobile", width=100)
        self.tree.column("dexit", width=70)
        self.tree.column("texit", width=90)
        self.tree.column("remark", width=100)
        self.tree.column("vnumber", width=110)
        self.tree.column("vparking",width=90)
        self.tree.grid(row=1,column=1,columnspan=3)
        lb=Label(down,text="Total: ",bg="yellow",font=("arial",18,"bold")).grid(row=2,column=2,sticky=(E))
        self.total=Entry(down,font=("arial",13,"bold"))
        self.total.grid(row=2,column=3,sticky=(W))

        #self.m = StringVar()
        lb = Label(down, text="Search Vehicle no", font=("Arial", 10), bg="white", fg="brown").grid(row=0, column=0,)

        self.vnumber = Entry(down)
        self.vnumber.grid(row=0, column=1, padx=5, pady=5, sticky=(E))

        bt1=Button(down, text="Go", font=("arial", 8, "bold"), fg="brown", width=10, command=self.date)
        bt1.grid(row=0, column=2)

        self.root.mainloop()

#-------------------------------------------------------------------------------------------
#x=sellr()