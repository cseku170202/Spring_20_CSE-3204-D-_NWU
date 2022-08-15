# pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import subprocess

# connection for phpmyadmin
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='tsms',
    )
    return conn


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)


root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='skyblue'
root.geometry("1080x720")



my_tree = ttk.Treeview(root)

# placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()


# placeholder set value function
def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM insertion")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def back():
    root.destroy()
    subprocess.call(["python", "admin_section.py"])


def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM insertion WHERE color_code='" + str(deleteData) + "'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()


def select():
    try:
        selected_item = my_tree.selection()[0]
        color_code = str(my_tree.item(selected_item)['values'][0])
        color = str(my_tree.item(selected_item)['values'][1])
        size = str(my_tree.item(selected_item)['values'][2])
        quantity = str(my_tree.item(selected_item)['values'][3])
        price = str(my_tree.item(selected_item)['values'][4])

        setph(color_code, 1)
        setph(color, 2)
        setph(size, 3)
        setph(quantity, 4)
        setph(price, 5)
    except:
        messagebox.showinfo("Error", "Please select a data row")




def update():
    selectedcolor_code = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedcolor_code = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    color_code = str(color_codeEntry.get())
    color = str(colorEntry.get())
    size = str(sizeEntry.get())
    quantity = str(quantityEntry.get())
    price = str(priceEntry.get())

    if (color_code== "" or color_code== " ") or (color== "" or color== " ") or (size== "" or size== " ") or (quantity== "" or quantity== " ") or (price== "" or price== " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE insertion SET color_code='" +
                           color_code + "' , color='" +
                           color + "' , size='" +
                           size + "' , quantity='" +
                           quantity + "' , price='" +
                           price + "' WHERE color_code='" +
                           selectedcolor_code + "' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "code already exist")
            return

    refreshTable()


label = Label(root, text="Product Information", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

color_codeLabel = Label(root, text="Color code", font=('Arial', 15))
colorLabel = Label(root, text="Color", font=('Arial', 15))
sizeLabel = Label(root, text="Size", font=('Arial', 15))
quantityLabel = Label(root, text="Quantity", font=('Arial', 15))
priceLabel = Label(root, text="Price", font=('Arial', 15))

color_codeLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
colorLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
sizeLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
quantityLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
priceLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

color_codeEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph1)
colorEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph2)
sizeEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph3)
quantityEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph4)
priceEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)

color_codeEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
colorEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
sizeEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
quantityEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
priceEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

backBtn = Button(
    root, text="Back", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=back)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=select)
'''resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)'''

updateBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
#searchBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
#resetBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
backBtn.grid(row=15, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("color_code", "color", "size", "quantity", "price")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("color_code", anchor=W, width=170)
my_tree.column("color", anchor=W, width=150)
my_tree.column("size", anchor=W, width=150)
my_tree.column("quantity", anchor=W, width=165)
my_tree.column("price", anchor=W, width=150)

my_tree.heading("color_code", text="color code", anchor=W)
my_tree.heading("color", text="color", anchor=W)
my_tree.heading("size", text="size", anchor=W)
my_tree.heading("quantity", text="quantity", anchor=W)
my_tree.heading("price", text="price", anchor=W)

refreshTable()

root.mainloop()