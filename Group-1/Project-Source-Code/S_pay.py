from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.geometry("1300x700+0+0")


def pay():
    if var_pay.get() == "":
        messagebox.showerror("Error", "Enter amount", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update room set Total_Bill=%s, Paid_Amount=%s, Due_Amount=%s where Mobile_No=%s",
                (
                    var_total.get(),
                    var_paid.get(),
                    var_due.get(),
                    var_contact.get()
                ))

            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Bill has been updated.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def fetch_data():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from room")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for i in rows:
            table.insert("", END, value=i)

        conn.commit()
    conn.close()

def get_data(event):
    cursor_row = table.focus()
    content = table.item(cursor_row)
    row = content["values"]

    var_contact.set(row[0]),
    var_check_in.set(row[1]),
    var_check_out.set(row[2]),
    var_rm_avail.set(row[4]),
    var_total.set(row[7]),
    var_paid.set(row[8]),
    var_due.set(row[9])

def total():
    if var_contact.get() == "" and var_pay.get() == "":
        messagebox.showerror("Error", "Enter all information correctly", parent=root)
    else:
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        query = "select Total_Bill, Paid_Amount, Due_Amount from room where Mobile_No=%s"
        value = (var_contact.get(),)
        my_cursor.execute(query, value)
        row3 = my_cursor.fetchone()

        q1 = float(row3[0])
        q2 = float(row3[1])
        q4 = float(var_pay.get())

        q5 = float(q2+q4)
        q6 = float(q1 - q5)
        p = str("%.2f" % q5)
        d = str("%.2f" % q6)

        var_paid.set(p)
        var_due.set(d)

def search():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from room where " + str(var_search.get()) + " LIKE '%" + str(
        txt_search.get()) + "%'")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for i in rows:
            table.insert("", END, value=i)
        conn.commit()
        conn.close()
    else:
        messagebox.showinfo("Info", "No Customer Information", parent=root)

def home():
    root.destroy()
    call(["python", "S_home.py"])

def back():
    root.destroy()
    call(["python", "S_bk_room.py"])


var_contact = StringVar()
var_check_in = StringVar()
var_check_out = StringVar()
var_rm_avail = StringVar()
var_total = StringVar()
var_paid = StringVar()
var_due = StringVar()
var_pay = StringVar()
var_search = StringVar()
txt_search = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=1300, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=140, width=1300, height=600)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=90)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

home_btn = Button(btn_frame, width=15, text="Home", command=home, font=("times new roman", 15, "bold"), bg="black", fg="white")
home_btn.grid(row=1, column=0, pady=1)

lbl_title = Label(main_frame, text="Room Booking Details", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=1110, height=40)

