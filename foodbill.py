# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:09:58 2022

@author: mitta
"""
from tkinter import *
import tkinter.font as font
import time
import datetime
import random
import tkinter.messagebox

top=Tk()
top.geometry("400x400")

def close():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        top.destroy()
        return
def total_bill(): 
    s=0
    r4.delete(0,END)
    r5.delete(0,END)
    r6.delete(0,END)
    temp=(chk1.get())
    if(temp==1):
        temp1=(n1.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*190
    temp=(chk2.get())
    if(temp==1):
        temp1=(n2.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*150
    temp=(chk3.get())
    if(temp==1):
        temp1=(n3.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*90
    temp=(chk4.get())
    if(temp==1):
        temp1=(n4.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*60
    temp=(chk5.get())
    if(temp==1):
        temp1=(n5.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*70
    temp=(chk6.get())
    if(temp==1):
        temp1=(n6.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*220
    temp=(chk7.get())
    if(temp==1):
        temp1=(n7.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*120
    temp=(chk8.get())
    if(temp==1):
        temp1=(n8.get())
        if 1 == temp1.isnumeric():
            s=s+int(temp1)*110
    tax=s*5/100
    total=s+tax 
    r4.insert(1,s)
    r5.insert(1,tax)
    r6.insert(1,total)
    return

def reset():
    r4.delete(0,END)
    r5.delete(0,END)
    r6.delete(0,END)
    
    n1.set("0")
    n2.set("0")
    n3.set("0")
    n4.set("0")
    n5.set("0")
    n6.set("0")
    n7.set("0")
    n8.set("0")
    
    r4.insert(END,r)
    r5.insert(END,r)
    r6.insert(END,r)
    
    chk1.set(0)
    chk2.set(0)
    chk3.set(0)
    chk4.set(0)
    chk5.set(0)
    chk6.set(0)
    chk7.set(0)
    chk8.set(0)
    
    e1.configure(state = DISABLED)
    e2.configure(state = DISABLED)
    e3.configure(state = DISABLED)
    e4.configure(state = DISABLED)
    e5.configure(state = DISABLED)
    e6.configure(state = DISABLED)
    e7.configure(state = DISABLED)
    e8.configure(state = DISABLED)
    return

def receipt():
    root=Tk()
    root.geometry("400x400")
    Receipt_F=Frame(root,bg='light blue',bd=4,relief=RIDGE)
    Receipt_F.pack()
    txtReceipt=Text(Receipt_F,width=46,height=14,bg='white',bd=4,font=('arial',12,'bold'))
    txtReceipt.grid(row=0,column=0)
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill:"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t'+"Cost of Items"+"\t\t      Quantity\n")
    txtReceipt.insert(END,'Pizza:\t\t'+'190\t\t\t'+ n1.get()+'\n')
    txtReceipt.insert(END,'Pasta:\t\t'+'150\t\t\t'+ n2.get()+'\n')
    txtReceipt.insert(END,'Burger:\t\t'+'90\t\t\t'+ n3.get()+'\n')
    txtReceipt.insert(END,'Patties:\t\t'+'60\t\t\t'+ n4.get()+'\n')
    txtReceipt.insert(END,'Sandwich:\t\t'+'70\t\t\t'+ n5.get()+'\n')
    txtReceipt.insert(END,'Sizzler:\t\t'+'220\t\t\t'+ n6.get()+'\n')
    txtReceipt.insert(END,'Vegrolls:\t\t'+'120\t\t\t'+ n7.get()+'\n')
    txtReceipt.insert(END,'Fires:\t\t'+'110\t\t\t'+ n8.get()+'\n\n')
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ cost.get() +'\nTax:\t\t\t\t'+ tax.get() +"\n")
    txtReceipt.insert(END,'Total Cost:\t\t\t\t'+ total.get()+"\n")
    # name=(n9.get())
    # num=int((n10.get()))
    
    # if name.replace(" ","").isalpha():
    #     print("valid")
    # else:
    #     print("Not")
    # if num>=1000000000 and num<=9999999999:
    #     print("right")
    # else:
    #     print("wrong")
    
    root.mainloop()
    
def pizza():
    if(chk1.get() == 1):
        e1.configure(state = NORMAL)
        e1.delete('0',END)
        e1.focus()
    elif(chk1.get() == 0):
        e1.configure(state = DISABLED)
        n1.set("0")

def pasta():
    if(chk2.get() == 1):
        e2.configure(state = NORMAL)
        e2.delete('0',END)
        e2.focus()
    elif(chk2.get() == 0):
        e2.configure(state = DISABLED)
        n2.set("0")

def burger():
    if(chk3.get() == 1):
        e3.configure(state = NORMAL)
        e3.delete('0',END)
        e3.focus()
    elif(chk3.get() == 0):
        e3.configure(state = DISABLED)
        n3.set("0")

def patties():
    if(chk4.get() == 1):
        e4.configure(state = NORMAL)
        e4.delete('0',END)
        e4.focus()
    elif(chk4.get() == 0):
        e4.configure(state = DISABLED)
        n4.set("0")
        
def sandwich():
    if(chk5.get() == 1):
        e5.configure(state = NORMAL)
        e5.delete('0',END)
        e5.focus()
    elif(chk5.get() == 0):
        e5.configure(state = DISABLED)
        n5.set("0")
        
def sizzler():
    if(chk6.get() == 1):
        e6.configure(state = NORMAL)
        e6.delete('0',END)
        e6.focus()
    elif(chk6.get() == 0):
        e6.configure(state = DISABLED)
        n6.set("0")
        
def vegrolls():
    if(chk7.get() == 1):
        e7.configure(state = NORMAL)
        e7.delete('0',END)
        e7.focus()
    elif(chk7.get() == 0):
        e7.configure(state = DISABLED)
        n7.set("0")
        
def fries():
    if(chk8.get() == 1):
        e8.configure(state = NORMAL)
        e8.delete('0',END)
        e8.focus()
    elif(chk8.get() == 0):
        e8.configure(state = DISABLED)
        n8.set("0")
        
c = Canvas(top,bg = "pink",height = "400",width="800")  
c.pack()

Receipt_Ref = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))

f = font.Font(family='Times New Roman', size=12, weight="bold")

n=Label(top,text="FOOD BILLING SYSTEM",bg="RED",bd=5,cursor="dot",font="Verdana",fg="pink",padx=4,pady=4).place(x=100,y=10)
# l1=Label(top,text="Customer Details",bg="RED",bd=4,cursor="dot",font="Verdana",fg="pink",padx=2,pady=2).place(x=150,y=60)
# l2=Label(top,text="Name     :",bg="pink")
# l2['font']=f
# l2.place(x=148,y=110)

# l3=Label(top,text="Number  :",bg="pink")
# l3['font']=f
# l3.place(x=148,y=135)

chk1=IntVar()
chk2=IntVar()
chk3=IntVar()
chk4=IntVar()
chk5=IntVar()
chk6=IntVar()
chk7=IntVar()
chk8=IntVar()

chkb1=Checkbutton(top,text="Pizza",bg="pink",variable=chk1,onvalue=1,offvalue=0,command=pizza).place(x=0,y=60)
chkb2=Checkbutton(top,text="Pasta",bg="pink",variable=chk2,onvalue=1,offvalue=0,command=pasta).place(x=0,y=85)
chkb3=Checkbutton(top,text="Burger",bg="pink",variable=chk3,onvalue=1,offvalue=0,command=burger).place(x=0,y=110)
chkb4=Checkbutton(top,text="Patties",bg="pink",variable=chk4,onvalue=1,offvalue=0,command=patties).place(x=0,y=135)
chkb5=Checkbutton(top,text="Sandwich",bg="pink",variable=chk5,onvalue=1,offvalue=0,command=sandwich).place(x=0,y=160)
chkb6=Checkbutton(top,text="Sizzler",bg="pink",variable=chk6,onvalue=1,offvalue=0,command=sizzler).place(x=0,y=185)
chkb7=Checkbutton(top,text="Vegrolls",bg="pink",variable=chk7,onvalue=1,offvalue=0,command=vegrolls).place(x=0,y=210)
chkb8=Checkbutton(top,text="Fries",bg="pink",variable=chk8,onvalue=1,offvalue=0,command=fries).place(x=0,y=235)



n1 = StringVar()  
n2 = StringVar()  
n3 = StringVar()  
n4 = StringVar()  
n5 = StringVar()  
n6 = StringVar()  
n7 = StringVar()  
n8 = StringVar()  

n1.set("0")
n2.set("0")
n3.set("0")
n4.set("0")
n5.set("0")
n6.set("0")
n7.set("0")
n8.set("0")

e1=Entry(top,textvariable=n1,width=4,state=DISABLED)
e2=Entry(top,textvariable=n2,width=4,state=DISABLED)
e3=Entry(top,textvariable=n3,width=4,state=DISABLED)
e4=Entry(top,textvariable=n4,width=4,state=DISABLED)
e5=Entry(top,textvariable=n5,width=4,state=DISABLED)
e6=Entry(top,textvariable=n6,width=4,state=DISABLED)
e7=Entry(top,textvariable=n7,width=4,state=DISABLED)
e8=Entry(top,textvariable=n8,width=4,state=DISABLED)

r=0


e1.place(x=80,y=60)
e2.place(x=80,y=85)
e3.place(x=80,y=110)
e4.place(x=80,y=135)
e5.place(x=80,y=160)
e6.place(x=80,y=185)
e7.place(x=80,y=210)
e8.place(x=80,y=235)

# n9=StringVar()
# n10=StringVar()

# e9=Entry(top,textvariable=n9).place(x=220,y=113)
# e10=Entry(top,textvariable=n10).place(x=220,y=138)

cost=StringVar()
tax=StringVar()
total=StringVar()

r1=Label(top,text="Amount",bg="pink")
r1['font']=f
r1.place(x=0,y=300)

r2=Label(top,text="Tax",bg="pink")
r2['font']=f
r2.place(x=0,y=320)

r3=Label(top,text="Total",bg="pink")
r3['font']=f
r3.place(x=0,y=340)

r4=Entry(top,textvariable=cost)
r5=Entry(top,textvariable=tax)
r6=Entry(top,textvariable=total)

r4.insert(END,r)
r5.insert(END,r)
r6.insert(END,r)

r4.place(x=60,y=305)
r5.place(x=60,y=325)
r6.place(x=60,y=345)

b=Button(top,text="Total",command=total_bill).place(x=0,y=260)
  
c=Button(top,text="Exit",command=close).place(x=160,y=260)

c=Button(top,text="Reset",command=reset).place(x=110,y=260)

c=Button(top,text="Receipt",command=receipt).place(x=50,y=260)


top.mainloop()