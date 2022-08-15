from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("500x440+400+100")


def login():
    if var_id.get() == "" or var_password.get() == "":
        messagebox.showerror("Error", "ID or Password is invalid")
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select * from ad_log where ID=%s and Password=%s"
            value = (var_id.get(), var_password.get(),)
            my_cursor.execute(query, value)

            rows = my_cursor.fetchone()
            if len(rows) != 0:
                admin = messagebox.askyesno("YesNo", "Access only admin")
                if admin > 0:
                    root.destroy()
                    call(["python", "A_home.py"])

                else:
                    if not admin:
                        return

            else:
                messagebox.showerror("Error", "Incorrect ID or Password")

            conn.commit()
            conn.close()

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=root)

def back():
    root.destroy()
    call(["python", "main.py"])


var_id = StringVar()
var_password = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 30, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=500, height=140)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=140, width=497, height=300)

canv = Canvas(main_frame, width=497, height=300, bg="lemon chiffon")
canv.place(x=0, y=0)

lebelframeleft = LabelFrame(main_frame, text="Admin LogIn", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"))
lebelframeleft.place(x=120, y=40, width=260, height=200)

lbl_id = Label(lebelframeleft, text="ID:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_id.grid(row=1, column=0)
entry_id = ttk.Entry(lebelframeleft, textvariable=var_id, font=("Arial Narrow", 12), width=15)
entry_id.grid(row=1, column=1)

lbl_password = Label(lebelframeleft, text="Password:", font=("Arial Narrow", 12, "bold"), padx=2, pady=5)
lbl_password.grid(row=2, column=0)
entry_password = ttk.Entry(lebelframeleft, textvariable=var_password, font=("Arial Narrow", 12), width=15, show=".")
entry_password.grid(row=2, column=1)

btn_frame = Frame(lebelframeleft, relief=RIDGE)
btn_frame.place(x=50, y=100, width=150, height=50)

login_btn = Button(btn_frame, width=10, text="Log In", command=login, font=("times new roman", 15, "bold"), bg="black", fg="white")
login_btn.grid(row=0, column=0, pady=1, padx=15)

back_btn = Button(main_frame, width=8, text="Back", command=back, font=("times new roman", 8, "bold"), bg="gray", fg="white")
back_btn.place(x=0, y=0)


root.mainloop()
