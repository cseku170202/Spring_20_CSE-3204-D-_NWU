from tkinter import *
import time
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
import sqlite3

def system():
    root = Tk()
    root.geometry("1700x900")
    root.title("Billing System")

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
        ptax = ((costfr + costpi + costbu + costnoo + costice + costdr) * 0.005)
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
    rightframe = Frame(root, width=400, height=700, relief=SUNKEN)
    rightframe.pack(side=RIGHT)

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
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "fr", "piz", "bur", "noo", "ice", "dr", "ct", "sb", "tax", "sr", "tot")
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
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("fr", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("piz", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bur", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("noo", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ice", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("dr", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)
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

    def add():
        Database()

        ord1 = orderno.get()

        french1 = french.get()
        if french1 == "":
            french1 = 0

        pizza1 = pizza.get()
        if pizza1 == "":
            pizza1 = 0

        burger1 = burger.get()
        if burger1 == "":
            burger1 = 0

        noodles1 = noodles.get()
        if noodles1 == "":
            noodles1 = 0

        ice1 = icecream.get()
        if ice1 == "":
            ice1 = 0

        drinks1 = drinks.get()
        if drinks1 == "":
            drinks1 = 0

        cost1 = cost.get()
        subtotal1 = subtotal.get()
        tax1 = tax.get()
        service1 = service.get()
        total1 = total.get()

        conn.execute(
            'INSERT INTO RECORD (ordno, fr, piz, bur ,noo, ice ,dr ,ct ,sb ,tax, sr, tot) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
            (ord1, french1, pizza1, burger1, noodles1, ice1, drinks1, cost1, subtotal1, tax1, service1, total1));
        conn.commit()
        messagebox.showinfo("Message", "Stored successfully")

        DisplayData()
        conn.close()

    # access data from sqlite
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = conn.execute("SELECT * FROM RECORD")
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
            if selecteditem[0] == "":
                selecteditem[0] = 0
            my_tree.delete(curItem)
            cursor = conn.execute("DELETE FROM RECORD WHERE ordno= %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

    localtime = time.asctime(time.localtime(time.time()))

    infolb = Label(topframe, font=('vardana', 30, 'bold'), text="Billing System", fg="#151B54", bd=10,
                   anchor=W)
    infolb.grid(row=0, column=0)
    infolb = Label(topframe, font=('varadana', 20,), text=localtime, fg="black", anchor=W)
    infolb.grid(row=1, column=0)
    # items
    ordlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Order No.", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=orderno).grid(row=1, column=1)
    # french fries
    frlbl = Label(leftframe, font=('aria', 16, 'bold'), text="French Fries", fg="black", bd=10, anchor=W).grid(row=2,
                                                                                                               column=0)
    frtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                  textvariable=french).grid(row=2, column=1)
    # Pizza
    pizlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Pizza", fg="black", bd=10, anchor=W).grid(row=3,
                                                                                                         column=0)
    piztxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=pizza).grid(row=3, column=1)
    # burger
    burlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Burger", fg="black", bd=10, anchor=W).grid(row=4,
                                                                                                          column=0)
    burtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=burger).grid(row=4, column=1)
    # Hakka Noodles
    noolbl = Label(leftframe, font=('aria', 16, 'bold'), text="Noodles", fg="black", bd=10, anchor=W).grid(row=5,
                                                                                                           column=0)
    nootxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4,  justify='right',
                   textvariable=noodles).grid(row=5, column=1)
    # icecream
    icelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Ice Cream", fg="black", bd=10, anchor=W).grid(row=6,
                                                                                                             column=0)
    icetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=icecream).grid(row=6, column=1)
    # drinks
    drinklbl = Label(leftframe, font=('aria', 16, 'bold'), text="Drinks", fg="black", bd=10, anchor=W).grid(row=1,
                                                                                                            column=2)
    drinktxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                     textvariable=drinks).grid(row=1, column=3)
    # cost
    costlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Cost", fg="#123456", bd=10, anchor=W).grid(row=2, column=2)
    costtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                    textvariable=cost).grid(row=2, column=3)
    # subtotal
    sublbl = Label(leftframe, font=('aria', 16, 'bold'), text="Subtotal", fg="#123456", bd=10, anchor=W).grid(row=3,
                                                                                                           column=2)
    subtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=subtotal).grid(row=3, column=3)
    # tax
    taxlbl = Label(leftframe, font=('aria', 16, 'bold'), text="Tax", fg="#123456", bd=10, anchor=W).grid(row=4, column=2)
    taxtxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=tax).grid(row=4, column=3)
    # service
    servicelbl = Label(leftframe, font=('aria', 16, 'bold'), text="Service", fg="#123456", bd=10, anchor=W).grid(row=5,
                                                                                                              column=2)
    servicetxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=service).grid(row=5, column=3)
    # total
    totallbl = Label(leftframe, font=('aria', 16, 'bold'), text="Total", fg="#123456", bd=10, anchor=W).grid(row=6,
                                                                                                          column=2)
    totaltxt = Entry(leftframe, font=('aria', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                     textvariable=total).grid(row=6, column=3)
    # ---button--
    # totalbutton
    totbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Total", bg="white", fg="#123456", bd=10, padx=5, pady=5,
                    width=10, command=tottal).grid(row=8, column=1)
    # clearbutton
    clearbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Clear", bg="white", fg="#560319", bd=10, padx=5,
                      pady=5, width=10, command=reset).grid(row=8, column=2)
    # exitbutton
    exitbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="black", bd=10, padx=5,
                     pady=5, width=10, command=exit).grid(row=8, column=3)
    # Add  recordbutton
    addbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Add", bg="white", fg="#151B54", bd=10, padx=5, pady=5,
                    width=10, command=add).grid(row=10, column=0)
    # Deleterecordbutton
    deletebtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Delete Record", bg="white", fg="#C34A2C", bd=10,
                       padx=5, pady=5, width=10, command=Delete).grid(row=10, column=3)

    def ok3():
        if ok3:
            root.destroy()
            call(['python', "fd_emp.py"])
            return True

    def back():
        root.destroy()
        call(['python', "prac.py"])

    # Feedbackbutton
    feedbtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Feedback", fg="#033E3E", bg="white", bd=10, padx=10,
                     pady=10, width=15, command=ok3).grid(row=10, column=1, columnspan=2)
    #backbutton
    Button(root, font=('vardana', 16, 'bold'), text="Back", bg="white", fg="#3D0C02", bd=10, padx=10, pady=10, width=7,
           command=back).place(x=0, y=0)
    def menu():
        root.destroy()
        call(['python', "add item.py"])

    # menubutton
    menubtn = Button(leftframe, font=('vardana', 16, 'bold'), text="Menu", bg="white", fg="#033E3E", bd=10, padx=5,
                     pady=5, width=10, command=menu).grid(row=8, column=0)
    root.mainloop()


system()