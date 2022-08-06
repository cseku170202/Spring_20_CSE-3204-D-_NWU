import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call

def delete():
    reg=e1.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root", password="",database="vms")
    mycursor=mysqldb.cursor()
    response = messagebox.askyesno('SYSTEM ALERT', 'Are you sure to Delete Info?')
    if response:
        try:
            sql = "DELETE FROM vms_info WHERE reg =" + reg + ""
            mycursor.execute(sql)
            mysqldb.commit()
            messagebox.showinfo("information", "Record deleted Successfully")

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")
    e1.delete(0, END)

root=Tk()
root.title("Delete")
root.configure(bg="#E6EFF0")

window_width,window_height=600,400

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

mylabel1=Label(root, text="\n Welcome To Khulna BRTA \n Vehicle Management System \n\n\n Delete Vehicle Information",font="Times 14 bold",bg="#E6EFF0")
mylabel1.pack()

global e1

Label(root,text="Enter Registration Number:",font="Times 14 bold",bg="#E6EFF0").place(x=50,y=200)
e1=Entry(root,font="Times 14 bold",bg="gray",fg="white")
e1.place(x=300,y=200)


Button(root,text="Delete",command=delete,height=2,width=9,bg="#738D8F",font="Times 14 bold",fg="white").place(x=240,y=240)

def log_out():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Log Out",command=log_out,height=2,width=7,bg="#738D8F",font="Times 14 bold").place(x=510,y=5)

def back():
    root.destroy()
    call(["python", "emp_main.py"])


Button(root,text="Back",command=back,height=2,width=7,bg="#738D8F",font="Times 14 bold").place(x=5,y=5)


root.mainloop()