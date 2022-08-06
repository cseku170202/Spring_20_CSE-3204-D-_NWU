import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from subprocess import call
from tkinter import messagebox

r = tk.Tk()
r.title("View vehicle case Details")
r.geometry("600x300")
r.configure(bg="#456179")

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

tree["columns"] = ("c_id", "c_det", "reg", "ser_id", "taka")

# assign the width,minwidth and anchor to the respective columns
tree.column("c_id", width=200, minwidth=50, anchor=tk.CENTER)
tree.column("c_det", width=500, minwidth=50, anchor=tk.CENTER)
tree.column("reg", width=150, minwidth=50, anchor=tk.CENTER)
tree.column("ser_id", width=200, minwidth=50, anchor=tk.CENTER)
tree.column("taka", width=200, minwidth=50, anchor=tk.CENTER)


# assign to the heading name to the respective columns
tree.heading("c_id", text="Case Id", anchor=tk.CENTER)
tree.heading("c_det", text="Case Details", anchor=tk.CENTER)
tree.heading("reg", text="Registration Number", anchor=tk.CENTER)
tree.heading("ser_id", text="Sergeant id", anchor=tk.CENTER)
tree.heading("taka", text="Fine Amount", anchor=tk.CENTER)



hsb = ttk.Scrollbar(r, orient="horizontal")

hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

tree.pack()


Label(r, text="Enter Reg Number", font="Times 12 bold", bg="#456179").place(x=200, y=250)
global e1
e1 = Entry(r, font="Times 12 bold", bg="gray",fg="white")
e1.place(x=350, y=250)



def log_out():
    r.destroy()
    call(["python", "main.py"])



Button(r, text="Log Out", command=log_out, height=2, width=7, font="Times 12 bold").place(x=1420, y=5)


def back():
    r.destroy()
    call(["python", "own_main.py"])



Button(r, text="Back", command=back, height=2, width=7, font="Times 12 bold").place(x=5, y=5)

def ok():
    reg = e1.get()
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
    conn = connect.cursor()
    conn.execute("select * from case_info where reg=" + reg + "")
    i = 0
    for ro in conn:
        tree.insert('', i, text="", values=(
            ro[0], ro[1], ro[2], ro[3], ro[4]))
        i = i + 1

Button(r, text="search", command=ok, height=2, width=10, font="Times 12 bold").place(x=550, y=240)

def Delete():
    if not tree.selection():
        messagebox.showwarning("Warning", "Select data to delete")
    else:
        result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                        icon="warning")
    if result == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        print(selecteditem[0])
        tree.delete(curItem)

Button(r, text="Temp Delete", command=Delete, height=2, width=10, font="Times 12 bold").place(x=680, y=240)
def cc():
    call(["python", "cal.py"])

Button(r, text="Open Calclutor", command=cc, height=2, width=14, font="Times 12 bold").place(x=50, y=240)

def okk():
    reg = e1.get()
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
    conn = connect.cursor()
    #z=conn.execute("select * from case_info where reg=" + reg + "")
    conn.execute("SELECT SUM(taka) AS Total_Fine_Ammount FROM case_info WHERE reg="+ reg +"")
    z=conn.fetchall()
    for i, in z:
        print(i, end="")
    print(type(i))
    t = str(i)
    print(t)
    print(t)
    print(type(t))
    Label(r,text="Total Fine:"+str(t)+"", font="Times 23 bold", bg="#456179").place(x=1100, y=240)

e5=Label(r, font="Times 12 bold", bg="#456179").place(x=500, y=350)
Button(r, text="Calculate Fine Ammount", command=okk, height=2, width=19, font="Times 12 bold").place(x=890, y=240)
r.mainloop()
