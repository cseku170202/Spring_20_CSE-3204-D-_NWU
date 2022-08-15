from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from subprocess import call


root = Tk()
root.title("Hotel Management System")
root.resizable(False, False)
root.geometry("800x650+0+0")


def search_info():
    if txt_search.get() == "":
        messagebox.showerror("Error", "Enter contact number...........", parent=root)
    else:
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        query = "select Name from customer where Mobile_No=%s"
        value = (txt_search.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "No customer with this contact number", parent=root)
        else:
            conn.commit()
            conn.close()

            showdataframe = Frame(details_table, bd=2, relief=RIDGE)
            showdataframe.place(x=100, y=10, width=300, height=350)

            lbl_nm = Label(showdataframe, text="Name:", font=("Arial Narrow", 12, "bold"))
            lbl_nm.grid(row=0, column=0)

            lbl1 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl1.grid(row=0, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Gender from customer where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_gnd = Label(showdataframe, text="Gender:", font=("Arial Narrow", 12, "bold"))
            lbl_gnd.grid(row=1, column=0)

            lbl2 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl2.grid(row=1, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Email from customer where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_mail = Label(showdataframe, text="E-mail:", font=("Arial Narrow", 12, "bold"))
            lbl_mail.grid(row=2, column=0)

            lbl3 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl3.grid(row=2, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Nationality from customer where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_nationality = Label(showdataframe, text="Nationality:", font=("Arial Narrow", 12, "bold"))
            lbl_nationality.grid(row=3, column=0)

            lbl4 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl4.grid(row=3, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select ID_Number from customer where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_id_num = Label(showdataframe, text="ID_Number:", font=("Arial Narrow", 12, "bold"))
            lbl_id_num.grid(row=4, column=0)

            lbl5 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl5.grid(row=4, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Address from customer where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_address = Label(showdataframe, text="Address:", font=("Arial Narrow", 12, "bold"))
            lbl_address.grid(row=5, column=0)

            lbl6 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl6.grid(row=5, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Check_In_Date from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_ck_in = Label(showdataframe, text="Check In Date:", font=("Arial Narrow", 12, "bold"))
            lbl_ck_in.grid(row=6, column=0)

            lbl7 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl7.grid(row=6, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Check_Out_Date from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_ck_out = Label(showdataframe, text="Check Out Date:", font=("Arial Narrow", 12, "bold"))
            lbl_ck_out.grid(row=7, column=0)

            lbl8 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl8.grid(row=7, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Room_Type from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_rm_type = Label(showdataframe, text="Room Type:", font=("Arial Narrow", 12, "bold"))
            lbl_rm_type.grid(row=8, column=0)

            lbl9 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl9.grid(row=8, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Room_No from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_rm = Label(showdataframe, text="Room No:", font=("Arial Narrow", 12, "bold"))
            lbl_rm.grid(row=9, column=0)

            lbl10 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl10.grid(row=9, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Total_Bill from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_tb = Label(showdataframe, text="Total Bill:", font=("Arial Narrow", 12, "bold"))
            lbl_tb.grid(row=10, column=0)

            lbl11 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl11.grid(row=10, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Paid_Amount from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_pb = Label(showdataframe, text="Paid Bill:", font=("Arial Narrow", 12, "bold"))
            lbl_pb.grid(row=11, column=0)

            lbl12 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl12.grid(row=11, column=1)

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Due_Amount from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lbl_due = Label(showdataframe, text="Rest Amount:", font=("Arial Narrow", 12, "bold"))
            lbl_due.grid(row=12, column=0)

            lbl13 = Label(showdataframe, text=row, font=("Arial Narrow", 13))
            lbl13.grid(row=12, column=1)

def Check_out():
    if txt_search.get() == "":
        messagebox.showerror("Error", ".....Enter the contact no", parent=root)
    else:
        a = messagebox.askyesno("HMS", "Do you really want to check out?", parent=root)
        if a > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "select Room_No from room where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            x = my_cursor.fetchone()
            rm = x
            conn.commit()
            conn.close()

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "update room set Status ='Checked Out' where Mobile_No=%s"
            value = (txt_search.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()

            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            q = ("update details set Available='Yes' where Room_No=%s")
            v = (rm)
            my_cursor.execute(q, v)

            conn.commit()
            conn.close()

            messagebox.showinfo("Check out", "The customer checked out.", parent=root)

            r = messagebox.askyesno("HMS", "Do you want to give a review?", parent=root)
            if r > 0:
                root.destroy()
                call(["python", "C_review.py"])

            else:
                root.destroy()
                call(["python", "C_home.py"])

        elif a == "No":
            if not a:
                return

def back():
    root.destroy()
    call(["python", "C_home.py"])


txt_search = StringVar()


lbl_title = Label(root, text="Hotel Management System", font=("times new roman", 35, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
lbl_title.place(x=0, y=0, width=800, height=100)

main_frame = Frame(root, bd=4, relief=RIDGE)
main_frame.place(x=0, y=100, width=800, height=550)

lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
lbl_menu.place(x=0, y=0, width=180)

btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
btn_frame.place(x=0, y=40, width=180, height=210)

back_btn = Button(btn_frame, width=15, text="Back", command=back, font=("times new roman", 15, "bold"), bg="black", fg="white")
back_btn.grid(row=0, column=0, pady=1)

tableframe = LabelFrame(main_frame, text="View Customer Information", bd=2, relief=RIDGE, font=("times new roman", 15, "bold", "italic"), padx=2)
tableframe.place(x=190, y=10, width=540, height=470)

lbl_search = Label(tableframe, text="Enter Mobile No.:", font=("Arial Narrow", 12, "bold"), fg="black")
lbl_search.grid(row=0, column=0, sticky=W, padx=2)

entry_search = ttk.Entry(tableframe, textvariable=txt_search, font=("Arial Narrow", 12), width=20)
entry_search.grid(row=0, column=2, padx=2)

search_btn = Button(tableframe, width=10, text="Search", command=search_info, font=("times new roman", 12, "bold"))
search_btn.grid(row=0, column=3, padx=2)

details_table = Frame(tableframe, bd=4, relief=RIDGE)
details_table.place(x=15, y=50, width=500, height=375)

chk_btn = Button(main_frame, width=9, text="Check Out", command=Check_out, font=("times new roman", 13, "bold"), bd=7, bg="red", fg="yellow")
chk_btn.place(x=400, y=500, width=100, height=40)


root.mainloop()
