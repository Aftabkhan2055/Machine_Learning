from tkinter import *
import tkinter.ttk as ttk
from connection import *
from datetime import *

class sellp:
    def __init__(self):
        self.root=Tk()
        self.root.configure(bg="dark green")
        # -=================================
        top=Frame(self.root,bg="dark green")
        top.pack()
        down=Frame(self.root,bg="dark green")
        down.pack()
        # -==========================================

        lb=Label(top,text="Today Earning",font=("arial",20,"bold"),bg="dark green",fg="pink").pack()
        tree = ttk.Treeview(down, column=("tid", "vnumber", "vtype","vparking", "price",  "dentry", "tentry", "plocation","mobile", "dexit", "texit","remark"))
        tree.heading("tid", text="Tid")
        tree.heading("vnumber", text="Vechicle_Number")
        tree.heading("vtype", text="Vechicle_type")
        tree.heading("vparking", text="Parking_type")
        tree.heading("price", text="Price")
        tree.heading("dentry", text="Date_of_Entry")
        tree.heading("tentry", text="Time_of_Entry")
        tree.heading("plocation", text="Parking_location")
        tree.heading("mobile", text="Mobile")
        tree.heading("dexit", text="Date_of_Exit")
        tree.heading("texit", text="Time_of_Exit")
        tree.heading("remark", text="remark")
        tree.column("#0",width=0)
        tree.column("price", width=90)
        tree.column("dentry", width=100)
        tree.column("plocation", width=100)
        tree.column("tentry", width=90)
        tree.column("tid", width=70)
        tree.column("mobile", width=100)
        tree.column("dexit", width=70)
        tree.column("texit", width=90)
        tree.column("remark", width=100)
        tree.column("vnumber", width=110)
        tree.column("vparking",width=90)
        tree.grid(row=1,column=1,columnspan=3)
        lb=Label(down,text="Total: ",bg="dark green",font=("arial",18,"bold")).grid(row=2,column=2,sticky=(E))
        total=Entry(down,font=("arial",13,"bold"))
        total.grid(row=2,column=3,sticky=(W))

        self.currentdate = datetime.now().strftime("%Y-%m-%d")

        dr=connection()
        query="select * from booking where dateofentry='"+self.currentdate+"'"
        #query="select * from booking where dateofentry='2018-07-16'"

        #print(query)
        cr=dr.conn.cursor()
        cr.execute(query)
        p=cr.fetchall()

        for i in range(0, len(p)):
            tree.insert("", value=p[i], index=i)

        query1="select price from booking where dateofentry='"+self.currentdate+"'"
        #query1="SELECT price from parking_ticket where dateofentry='2018-07-16'"
        cd=dr.conn.cursor()
        cd.execute(query1)
        q=cd.fetchall()
        s=0
        for i in q:
            for j in range(0,1):
                s=s+int(i[j])
        total.insert(0,s)
        total.config(state="readonly")
        self.root.mainloop()

#-------------------------------------------------------------------------------------------
#x=sellp()