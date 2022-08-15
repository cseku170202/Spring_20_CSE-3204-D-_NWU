from tkinter import *
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("1300x1000+0+0")


def add_data():
    if var_mobile.get() == "" or var_nm.get() == "":
        messagebox.showerror("Error", "Enter all information correctly", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                var_ref.get(),
                var_nm.get(),
                var_age.get(),
                var_gnd.get(),
                var_post_code.get(),
                var_mobile.get(),
                var_email.get(),
                var_nationality.get(),
                var_id_proof.get(),
                var_id_num.get(),
                var_address.get()
            ))

            conn.commit()
            fetch_data()
            conn.close()

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            q = ("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            v = (var_mobile.get(), "", "", "", "", "", "", "", "", "", "")
            my_cursor.execute(q, v)

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Customer data has been added.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def fetch_data():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from customer")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Cust_details_table.delete(*Cust_details_table.get_children())
        for i in rows:
            Cust_details_table.insert("", END, value=i)

        conn.commit()
    conn.close()

def get_data(event):
    cursor_row = Cust_details_table.focus()
    content = Cust_details_table.item(cursor_row)
    row = content["values"]

    var_ref.set(row[0]),
    var_nm.set(row[1]),
    var_age.set(row[2]),
    var_gnd.set(row[3]),
    var_post_code.set(row[4]),
    var_mobile.set(row[5]),
    var_email.set(row[6]),
    var_nationality.set(row[7]),
    var_id_proof.set(row[8]),
    var_id_num.set(row[9]),
    var_address.set(row[10])

def update_data():
    if var_ref.get() == "":
        messagebox.showerror("Error", "Enter the contact no", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update customer set Name=%s, Age=%s, Gender=%s, Post_Code=%s, Mobile_No=%s, Email=%s, Nationality=%s, ID_Proof_Type=%s, ID_Number=%s, Address=%s  where Ref_No=%s ",
                (
                    var_nm.get(),
                    var_age.get(),
                    var_gnd.get(),
                    var_post_code.get(),
                    var_mobile.get(),
                    var_email.get(),
                    var_nationality.get(),
                    var_id_proof.get(),
                    var_id_num.get(),
                    var_address.get(),
                    var_ref.get()
                ))

            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def delete_data():
    if var_nm.get() == "" and var_mobile.get() == "":
        messagebox.showerror("Error", "Enter information", parent=root)
    else:
        try:
            delete = messagebox.askyesno("HMS", "Do you really want to delete the information of this customer?", parent=root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = "delete from customer where Name = %s"
                value = (var_nm.get(),)
                my_cursor.execute(query, value)

                query = "delete from room where Mobile_No=%s"
                value = (var_mobile.get(),)
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
    var_nm.set(""),
    var_age.set(""),
    var_gnd.set(""),
    var_post_code.set(""),
    var_mobile.set(""),
    var_email.set(""),
    var_nationality.set(""),
    var_id_num.set(""),
    var_address.set("")

    x = random.randint(1, 1000)
    var_ref.set(str(x))

def search():
    if var_search.get() == "" and txt_search.get() == "":
        messagebox.showerror("Error", "Enter informarion", parent=root)
    else:
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where " + str(var_search.get()) + " LIKE '%" + str(txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            Cust_details_table.delete(*Cust_details_table.get_children())
            for i in rows:
                Cust_details_table.insert("", END, value=i)

            conn.commit()
            conn.close()

        else:
            messagebox.showerror("Error", "No customer", parent=root)

def Room_book():
    root.destroy()
    call(["python", "S_bk_room.py"])

def back():
    root.destroy()
    call(["python", "S_home.py"])


var_ref = StringVar()
x = random.randint(1, 1000)
var_ref.set(str(x))

var_nm = StringVar()
var_age = StringVar()
var_gnd = StringVar()
var_post_code = StringVar()
var_mobile = StringVar()
var_email = StringVar()
var_nationality = StringVar()
var_id_proof = StringVar()
var_id_num = StringVar()
var_address = StringVar()
var_search = StringVar()
txt_search = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=1300, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=140, width=1300, height=600)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=210)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

lbl_title = Label(main_frame, text="Add Customer Details", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=1100, height=40)

