import tkinter
from io import BytesIO
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.geometry("1000x800")

def back():
    root.destroy()
    import user

def show1():
    top = Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")

    def back():
        top.destroy()

    back_btn = Button(top, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=back)
    back_btn.place(x=800, y=50)

    def booking():
        book = Toplevel(root)
        book.geometry("1000x700")
        book.title("Child Window")

        def user():
            book.destroy()
            import all_rent

        def rent():
            mysqldb = sqlite3.connect(database="brm.db")
            mycursor = mysqldb.cursor()
            image = image_field.get()
            title = title_field.get()
            address = address_field.get()
            contact = contact_field.get()
            payment_method = payment_clicked.get()
            definition = definition_field.get()
            toEmail = owner_field.get()
            sql = "INSERT INTO rent (name, title, address, contact, payment_method, email, owner) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (image, title, address, contact, payment_method, definition, toEmail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("", "Booking success")
            cur.execute("SELECT rent FROM std limit 1")
            rents = cur.fetchall()
            for x in rents:
                for rent in x:
                    price_label = Label(top, text=((str(rent))+"/="), font=('areal', 25, 'bold'), fg='#FF8A00')
                    price_label.place(x=540, y=210)
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)", (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()

        def cancel():
            book.destroy()

        back_btn = Button(book, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=cancel)
        back_btn.place(x=60, y=50)

        login_label = Label(book, text="Booking", font=('areal', 30, 'bold'))
        login_label.place(x=430, y=50)

        ownerName = Label(book, text="Owner", font=('areal', 15, 'bold'))
        ownerName.place(x=480, y=295)
        owner_field = Entry(book, width=22, font=('areal', 15))
        owner_field.place(x=700, y=310, anchor='center')

        image = Label(book, text="Name", font=('areal', 15, 'bold'))
        image.place(x=80, y=145)
        image_field = Entry(book, textvariable="Chose file", width=22, font=('areal', 15))
        image_field.place(x=280, y=160, anchor='center')

        title = Label(book, text="Title", font=('areal', 15, 'bold'))
        title.place(x=80, y=215)
        title_field = Entry(book, width=22, font=('areal', 15))
        title_field.place(x=280, y=230, anchor='center')

        address = Label(book, text="Address", font=('areal', 15, 'bold'))
        address.place(x=75, y=305)
        address_field = Entry(book, width=22, font=('areal', 15))
        address_field.place(x=280, y=320, anchor='center')

        contact = Label(book, text="Contact", font=('areal', 15, 'bold'))
        contact.place(x=475, y=125)
        contact_field = Entry(book, width=22, font=('areal', 15))
        contact_field.place(x=700, y=150, anchor='center')

        definition = Label(book, text="Email", font=('areal', 15, 'bold'))
        definition.place(x=475, y=210)
        definition_field = Entry(book, width=22, font=('areal', 15))
        definition_field.place(x=700, y=225, anchor='center')

        payment_clicked = StringVar()
        payment_clicked.set('Select payment method')
        payment = OptionMenu(book, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
        payment.config(font=('areal', 12))
        payment.place(x=580, y=370)

        rent_btn = Button(book, text='Rent', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=rent)
        rent_btn.place(x=430, y=450)

    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            title_label = Label(top, text=result, font=('areal', 25, 'bold'))
            title_label.place(x=540, y=150)
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(top, text="")
    img_LabelFrame.place(x=120, y=150, width=200, height=150)
    # create the label_photo inside img_LabelFrame
    label_photo = Label(img_LabelFrame)
    label_photo.pack()
    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo
    results = cur.fetchall()
    for x in results:
        for result in x:
            heading_label = Label(top, text=result, font=('areal', 25, 'bold'))
            heading_label.place(x=540, y=150)

    cur.execute("SELECT email FROM std limit 1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top,text="Contact: ",font=('areal',15)).place(x=540,y=330)
            onwerEmail = Label(top,text=email,font=('areal',15)).place(x=630,y=330)

    cur.execute("SELECT contact FROM std limit 1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

    cur.execute("SELECT rent FROM std limit 1")
    rents = cur.fetchall()
    for x in rents:
        for rent in x:
            price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
            price_label.place(x=540, y=210)



    user_frame = LabelFrame(top, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
    user_frame.grid(pady=40)

    logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
    logo_label.grid(row=0, column=1, padx=20)

    title_label = Label(user_frame, text='Title', font=('areal', 15), padx=300, bg='#ffffff')
    title_label.grid(row=0, column=2)

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2',command=booking)
    rent_btn.place(x=540, y=270)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT definition FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            rent_details = tkinter.Message(top,text=result,font=('areal',15),width=900)
            rent_details.place(x=20, y=440)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result,font=('areal',15))
            condition1.place(x=20, y=550)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=600)
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms2 FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result,font=('areal',15))
            condition1.place(x=20, y=650)
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms3 FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition3 = Label(top, text=result,font=('areal',15))
            condition3.place(x=20, y=700)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show2():
    top = Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")

    def booking():
        book = Toplevel(root)
        book.geometry("1000x700")
        book.title("Child Window")

        def user():
            book.destroy()
            import all_rent

        def rent():
            mysqldb = sqlite3.connect(database="brm.db")
            mycursor = mysqldb.cursor()
            image = image_field.get()
            title = title_field.get()
            address = address_field.get()
            contact = contact_field.get()
            payment_method = payment_clicked.get()
            definition = definition_field.get()
            toEmail = owner_field.get()
            sql = "INSERT INTO rent (name, title, address, contact, payment_method, email, owner) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (image, title, address, contact, payment_method, definition, toEmail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("", "Booking success")

            cur.execute("SELECT contact FROM std limit 1,1")
            emails = cur.fetchall()
            for x in emails:
                for email in x:
                    ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
                    onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

            cur.execute("SELECT rent FROM std limit 1,1")
            rents = cur.fetchall()
            for x in rents:
                for rent in x:
                    price_label = Label(top, text=(rent + "/="), font=('areal', 25, 'bold'), fg='#FF8A00')
                    price_label.place(x=540, y=210)
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)",
                             (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)", (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()

        def cancel():
            book.destroy()

        back_btn = Button(book, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=cancel)
        back_btn.place(x=60, y=50)

        login_label = Label(book, text="Booking", font=('areal', 30, 'bold'))
        login_label.place(x=430, y=50)

        ownerName = Label(book, text="Owner", font=('areal', 15, 'bold'))
        ownerName.place(x=480, y=295)
        owner_field = Entry(book, width=22, font=('areal', 15))
        owner_field.place(x=700, y=310, anchor='center')

        image = Label(book, text="Name", font=('areal', 15, 'bold'))
        image.place(x=80, y=145)
        image_field = Entry(book, textvariable="Chose file", width=22, font=('areal', 15))
        image_field.place(x=280, y=160, anchor='center')

        title = Label(book, text="Title", font=('areal', 15, 'bold'))
        title.place(x=80, y=215)
        title_field = Entry(book, width=22, font=('areal', 15))
        title_field.place(x=280, y=230, anchor='center')

        address = Label(book, text="Address", font=('areal', 15, 'bold'))
        address.place(x=75, y=305)
        address_field = Entry(book, width=22, font=('areal', 15))
        address_field.place(x=280, y=320, anchor='center')

        contact = Label(book, text="Contact", font=('areal', 15, 'bold'))
        contact.place(x=475, y=125)
        contact_field = Entry(book, width=22, font=('areal', 15))
        contact_field.place(x=700, y=150, anchor='center')

        definition = Label(book, text="Email", font=('areal', 15, 'bold'))
        definition.place(x=475, y=210)
        definition_field = Entry(book, width=22, font=('areal', 15))
        definition_field.place(x=700, y=225, anchor='center')

        payment_clicked = StringVar()
        payment_clicked.set('Select payment method')
        payment = OptionMenu(book, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
        payment.config(font=('areal', 12))
        payment.place(x=580, y=370)

        rent_btn = Button(book, text='Rent', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=rent)
        rent_btn.place(x=430, y=450)

    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            title_label = Label(top, text=result, font=('areal', 25, 'bold'))
            title_label.place(x=540, y=150)
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 1,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(top, text="")
    img_LabelFrame.place(x=120, y=150, width=200, height=150)
    # create the label_photo inside img_LabelFrame
    label_photo = Label(img_LabelFrame)
    label_photo.pack()
    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo
    results = cur.fetchall()
    for x in results:
        for result in x:
            heading_label = Label(top, text=result, font=('areal', 25, 'bold'))
            heading_label.place(x=540, y=150)

    cur.execute("SELECT email FROM std limit 1,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Contact: ", font=('areal', 15)).place(x=540, y=330)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=330)

    cur.execute("SELECT contact FROM std limit 1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

    cur.execute("SELECT rent FROM std limit 1,1")
    rents = cur.fetchall()
    for x in rents:
        for rent in x:
            price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
            price_label.place(x=540, y=210)

    user_frame = LabelFrame(top, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
    user_frame.grid(pady=40)

    logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
    logo_label.grid(row=0, column=1, padx=20)

    title_label = Label(user_frame, text='Title', font=('areal', 15), padx=300, bg='#ffffff')
    title_label.grid(row=0, column=2)

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2',command=booking)
    rent_btn.place(x=540, y=270)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT definition FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            rent_details = tkinter.Message(top,text=result,font=('areal',15),width=900)
            rent_details.place(x=20, y=440)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result,font=('areal',15))
            condition1.place(x=20, y=550)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=600)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms2 FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result,font=('areal',15))
            condition1.place(x=20, y=650)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms3 FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result,font=('areal',15))
            condition1.place(x=20, y=700)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show3():
    top = Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")

    def booking():
        book = Toplevel(root)
        book.geometry("1000x700")
        book.title("Child Window")

        def user():
            book.destroy()
            import all_rent

        def rent():
            mysqldb = sqlite3.connect(database="brm.db")
            mycursor = mysqldb.cursor()
            image = image_field.get()
            title = title_field.get()
            address = address_field.get()
            contact = contact_field.get()
            payment_method = payment_clicked.get()
            definition = definition_field.get()
            toEmail = owner_field.get()
            sql = "INSERT INTO rent (name, title, address, contact, payment_method, email, owner) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (image, title, address, contact, payment_method, definition, toEmail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("", "Booking success")
            cur.execute("SELECT rent FROM std limit 2,1")
            rents = cur.fetchall()
            for x in rents:
                for rent in x:
                    price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
                    price_label.place(x=540, y=210)
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)", (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()

        def cancel():
            book.destroy()

        back_btn = Button(book, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=cancel)
        back_btn.place(x=60, y=50)

        login_label = Label(book, text="Booking", font=('areal', 30, 'bold'))
        login_label.place(x=430, y=50)

        ownerName = Label(book, text="Owner", font=('areal', 15, 'bold'))
        ownerName.place(x=480, y=295)
        owner_field = Entry(book, width=22, font=('areal', 15))
        owner_field.place(x=700, y=310, anchor='center')

        image = Label(book, text="Name", font=('areal', 15, 'bold'))
        image.place(x=80, y=145)
        image_field = Entry(book, textvariable="Chose file", width=22, font=('areal', 15))
        image_field.place(x=280, y=160, anchor='center')

        title = Label(book, text="Title", font=('areal', 15, 'bold'))
        title.place(x=80, y=215)
        title_field = Entry(book, width=22, font=('areal', 15))
        title_field.place(x=280, y=230, anchor='center')

        address = Label(book, text="Address", font=('areal', 15, 'bold'))
        address.place(x=75, y=305)
        address_field = Entry(book, width=22, font=('areal', 15))
        address_field.place(x=280, y=320, anchor='center')

        contact = Label(book, text="Contact", font=('areal', 15, 'bold'))
        contact.place(x=475, y=125)
        contact_field = Entry(book, width=22, font=('areal', 15))
        contact_field.place(x=700, y=150, anchor='center')

        definition = Label(book, text="Email", font=('areal', 15, 'bold'))
        definition.place(x=475, y=210)
        definition_field = Entry(book, width=22, font=('areal', 15))
        definition_field.place(x=700, y=225, anchor='center')

        payment_clicked = StringVar()
        payment_clicked.set('Select payment method')
        payment = OptionMenu(book, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
        payment.config(font=('areal', 12))
        payment.place(x=580, y=370)

        rent_btn = Button(book, text='Rent', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=rent)
        rent_btn.place(x=430, y=450)

    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            title_label = Label(top, text=result, font=('areal', 25, 'bold'))
            title_label.place(x=540, y=150)
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 2,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(top, text="")
    img_LabelFrame.place(x=120, y=150, width=200, height=150)
    # create the label_photo inside img_LabelFrame
    label_photo = Label(img_LabelFrame)
    label_photo.pack()
    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo
    results = cur.fetchall()
    for x in results:
        for result in x:
            heading_label = Label(top, text=result, font=('areal', 25, 'bold'))
            heading_label.place(x=540, y=150)

    cur.execute("SELECT email FROM std limit 2,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Contact: ", font=('areal', 15)).place(x=540, y=330)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=330)

    cur.execute("SELECT contact FROM std limit 2,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

    cur.execute("SELECT rent FROM std limit 2,1")
    rents = cur.fetchall()
    for x in rents:
        for rent in x:
            price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
            price_label.place(x=540, y=210)

    user_frame = LabelFrame(top, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
    user_frame.grid(pady=40)

    logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
    logo_label.grid(row=0, column=1, padx=20)

    title_label = Label(user_frame, text='Title', font=('areal', 15), padx=300, bg='#ffffff')
    title_label.grid(row=0, column=2)

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2', command=booking)
    rent_btn.place(x=540, y=270)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT definition FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            rent_details = tkinter.Message(top, text=result, font=('areal', 15), width=900)
            rent_details.place(x=20, y=440)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=550)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=600)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms2 FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=650)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms3 FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=700)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show4():
    top = Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")

    def booking():
        book = Toplevel(root)
        book.geometry("1000x700")
        book.title("Child Window")

        def user():
            book.destroy()
            import all_rent

        def rent():
            mysqldb = sqlite3.connect(database="brm.db")
            mycursor = mysqldb.cursor()
            image = image_field.get()
            title = title_field.get()
            address = address_field.get()
            contact = contact_field.get()
            payment_method = payment_clicked.get()
            definition = definition_field.get()
            toEmail = owner_field.get()
            sql = "INSERT INTO rent (name, title, address, contact, payment_method, email, owner) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (image, title, address, contact, payment_method, definition, toEmail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("", "Booking success")
            cur.execute("SELECT rent FROM std limit 3,1")
            rents = cur.fetchall()
            for x in rents:
                for rent in x:
                    price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
                    price_label.place(x=540, y=210)
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)", (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()

        def cancel():
            book.destroy()

        back_btn = Button(book, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=cancel)
        back_btn.place(x=60, y=50)

        login_label = Label(book, text="Booking", font=('areal', 30, 'bold'))
        login_label.place(x=430, y=50)

        ownerName = Label(book, text="Owner", font=('areal', 15, 'bold'))
        ownerName.place(x=480, y=295)
        owner_field = Entry(book, width=22, font=('areal', 15))
        owner_field.place(x=700, y=310, anchor='center')

        image = Label(book, text="Name", font=('areal', 15, 'bold'))
        image.place(x=80, y=145)
        image_field = Entry(book, textvariable="Chose file", width=22, font=('areal', 15))
        image_field.place(x=280, y=160, anchor='center')

        title = Label(book, text="Title", font=('areal', 15, 'bold'))
        title.place(x=80, y=215)
        title_field = Entry(book, width=22, font=('areal', 15))
        title_field.place(x=280, y=230, anchor='center')

        address = Label(book, text="Address", font=('areal', 15, 'bold'))
        address.place(x=75, y=305)
        address_field = Entry(book, width=22, font=('areal', 15))
        address_field.place(x=280, y=320, anchor='center')

        contact = Label(book, text="Contact", font=('areal', 15, 'bold'))
        contact.place(x=475, y=125)
        contact_field = Entry(book, width=22, font=('areal', 15))
        contact_field.place(x=700, y=150, anchor='center')

        definition = Label(book, text="Email", font=('areal', 15, 'bold'))
        definition.place(x=475, y=210)
        definition_field = Entry(book, width=22, font=('areal', 15))
        definition_field.place(x=700, y=225, anchor='center')

        payment_clicked = StringVar()
        payment_clicked.set('Select payment method')
        payment = OptionMenu(book, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
        payment.config(font=('areal', 12))
        payment.place(x=580, y=370)

        rent_btn = Button(book, text='Rent', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=rent)
        rent_btn.place(x=430, y=450)

    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            title_label = Label(top, text=result, font=('areal', 25, 'bold'))
            title_label.place(x=540, y=150)
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 3,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(top, text="")
    img_LabelFrame.place(x=120, y=150, width=200, height=150)
    # create the label_photo inside img_LabelFrame
    label_photo = Label(img_LabelFrame)
    label_photo.pack()
    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo
    results = cur.fetchall()
    for x in results:
        for result in x:
            heading_label = Label(top, text=result, font=('areal', 25, 'bold'))
            heading_label.place(x=540, y=150)

    cur.execute("SELECT email FROM std limit 3,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Contact: ", font=('areal', 15)).place(x=540, y=330)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=330)

    cur.execute("SELECT contact FROM std limit 3,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

    cur.execute("SELECT rent FROM std limit 3,1")
    rents = cur.fetchall()
    for x in rents:
        for rent in x:
            price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
            price_label.place(x=540, y=210)

    user_frame = LabelFrame(top, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
    user_frame.grid(pady=40)

    logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
    logo_label.grid(row=0, column=1, padx=20)

    title_label = Label(user_frame, text='Title', font=('areal', 15), padx=300, bg='#ffffff')
    title_label.grid(row=0, column=2)

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2', command=booking)
    rent_btn.place(x=540, y=270)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT definition FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            rent_details = tkinter.Message(top, text=result, font=('areal', 15), width=900)
            rent_details.place(x=20, y=440)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=550)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=600)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms2 FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=650)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms3 FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=700)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show5():
    top = Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")

    def booking():
        book = Toplevel(root)
        book.geometry("1000x700")
        book.title("Child Window")

        def user():
            book.destroy()
            import all_rent

        def rent():
            mysqldb = sqlite3.connect(database="brm.db")
            mycursor = mysqldb.cursor()
            image = image_field.get()
            title = title_field.get()
            address = address_field.get()
            contact = contact_field.get()
            payment_method = payment_clicked.get()
            definition = definition_field.get()
            toEmail = owner_field.get()
            sql = "INSERT INTO rent (name, title, address, contact, payment_method, email, owner) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (image, title, address, contact, payment_method, definition, toEmail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("", "Booking success")
            cur.execute("SELECT rent FROM std limit 4,1")
            rents = cur.fetchall()
            for x in rents:
                for rent in x:
                    price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
                    price_label.place(x=540, y=210)
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)", (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()

        def cancel():
            book.destroy()

        back_btn = Button(book, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=cancel)
        back_btn.place(x=60, y=50)

        login_label = Label(book, text="Booking", font=('areal', 30, 'bold'))
        login_label.place(x=430, y=50)

        ownerName = Label(book, text="Owner", font=('areal', 15, 'bold'))
        ownerName.place(x=480, y=295)
        owner_field = Entry(book, width=22, font=('areal', 15))
        owner_field.place(x=700, y=310, anchor='center')

        image = Label(book, text="Name", font=('areal', 15, 'bold'))
        image.place(x=80, y=145)
        image_field = Entry(book, textvariable="Chose file", width=22, font=('areal', 15))
        image_field.place(x=280, y=160, anchor='center')

        title = Label(book, text="Title", font=('areal', 15, 'bold'))
        title.place(x=80, y=215)
        title_field = Entry(book, width=22, font=('areal', 15))
        title_field.place(x=280, y=230, anchor='center')

        address = Label(book, text="Address", font=('areal', 15, 'bold'))
        address.place(x=75, y=305)
        address_field = Entry(book, width=22, font=('areal', 15))
        address_field.place(x=280, y=320, anchor='center')

        contact = Label(book, text="Contact", font=('areal', 15, 'bold'))
        contact.place(x=475, y=125)
        contact_field = Entry(book, width=22, font=('areal', 15))
        contact_field.place(x=700, y=150, anchor='center')

        definition = Label(book, text="Email", font=('areal', 15, 'bold'))
        definition.place(x=475, y=210)
        definition_field = Entry(book, width=22, font=('areal', 15))
        definition_field.place(x=700, y=225, anchor='center')

        payment_clicked = StringVar()
        payment_clicked.set('Select payment method')
        payment = OptionMenu(book, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
        payment.config(font=('areal', 12))
        payment.place(x=580, y=370)

        rent_btn = Button(book, text='Rent', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=rent)
        rent_btn.place(x=430, y=450)

    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            title_label = Label(top, text=result, font=('areal', 25, 'bold'))
            title_label.place(x=540, y=150)
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 4,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(top, text="")
    img_LabelFrame.place(x=120, y=150, width=200, height=150)
    # create the label_photo inside img_LabelFrame
    label_photo = Label(img_LabelFrame)
    label_photo.pack()
    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo
    results = cur.fetchall()
    for x in results:
        for result in x:
            heading_label = Label(top, text=result, font=('areal', 25, 'bold'))
            heading_label.place(x=540, y=150)

    cur.execute("SELECT email FROM std limit 4,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Contact: ", font=('areal', 15)).place(x=540, y=330)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=330)

    cur.execute("SELECT contact FROM std limit 4,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

    cur.execute("SELECT rent FROM std limit 4,1")
    rents = cur.fetchall()
    for x in rents:
        for rent in x:
            price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
            price_label.place(x=540, y=210)

    user_frame = LabelFrame(top, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
    user_frame.grid(pady=40)

    logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
    logo_label.grid(row=0, column=1, padx=20)

    title_label = Label(user_frame, text='Title', font=('areal', 15), padx=300, bg='#ffffff')
    title_label.grid(row=0, column=2)

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2', command=booking)
    rent_btn.place(x=540, y=270)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT definition FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            rent_details = tkinter.Message(top, text=result, font=('areal', 15), width=900)
            rent_details.place(x=20, y=440)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=550)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=600)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms2 FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=650)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms3 FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=700)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show6():
    top = Toplevel(root)
    top.geometry("1000x700")
    top.title("Child Window")

    def booking():
        book = Toplevel(root)
        book.geometry("1000x700")
        book.title("Child Window")

        def user():
            book.destroy()
            import all_rent

        def rent():
            mysqldb = sqlite3.connect(database="brm.db")
            mycursor = mysqldb.cursor()
            image = image_field.get()
            title = title_field.get()
            address = address_field.get()
            contact = contact_field.get()
            payment_method = payment_clicked.get()
            definition = definition_field.get()
            toEmail = owner_field.get()
            sql = "INSERT INTO rent (name, title, address, contact, payment_method, email, owner) VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (image, title, address, contact, payment_method, definition, toEmail)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("", "Booking success")
            cur.execute("SELECT rent FROM std limit 1")
            rents = cur.fetchall()
            for x in rents:
                for rent in x:
                    price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
                    price_label.place(x=540, y=210)
            admin_pay = rent * 10
            admin_amount = admin_pay / 100
            owner_amount = rent - admin_amount
            mycursor.execute("INSERT INTO amount(ownerAmount,adminAmount,email,mainAmount) VALUES (?, ?, ?, ?)", (owner_amount, admin_amount, owner_field.get(), rent))
            mysqldb.commit()

        def cancel():
            book.destroy()

        back_btn = Button(book, text='Back', padx=10, font=('areal', 10), fg='#ffffff', bg='#ff0000', command=cancel)
        back_btn.place(x=60, y=50)

        login_label = Label(book, text="Booking", font=('areal', 30, 'bold'))
        login_label.place(x=430, y=50)

        ownerName = Label(book, text="To(email)", font=('areal', 15, 'bold'))
        ownerName.place(x=480, y=295)
        owner_field = Entry(book, width=22, font=('areal', 15))
        owner_field.place(x=700, y=310, anchor='center')

        image = Label(book, text="Name", font=('areal', 15, 'bold'))
        image.place(x=80, y=145)
        image_field = Entry(book, textvariable="Chose file", width=22, font=('areal', 15))
        image_field.place(x=280, y=160, anchor='center')

        title = Label(book, text="Title", font=('areal', 15, 'bold'))
        title.place(x=80, y=215)
        title_field = Entry(book, width=22, font=('areal', 15))
        title_field.place(x=280, y=230, anchor='center')

        address = Label(book, text="Address", font=('areal', 15, 'bold'))
        address.place(x=75, y=305)
        address_field = Entry(book, width=22, font=('areal', 15))
        address_field.place(x=280, y=320, anchor='center')

        contact = Label(book, text="Contact", font=('areal', 15, 'bold'))
        contact.place(x=475, y=125)
        contact_field = Entry(book, width=22, font=('areal', 15))
        contact_field.place(x=700, y=150, anchor='center')

        definition = Label(book, text="From(email)", font=('areal', 15, 'bold'))
        definition.place(x=475, y=210)
        definition_field = Entry(book, width=22, font=('areal', 15))
        definition_field.place(x=700, y=225, anchor='center')

        payment_clicked = StringVar()
        payment_clicked.set('Select payment method')
        payment = OptionMenu(book, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
        payment.config(font=('areal', 12))
        payment.place(x=580, y=370)

        rent_btn = Button(book, text='Rent', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=rent)
        rent_btn.place(x=430, y=450)

    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 5,1")
    results = my_conn.fetchall()
    for x in results:
        global result
        for result in x:
            title_label = Label(top, text=result, font=('areal', 25, 'bold'))
            title_label.place(x=540, y=150)
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 5,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(top, text="")
    img_LabelFrame.place(x=120, y=150, width=200, height=150)
    # create the label_photo inside img_LabelFrame
    label_photo = Label(img_LabelFrame)
    label_photo.pack()
    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo
    results = cur.fetchall()
    for x in results:
        for result in x:
            heading_label = Label(top, text=result, font=('areal', 25, 'bold'))
            heading_label.place(x=540, y=150)

    cur.execute("SELECT email FROM std limit 5,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Contact: ", font=('areal', 15)).place(x=540, y=330)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=330)

    cur.execute("SELECT contact FROM std limit 5,1")
    emails = cur.fetchall()
    for x in emails:
        for email in x:
            ownerEmail_label = Label(top, text="Phone: ", font=('areal', 15)).place(x=540, y=370)
            onwerEmail = Label(top, text=email, font=('areal', 15)).place(x=630, y=370)

    cur.execute("SELECT rent FROM std  limit 5,1")
    rents = cur.fetchall()
    for x in rents:
        for rent in x:
            price_label = Label(top, text=rent, font=('areal', 25, 'bold'), fg='#FF8A00')
            price_label.place(x=540, y=210)

    user_frame = LabelFrame(top, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
    user_frame.grid(pady=40)

    logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
    logo_label.grid(row=0, column=1, padx=20)

    title_label = Label(user_frame, text='Title', font=('areal', 15), padx=300, bg='#ffffff')
    title_label.grid(row=0, column=2)

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2',command=booking)
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms1 FROM std limit 5,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=600)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms2 FROM std limit 5,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=650)

    my_conn = my_connect.cursor()
    my_conn.execute("SELECT turms3 FROM std limit 5,1")
    results = my_conn.fetchall()
    for x in results:
        for result in x:
            condition1 = Label(top, text=result, font=('areal', 15))
            condition1.place(x=20, y=700)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo


