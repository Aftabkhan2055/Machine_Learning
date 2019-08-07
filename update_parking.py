from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from  pymysql import *
from connection import *

class parking:
    def search(self):
        if self.textbox1==" " or self.cb1.get()==" "or self.cb2.get()==" " or self.textbox2==" ":
            showerror("","All field are mendatory")
        else:
            query = "select * from rates where Rateid='" + self.textbox1.get()+"'"
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query)
            p = cr.fetchone()
            self.textbox2.delete(0,END)
            self.cb1.set(p[1])
            self.cb2.set(p[2])
            self.textbox2.insert(0,p[3])
    def remove(self):
        if self.textbox1.get()==" " or self.cb1.get()==" " or self.cb2.get()==" "or self.textbox2.get()==" ":
            showerror("","All field are mendatory")
        else:
            query2="delete  from rates where Rateid='"+self.textbox1.get()+"'"
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query2)
            db.conn.commit()
            showinfo("","parking Delete Successfully")

    def save(self):

        if self.textbox1.get()==" " or self.cb1.get()==" " or self.cb2.get()==" "or self.textbox2.get()==" ":
            showerror("","All field are mendatory")
        else:
            query3 ="update rates set Vehicletype='"+ self.cb1.get()+"',Parkingtype='"+self.cb2.get()+"',price='"+self.textbox2.get()+"' where Rateid='" +self.textbox1.get()+"'"
            db = connection()
            cr = db.conn.cursor()
            cr.execute(query3)
            showinfo("", "parking update Successfully")

    def __init__(self):
        self.root = Tk()
        self.root.title(" Parking Window")
        self.root.config(bg='light gray')
        self.root.geometry("400x230")
        self.root.resizable(0, 0)
        self.lb_heading = Label(self.root, text='RATES')
        labelfont = ('Arial', 20, 'bold')
        self.lb_heading.configure(foreground='brown', background='light gray', font=labelfont)

        self.lb1 = Label(self.root, text="Select rate id ", background="light gray", foreground="brown")
        self.lb2=Label(self.root,text="Select vehicle type ",background="light gray",foreground="brown")
        self.lb3=Label(self.root,text="Select parking type ",background="light gray",foreground="brown")
        self.lb4=Label(self.root,text="Enter Price",background="light gray",foreground="brown")

        self.textbox1 = Combobox(self.root,state="readonly")

        db = connection()
        cr = db.conn.cursor()
        query="select Rateid from rates order by Rateid"
        cr.execute(query)
        p=cr.fetchall()
        lst = []
        for i in range(0,len(p)):
            lst.append(p[i][0])
        self.textbox1.config(values=tuple(lst))

        self.cb1=Combobox(self.root,state="readonly",values=("Two Wheeler","Four Wheeler","Truck"))
        self.cb2=Combobox(self.root,state="readonly",values=("3 Hours","Half day","Full day"))
        self.textbox2=Entry(self.root)

        self.lb_heading.grid(row=0, column=1, columnspan=3)
        self.lb1.grid(row=1, column=0, sticky=(W))
        self.lb2.grid(row=2,column=0,sticky=(W))
        self.lb3.grid(row=3,column=0,sticky=(W))
        self.lb4.grid(row=4,column=0,sticky=(W))

        self.textbox1.grid(row=1, column=1, padx=5, pady=5, sticky=(N, E, W))
        self.cb1.grid(row=2,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.cb2.grid(row=3,column=1,padx=5,pady=5,sticky=(N,E,W))
        self.textbox2.grid(row=4,column=1,padx=5,pady=5,sticky=(N,E,W))

        #self.bt=Button(self.root,text="submit",width=20)
        #self.bt.grid(row=4,column=1)


        self.bt1=Button(self.root,text="Find",command=self.search)
        self.bt2=Button(self.root,text="Delete",command=self.remove)
        self.bt3=Button(self.root,text="Update",command=self.save)

        self.bt1.grid(row=1,column=3)
        self.bt2.grid(row=2,column=3)
        self.bt3.grid(row=4,column=3)
        self.root.mainloop()


#--------------------------------------------------------------
#x=parking()