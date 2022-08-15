import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess
from PIL import ImageTk, Image

root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='gray'
root.geometry("1000x600")

def run_program():
    root.destroy()
    subprocess.call(["python", "admin_section.py"])

def comboFunction(event):
    print(combo1.get())

def ok():
    color_code = combo1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root",password="",database="tsms")
    mycursor = mysqldb.cursor()
    mycursor.execute("select * from insertion where color_code="+color_code)

    tree = ttk.Treeview(root)
    tree['show'] = 'headings'


    s = ttk.Style(root)
    s.theme_use("xpnative")
    s.configure(".", font=('Helvetic', 11))
    s.configure("Treeview.Heading", foreground='blue', font=('Helvetic', 11))

    # define number of columns
    tree["columns"] = ("color_code", "color", "size", "quantity", "price")

    # assign the width,minwidth and anchor to the respective columns
    tree.column("color_code", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("color", width=110, minwidth=50, anchor=tk.CENTER)
    tree.column("size", width=100, minwidth=100, anchor=tk.CENTER)
    tree.column("quantity", width=100, minwidth=50, anchor=tk.CENTER)
    tree.column("price", width=100, minwidth=50, anchor=tk.CENTER)


    # assign to the heading name to the respective columns
    tree.heading("color_code", text="Color Code", anchor=tk.CENTER)
    tree.heading("color", text="Color", anchor=tk.CENTER)
    tree.heading("size", text="Size", anchor=tk.CENTER)
    tree.heading("quantity", text="Quantity", anchor=tk.CENTER)
    tree.heading("price", text="Price", anchor=tk.CENTER)


    i = 0
    for ro in mycursor:
        tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4]))
        i = i + 1

    hsb = ttk.Scrollbar(root, orient="horizontal")

    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    # tree.pack(padx=40,pady=40)
    tree.place(x=40,y=40)


    #subprocess.call(["python", "admin_section.py"])
def run_program3():
    root.destroy()
    subprocess.call(["python", "show.py"])

#label
Label(root,text="Show Data",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('show2.jpg')
image1.thumbnail((820, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

Label(root,text="Enter Color Code:",font="5").place(x=820,y=76)
combo1 = ttk.Combobox(root,values=["1","2","3","4"],height=25,width=25)
# combo1.pack(padx=20,pady=40)
combo1.place(x=820,y=120)

combo1.set("Select Color Code")
combo1.bind('<<ComboboxSelected>>',comboFunction)

#Button
Button(root,text="Search",command=ok ,font="20").place(x=850,y=200)
Button(root,text="Back",command=run_program,font="20").place(x=900,y=500)
Button(root,text="For Update & Delete",command=run_program3,font="20").place(x=820,y=350)
root.mainloop()