pageTitle  = Label(root,text='All rent',font=('areal',25,'bold')).place(x=480,y=20)

#1
user_frame = Canvas(root, width=220, border=0,bg='#ffffff')
user_frame.place(x=100,y=100)
#Image
con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("SELECT image FROM std limit 1")
row = cur.fetchone()
# photo = ImageTk.PhotoImage(data=row[0])
img_LabelFrame = ttk.LabelFrame(root, text="")
img_LabelFrame.place(x=112, y=93, width=200, height=150)
# create the label_photo inside img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()
if row:
    photo = ImageTk.PhotoImage(data=row[0])
    label_photo.config(image=photo)
    label_photo.image = photo
cur.execute("SELECT title FROM std limit 1")
showTitle = cur.fetchall()
for x in showTitle:
    for title1 in x:
        label = Label(user_frame, text=title1).place(x=75,y=150)
btn = Button(user_frame,text='See more',command=show1).place(x=82,y=210)

#2
user_frame = Canvas(root, width=220, border=0,bg='#ffffff')
user_frame.place(x=400,y=100)
#Image
con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("SELECT image FROM std limit 1,1")
row = cur.fetchone()
# photo = ImageTk.PhotoImage(data=row[0])
img_LabelFrame = ttk.LabelFrame(root, text="")
img_LabelFrame.place(x=412, y=93, width=200, height=150)
# create the label_photo inside img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()
if row:
    photo = ImageTk.PhotoImage(data=row[0])
    label_photo.config(image=photo)
    label_photo.image = photo
