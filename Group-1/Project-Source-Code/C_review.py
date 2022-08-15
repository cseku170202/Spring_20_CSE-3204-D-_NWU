from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.geometry("950x500+200+50")


def add_data():
    if var_phn.get() == "":
        messagebox.showerror("Error", "Enter all information correctly", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into review values(%s,%s,%s)", (
                var_nm.get(),
                var_phn.get(),
                var_rvw.get()
            ))

            conn.commit()
            fetch_data()
            conn.close()

            messagebox.showinfo("Success", "New information added", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

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

def get_data(event):
    cursor_row = table.focus()
    content = table.item(cursor_row)
    row = content["values"]

    var_nm.set(row[0]),
    var_phn.set(row[1])
    var_rvw.set(row[2])

def update_data():
    if var_nm.get() == "":
        messagebox.showerror("Error", "Required all information", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update review set Name=%s ,Review=%s where Phone=%s",
                (
                    var_nm.get(),
                    var_rvw.get(),
                    var_phn.get()
                ))

            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Updated.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def delete_data():
    if var_phn.get() == "":
        messagebox.showerror("Error", "Required all information", parent=root)
    else:
        try:
            delete = messagebox.askyesno("HMS", "Do you really want to delete?", parent=root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()

                query = "delete from review where Phone=%s"
                value = (var_phn.get(),)
                my_cursor.execute(query, value)

                conn.commit()
                fetch_data()
                conn.close()

            elif delete == "No":
                if not delete:
                    return

        except EXCEPTION as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def reset():
    var_nm.set(""),
    var_phn.set("")
    var_rvw.set("")

def back():
    root.destroy()
    call(["python", "C_home.py"])


var_nm = StringVar()
var_phn = StringVar()
var_rvw = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=950, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE, bg="light yellow")
main_frame.place(x=0, y=140, width=1300, height=600)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=220)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

lbl_title = Label(main_frame, text="Meal Details", font=("times new roman", 20, "bold"), bg="black" ,fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=760, height=40)

lebelframeleft = LabelFrame(main_frame, text="Information", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
lebelframeleft.place(x=200, y=45, width=290, height=230)

lbl_nm = Label(lebelframeleft, text="Name:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_nm.grid(row=0, column=0, sticky=W)
entry_nm = ttk.Entry(lebelframeleft, textvariable=var_nm, font=("Arial Narrow", 12), width=19)
entry_nm.grid(row=0, column=1)

lbl_phn = Label(lebelframeleft, text="Phone:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_phn.grid(row=1, column=0, sticky=W)
entry_phn = ttk.Entry(lebelframeleft, textvariable=var_phn, font=("Arial Narrow", 12), width=19)
entry_phn.grid(row=1, column=1)

lbl_rvw = Label(lebelframeleft, text="Review:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rvw.grid(row=2, column=0, sticky=W)
entry_rvw = ttk.Entry(lebelframeleft, textvariable=var_rvw, font=("Arial Narrow", 12), width=19)
entry_rvw.grid(row=2, column=1)

btn_frame = Frame(lebelframeleft, relief=RIDGE)
btn_frame.place(x=5, y=110, width=250, height=80)

add_btn = Button(btn_frame, width=9, text="ADD", command=add_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
add_btn.grid(row=0, column=0, pady=5, padx=20)

update_btn = Button(btn_frame, width=9, text="UPDATE", command=update_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
update_btn.grid(row=0, column=1, pady=5, padx=20)

delete_btn = Button(btn_frame, width=9, text="DELETE", command=delete_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
delete_btn.grid(row=1, column=0, pady=5, padx=20)

reset_btn = Button(btn_frame, width=9, text="RESET", command=reset, font=("times new roman", 13, "bold"), bg="black", fg="white")
reset_btn.grid(row=1, column=1, pady=5, padx=20)

tableframe = LabelFrame(main_frame, text="View Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=500, y=45, width=410, height=220)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=20, width=400, height=170)

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
table.bind("<ButtonRelease-1>", get_data)
fetch_data()


root.mainloop()
