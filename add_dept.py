from pymysql import *
from tkinter import *
from tkinter.messagebox import *

def test4():

    if textbox1.get()=="" or textbox2.get()=="" or textbox3.get()=="":
        showinfo("","Cannot Leave Fields Blank")
    else:

        query="insert into course values('"+textbox1.get()+"','"+textbox2.get()+"','"+textbox3.get()+"')"

        conn=Connect("127.0.0.1","root",'',"testfile")

        cr=conn.cursor()

        cr.execute(query)

        conn.commit()

        showinfo("","Department Added Sucessfully")



root=Tk()

lb1=Label(root,text="Enter Department Name")
lb2=Label(root,text="Enter Location")
lb3=Label(root,text="Enter Head Name")

textbox1=Entry(root)
textbox2=Entry(root)
textbox3=Entry(root)

bt1=Button(root,text="Submit",command=test4)

lb1.grid(row=0,column=0)
textbox1.grid(row=0,column=1)

lb2.grid(row=1,column=0)
textbox2.grid(row=1,column=1)

lb3.grid(row=2,column=0)
textbox3.grid(row=2,column=1)

bt1.grid(row=3,column=1)

root.mainloop()




