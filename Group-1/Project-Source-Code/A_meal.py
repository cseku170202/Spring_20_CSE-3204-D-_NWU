from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.geometry("950x500+200+50")


def add_data():
    if var_meal_price.get() == "" or var_meal_type.get() == "":
        messagebox.showerror("Error", "Enter all information correctly", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into details_meal values(%s,%s)", (
                var_meal_type.get(),
                var_meal_price.get()
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
    my_cursor.execute("select * from details_meal")
    rows = my_cursor.fetchall()
    if len(rows) != 0:
        Meal_table.delete(*Meal_table.get_children())
        for i in rows:
            Meal_table.insert("", END, value=i)

        conn.commit()
        conn.close()

def get_data(event):
    cursor_row = Meal_table.focus()
    content = Meal_table.item(cursor_row)
    row = content["values"]

    var_meal_type.set(row[0]),
    var_meal_price.set(row[1])

def update_data():
    if var_meal_type.get() == "":
        messagebox.showerror("Error", "Required all information", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update details_meal set Price=%s where Meal_Type=%s",
                (
                    var_meal_price.get(),
                    var_meal_type.get()
                ))

            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Price has been updated.", parent=root)

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def delete_data():
    if var_meal_type.get() == "":
        messagebox.showerror("Error", "Required all information", parent=root)
    else:
        try:
            delete = messagebox.askyesno("HMS", "Do you really want to delete?", parent=root)
            if delete > 0:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()

                query = "delete from details_meal where Meal_Type=%s"
                value = (var_meal_type.get(),)
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
    var_meal_type.set(""),
    var_meal_price.set("")

def back():
    root.destroy()
    call(["python", "A_home.py"])


var_meal_type = StringVar()
var_meal_price = StringVar()


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

lbl_title = Label(main_frame, text="Meal Details", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=2, relief=RIDGE)
lbl_title.place(x=190, y=0, width=760, height=40)

lebelframeleft = LabelFrame(main_frame, text="Information", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
lebelframeleft.place(x=200, y=45, width=290, height=220)

lbl_meal_type = Label(lebelframeleft, text="Meal Type:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_meal_type.grid(row=0, column=0, sticky=W)
combo_meal_type = ttk.Combobox(lebelframeleft, textvariable=var_meal_type, font=("Arial Narrow", 12), width=17, state="readonly")
combo_meal_type["value"] = ("", "One Meal", "Two Meal", "Three Meal", "None")
combo_meal_type.current(0)
combo_meal_type.grid(row=0, column=1)

lbl_meal_price = Label(lebelframeleft, text="Price:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_meal_price.grid(row=1, column=0, sticky=W)
entry_meal_price = ttk.Entry(lebelframeleft, textvariable=var_meal_price, font=("Arial Narrow", 12), width=19)
entry_meal_price.grid(row=1, column=1)

btn_frame = Frame(lebelframeleft, relief=RIDGE)
btn_frame.place(x=5, y=100, width=250, height=80)

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
Meal_table.bind("<ButtonRelease-1>", get_data)
fetch_data()


root.mainloop()
