import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image
import Image

def exit():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
   if response:
      root.destroy()
      #call(['python', "main.py"])

   else:
      messagebox.showinfo("SYSTEM ALERT", "Canceled")

def back():
    root.destroy()
    call(['python', "main.py"])

def ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
    mycursor = mysqldb.cursor()
    e_id = e1.get()
    e_pass = e2.get()

    sql = "select * from log_in where id = %s and pass = %s"
    mycursor.execute(sql, [(e_id), (e_pass)])
    results = mycursor.fetchall()
    if results:
        root.destroy()
        call(['python', "billing.py"])
        return True

    else:
        messagebox.showinfo("", "incorrect username and password")
        return False

root = Tk()
root.title(" Employee login")
root.configure(bg="#F0FFF0")
root.geometry('950x975')
canv = Canvas(root, width=1850, height=1375, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rb2.webp"))
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="Employee LogIn",font='Times 35 bold',bg="black",fg="White").place(x=285,y=10)
root.configure(bg="pink")
root.geometry('950x975')

global e1
global e2

Label(root, text="Enter Username", font="80",bg="black",fg="White",width=15,height=2).place(x=50, y=120)
Label(root, text="Enter password", font="80",bg="black",fg="White",width=15,height=2).place(x=50, y=200)

e1 = Entry(root, font=60)
e1.place(x=280, y=120)

e2 = Entry(root, font="60")
e2.place(x=280, y=200)
e2.config(show="*")

Button(root, text="Log in", command=ok, width=10, bg="black", fg="white", font=('vardana',17,'bold'), bd=10, padx=5, pady=5).place(x=100,y=300)
Button(root, font=('vardana', 16, 'bold'), text="Back", bg="black", fg="white", bd=10, padx=10,pady=10, width=10, command=back).place(x=310,y=300)
Button(root, font=('vardana', 16, 'bold'), text="Exit", bg="black", fg="white", bd=10, padx=10,pady=10, width=10, command=exit).place(x=230, y=400)

root.mainloop()