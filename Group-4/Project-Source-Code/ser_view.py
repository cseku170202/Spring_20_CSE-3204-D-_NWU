import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from subprocess import call

r = tk.Tk()
r.title("View Vehicle Details")
r.geometry("600x300")
r.configure(bg="#1D766E")

window_width, window_height = 1500, 400

screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

r.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')





tree = ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("xpnative")
s.configure(".", font=('Helvetic', 11))
s.configure("Treeview.Heading", foreground='red', font=('Helvetic', 11))

# define number of columns

tree["columns"] = ("type", "c_name", "model", "origin", "capasity", "color", "name", "reg", "m_date", "e_num", "c_num", "weight",
    "r_date", "b_from", "price")

# assign the width,minwidth and anchor to the respective columns
tree.column("type", width=50, minwidth=50, anchor=tk.CENTER)
tree.column("c_name", width=110, minwidth=50, anchor=tk.CENTER)
tree.column("model", width=50, minwidth=50, anchor=tk.CENTER)
tree.column("origin", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("capasity", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("color", width=50, minwidth=50, anchor=tk.CENTER)
tree.column("name", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("reg", width=70, minwidth=50, anchor=tk.CENTER)
tree.column("m_date", width=110, minwidth=50, anchor=tk.CENTER)
tree.column("e_num", width=150, minwidth=50, anchor=tk.CENTER)
tree.column("c_num", width=150, minwidth=50, anchor=tk.CENTER)
tree.column("weight", width=50, minwidth=50, anchor=tk.CENTER)
tree.column("r_date", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("b_from", width=70, minwidth=50, anchor=tk.CENTER)
tree.column("price", width=80, minwidth=50, anchor=tk.CENTER)

# assign to the heading name to the respective columns
tree.heading("type", text="Type", anchor=tk.CENTER)
tree.heading("c_name", text="Company name", anchor=tk.CENTER)
tree.heading("model", text="Model", anchor=tk.CENTER)
tree.heading("origin", text="Brand Origin", anchor=tk.CENTER)
tree.heading("capasity", text="Seat Capasity", anchor=tk.CENTER)
tree.heading("color", text="color", anchor=tk.CENTER)
tree.heading("name", text="Owner Name", anchor=tk.CENTER)
tree.heading("reg", text="Reg NO", anchor=tk.CENTER)
tree.heading("m_date", text="Manufact Date", anchor=tk.CENTER)
tree.heading("e_num", text="Engine Number", anchor=tk.CENTER)
tree.heading("c_num", text="Cassis Number", anchor=tk.CENTER)
tree.heading("weight", text="weight", anchor=tk.CENTER)
tree.heading("r_date", text="Reg Date", anchor=tk.CENTER)
tree.heading("b_from", text="Buy from", anchor=tk.CENTER)
tree.heading("price", text="Price", anchor=tk.CENTER)



hsb = ttk.Scrollbar(r, orient="horizontal")

hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

tree.pack()


Label(r, text="Enter Reg Number", font="Times 12 bold", bg="#1D766E").place(x=500, y=250)
global e1
e1 = Entry(r, font="Times 12 bold", bg="gray",fg="white")
e1.place(x=650, y=250)

def ok():
    reg = e1.get()
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
    conn = connect.cursor()
    conn.execute("select * from vms_info where reg=" + reg + "")

    i = 0
    for ro in conn:
        tree.insert('', i, text="", values=(
            ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10], ro[11], ro[12], ro[13],
            ro[14]))
        i = i + 1


Button(r, text="search", command=ok, height=2, width=10, font="Times 12 bold").place(x=850, y=240)


def log_out():
    r.destroy()
    call(["python", "main.py"])



Button(r, text="Log Out", command=log_out, height=2, width=7,  font="Times 12 bold").place(x=1420, y=5)


def back():
    r.destroy()
    call(["python", "ser_main.py"])



Button(r, text="Back", command=back, height=2, width=7, font="Times 12 bold").place(x=5, y=5)

r.mainloop()
