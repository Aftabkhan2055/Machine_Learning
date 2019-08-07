from tkinter import *
from tkinter.messagebox import *


def reset():
    bt1["text"]="  "
    bt1["state"]="normal"

    bt2["text"] = "  "
    bt2["state"] = "normal"

    bt3["text"] = "  "
    bt3["state"] = "normal"

    bt4["text"] = "  "
    bt4["state"] = "normal"

    bt5["text"] = "  "
    bt5["state"] = "normal"

    bt6["text"] = "  "
    bt6["state"] = "normal"

    bt7["text"] = "  "
    bt7["state"] = "normal"

    bt8["text"] = "  "
    bt8["state"] = "normal"

    bt9["text"] = "  "
    bt9["state"] = "normal"


def checkwin():
    if bt1["text"]=="x"and bt2["text"]=="x" and bt3["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt4["text"]=="x"and bt5["text"]=="x" and bt6["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt7["text"]=="x"and bt8["text"]=="x" and bt9["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt1["text"]=="x"and bt4["text"]=="x" and bt7["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt2["text"]=="x"and bt5["text"]=="x" and bt8["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt3["text"]=="x"and bt6["text"]=="x" and bt9["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt1["text"]=="x"and bt5["text"]=="x" and bt9["text"]=="x":
        showinfo("","palyer 1 win")
        reset()
    elif bt3["text"]=="x"and bt5["text"]=="x" and bt7["text"]=="x":
        showinfo("","palyer 1 win")
        reset()

    elif bt1["text"]=="0"and bt2["text"]=="0" and bt3["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt4["text"]=="0"and bt5["text"]=="0" and bt6["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt7["text"]=="0"and bt8["text"]=="0" and bt9["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt1["text"]=="0"and bt4["text"]=="0" and bt7["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt2["text"]=="0"and bt5["text"]=="0" and bt8["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt3["text"]=="0"and bt6["text"]=="0" and bt9["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt1["text"]=="0"and bt5["text"]=="0" and bt9["text"]=="0":
        showinfo("","palyer 2 win")
        reset()
    elif bt3["text"]=="0"and bt5["text"]=="0" and bt7["text"]=="0":
        showinfo("","palyer 2 win")
        reset()

def click1():
    global play
    if play%2==0:
        bt1["text"]="x"
    else:
        bt1["text"]="0"
    play=play+1
    bt1['state']="disable"
    checkwin()

def click2():
    global play
    if play%2==0:
        bt2["text"]="x"
    else:
        bt2["text"]="0"
    play=play+1
    bt2['state'] = "disable"
    checkwin()


def click3():
    global play
    if play%2==0:
        bt3["text"]="x"
    else:
        bt3["text"]="0"
    play=play+1
    bt3['state'] = "disable"
    checkwin()

def click4():
    global play
    if play%2==0:
        bt4["text"]="x"
    else:
        bt4["text"]="0"
    play=play+1
    bt4['state'] = "disable"
    checkwin()

def click5():
    global play
    if play%2==0:
        bt5["text"]="x"
    else:
        bt5["text"]="0"
    play=play+1
    bt5['state'] = "disable"
    checkwin()

def click6():
    global play
    if play%2==0:
        bt6["text"]="x"
    else:
        bt6["text"]="0"
    play=play+1
    bt6['state'] = "disable"
    checkwin()

def click7():
    global play
    if play%2==0:
        bt7["text"]="x"
    else:
        bt7["text"]="0"
    play=play+1
    bt7['state'] = "disable"
    checkwin()

def click8():
    global play
    if play%2==0:
        bt8["text"]="x"
    else:
        bt8["text"]="0"
    play=play+1
    bt8['state'] = "disable"
def click9():
    global play
    if play%2==0:
        bt9["text"]="x"
    else:
        bt9["text"]="0"
    play=play+1
    bt9['state'] = "disable"
    checkwin()

root=Tk()
play=0

root.geometry("550x200")
root.title("aftab")



bt1=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click1)
bt2=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click2)
bt3=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click3)
bt4=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click4)
bt5=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click5)
bt6=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click6)
bt7=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click7)
bt8=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click8)
bt9=Button(root,text="  ",padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=9,borderwidth=7,command=click9)

bt_reset=Button(root,text="reset",command=reset)
bt10=Button(root,text="quit",command=quit)



bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)
bt3.grid(row=0,column=2)
bt4.grid(row=1,column=0)
bt5.grid(row=1,column=1)
bt6.grid(row=1,column=2)
bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)

bt_reset.grid(row=3,column=3)
bt10.grid(row=3,column=0)

root.mainloop()
