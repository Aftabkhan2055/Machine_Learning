from datetime import *
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
import tkinter.ttk as ttk
from connection import *



class ticketbook1:
    def search(self):
        query = "select * from booking  where Vehicle_number='" + self.vnumber.get() + "'"
        db = connection()
        cr = db.conn.cursor()
        cr.execute(query)

        p = cr.fetchone()
        self.cbvehicle.set(p[2])
        self.cbparking.set(p[3])
        self.price.insert(0,p[4])
        # self.dateofentry.insert(0,p[5])
        # self.timeofentry.insert(0,p[6])
        self.parking_location.insert(0, p[7])
        self.mobile.insert(0,p[8])
    def save(self):
         query3 ="update booking set dateofexit='"+self.dateofexit.get()+"',timeofexit='"+self.timeofexit.get()+"'where Vehicle_number='"+self.vnumber.get()+"'"
         db = connection()
         cr = db.conn.cursor()
         cr.execute(query3)
         db.conn.commit()
         showinfo("", "Exit Successfully")
         #print(query3)

    def __init__(self):
        self.root=Tk()
        self.root.title("Parking Ticket")
        self.root.geometry("410x400")
    #-=================================================================================
        top=Frame(self.root,width=100)
        top.pack()
        down=Frame(self.root)
        down.pack()
    #-====================================================================================
        lb=Label(top,text="PARKING TICKET",font=("Britannic Bold",20,"underline"),fg="green").pack()
    #-=====================================================================================
        self.m=StringVar()
        lb = Label(down, text="Vehicle_Number",font=('arial',10,"bold"),fg="brown").grid(row=1, column=0,sticky=(W))
        lb = Label(down, text="Vehicle_Type",font=('arial',10,"bold"),fg="brown").grid(row=2, column=0,sticky=(W))
        lb = Label(down, text="Parking_Type",font=('arial',10,"bold"),fg="brown").grid(row=3, column=0,sticky=(W))
        lb = Label(down, text="Price",font=('arial',10,"bold"),fg="brown").grid(row=4, column=0,sticky=(W))
        lb = Label(down, text="parking_location",font=('arial',10,"bold"),fg="brown").grid(row=5, column=0,sticky=(W))
        # lb = Label(down, text="Date_Of_Entry",font=('arial',10,"bold"),fg="brown").grid(row=6, column=0,sticky=(W))
        # lb = Label(down, text="Time_of_Entry",font=('arial',10,"bold"),fg="brown").grid(row=7, column=0,sticky=(W))
        lb = Label(down, text="mobile",font=('arial',10,"bold"),fg="brown").grid(row=8, column=0,sticky=(W))
        lb = Label(down, text="Date_Of_Exit", font=('arial', 10, "bold"), fg="brown").grid(row=9, column=0, sticky=(W))
        lb = Label(down, text="Time_of_Exit", font=('arial', 10, "bold"), fg="brown").grid(row=10, column=0, sticky=(W))

        self.vnumber = Entry(down)
        self.cbvehicle = ttk.Combobox(down,width=30,state="readonly",value=("Two Wheeler Light Vechicle","Two Wheeler Heavy Vechicle","Four Wheeler Light Vechicle","Four Wheeler Heavy Vechicle",))
        self.cbparking = ttk.Combobox(down,width=30,state="readonly",value=("Full day","12 Hour","6 Hour","3 Hour"))
        self.price = Entry(down)
        self.parking_location = Entry(down,textvariable=self.m)
        # self.dateofentry = Entry(down)
        # self.timeofentry = Entry(down)
        self.mobile = Entry(down)
        self.dateofexit = Entry(down)
        self.timeofexit= Entry(down)

        self.vnumber.grid(row=1, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.cbvehicle.grid(row=2, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.cbparking.grid(row=3, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.price.grid(row=4, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.parking_location.grid(row=5, column=1,padx=5, pady=5,sticky=(E,N,W))
        # self.dateofentry.grid(row=6, column=1,padx=5, pady=5,sticky=(E,N,W))
        # self.timeofentry.grid(row=7, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.mobile.grid(row=8, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.dateofexit.grid(row=9, column=1, padx=5, pady=5, sticky=(E, N, W))
        self.timeofexit.grid(row=10, column=1, padx=5, pady=5, sticky=(E, N, W))
    #-===================================================================================================================
        self.currentdate= datetime.now().strftime("%Y-%m-%d")
        self.currenttime=str(datetime.now().hour) +":"+str(datetime.now().minute) +":"+str(datetime.now().second)
        # self.dateofentry.delete(0, END)
        # self.timeofentry.delete(0,END)
        self.dateofexit.delete(0, END)
        self.timeofexit.delete(0, END)
        # self.dateofentry.insert(0,self.currentdate)
        # self.timeofentry.insert(0,self.currenttime)
        self.dateofexit.insert(0, self.currentdate)
        self.timeofexit.insert(0, self.currenttime)
    #-==================================================================================================================

        bt1=Button(down,text="find",font=('arial',10,"bold"),borderwidth=3,command=self.search,width=7).grid(row=11, column=1)
        bt2 = Button(down, text="exit", font=('arial', 10, "bold"), borderwidth=3, command=self.save, width=7).grid(row=11, column=2)

        self.root.mainloop()
#-========================================================================================================================
x=ticketbook1()
