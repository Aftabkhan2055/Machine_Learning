from tkinter import *
from connection import *
from ticket_book import *
from booking_update import *
from add_parking import *
from update_parking import *
from view_parking import *
from today_sell import *
from  from_date import *
from v_number import*
from add_admin import *
from update_admin import *
from view_admin import *


class combinder:

    def test1(self):
        obj=ticketbook()
    def test2(self):
        obj2=ticketbook1()
    def test3(self):
        obj3=addparking()
    def test4(self):
        obj4=parking()
    def test5(self):
        obj5=view()
    def test6(self):
        obj6=sellp()
    def test7(self):
        obj7=sellq()
    def test8(self):
        obj8=sellr()
    def test9(self):
        obj9=admin()
    def test10(self):
        obj10=update()
    def test11(self):
        obj11=view()
    def __init__(self):
        self.x=Tk()
        self.x.geometry("1024x768")
        mymenu=Menu(self.x)
        self.x.config(menu=mymenu)

        option1=Menu(mymenu,tearoff=0)
        mymenu.add_cascade(label="Ticket booking",menu=option1)

        option1.add_command(label="Add ticket",command=self.test1)
        option1.add_command(label="Update ticket",command=self.test2)



        option2=Menu(mymenu)
        mymenu.add_cascade(label="parking(rate)",menu=option2)

        option2.add_command(label="add parking",command=self.test3)
        option2.add_command(label="update parking ",command=self.test4)
        option2.add_command(label="view parking",command=self.test5)

        option3=Menu(mymenu)
        mymenu.add_cascade(label="sell",menu=option3)

        option3.add_command(label="Today sell",command=self.test6)
        option3.add_command(label="From date and to date",command=self.test7)
        option3.add_command(label="total price aacording vehicle no",command=self.test8)


        option4=Menu(mymenu)
        mymenu.add_cascade(label="admin",menu=option4)

        option4.add_command(label="Add ADMIN",command=self.test9)
        option4.add_command(label="Update/Delete Admin",command=self.test10)
        option4.add_command(label="View Admin", command=self.test11)



        self.x.mainloop()


#---------------------------------------------------------------------
x=combinder()