lebelframeleft = LabelFrame(main_frame, text="Room Booking Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
lebelframeleft.place(x=195, y=40, width=450, height=350)

lbl_contact = Label(lebelframeleft, text="Customer Contact:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_contact.grid(row=0, column=0, sticky=W)
entry_contact = ttk.Entry(lebelframeleft, textvariable=var_contact, font=("Arial Narrow", 12), width=30)
entry_contact.grid(row=0, column=1, sticky=W)

lbl_check_in = Label(lebelframeleft, text="Check In Date:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_check_in.grid(row=1, column=0, sticky=W)
entry_check_in = ttk.Entry(lebelframeleft, textvariable=var_check_in, font=("Arial Narrow", 12), width=30)
entry_check_in.grid(row=1, column=1)

lbl_check_out = Label(lebelframeleft, text="Check Out Date:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_check_out.grid(row=2, column=0, sticky=W)
entry_check_out = ttk.Entry(lebelframeleft, textvariable=var_check_out, font=("Arial Narrow", 12), width=30)
entry_check_out.grid(row=2, column=1)

lbl_rm_avail = Label(lebelframeleft, text="Available Room:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm_avail.grid(row=3, column=0, sticky=W)
entry_rm_avail = ttk.Entry(lebelframeleft, textvariable=var_rm_avail, font=("Arial Narrow", 12), width=30, state="readonly")
entry_rm_avail.grid(row=3, column=1, sticky=W)

lbl_total = Label(lebelframeleft, text="Total Cost:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_total.grid(row=4, column=0, sticky=W)
entry_total = ttk.Entry(lebelframeleft, textvariable=var_total, font=("Arial Narrow", 12), width=30)
entry_total.grid(row=4, column=1)

lbl_paid = Label(lebelframeleft, text="Paid Amount:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_paid.grid(row=5, column=0, sticky=W)
entry_paid = ttk.Entry(lebelframeleft, textvariable=var_paid, font=("Arial Narrow", 12), width=30)
entry_paid.grid(row=5, column=1)

lbl_due = Label(lebelframeleft, text="Due Amount:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_due.grid(row=9, column=0, sticky=W)
entry_due = ttk.Entry(lebelframeleft, textvariable=var_due, font=("Arial Narrow", 12), width=30)
entry_due.grid(row=9, column=1)

lbl_p = Label(lebelframeleft, text="Pay:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_p.grid(row=10, column=0, sticky=W)
entry_p = ttk.Entry(lebelframeleft, textvariable=var_pay, font=("Arial Narrow", 12), width=30)
entry_p.grid(row=10, column=1)

bill_btn = Button(lebelframeleft, width=9, text="Bill", command=total, font=("times new roman", 13, "bold"), bg="black", fg="white")
bill_btn.grid(row=11, column=0, pady=1, padx=2)

pay_btn = Button(lebelframeleft, width=9, text="Pay", command=pay, font=("times new roman", 13, "bold"), bg="black", fg="white")
pay_btn.grid(row=11, column=1, pady=1, padx=2)

tableframe = LabelFrame(main_frame, text="View Details and Search System", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=650, y=40, width=630, height=320)

lbl_search = Label(tableframe, text="Search By:", font=("Arial Narrow", 12, "bold"), bg="yellow", fg="black")
lbl_search.grid(row=0, column=0, sticky=W, padx=2)

combo_search = ttk.Combobox(tableframe, textvariable=var_search, font=("Arial Narrow", 12), width=10, state="readonly")
combo_search["value"] = ("Mobile_No", "Room_No")
combo_search.grid(row=0, column=1, padx=2)

entry_search = ttk.Entry(tableframe, textvariable=txt_search, font=("Arial Narrow", 12), width=20)
entry_search.grid(row=0, column=2, padx=2)

search_btn = Button(tableframe, width=10, text="Search", command=search, font=("times new roman", 12, "bold"), bg="green")
search_btn.grid(row=0, column=3, padx=2)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=40, width=620, height=250)

show_btn = Button(main_frame, width=10, text="Show", command=fetch_data, font=("times new roman", 12, "bold"), bg="light green")
show_btn.place(x=900, y=380)

scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

table = ttk.Treeview(details_table, column=(
    "contact", "check_in", "check_out", "rm_type", "rm_avail", "meal", "days_no", "t_bill", "p_bill", "due"),
                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)

table.heading("contact", text="Mobile No.")
table.heading("check_in", text="Check In Date")
table.heading("check_out", text="Check Out Date")
table.heading("rm_type", text="Room Type")
table.heading("rm_avail", text="Room No.")
table.heading("meal", text="Meal")
table.heading("days_no", text="No. of Days")
table.heading("t_bill", text="Total Bill")
table.heading("p_bill", text="Paid Amount")
table.heading("due", text="Due Amount")

table["show"] = "headings"

table.column("contact", width=100)
table.column("check_in", width=100)
table.column("check_out", width=100)
table.column("rm_type", width=100)
table.column("rm_avail", width=100)
table.column("meal", width=100)
table.column("days_no", width=100)
table.column("t_bill", width=100)
table.column("p_bill", width=100)
table.column("due", width=100)

table.pack(fill=BOTH, expand=1)
table.bind("<ButtonRelease-1>", get_data)
fetch_data()


root.mainloop()
