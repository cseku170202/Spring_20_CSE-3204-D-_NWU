import mysql.connector
from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image

root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='gray'
root.geometry("800x500")

def run_program1():
    root.destroy()
    subprocess.call(["python", "main.py"])

def ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root",password="",database="tsms")
    mycursor = mysqldb.cursor()
    user_id = UserID_entry.get()
    password=Password_entry.get()


    sql = "select * from login_admin where user_id = %s and password = %s"
    mycursor.execute(sql, [(user_id), (password)])
    results= mycursor.fetchall()
    if results:
        messagebox.showinfo("","Login Success")
        root.destroy()
        subprocess.call(["python", "admin_section.py"])
        return True

    else :
        messagebox.showinfo("", "Incorrect Username and Password")
        return False


#label
Label(root,text="Admin Login",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=420,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('admin_background.jpg')
image1.thumbnail((505, 605))

i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

Label(root,text="User ID:",font="20").place(x=470,y=82)
Label(root,text="Password:",font="20").place(x=470,y=152)

#Entry
UserID_entry=Entry(root,font="10",bd=4)
UserID_entry.place(x=570,y=80)
Password_entry=Entry(root,font="10",bd=4)
Password_entry.place(x=570,y=150)
Password_entry.config(show="*")


#Button
Button(root,text="Login",command=ok,font="ariel 20 bold").place(x=540,y=255)
Button(root,text="Back",command=run_program1,font="ariel 20 bold").place(x=680,y=255)
root.mainloop()