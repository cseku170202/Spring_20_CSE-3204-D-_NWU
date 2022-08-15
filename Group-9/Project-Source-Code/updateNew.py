import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['color_code'])
    e2.insert(0, select['color'])
    e3.insert(0, select['size'])
    e4.insert(0, select['quantity'])
    e5.insert(0, select['price'])


def update():
    color_code = e1.get()
    color = e2.get()
    size = e3.get()
    quantity = e4.get()
    price = e5.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="tsms")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  insertion set color= %s,size= %s,quantity= %s,price= %s where color_code= %s"
        val = (color, size, quantity,price,color_code)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updated successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    color_code = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="tsms")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from insertion where color_code = %s"
        val = (color_code,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Delete successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="tsms")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT color_code, color, size, quantity, price, image FROM insertion")
    records = mycursor.fetchall()
    print(records)

    for i, (color_code, color, size, quantity,price,image) in enumerate(records, start=1):
        listBox.insert("", "end", values=(color_code, color, size, quantity,price,image))
        mysqldb.close()


root = Tk()
root.geometry("1000x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Update and Delete Product", fg="red", font=(None, 15)).place(x=300, y=5)

tk.Label(root, text="Color Code").place(x=10, y=10)
Label(root, text="Color").place(x=10, y=40)
Label(root, text="Size").place(x=10, y=70)
Label(root, text="Quantity").place(x=10, y=100)
Label(root, text="Price").place(x=10, y=80)
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=140, y=130)

#Button(root, text="Add", command=Add, height=3, width=13).place(x=250, y=130)
Button(root, text="update", command=update, height=3, width=13).place(x=350, y=130)
Button(root, text="Delete", command=delete, height=3, width=13).place(x=450, y=130)

cols = ('color_code', 'color', 'size', 'quantity', 'price')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()