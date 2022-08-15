from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from subprocess import call
from tkcalendar import DateEntry


root = Tk()
root.title("Hotel Management System")
root.geometry("1300x700+0+0")


def fetch_contact():
    if var_contact.get() == "":
        messagebox.showerror("Error", "Enter contact number", parent=root)
    else:
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        query = "select Name from customer where Mobile_No=%s"
        value = (var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "No customer with this contact number", parent=root)
        else:
            conn.commit()
            conn.close()

            showdataframe = Frame(root, bd=2, relief=RIDGE)
            showdataframe.place(x=640, y=500, width=280, height=180)

            lbl_nm = Label(showdataframe, text="Name:", font=("Arial Narrow", 12, "bold"))
            lbl_nm.grid(row=0, column=0)

            lbl1 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl1.grid(row=0, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Gender from customer where Mobile_No=%s"
            value = (var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_gnd = Label(showdataframe, text="Gender:", font=("Arial Narrow", 12, "bold"))
            lbl_gnd.grid(row=1, column=0)

            lbl2 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl2.grid(row=1, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Email from customer where Mobile_No=%s"
            value = (var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_mail = Label(showdataframe, text="E-mail:", font=("Arial Narrow", 12, "bold"))
            lbl_mail.grid(row=2, column=0)

            lbl3 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl3.grid(row=2, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Nationality from customer where Mobile_No=%s"
            value = (var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_nationality = Label(showdataframe, text="Nationality:", font=("Arial Narrow", 12, "bold"))
            lbl_nationality.grid(row=3, column=0)

            lbl4 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl4.grid(row=3, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select ID_Number from customer where Mobile_No=%s"
            value = (var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_id_num = Label(showdataframe, text="ID_Number:", font=("Arial Narrow", 12, "bold"))
            lbl_id_num.grid(row=4, column=0)

            lbl5 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl5.grid(row=4, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Address from customer where Mobile_No=%s"
            value = (var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_address = Label(showdataframe, text="Address:", font=("Arial Narrow", 12, "bold"))
            lbl_address.grid(row=5, column=0)

            lbl6 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl6.grid(row=5, column=1)

def fetch_data():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from room")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Room_details_table.delete(*Room_details_table.get_children())
        for i in rows:
            Room_details_table.insert("", END, value=i)

        conn.commit()
    conn.close()

def get_data(event):
    cursor_row = Room_details_table.focus()
    content = Room_details_table.item(cursor_row)
    row = content["values"]

    var_contact.set(row[0]),
    var_check_in.set(row[1]),
    var_check_out.set(row[2]),
    var_rm_type.set(row[3]),
    var_rm_avail.set(row[4]),
    var_meal.set(row[5]),
    var_days_no.set(row[6])

def update_data():
    if var_contact.get() == "":
        messagebox.showerror("Error", "Enter the contact no", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update room set Check_In_Date=%s, Check_Out_Date=%s, Room_Type=%s, Room_No=%s, Meal=%s, Days_Number=%s, Total_Bill=%s, Paid_Amount='0', Due_Amount=%s, Status='Checked In' where Mobile_No=%s",
                (
                    var_check_in.get(),
                    var_check_out.get(),
                    var_rm_type.get(),
                    var_rm_avail.get(),
                    var_meal.get(),
                    var_days_no.get(),
                    var_total.get(),
                    var_due.get(),
                    var_contact.get()
                ))

            conn.commit()
            fetch_data()
            conn.close()

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            q = ("update details set Available='No' where Room_No=%s")
            v = (var_rm_avail.get(),)
            my_cursor.execute(q, v)

            conn.commit()
            fetch_data()
            conn.close()

            messagebox.showinfo("Update", "Booking details has been updated.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def delete_data():
    if var_contact.get() == "":
        messagebox.showerror("Error", "Enter information", parent=root)
    else:
        try:
            delete = messagebox.askyesno("HMS", "Do you really want to delete the information of this customer?", parent=root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = "delete from customer where Mobile_No = %s"
                value = (var_contact.get(),)
                my_cursor.execute(query, value)

                query = "delete from room where Mobile_No=%s"
                value = (var_contact.get(),)
                my_cursor.execute(query, value)

                conn.commit()
                fetch_data()
                conn.close()

                messagebox.showinfo("Delete", "Customer details has been deleted.", parent=root)

            else:
                if not delete:
                    return

        except mysql.connector as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def reset():
    var_contact.set(""),
    var_check_in.set(""),
    var_check_out.set(""),
    var_rm_type.set(""),
    var_rm_avail.set(""),
    var_meal.set(""),
    var_days_no.set(""),
    var_sub_total.set(""),
    var_tax.set(""),
    var_total.set("")

def total():
    indate = var_check_in.get()
    outdate = var_check_out.get()
    indt = datetime.strptime(indate, "%d/%m/%Y")
    outdt = datetime.strptime(outdate, "%d/%m/%Y")
    var_days_no.set(abs(outdt - indt).days)

    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    query = "select Price from details where Room_No=%s"
    value = (var_rm_avail.get(),)
    my_cursor.execute(query,value)
    rows = my_cursor.fetchone()

    q1 = float(rows[0])
    q2 = float(var_days_no.get())

    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    query = "select Price from details_meal where Meal_Type=%s"
    value = (var_meal.get(),)
    my_cursor.execute(query, value)
    row4 = my_cursor.fetchone()

    q3 = float(row4[0])

    q4 = float(q1+q3)
    q5 = float(q4 * q2)
    st = str("%.2f" % q5)
    tax = str("%.2f" % (q5 * 0.01))
    total = str("%.2f " % (q5 + (q5 * 0.01)))
    var_sub_total.set(st)
    var_tax.set(tax)
    var_total.set(total)
    var_due.set(total)

def search():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from room where " + str(var_search.get()) + " LIKE '%" + str(
        txt_search.get()) + "%'")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Room_details_table.delete(*Room_details_table.get_children())
        for i in rows:
            Room_details_table.insert("", END, value=i)
        conn.commit()
        conn.close()

    else:
        messagebox.showinfo("Info", "No Customer Information", parent=root)

def search_rm():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    query = "select Room_No from details where Available='Yes' and Room_Type= %s "
    value = (var_rm_type.get(),)
    my_cursor.execute(query, value)
    # my_cursor.execute("select Room_No from details")
    row2 = my_cursor.fetchall()

    if len(row2) > 0:
        combo_rm_avail = ttk.Combobox(lebelframeleft, textvariable=var_rm_avail, font=("Arial Narrow", 12), width=28, state="readonly")
        combo_rm_avail["value"] = row2
        combo_rm_avail.grid(row=4, column=1)

        conn.commit()
        conn.close()

    else:
        combo_rm_avail = ttk.Combobox(lebelframeleft, textvariable=var_rm_avail, font=("Arial Narrow", 12), width=28, state="readonly")
        combo_rm_avail["value"] = ("No_room_available")
        combo_rm_avail.grid(row=4, column=1)

        conn.commit()
        conn.close()

def Bill():
    root.destroy()
    call(["python", "S_pay.py"])

def back():
    root.destroy()
    call(["python", "S_cust.py"])


var_contact = StringVar()
var_check_in = StringVar()
var_check_out = StringVar()
var_rm_type = StringVar()
var_rm_avail = StringVar()
var_meal = StringVar()
var_days_no = StringVar()
var_sub_total = StringVar()
var_tax = StringVar()
var_total = StringVar()
var_paid = StringVar()
var_due = StringVar()
var_status = StringVar()
var_search = StringVar()
txt_search = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=1300, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=140, width=1300, height=600)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=50)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

lbl_title = Label(main_frame, text="Room Booking Details", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=1110, height=40)

lebelframeleft = LabelFrame(main_frame, text="Room Booking Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
lebelframeleft.place(x=195, y=40, width=450, height=440)

lbl_contact = Label(lebelframeleft, text="Customer Contact:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_contact.grid(row=0, column=0, sticky=W)
entry_contact = ttk.Entry(lebelframeleft, textvariable=var_contact, font=("Arial Narrow", 12), width=22)
entry_contact.grid(row=0, column=1, sticky=W)

fetch_btn = Button(lebelframeleft, width=9, command=fetch_contact, text="Fetch Data", font=("times new roman", 11), bg="black", fg="white")
fetch_btn.place(x=360, y=3)

lbl_check_in = Label(lebelframeleft, text="Check In Date:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_check_in.grid(row=1, column=0, sticky=W)
entry_check_in = DateEntry(lebelframeleft, selectmode='day', date_pattern='dd/mm/yyyy', textvariable=var_check_in, font=("Arial Narrow", 12), width=28)
entry_check_in.grid(row=1, column=1)

lbl_check_out = Label(lebelframeleft, text="Check Out Date:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_check_out.grid(row=2, column=0, sticky=W)
entry_check_out = DateEntry(lebelframeleft, selectmode='day', date_pattern='dd/mm/yyyy',  textvariable=var_check_out, font=("Arial Narrow", 12), width=28)
entry_check_out.grid(row=2, column=1)

lbl_rm_type = Label(lebelframeleft, text="Room Type:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm_type.grid(row=3, column=0, sticky=W)

conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
my_cursor = conn.cursor()
my_cursor.execute("select Room_Type from details GROUP BY Room_Type")
row1 = my_cursor.fetchall()

combo_rm_type = ttk.Combobox(lebelframeleft, textvariable=var_rm_type, font=("Arial Narrow", 12), width=18, state="readonly")
combo_rm_type["value"] = row1
combo_rm_type.grid(row=3, column=1, sticky=W)

fetch_btn = Button(lebelframeleft, width=12, command=search_rm, text="Room Available", font=("times new roman", 10), bg="black", fg="white")
fetch_btn.place(x=347, y=100)

lbl_rm_avail = Label(lebelframeleft, text="Available Room:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm_avail.grid(row=4, column=0, sticky=W)

combo_rm_avail = ttk.Combobox(lebelframeleft, textvariable=var_rm_avail, font=("Arial Narrow", 12), width=28, state="readonly")
combo_rm_avail.grid(row=4, column=1)

lbl_meal = Label(lebelframeleft, text="Meal:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_meal.grid(row=5, column=0, sticky=W)
combo_meal = ttk.Combobox(lebelframeleft, textvariable=var_meal, font=("Arial Narrow", 12), width=28, state="readonly")
combo_meal["value"] = ("One Meal", "Two Meal", "Three Meal", "None")
combo_meal.grid(row=5, column=1)

lbl_days_no = Label(lebelframeleft, text="No. of Days:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_days_no.grid(row=6, column=0, sticky=W)
entry_days_no = ttk.Entry(lebelframeleft, textvariable=var_days_no, font=("Arial Narrow", 12), width=30)
entry_days_no.grid(row=6, column=1)

lbl_sub_total = Label(lebelframeleft, text="Sub Total:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_sub_total.grid(row=8, column=0, sticky=W)
entry_sub_total = ttk.Entry(lebelframeleft, textvariable=var_sub_total, font=("Arial Narrow", 12), width=30)
entry_sub_total.grid(row=8, column=1)

lbl_tax = Label(lebelframeleft, text="Tax:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_tax.grid(row=7, column=0, sticky=W)
entry_tax = ttk.Entry(lebelframeleft, textvariable=var_tax, font=("Arial Narrow", 12), width=30)
entry_tax.grid(row=7, column=1)

lbl_total = Label(lebelframeleft, text="Total Cost:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_total.grid(row=9, column=0, sticky=W)
entry_total = ttk.Entry(lebelframeleft, textvariable=var_total, font=("Arial Narrow", 12), width=30)
entry_total.grid(row=9, column=1)

btn_frame = Frame(lebelframeleft, relief=RIDGE)
btn_frame.place(x=10, y=355, width=415, height=48)

bill_btn = Button(btn_frame, width=9, text="Bill", command=total, font=("times new roman", 13, "bold"), bg="black", fg="white")
bill_btn.grid(row=0, column=0, pady=5, padx=2)

update_btn = Button(btn_frame, width=9, text="UPDATE", command=update_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
update_btn.grid(row=0, column=1, pady=5, padx=2)

delete_btn = Button(btn_frame, width=9, text="Delete", command=delete_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
delete_btn.grid(row=0, column=2, pady=5, padx=2)

reset_btn = Button(btn_frame, width=9, text="RESET", command=reset, font=("times new roman", 13, "bold"), bg="black", fg="white")
reset_btn.grid(row=0, column=3, pady=5, padx=2)

pay_btn = Button(main_frame, width=9, text="Pay Bill", command=Bill, font=("times new roman", 13, "bold"), bg="black", fg="white")
pay_btn.place(x=320, y=490, width=200, height=30)

tableframe = LabelFrame(main_frame, text="View Details and Search System", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=650, y=40, width=630, height=320)

lbl_search = Label(tableframe, text="Search By:", font=("Arial Narrow", 12, "bold"), bg="yellow", fg="black")
lbl_search.grid(row=0, column=0, sticky=W, padx=2)

combo_search = ttk.Combobox(tableframe, textvariable=var_search, font=("Arial Narrow", 12), width=10, state="readonly")
combo_search["value"] = ("Mobile_No", "Room_No", "Status")
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

Room_details_table = ttk.Treeview(details_table, column=(
    "contact", "check_in", "check_out", "rm_type", "rm_avail", "meal", "days_no", "t_bill", "p_bill", "due", "status"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=Room_details_table.xview)
scroll_y.config(command=Room_details_table.yview)

Room_details_table.heading("contact", text="Mobile No.")
Room_details_table.heading("check_in", text="Check In Date")
Room_details_table.heading("check_out", text="Check Out Date")
Room_details_table.heading("rm_type", text="Room Type")
Room_details_table.heading("rm_avail", text="Room No.")
Room_details_table.heading("meal", text="Meal")
Room_details_table.heading("days_no", text="No. of Days")
Room_details_table.heading("t_bill", text="Total Bill")
Room_details_table.heading("p_bill", text="Paid Amount")
Room_details_table.heading("due", text="Due Amount")
Room_details_table.heading("status", text="Status")

Room_details_table["show"] = "headings"

Room_details_table.column("contact", width=100)
Room_details_table.column("check_in", width=100)
Room_details_table.column("check_out", width=100)
Room_details_table.column("rm_type", width=100)
Room_details_table.column("rm_avail", width=100)
Room_details_table.column("meal", width=100)
Room_details_table.column("days_no", width=100)
Room_details_table.column("t_bill", width=100)
Room_details_table.column("p_bill", width=100)
Room_details_table.column("due", width=100)
Room_details_table.column("status", width=100)

Room_details_table.pack(fill=BOTH, expand=1)
Room_details_table.bind("<ButtonRelease-1>", get_data)
fetch_data()


root.mainloop()
