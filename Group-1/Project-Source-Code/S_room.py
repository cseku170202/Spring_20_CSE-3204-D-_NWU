from tkinter import *
from tkinter import ttk
import mysql.connector
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.resizable(False,False)
root.geometry("850x500+280+90")


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

def back():
    root.destroy()
    call(["python", "S_home.py"])


var_floor = StringVar()
var_rm = StringVar()
var_rm_type = StringVar()
var_rm_avail = StringVar()
var_rm_price = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=850, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=140, width=850, height=360)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=210)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

tableframe = LabelFrame(main_frame, text="View Room Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=200, y=20, width=610, height=240)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=10, width=600, height=200)

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
fetch_data()


root.mainloop()
