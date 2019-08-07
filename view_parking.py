from pymysql import *
from tkinter.ttk import*
from tkinter import *
from connection import *
class view:

    def __init__(self):
        self.root = Tk()
        self.root.title("Parking admin")
        self.root.config(bg='light gray')
        self.lb_heading=Label(self.root,text="RATES")
        labelfont=('Arial',20,'bold')
        self.lb_heading.configure(foreground='brown',background='light gray',font=labelfont)



        self.lb_heading.pack()
        self.t = Treeview(self.root,columns=("Rateid", "Vehicletype", "Parkingtype","Price"))
        self.t.heading("Rateid", text="Rate ID")
        self.t.heading("Vehicletype", text="Different vehicle")
        self.t.heading("Parkingtype", text="Parking ")
        self.t.heading("Price", text="Price")



        query = "select * from rates"
        db = connection()
        cr = db.conn.cursor()
        cr.execute(query)

        p = cr.fetchall()

        for i in range(0, len(p)):
            self.t.insert("", values=p[i], index=i)
        self.t.pack()

        self.root.mainloop()
#-----------------------------------------------------------------
#x=view()