cur.execute("SELECT title FROM std limit 1,1")
showTitle = cur.fetchall()
for x in showTitle:
    for title2 in x:
        label = Label(user_frame, text=title2).place(x=80,y=150)
btn = Button(user_frame,text='See more',command=show2).place(x=82,y=210)

#3
user_frame = Canvas(root, width=220, border=0,bg='#ffffff')
user_frame.place(x=690,y=100)
#Image
con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("SELECT image FROM std limit 2,1")
row = cur.fetchone()
# photo = ImageTk.PhotoImage(data=row[0])
img_LabelFrame = ttk.LabelFrame(root, text="")
img_LabelFrame.place(x=702, y=93, width=200, height=150)
# create the label_photo inside img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()
if row:
    photo = ImageTk.PhotoImage(data=row[0])
    label_photo.config(image=photo)
    label_photo.image = photo
cur.execute("SELECT title FROM std limit 2,1")
showTitle = cur.fetchall()
for x in showTitle:
    for title3 in x:
        label = Label(user_frame, text=title3).place(x=60,y=150)
btn = Button(user_frame,text='See more',command=show3).place(x=82,y=210)

#4
user_frame = Canvas(root, width=220, border=0,bg='#ffffff')
user_frame.place(x=100,y=400)
#Image
con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("SELECT image FROM std limit 3,1")
row = cur.fetchone()
# photo = ImageTk.PhotoImage(data=row[0])
img_LabelFrame = ttk.LabelFrame(root, text="")
img_LabelFrame.place(x=112, y=395, width=200, height=150)
# create the label_photo inside img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()
if row:
    photo = ImageTk.PhotoImage(data=row[0])
    label_photo.config(image=photo)
    label_photo.image = photo
