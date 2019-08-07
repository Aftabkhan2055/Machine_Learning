from datetime import *
from tkinter import *
from pymysql import *
from tkinter.messagebox import *
import tkinter.ttk as ttk
from connection import *
import http.client

bt_list=[]
bt_dict={}

class ticketbook:
    def park2(self, x, y):
        p = str(x) + "-" + str(y)
        global operation
        operation = str(x) + "-" + str(y)
        self.m.set(operation)
        self.rk.destroy()


    def parking2(self):
        self.rk=Tk()
        self.rk.title("parking2")
        global bt_list

        for i in range(101, 111):
            for j in range(101, 111):
                s = str(i) + "-" + str(j)
                bt_list.append(s)
                dr =connection()
                query = "select * from booking where parkingplace='" + s + "' and dateofexit is null"
                cr = dr.conn.cursor()
                cr.execute(query)
                p = cr.fetchall()

                if len(p)> 0:
                    bt_dict[bt_list[-1]] = ttk.Button(self.rk, text="O",width="7",state="disabled")
                else:
                    bt_dict[bt_list[-1]] = ttk.Button(self.rk, width=7,text=s)#,bg="green",fg="yellow")
                    bt_dict[bt_list[-1]]["command"] = lambda x=i, y=j: self.park2(x, y)
                bt_dict[bt_list[-1]].grid(row=i, column=j, padx=5, pady=3)

        self.rk.mainloop()
                                         #PARKING 1:-START
#-====================================================================================================================

    def park1(self, x, y):
        global operation
        operation= str(x) + "-" + str(y)
        self.parking_location.delete(0, END)
        self.m.set(operation)

        self.parking_location.insert(0,operation)

        self.win.destroy()
    #-===========================================================================================================
    def parking1(self):
        self.win= Tk()
        self.win.title("parking1")
        global bt_list

        for i in range(1,11):
            for j in range(1,11):
                s = str(i)+"-"+str(j)
                bt_list.append(s)
                dr = connection()
                query = "select * from booking where parkingplace='"+s+"' and dateofexit is null"
                cr = dr.conn.cursor()
                cr.execute(query)
                p = cr.fetchall()

                if len(p)>0:
                    bt_dict[bt_list[-1]] = ttk.Button(self.win, text="O", width="5",state="disabled")
                else:
                    bt_dict[bt_list[-1]] = ttk.Button(self.win, width=5,text=s)#,bg="green",fg="yellow")
                    bt_dict[bt_list[-1]]["command"] = lambda x=i, y=j : self.park1(x, y)
                bt_dict[bt_list[-1]].grid(row=i, column=j,padx=5,pady=3)
        self.win.mainloop()
#-====================================================================================================================
    def insert(self):
        if self.vnumber.get()=="" or self.cbvechicle.get()=="" or self.cbparking.get()=="" or self.price=="" or self.parking_location=="" or self.parking_location.get()=="" or self.mobile.get()=="":
            showerror("","All Fields are mandatory")
        else:
            dr=connection()
            query="insert into booking value (null, '"+self.vnumber.get()+"','"+self.cbvechicle.get()+"','"+self.cbparking.get()+"',"+self.price.get()+",'"+self.dateofentry.get()+"','"+self.timeofentry.get()+"','"+self.parking_location.get()+"','"+self.mobile.get()+"',null,null)"
            cr=dr.conn.cursor()
            cr.execute(query)
            dr.conn.commit()

            conn = http.client.HTTPConnection("server1.vmm.education")
            textmessage="Your Vehicle no " + self.vnumber.get()+" is Parked at row "+self.parking_location.get()+" and parking Date and Time respectively "+self.currentdate+","+self.currenttime+"Your friend Aftab"
            textmessage= textmessage.replace(" ","%20")
            conn.request('GET',"/VMMCloudMessaging/AWS_SMS_Sender?username=dhk_py&password=GNEP0QCE&message="+textmessage+"&phone_numbers=" + self.mobile.get())
            response = conn.getresponse()
            print(response.read())


            showinfo("","booking sucess")
            print(query)
#-====================================================================================================================
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
        self.m=StringVar(self.root)
        lb = Label(down, text="Vehicle_Number",font=('arial',10,"bold"),fg="brown").grid(row=1, column=0,sticky=(W))
        lb = Label(down, text="Vehicle_Type",font=('arial',10,"bold"),fg="brown").grid(row=2, column=0,sticky=(W))
        lb = Label(down, text="Parking_Type",font=('arial',10,"bold"),fg="brown").grid(row=3, column=0,sticky=(W))
        lb = Label(down, text="Price",font=('arial',10,"bold"),fg="brown").grid(row=4, column=0,sticky=(W))
        lb = Label(down, text="parking_location",font=('arial',10,"bold"),fg="brown").grid(row=5, column=0,sticky=(W))
        lb = Label(down, text="Date_Of_Entry",font=('arial',10,"bold"),fg="brown").grid(row=6, column=0,sticky=(W))
        lb = Label(down, text="Time_of_Entry",font=('arial',10,"bold"),fg="brown").grid(row=7, column=0,sticky=(W))
        lb = Label(down, text="mobile",font=('arial',10,"bold"),fg="brown").grid(row=8, column=0,sticky=(W))

        self.vnumber = Entry(down)
        self.cbvechicle = ttk.Combobox(down,width=30,state="readonly",value=("Two Wheeler Light Vechicle","Two Wheeler Heavy Vechicle","Four Wheeler Light Vechicle","Four Wheeler Heavy Vechicle",))
        self.cbparking = ttk.Combobox(down,width=30,state="readonly",value=("Full day","12 Hour","6 Hour","3 Hour"))
        self.price = Entry(down)
        self.parking_location = Entry(down,textvariable=self.m,state="readonly")
        self.dateofentry = Entry(down)
        self.timeofentry = Entry(down)
        self.mobile = Entry(down)

        self.vnumber.grid(row=1, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.cbvechicle.grid(row=2, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.cbparking.grid(row=3, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.price.grid(row=4, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.parking_location.grid(row=5, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.dateofentry.grid(row=6, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.timeofentry.grid(row=7, column=1,padx=5, pady=5,sticky=(E,N,W))
        self.mobile.grid(row=8, column=1,padx=5, pady=5,sticky=(E,N,W))
    #-===================================================================================================================
        self.currentdate= datetime.now().strftime("%Y-%m-%d")
        self.currenttime=str(datetime.now().hour) +":"+str(datetime.now().minute) +":"+str(datetime.now().second)
        self.dateofentry.delete(0,END)
        self.timeofentry.delete(0,END)
        self.dateofentry.insert(0,self.currentdate)
        self.timeofentry.insert(0,self.currenttime)
    #-==================================================================================================================

        bt1=Button(down,text="Submit",font=('arial',10,"bold"),borderwidth=3,command=self.insert,width=7).grid(row=9, column=1)
        bt=Button(down,text="2 wheeler",font=('arial',10,"bold"),borderwidth=3,command=self.parking1).grid(row=5, column=2)
        bt2=Button(down,text="4 wheeler",font=('arial',10,"bold"),borderwidth=3,command=self.parking2).grid(row=7, column=2)
        self.root.mainloop()
#-========================================================================================================================
x=ticketbook()