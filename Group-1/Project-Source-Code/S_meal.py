from tkinter import *
from tkinter import ttk
import mysql.connector
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("600x400+350+120")


def fetch_data():
    conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
    my_cursor = conn.cursor()
    my_cursor.execute("select * from details_meal")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Meal_table.delete(*Meal_table.get_children())
        for i in rows:
            Meal_table.insert("", END, value=i)

        conn.commit()
    conn.close()

def back():
    root.destroy()
    call(["python", "S_home.py"])


var_meal_type = StringVar()
var_meal_price = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 30, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=600, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=140, width=600, height=260)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=190)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=190, height=150)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

tableframe = LabelFrame(main_frame, text="View Details", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=230, y=10, width=330, height=190)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=0, y=10, width=320, height=150)

scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

Meal_table = ttk.Treeview(details_table, column=(
    "meal_type", "meal_price"),
                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=Meal_table.xview)
scroll_y.config(command=Meal_table.yview)

Meal_table.heading("meal_type", text="Meal Type")
Meal_table.heading("meal_price", text="Price")

Meal_table["show"] = "headings"

Meal_table.column("meal_type", width=5)
Meal_table.column("meal_price", width=5)

Meal_table.pack(fill=BOTH, expand=1)
fetch_data()


root.mainloop()
