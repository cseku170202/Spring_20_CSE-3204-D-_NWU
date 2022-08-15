from tkinter import *
from tkinter import ttk
import mysql.connector
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("792x500+200+50")


def fetch_data():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from review")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        table.delete(*table.get_children())
        for i in rows:
            table.insert("", END, value=i)

        conn.commit()
    conn.close()

def back():
    root.destroy()
    call(["python", "A_home.py"])


var_nm = StringVar()
var_phn = StringVar()
var_rvw = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 35, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=792, height=120)

main_frame = Frame(root, bd=4, relief=RIDGE, bg="light yellow")
main_frame.place(x=0, y=120, width=792, height=380)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=220)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

lbl_title = Label(main_frame, text="Customer's Review", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=600, height=40)

tableframe = LabelFrame(main_frame, text="View Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=200, y=45, width=550, height=220)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=20, width=540, height=170)

scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

table = ttk.Treeview(details_table, column=(
    "nm", "phn", "rvw"),
                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)

table.heading("nm", text="Name")
table.heading("phn", text="Phone")
table.heading("rvw", text="Review")

table["show"] = "headings"

table.column("nm", width=100)
table.column("phn", width=100)
table.column("rvw", width=200)

table.pack(fill=BOTH, expand=1)
fetch_data()


root.mainloop()
