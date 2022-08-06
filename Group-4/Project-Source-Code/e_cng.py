import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image

def update():
    reg=e1.get()
    name=e2.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root", password="",database="vms")
    mycursor=mysqldb.cursor()
    response = messagebox.askyesno('SYSTEM ALERT', 'Are you sure you want to Change Name?')
    if response:
        try:
            sql = "update vms_info set name= %s where reg=%s"
            val = (name, reg)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("information", "Record Updated Successfully")

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")

    e1.delete(0, END)
    e2.delete(0, END)


root=Tk()
root.title("Update")
root.configure(bg="#E6EFF0")

window_width,window_height=650,450

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
canv = Canvas(root, width=650, height=450,)
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("cng11.png"))  # PIL solution
canv.create_image(0,150, anchor=NW, image=img)


mylabel1=Label(root, text="\n Welcome To Khulna BRTA \n Vehicle Management System \n\n\n Owner Name Change",font="Times 14 bold",bg="#E6EFF0").place(x=270,y=5)
#mylabel1.pack()

global e1
global e2

Label(root,text="Enter Registration Number:",font="Times 14 bold",bg="#E6EFF0").place(x=220,y=180)
e1=Entry(root,bg="gray",font="Times 14 bold",fg="white")
e1.place(x=450,y=180)

Label(root,text="Enter New Owner Name:",font="Times 14 bold",bg="#E6EFF0").place(x=220,y=240)
e2=Entry(root,bg="gray",font="Times 14 bold",fg="white")
e2.place(x=450,y=240)


Button(root,text="Change",command=update,height=2,width=9,bg="#B4CACB",font="Times 14 bold").place(x=280,y=300)

def log_out():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Log Out",command=log_out,height=2,width=7,bg="#B4CACB",font="Times 14 bold").place(x=540,y=5)

def back():
    root.destroy()
    call(["python", "emp_main.py"])


Button(root,text="Back",command=back,height=2,width=7,bg="#B4CACB",font="Times 14 bold").place(x=5,y=5)

root.mainloop()