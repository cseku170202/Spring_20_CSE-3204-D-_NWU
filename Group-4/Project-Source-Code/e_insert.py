import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from tkcalendar import DateEntry
from PIL import ImageTk, Image

def ok():
    type=e1.get()
    c_name=e2.get()
    model=e3.get()
    origin=e4.get()
    capasity=e5.get()
    color=e6.get()
    name=e7.get()
    reg=e8.get()
    m_date=e9.get()
    e_num=e10.get()
    c_num=e11.get()
    weight=e12.get()
    r_date=e13.get()
    b_from=e14.get()
    price=e15.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
    mycursor = mysqldb.cursor()

    response = messagebox.askyesno('SYSTEM ALERT', 'Are you sure you want to Insert Data?')
    if response:
        try:
            sql = "insert into own_log(id,pass) values(%s,%s)"
            val = (name, reg)
            mycursor.execute(sql, val)
            mysqldb.commit()
        except EXCEPTION as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

        try:
            sql = "insert into vms_info(type,c_name,model,origin,capasity,color,name,reg,m_date,e_num,c_num,weight,r_date,b_from,price) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (
            type, c_name, model, origin, capasity, color, name, reg, m_date, e_num, c_num, weight, r_date, b_from,
            price)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("Information", "Record Successfully")
        except EXCEPTION as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")




root=Tk()
root.title("Insert")
root.configure(bg="#90EE90")

window_width,window_height=1000,700

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

canv = Canvas(root, width=1000, height=700, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("in11.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="\n Welcome To Khulna BRTA \n Vehicle Management System \nRegister A New Vehicle",font="Times 18 bold",bg="white").place(x=550,y=5)
#mylabel1.pack()

global e1
global e2
global e3
global e4
global e5
global e6
global e7
global e8
global e9
global e10
global e11
global e12
global e13
global e14
global e15

Label(root,text="Enter Vehicle Type",font="Times 13 bold",bg="white").place(x=530,y=120)
e1=Entry(root,font="Times 13 bold",bg="black",fg="white")
e1.place(x=750,y=120)
Label(root,text="Enter Company Name",font="Times 13 bold",bg="white").place(x=530,y=150)
e2=Entry(root,font="Times 13 bold",bg="black",fg="white")
e2.place(x=750,y=150)
Label(root,text="Enter Vehicle Model",font="Times 13 bold",bg="white").place(x=530,y=180)
e3=Entry(root,font="Times 13 bold",bg="black",fg="white")
e3.place(x=750,y=180)
Label(root,text="Enter Brand Origin",font="Times 13 bold",bg="white").place(x=530,y=210)
e4=Entry(root,font="Times 13 bold",bg="black",fg="white")
e4.place(x=750,y=210)
Label(root,text="Enter Seat Capacity",font="Times 13 bold",bg="white").place(x=530,y=240)
e5=Entry(root,font="Times 13 bold",bg="black",fg="white")
e5.place(x=750,y=240)
Label(root,text="Enter Vehicle Color",font="Times 13 bold",bg="white").place(x=530,y=270)
e6=Entry(root,font="Times 13 bold",bg="black",fg="white")
e6.place(x=750,y=270)
Label(root,text="Enter Owner Name",font="Times 13 bold",bg="white").place(x=530,y=300)
e7=Entry(root,font="Times 13 bold",bg="black",fg="white")
e7.place(x=750,y=300)
Label(root,text="Enter Registration Number",font="Times 13 bold",bg="white").place(x=530,y=330)
e8=Entry(root,font="Times 13 bold",bg="black",fg="white")
e8.place(x=750,y=330)
Label(root,text="Enter Manufacturer Date",font="Times 13 bold",bg="white").place(x=530,y=360)
e9=DateEntry(root,selectmode='day')
e9.place(x=750,y=360)
Label(root,text="Enter Engine Number",font="Times 13 bold",bg="white").place(x=530,y=390)
e10=Entry(root,font="Times 13 bold",bg="black",fg="white")
e10.place(x=750,y=390)
Label(root,text="Enter Chassis Number",font="Times 13 bold",bg="white").place(x=530,y=420)
e11=Entry(root,font="Times 13 bold",bg="black",fg="white")
e11.place(x=750,y=420)
Label(root,text="Enter Vehicle Weight",font="Times 13 bold",bg="white").place(x=530,y=450)
e12=Entry(root,font="Times 13 bold",bg="black",fg="white")
e12.place(x=750,y=450)
Label(root,text="Enter Date Of Registration",font="Times 13 bold",bg="white").place(x=530,y=480)
e13=DateEntry(root,selectmode='day')
e13.place(x=750,y=480)
Label(root,text="Buy From",font="Times 13 bold",bg="white").place(x=530,y=510)
e14=Entry(root,font="Times 13 bold",bg="black",fg="white")
e14.place(x=750,y=510)
Label(root,text="Vehicle Price",font="Times 13 bold",bg="white").place(x=530,y=540)
e15=Entry(root,font="Times 13 bold",bg="black",fg="white")
e15.place(x=750,y=540)

Button(root,text="SUBMIT",command=ok,height=4,width=18,bg="black",font="Times 13 bold",fg="white").place(x=750,y=590)

def log_out():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Log Out",command=log_out,height=2,width=7,bg="black",font="Times 13 bold",fg="white").place(x=890,y=5)

def back():
    root.destroy()
    call(["python", "emp_main.py"])


Button(root,text="Back",command=back,height=2,width=7,bg="black",font="Times 13 bold",fg="white").place(x=5,y=5)


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)
    e12.delete(0, END)
    e13.delete(0, END)
    e14.delete(0, END)
    e15.delete(0, END)

Button(root,text="clear",command=clear,height=4,width=18,bg="black",font="Times 13 bold",fg="white").place(x=530,y=590)

root.mainloop()