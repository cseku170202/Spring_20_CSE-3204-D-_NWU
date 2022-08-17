import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
from subprocess import call


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Id'])
    e2.insert(0, select['Student name'])
    e3.insert(0, select['Course'])
    e4.insert(0, select['Fee'])




def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="db")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO record (id,stname,course,fee) Values (%s,%s,%s,%s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Student inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        show()
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="db")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update record set stname= %s ,course = %s ,fee= %s where id= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updated successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        show()
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="db")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from record where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Delete successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        show()
        mysqldb.close()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="db")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,stname,course,fee FROM record")
    records = mycursor.fetchall()

    for row in listBox.get_children():
        listBox.delete(row)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()

def showcourse(coursename):
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="db")
    mycursor = mysqldb.cursor()
    print("SELECT id,stname,course,fee FROM record Where course ='" + str(coursename)+"'")
    mycursor.execute("SELECT id,stname,course,fee FROM record Where course ='" + str(coursename)+"'")

    records = mycursor.fetchall()

    for row in listBox.get_children():
        listBox.delete(row)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()







def search():
    coursename =e5.get()
    showcourse(coursename)






root = Tk()
root['bg']='Orange'
root.geometry("800x500")
root.title('Student Information')
global e1
global e2
global e3
global e4
global e5
global e6
tk.Label(root, text="Student Details", fg="green",bg="orange", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Student ID",bg="red").place(x=10, y=10)
Label(root, text="Student Name",bg="red").place(x=10, y=40)
Label(root, text="Course",bg="red").place(x=10, y=70)
Label(root, text="Fee",bg="red").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)
e5 = Entry(root)
e5.place(x=400, y=150)


Button(root, text="Add", command=Add, height=3,bg="green", width=13).place(x=30, y=130)
Button(root, text="update", command=update,bg="green", height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command=delete,bg="green", height=3, width=13).place(x=250, y=130)
Button(root, text="Search",command=search,bg="green",height=3, width=13).place(x=550, y=130)
def Back():
    root.destroy()
Button(root, text="Back",command=Back,bg="green",height=3, width=13).place(x=680, y=130)



cols = ('id', 'stname', 'course', 'fee')
listBox = ttk.Treeview(root, columns=cols, show='headings')
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

cols = ('Id', 'Student name', 'Course', 'Fee')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

listBox.bind('<Double-Button-1>', GetValue)

show()
root.mainloop()