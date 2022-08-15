from tkinter import *
from tkinter import ttk
import mysql.connector
from subprocess import call

root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("1300x500+30+80")


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

def back():
    root.destroy()
    call(["python", "A_home.py"])

def info():
    root.destroy()
    call(["python", "A_cust_st.py"])


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

cust_btn = Button(btn_frame, width=15, text="More Customer Info.", command=info, font=("times new roman", 15, "bold"), bg="black", fg="white")
cust_btn.grid(row=1, column=0, pady=1)

tableframe = LabelFrame(main_frame, text="View Customer Information", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=200, y=10, width=1085, height=240)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=10, width=1080, height=200)

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
fetch_data()


root.mainloop()