cur.execute("SELECT title FROM std limit 3,1")
showTitle = cur.fetchall()
for x in showTitle:
    for title4 in x:
        label = Label(user_frame, text=title4).place(x=82,y=150)
btn = Button(user_frame,text='See more',command=show4).place(x=82,y=210)


#5
user_frame = Canvas(root, width=220, border=0,bg='#ffffff')
user_frame.place(x=400,y=400)
#Image
con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("SELECT image FROM std limit 4,1")
row = cur.fetchone()
# photo = ImageTk.PhotoImage(data=row[0])
img_LabelFrame = ttk.LabelFrame(root, text="")
img_LabelFrame.place(x=412, y=395, width=200, height=150)
# create the label_photo inside img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()
if row:
    photo = ImageTk.PhotoImage(data=row[0])
    label_photo.config(image=photo)
    label_photo.image = photo
cur.execute("SELECT title FROM std limit 4,1")
showTitle = cur.fetchall()
for x in showTitle:
    for title5 in x:
        label = Label(user_frame, text=title5).place(x=80,y=150)
btn = Button(user_frame,text='See more',command=show5).place(x=82,y=210)

#6
user_frame = Canvas(root, width=220, border=0,bg='#ffffff')
user_frame.place(x=690,y=400)
#Image
con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("SELECT image FROM std limit 5,1")
row = cur.fetchone()
# photo = ImageTk.PhotoImage(data=row[0])
img_LabelFrame = ttk.LabelFrame(root, text="")
img_LabelFrame.place(x=702, y=395, width=200, height=150)
# create the label_photo inside img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()
if row:
    photo = ImageTk.PhotoImage(data=row[0])
    label_photo.config(image=photo)
    label_photo.image = photo
cur.execute("SELECT title FROM std limit 5,1")
showTitle = cur.fetchall()
for x in showTitle:
    for title6 in x:
        label = Label(user_frame, text=title6).place(x=80,y=150)
btn = Button(user_frame,text='See more',command=show6).place(x=82,y=210)

btn = Button(root,text='Back',font=('areal',10,'bold') ,bg='#ff0000', fg='#ffffff', padx=20,command=back).place(x=20, y=30)
con = sqlite3.connect(database="brm.db")
cur = con.cursor()

root.mainloop()