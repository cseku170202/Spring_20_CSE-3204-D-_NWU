import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image


def ok():
    c_det=e2.get()
    reg=e3.get()
    ser_id=e4.get()
    taka=e5.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
    mycursor = mysqldb.cursor()

    response = messagebox.askyesno('SYSTEM ALERT', 'Are you sure you want to INSERT?')
    if response:
        try:
            sql = "insert into case_info(c_det,reg,ser_id,taka) values(%s,%s,%s,%s)"
            val = (c_det, reg, ser_id, taka)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("Information", "Case Record Successfully")
        except EXCEPTION as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")


root=Tk()
root.title("New Case File")
root.configure(bg="#A6B5D3")

window_width,window_height=800,380
root.resizable(False, False)
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')



canv = Canvas(root, width=400, height=380, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("cas1.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)



mylabel1=Label(root, text="\n Welcome To Khulna BRTA \n Vehicle Management System \n\n\nSergent New Case File",font='Times 12 bold',bg="#A6B5D3").place(x=450,y=0)
#mylabel1.pack()

global e2
global e3
global e4
global e5


Label(root,text="Enter Case Details",font="Times 12 bold",bg="#A6B5D3").place(x=420,y=150)
e2=Entry(root,font="Times 12 bold",bg="gray",fg="white")
e2.place(x=600,y=150)
Label(root,text="Enter Reg Number",font="Times 12 bold",bg="#A6B5D3").place(x=420,y=180)
e3=Entry(root,font="Times 12 bold",bg="gray",fg="white")
e3.place(x=600,y=180)
Label(root,text="Enter Sergeant Id",font="Times 12 bold",bg="#A6B5D3").place(x=420,y=210)
e4=Entry(root,font="Times 12 bold",bg="gray",fg="white")
e4.place(x=600,y=210)
Label(root,text="Enter Amount",font="Times 12 bold",bg="#A6B5D3").place(x=420,y=240)
e5=Entry(root,font="Times 12 bold",bg="gray",fg="white")
e5.place(x=600,y=240)


Button(root,text="SUBMIT",command=ok,height=3,width=12,bg="#BCCFC9",font='Times 11 bold').place(x=600,y=300)

def log_out():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Log Out",command=log_out,height=2,width=7,bg="#BCCFC9",font='Times 11 bold').place(x=700,y=5)

def back():
    root.destroy()
    call(["python", "ser_main.py"])


Button(root,text="Back",command=back,height=2,width=7,bg="#BCCFC9",font='Times 11 bold').place(x=5,y=5)


def clear():
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

Button(root,text="clear",command=clear,height=3,width=12,bg="#BCCFC9",font='Times 11 bold').place(x=429,y=300)


root.mainloop()