lebelframeleft = LabelFrame(main_frame, text="Customer Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
lebelframeleft.place(x=200, y=40, width=430, height=450)

lbl_cust_nm = Label(lebelframeleft, text="Customer Name:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_cust_nm.grid(row=1, column=0, sticky=W)
entry_nm = ttk.Entry(lebelframeleft, textvariable=var_nm, font=("Arial Narrow", 12), width=30)
entry_nm.grid(row=1, column=1)

lbl_ag = Label(lebelframeleft, text="Age:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_ag.grid(row=2, column=0, sticky=W)
entry_ag = ttk.Entry(lebelframeleft, textvariable=var_age, font=("Arial Narrow", 12), width=30)
entry_ag.grid(row=2, column=1)

lbl_gnd = Label(lebelframeleft, text="Gender:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_gnd.grid(row=3, column=0, sticky=W)
combo_gnd = ttk.Combobox(lebelframeleft, textvariable=var_gnd, font=("Arial Narrow", 12), width=28, state="readonly")
combo_gnd["value"] = ("Male", "Female")
combo_gnd.grid(row=3, column=1)

lbl_post_code = Label(lebelframeleft, text="Post Code:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_post_code.grid(row=4, column=0, sticky=W)
entry_post_code = ttk.Entry(lebelframeleft, textvariable=var_post_code, font=("Arial Narrow", 12), width=30)
entry_post_code.grid(row=4, column=1)

lbl_mobile = Label(lebelframeleft, text="Mobile No.:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_mobile.grid(row=5, column=0, sticky=W)
entry_mobile = ttk.Entry(lebelframeleft, textvariable=var_mobile, font=("Arial Narrow", 12), width=30)
entry_mobile.grid(row=5, column=1)

lbl_email = Label(lebelframeleft, text="E-mail:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_email.grid(row=6, column=0, sticky=W)
entry_email = ttk.Entry(lebelframeleft, textvariable=var_email, font=("Arial Narrow", 12), width=30)
entry_email.grid(row=6, column=1)

lbl_nationality = Label(lebelframeleft, text="Nationality:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_nationality.grid(row=7, column=0, sticky=W)
combo_nationality = ttk.Combobox(lebelframeleft, textvariable=var_nationality, font=("Arial Narrow", 12), width=28, state="readonly")
combo_nationality["value"] = ("Bangladeshi", "Indian", "American", "British")
combo_nationality.grid(row=7, column=1)

lbl_id_type = Label(lebelframeleft, text="ID Proof Type:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_id_type.grid(row=8, column=0, sticky=W)
combo_id_type = ttk.Combobox(lebelframeleft, textvariable=var_id_proof, font=("Arial Narrow", 12), width=28, state="readonly")
combo_id_type["value"] = ("National ID Card", "Driving Licence", "Passport")
combo_id_type.current(0)
combo_id_type.grid(row=8, column=1)

lbl_id_num = Label(lebelframeleft, text="ID Number:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_id_num.grid(row=9, column=0, sticky=W)
entry_id_num = ttk.Entry(lebelframeleft, textvariable=var_id_num, font=("Arial Narrow", 12), width=30)
entry_id_num.grid(row=9, column=1)

lbl_address = Label(lebelframeleft, text="Address:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_address.grid(row=10, column=0, sticky=W)
entry_address = ttk.Entry(lebelframeleft, textvariable=var_address, font=("Arial Narrow", 12), width=30)
entry_address.grid(row=10, column=1)

btn_frame = Frame(lebelframeleft, relief=RIDGE)
btn_frame.place(x=0, y=375, width=420, height=45)

add_btn = Button(btn_frame, width=9, text="ADD", command=add_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
add_btn.grid(row=0, column=0, pady=1, padx=2)

update_btn = Button(btn_frame, width=9, text="UPDATE", command=update_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
update_btn.grid(row=0, column=1, pady=1, padx=2)

delete_btn = Button(btn_frame, width=9, text="DELETE", command=delete_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
delete_btn.grid(row=0, column=2, pady=1, padx=2)

reset_btn = Button(btn_frame, width=9, text="RESET", command=reset, font=("times new roman", 13, "bold"), bg="black", fg="white")
reset_btn.grid(row=0, column=3, pady=1, padx=2)

rm_book_btn = Button(main_frame, width=9, text="ROOM BOOKING", command=Room_book, font=("times new roman", 13, "bold"), bg="black", fg="white")
rm_book_btn.place(x=320, y=500, width=200, height=30)

tableframe = LabelFrame(main_frame, text="View Details and Search System", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=645, y=40, width=630, height=320)

lbl_search = Label(tableframe, text="Search By:", font=("Arial Narrow", 12, "bold"), bg="yellow", fg="black")
lbl_search.grid(row=0, column=0, sticky=W, padx=2)

combo_search = ttk.Combobox(tableframe, textvariable=var_search, font=("Arial Narrow", 12), width=10, state="readonly")
combo_search["value"] = ("Mobile_No", "Name", "ID_Number", "Address", "Gender", "Nationality")
combo_search.grid(row=0, column=1, padx=2)

entry_search = ttk.Entry(tableframe, textvariable=txt_search, font=("Arial Narrow", 12), width=20)
entry_search.grid(row=0, column=2, padx=2)

search_btn = Button(tableframe, width=10, text="Search", command=search, font=("times new roman", 12, "bold"))
search_btn.grid(row=0, column=3, padx=2)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=40, width=620, height=250)

show_btn = Button(main_frame, width=30, text="Show All Customer Information", command=fetch_data, font=("times new roman", 12, "bold"))
show_btn.place(x=820, y=370)

scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

Cust_details_table = ttk.Treeview(details_table, column=(
    "ref.", "name", "age", "gender", "post_code", "mobile", "email", "nationality", "id_proof", "id_number", "address"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=Cust_details_table.xview)
scroll_y.config(command=Cust_details_table.yview)

Cust_details_table.heading("ref.", text="Ref No.")
Cust_details_table.heading("name", text="Name")
Cust_details_table.heading("age", text="Age")
Cust_details_table.heading("gender", text="Gender")
Cust_details_table.heading("post_code", text="Post Code")
Cust_details_table.heading("mobile", text="Mobile No.")
Cust_details_table.heading("email", text="Email")
Cust_details_table.heading("nationality", text="Nationality")
Cust_details_table.heading("id_proof", text="ID Proof")
Cust_details_table.heading("id_number", text="ID Number")
Cust_details_table.heading("address", text="Address")

Cust_details_table["show"] = "headings"

Cust_details_table.column("ref.", width=100)
Cust_details_table.column("name", width=100)
Cust_details_table.column("age", width=100)
Cust_details_table.column("gender", width=100)
Cust_details_table.column("post_code", width=100)
Cust_details_table.column("mobile", width=100)
Cust_details_table.column("email", width=100)
Cust_details_table.column("nationality", width=100)
Cust_details_table.column("id_proof", width=100)
Cust_details_table.column("id_number", width=100)
Cust_details_table.column("address", width=100)

Cust_details_table.pack(fill=BOTH, expand=1)
Cust_details_table.bind("<ButtonRelease-1>", get_data)
fetch_data()


root.mainloop()
