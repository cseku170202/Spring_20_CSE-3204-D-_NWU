from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.geometry("1300x500+30+80")


def add_data():
    if var_floor.get() == "" or var_rm_type.get() == "":
        messagebox.showerror("Error", "Enter all information correctly", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into details values(%s,%s,%s,%s,%s)", (
                var_floor.get(),
                var_rm.get(),
                var_rm_type.get(),
                var_rm_avail.get(),
                var_rm_price.get()
            ))

            conn.commit()
            fetch_data()
            conn.close()

            messagebox.showinfo("Success", "New room added", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def fetch_data():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from details")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Room_table.delete(*Room_table.get_children())
        for i in rows:
            Room_table.insert("", END, value=i)

        conn.commit()
    conn.close()

def get_data(event):
    cursor_row = Room_table.focus()
    content = Room_table.item(cursor_row)
    row = content["values"]

    var_floor.set(row[0]),
    var_rm.set(row[1]),
    var_rm_type.set(row[2]),
    var_rm_avail.set(row[3]),
    var_rm_price.set(row[4])

def update_data():
    if var_floor.get() == "":
        messagebox.showerror("Error", "Enter the floor no", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update details set Floor=%s, Room_Type=%s, Available=%s, Price=%s where Room_No=%s",
                (
                    var_floor.get(),
                    var_rm_type.get(),
                    var_rm_avail.get(),
                    var_rm_price.get(),
                    var_rm.get()
                ))

            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def delete_data():
    if var_rm.get() == "":
        messagebox.showerror("Error", "Enter the room no", parent=root)
    else:
        try:
            delete = messagebox.askyesno("HMS", "Do you really want to delete?", parent=root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()

                query = "delete from details where Room_No=%s"
                value = (var_rm.get(),)
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
    var_floor.set(""),
    var_rm.set(""),
    var_rm_type.set(""),
    var_rm_avail.set("")
    var_rm_price.set("")

def back():
    root.destroy()
    call(["python", "A_home.py"])


var_floor = StringVar()
var_rm = StringVar()
var_rm_type = StringVar()
var_rm_avail = StringVar()
var_rm_price = StringVar()


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

lbl_title = Label(main_frame, text="Room Details", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=1110, height=40)

lebelframeleft = LabelFrame(main_frame, text="Room Info.", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
lebelframeleft.place(x=200, y=45, width=430, height=260)

lbl_floor = Label(lebelframeleft, text="Floor:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_floor.grid(row=0, column=0, sticky=W)
entry_floor = ttk.Entry(lebelframeleft, textvariable=var_floor, font=("Arial Narrow", 12), width=30)
entry_floor.grid(row=0, column=1, sticky=W)

lbl_rm = Label(lebelframeleft, text="Room No.:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm.grid(row=1, column=0, sticky=W)
entry_rm = ttk.Entry(lebelframeleft, textvariable=var_rm, font=("Arial Narrow", 12), width=30)
entry_rm.grid(row=1, column=1)

lbl_rm_type = Label(lebelframeleft, text="Room Type:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm_type.grid(row=2, column=0, sticky=W)
combo_rm_type = ttk.Combobox(lebelframeleft, textvariable=var_rm_type, font=("Arial Narrow", 12), width=28, state="readonly")
combo_rm_type["value"] = ("Single", "Double", "Luxury")
combo_rm_type.current(0)
combo_rm_type.grid(row=2, column=1)

lbl_rm_avail = Label(lebelframeleft, text="Room Available:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm_avail.grid(row=3, column=0, sticky=W)
entry_rm_avail = ttk.Entry(lebelframeleft, textvariable=var_rm_avail, font=("Arial Narrow", 12), width=30)
entry_rm_avail.grid(row=3, column=1)

lbl_rm_price = Label(lebelframeleft, text="Room Price:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_rm_price.grid(row=4, column=0, sticky=W)
entry_rm_price = ttk.Entry(lebelframeleft, textvariable=var_rm_price, font=("Arial Narrow", 12), width=30)
entry_rm_price.grid(row=4, column=1)

btn_frame = Frame(lebelframeleft, relief=RIDGE)
btn_frame.place(x=2, y=170, width=420, height=50)

add_btn = Button(btn_frame, width=9, text="ADD", command=add_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
add_btn.grid(row=0, column=0, pady=5, padx=2)

update_btn = Button(btn_frame, width=9, text="UPDATE", command=update_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
update_btn.grid(row=0, column=1, pady=5, padx=2)

delete_btn = Button(btn_frame, width=9, text="DELETE", command=delete_data, font=("times new roman", 13, "bold"), bg="black", fg="white")
delete_btn.grid(row=0, column=2, pady=5, padx=2)

reset_btn = Button(btn_frame, width=9, text="RESET", command=reset, font=("times new roman", 13, "bold"), bg="black", fg="white")
reset_btn.grid(row=0, column=3, pady=5, padx=2)

tableframe = LabelFrame(main_frame, text="View Room Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=650, y=45, width=630, height=260)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=20, width=620, height=200)

scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

Room_table = ttk.Treeview(details_table, column=(
    "floor", "room_no", "room_type", "room_avail", "room_price"),
                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=Room_table.xview)
scroll_y.config(command=Room_table.yview)

Room_table.heading("floor", text="Floor")
Room_table.heading("room_no", text="Room No")
Room_table.heading("room_type", text="Room Type")
Room_table.heading("room_avail", text="Available")
Room_table.heading("room_price", text="Price")

Room_table["show"] = "headings"

Room_table.column("floor", width=5)
Room_table.column("room_no", width=5)
Room_table.column("room_type", width=5)
Room_table.column("room_avail", width=5)
Room_table.column("room_price", width=5)

Room_table.pack(fill=BOTH, expand=1)
Room_table.bind("<ButtonRelease-1>", get_data)
fetch_data()


root.mainloop()
