from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import mysql.connector
from subprocess import call

def system():
    root = Tk()
    root.geometry("900x750")
    root.title("Admin Mode")

    ############database###########
    def Database():
        global conn, cursor
        # creating system database
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS food_list2(Itemname,Catagory,Price, Designation)")

    # variable datatype assignment
    e1= StringVar()
    e2 = StringVar()
    e3 = StringVar()

    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

    def exit():
        root.destroy()

    def back():
        root.destroy()
        call(['python', "billing.py"])

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=900, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    # rightframe
    rightframe = Frame(root, width=600, height=700, relief=SUNKEN)
    rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():

        connect = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
        conn = connect.cursor()
        conn.execute("SELECT * FROM `food_list2`")

        i = 0
        for ro in conn:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2]))
            i = i + 1

    # add some style
    style = ttk.Style()
    style.theme_use("classic")

    style.configure("Treeview",
                    background="#CFECEC",
                    foregroung="black",
                    rowheight=30,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', '#ece284')])

    ###########  Creating table #############
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("Item name", "Catagory", "Price")
    ############ creating  for table ################
    hsb = ttk.Scrollbar(rightframe, orient="horizontal")
    hsb.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    vsb = ttk.Scrollbar(rightframe, orient="vertical")
    vsb.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)
    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("Item name", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Catagory", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("Price", anchor=CENTER, width=60, minwidth=25)

    # defining  headings for table
    my_tree.heading("Item name", text="Item name", anchor=CENTER)
    my_tree.heading("Catagory", text="Catagory", anchor=CENTER)
    my_tree.heading("Price", text="Price", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    def add():
        Database()

        Itemname = e1.get()
        Catagory = e2.get()
        Price = e3.get()

        if Itemname == "" or Catagory == "" or Price == "" :
            messagebox.showinfo("Warning", "fill the empty field!!!")
        else:
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
            cursor = mysqldb.cursor()
            sql = "INSERT INTO food_list2 (Itemname, Catagory, Price) VALUES (%s,%s,%s)"
            val = (Itemname, Catagory,Price)
            cursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("Message", "Stored successfully")

        DisplayData()
        conn.close()

    # access data from sqlite
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM food_list2")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    # defining function to delete record
    def Delete():
        # open database
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)

            mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
            mycursor = mysqldb.cursor()
            sql = "DELETE FROM food_list2 WHERE Price =" + str(selecteditem[2]) + ""
            mycursor.execute(sql)
            mysqldb.commit()

    localtime = time.asctime(time.localtime(time.time()))

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Menu Management", fg="#151B54", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=0)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=0)

    # items
    Itemlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Item Name", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)
    # Catagory
    catlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Catagory", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)
    # Price
    prilbl = Label(leftframe, font=('aria', 16, 'bold'), text="Price", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)

    e1 = Entry(root, font=40)
    e1.place(x=250, y=270)
    e2 = Entry(root, font="40")
    e2.place(x=250, y=310)
    e3 = Entry(root, font=40)
    e3.place(x=250, y=350)

    # ---button--
    # clearbutton
    clearbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Clear", bg="white", fg="#560319", bd=10, padx=5,
                      pady=5, width=10, command=reset).grid(row=10, column=0)
    # exitbutton
    exitbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=10, column=3)
    # Add  recordbutton
    addbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Add", bg="white", fg="#151B54", bd=10, padx=5, pady=5,
                    width=10, command=add).grid(row=8, column=0)
    # Deleterecordbutton
    deletebtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Delete Record", bg="white", fg="#C34A2C", bd=10,
                       padx=5, pady=5, width=10, command=Delete).grid(row=8, column=3)
    # BackButton
    backdbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Back", fg="#254117", bg="white", bd=10, padx=10,
                    pady=10, width=10,command=back).grid(row=10, column=1, columnspan=2)

    def select():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

        selected = my_tree.focus()

        values = my_tree.item(selected, 'values')

        e1.insert(0, values[0])
        e2.insert(0, values[1])
        e3.insert(0, values[2])

    selectbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Select", fg="#254117", bg="white", bd=10, padx=10,
                      pady=10, width=10, command=select).grid(row=11, column=1, columnspan=2)
    # updatebutton
    def up():
        selected = my_tree.focus()

        my_tree.item(selected, text="", values=(e1.get(), e2.get(), e3.get()))

        reg = e1.get()
        name = e2.get()
        cat = e3.get()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
        mycursor = mysqldb.cursor()
        response = messagebox.askyesno('SYSTEM ALERT', 'Are you sure you want to Change Name?')
        if response:
            try:
                sql = "update food_list2 set Price= %s, Catagory=%s where Itemname=%s"
                val = (cat, name, reg)
                mycursor.execute(sql, val)
                mysqldb.commit()
                messagebox.showinfo("information", "Record Updated Successfully")

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showinfo("SYSTEM ALERT", "Canceled")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)


    updatebtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Update", bg="white", fg="#033E3E", bd=10, padx=5,
                     pady=5, width=10,command=up).grid(row=8, column=2)

    def refresh():
        root.destroy()
        system()

    refreshbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Refresh", bg="white", fg="#C34A2C", bd=10,
                       padx=5, pady=5, width=10, command=refresh).grid(row=11, column=0)

    root.mainloop()

system()