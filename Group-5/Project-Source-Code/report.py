import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image


def Ok():
    global myresult
    STUDID = e1.get()
    year = e2.get()
    semister = e3.get()
    Grade = e4.get()


    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="db")
    mycursor = mysqldb.cursor()

    try:
        mycursor.execute("SELECT * FROM students where STUDID  = '" + STUDID + "'")
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        e2.delete(0, END)
        e2.insert(END, x[2])
        e3.delete(0, END)
        e3.insert(END, x[3])
        e4.delete(0, END)
        e4.insert(END, x[4])



    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


root = Tk()
root.title("Search Mysql")
frame = Frame(root)
frame.pack(pady=200, padx=200)
frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("book-863418_960_720.webp"))
label = Label(frame, image=img)
label.pack()
root.geometry("800x500")
Label(root, text="Student ID", bg="red").place(x=260, y=10)
Button(root, text="Search", command=Ok, bg="red", height=1, width=13).place(x=340, y=40)
Label(root, text="Year", bg="red").place(x=260, y=80)
Label(root, text="Grade", bg="red").place(x=260, y=120)
Label(root, text="CGPA", bg="red").place(x=260, y=150)
def Back():
    call(["python", "stu details.py"])
Button(root, text="Back", command=Back,bg="White",height = 1, width = 13).place(x=480, y=300,width=200,height=40)


e1 = Entry(root)
e1.place(x=340, y=10)

e2 = Entry(root)
e2.place(x=340, y=80)

e3 = Entry(root)
e3.place(x=340, y=120)
e4 = Entry(root)
e4.place(x=340, y=150)

root.mainloop()