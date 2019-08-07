from tkinter import *

root=Tk()


root.geometry("300x340+50+50")
root.title("calculator")
#root.wm_iconbitmap("pic.jpg")
root.configure(background="green")



Tops=Frame(root,width=300,height=20,bd=4)#,relief=raise)
Tops.pack(side=TOP)

Below=Frame(root,width=300,height=300,bd=4)#,relief="raise")
Below.pack(side=BOTTOM)

#==========================================================================
def btclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btClear():
    global operator
    operator=""
    text_Input.set("")

def btEquals():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator=""

operator = ""
text_Input= StringVar()

#=================================================================================
txtDisplay=Entry(Tops,font=('arial',18,'bold'),textvariable=text_Input,width=21,bd=4,justify='right')
txtDisplay.grid(row=0,column=0)


bt7=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="7",command=lambda:btclick(7))
bt7.grid(row=0,column=0)
bt8=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="8",command=lambda:btclick(8))
bt8.grid(row=0,column=1)
bt9=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="9",command=lambda:btclick(9))
bt9.grid(row=0,column=2)
btAdd=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="+",command=lambda:btclick("+"))
btAdd.grid(row=0,column=3)


bt4=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="4",command=lambda:btclick(4))
bt4.grid(row=1,column=0)
bt5=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="5",command=lambda:btclick(5))
bt5.grid(row=1,column=1)
bt6=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="6",command=lambda:btclick(6))
bt6.grid(row=1,column=2)
btSub=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="-",command=lambda:btclick("-"))
btSub.grid(row=1,column=3)
bt1=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="1",command=lambda:btclick(1))
bt1.grid(row=2,column=0)
bt2=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="2",command=lambda:btclick(2))
bt2.grid(row=2,column=1)
bt3=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="3",command=lambda:btclick(3))
bt3.grid(row=2,column=2)
btMult=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="*",command=lambda:btclick("*"))
btMult.grid(row=2,column=3)


bt0=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="0",command=lambda:btclick(0))
bt0.grid(row=3,column=1)
btClear=Button(Below,padx=16,pady=1,bd=4,fg="green",font=('arial',16,'bold'),width=2,height=2,text="C",command=btClear)
btClear.grid(row=3,column=0)
btEquals=Button(Below,padx=16,pady=1,bd=4,fg="yellow",font=('arial',16,'bold'),width=2,height=2,text="=",command=btEquals)
btEquals.grid(row=3,column=2)
btDiv=Button(Below,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=2,height=2,text="/",command=lambda:btclick("/"))
btDiv.grid(row=3,column=3)



root.mainloop()
