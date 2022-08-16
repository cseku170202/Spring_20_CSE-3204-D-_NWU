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
    root.title("Menu list for User")

    ############database###########
    def Database():
        global conn, cursor
        # creating system database
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS food_list2(Itemname,Catagory,Price)")

    # variable datatype assignment
    e1 = StringVar()
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
        call(['python', "main.py"])

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=1500, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    # rightframe
    #rightframe = Frame(root, width=600, height=700, relief=SUNKEN)
    #rightframe.pack(side=RIGHT)

    bframe = Frame(root, width=600, height=700, relief=SUNKEN)
    bframe.pack(side=BOTTOM)

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
    my_tree = ttk.Treeview(leftframe)
    my_tree['columns'] = ("Item name", "Catagory", "Price")
    ############ creating  for table ################
    hsb = ttk.Scrollbar(leftframe, orient="horizontal")
    hsb.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    vsb = ttk.Scrollbar(leftframe, orient="vertical")
    vsb.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=X, side=RIGHT)
    # defining column for table
    my_tree.column("#0", width=10, minwidth=10)
    my_tree.column("Item name", anchor=CENTER, width=290, minwidth=25)
    my_tree.column("Catagory", anchor=CENTER, width=290, minwidth=25)
    my_tree.column("Price", anchor=CENTER, width=290, minwidth=25)

    # defining  headings for table
    my_tree.heading("Item name", text="Item name", anchor=CENTER)
    my_tree.heading("Catagory", text="Catagory", anchor=CENTER)
    my_tree.heading("Price", text="Price", anchor=CENTER)

    my_tree.pack()
    DisplayData()


    # access data from sqlite



    localtime = time.asctime(time.localtime(time.time()))

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Menu-List", fg="#151B54", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=1)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=1)


    # ---button--
    # clearbutton

    # exitbutton
    exitbtn = Button(topframe, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=2, column=3, pady=10)
    # Add  recordbutton

    # Deleterecordbutton

    # BackButton
    backdbtn = Button(topframe, font=('vardana', 16, 'bold'), text="Back", fg="#254117", bg="white", bd=10, padx=10,
                    pady=10, width=10,command=back).grid(row=2, column=1, columnspan=2, pady=10)
    # updatebutton


    def refresh():
        root.destroy()
        system()

    refreshbtn = Button(topframe, font=('vardana', 16, 'bold'), text="Refresh", bg="white", fg="#C34A2C", bd=10,
                       padx=5, pady=5, width=10, command=refresh).grid(row=2, column=0, pady=30)

    root.mainloop()

system()