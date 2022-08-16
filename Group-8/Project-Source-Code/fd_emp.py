import tkinter as tk
from tkinter import *
from tkinter import messagebox
from subprocess import call
import mysql.connector
from PIL import ImageTk, Image
import Image

def submit():
    global e1
    global e2
    global e3
    print('Name:{}'.format(e1.get()))
    print('Email:{}'.format(e2.get()))
    print('Comment:{}'.format(e3.get()))

    name = e1.get()
    mail = e2.get()
    com = e3.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
    mycursor = mysqldb.cursor()
    response = messagebox.askyesno('SYSTEM ALERT', 'Do you want to Insert Data?')
    if response:
        try:
            sql = "insert into emp_feed (`Name`, `email`, `Comments`) values(%s,%s,%s)"
            #"INSERT INTO `feedback` (`Name`, `email`, `Comments`) VALUES ('xgcbtgsd', 'sdfsvd', 'vsdgbfd')";
            val = (name, mail,com)
            mycursor.execute(sql, val)
            mysqldb.commit()
        except EXCEPTION as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")

    messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

def back():
    win.destroy()
    call(['python', "billing.py"])

win = Tk()
win.title("Employee Feedback")
win.geometry("800x533")

canv = Canvas(win, width=850, height=533, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rw.jpg"))
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(win, text="Employee Feedback",font='Times 27 bold',fg='#6D6875').place(x=255,y=5)
mylabel1=Label(win, text="'Please tell me what do you think'",font='Times 15 bold',fg='#B5838D').place(x=265,y=60)

global e1
global e2
global e3

Label(win, text="Name", font="80",width=15,height=2).place(x=120, y=95)
Label(win, text="Email", font="80",width=15,height=2).place(x=120, y=150)
Label(win, text="Comments", font="80",width=15,height=2).place(x=120, y=225)

e1 = Entry(win, font=100)
e1.place(x=320, y=105)

e2 = Entry(win, font=100)
e2.place(x=320, y=160)

e3 = Entry(win, font=100)
e3.place(x=320, y=235)

Button(win, text="Submit",  width=10,font=('vardana',17,'bold'), bd=10, padx=5, pady=5,command=submit).place(x=280,y=300)
Button(win, font=('vardana', 16, 'bold'), text="Clear", bd=10, padx=5,pady=5, width=10, command=clear).place(x=500, y=300)
Button(win, font=('vardana', 16, 'bold'), text="Back",padx=9,pady=9, width=10, command=back).place(x=0,y=0)

win.mainloop()