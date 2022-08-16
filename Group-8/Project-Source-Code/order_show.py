from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import mysql.connector
from subprocess import call

def system():
    root = Tk()
    root.geometry("1350x900")
    root.title("Show Order-list")

    ############database###########
    def Database():
        global conn, cursor
        # creating system database
        conn = sqlite3.connect("Restaurant.db")
        cursor = conn.cursor()
        # creating bill table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS RECORD(ordno text, fr text ,piz text,bur text,noo text,ice text, dr text, ct text,sb text,tax text,sr text,tot text)")

    # variable datatype assignment
    orderno = StringVar()
    french = StringVar()
    pizza = StringVar()
    burger = StringVar()
    noodles = StringVar()
    icecream = StringVar()
    drinks = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    # defining total function
    def tottal():
        order = (orderno.get())

        if french.get() == '':
            fr = 0
        else:
            fr = (float(french.get()))

        if pizza.get() == "":
            pi = 0
        else:
            pi = float(pizza.get())

        if burger.get() == "":
            bu = 0
        else:
            bu = float(burger.get())

        if noodles.get() == "":
            noo = 0
        else:
            noo = float(noodles.get())

        if icecream.get() == "":
            ice = 0
        else:
            ice = float(icecream.get())

        if drinks.get() == "":
            dr = 0
        else:
            dr = float(drinks.get())


        # computing cost of items
        costfr = fr * 60
        costpi = pi * 220
        costbu = bu * 120
        costnoo = noo * 80
        costice = ice * 100
        costdr = dr * 50

        # computing the charges
        costofmeal = (costfr + costpi + costbu + costnoo + costice + costdr)
        ptax = ((costfr + costpi + costbu + costnoo + costice + costdr) * 0.05)
        sub = (costfr + costpi + costbu + costnoo + costice + costdr)
        ser = ((costfr + costpi + costbu + costnoo + costice + costdr) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)

        # Displaying values
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

    def reset():
        orderno.set("")
        french.set("")
        pizza.set("")
        burger.set("")
        noodles.set("")
        icecream.set("")
        drinks.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

    def exit():
        root.destroy()

    # Topframe
    topframe = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
    topframe.pack(side=TOP)
    # Leftframe
    leftframe = Frame(root, width=900, height=700, relief=SUNKEN)
    leftframe.pack(side=LEFT)
    # rightframe
    #rightframe = Frame(root, width=400, height=700, relief=SUNKEN)
    #rightframe.pack(side=RIGHT)

    ################## display data ####################
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM RECORD")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
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
    my_tree['columns'] = ("ordno", "fr", "piz", "bur", "noo", "ice", "dr", "ct", "sb", "tax", "sr", "tot")
    ############ creating  for table ################
    hsb = ttk.Scrollbar(leftframe, orient="horizontal")
    hsb.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X, side=BOTTOM)

    vsb = ttk.Scrollbar(leftframe, orient="vertical")
    vsb.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y, side=RIGHT)
    # defining column for table
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("fr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("piz", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("bur", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("noo", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("dr", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=120, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=120, minwidth=25)
    # defining  headings for table
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("fr", text="French fries", anchor=CENTER)
    my_tree.heading("piz", text="Pizza", anchor=CENTER)
    my_tree.heading("bur", text="Burger", anchor=CENTER)
    my_tree.heading("noo", text="Noodles", anchor=CENTER)
    my_tree.heading("ice", text="Ice cream", anchor=CENTER)
    my_tree.heading("dr", text="Drinks", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()


    # ---button--
    # clearbutton

    localtime = time.asctime(time.localtime(time.time()))

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Show Orders", fg="#151B54", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=1)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=1)

    # exitbutton
    exitbtn = Button(topframe, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=2, column=3, pady=10)
    # Add  recordbutton

    # Deleterecordbutton

    def back():
        root.destroy()
        call(['python', "after_admin_login_pg.py"])

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