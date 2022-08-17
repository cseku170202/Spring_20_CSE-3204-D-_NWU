import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image
def Ok():
    global myresult
    studname = e1.get()
    coursename = e2.get()
    fee = e3.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="db")
    mycursor=mysqldb.cursor()

    try:
        mycursor.execute("SELECT * FROM record where id = '" + studname + "'")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        e2.delete(0, END)
        e2.insert(END, x[2])
        e3.delete(0, END)
        e3.insert(END, x[3])

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

root = Tk()
root.title("Details search")
frame = Frame(root)
frame.pack(pady=200,padx=200)
frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("aa.jpg"))
label = Label(frame, image = img)
label.pack()
root.geometry("800x500")
Label(root, text="Student ID",bg="White").place(x=260, y=10,width=200,height=40)
Button(root, text="Search", command=Ok ,bg="White",height = 1, width = 13).place(x=480, y=60,width=200,height=40)
Label(root, text="Course",bg="White").place(x=260, y=110,width=200,height=40)
Label(root, text="Fee",bg="White").place(x=260, y=160,width=200,height=40)
def Back():
    root.destroy()
Button(root, text="Back", command=Back,bg="White",height = 1, width = 13).place(x=480, y=300,width=200,height=40)

e1 = Entry(root)
e1.place(x=480, y=10,width=200,height=30)

e2 = Entry(root)
e2.place(x=480, y=110,width=200,height=30)

e3 = Entry(root)
e3.place(x=480, y=160,width=200,height=30)

root.mainloop()