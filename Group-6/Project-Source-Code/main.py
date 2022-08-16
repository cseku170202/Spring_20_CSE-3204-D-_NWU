from tkinter import *
from tkinter import messagebox, ttk
from subprocess import call
import sqlite3

from PIL import ImageTk

main = Tk()

def login():
    mysqldb = sqlite3.connect(database="brm.db")
    mycursor = mysqldb.cursor()
    Email = email_field.get()
    Pass = password_field.get()

    sql = "select * from user_data where Email = ? and Pass = ?"
    mycursor.execute(sql, [(Email), (Pass)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login success")
        main.destroy()
        call(["python", "user.py"])
        return True
    else:
        messagebox.showinfo("", "Incorrect username or password")
        return False

def adminLogin():
    mysqldb = sqlite3.connect(database="brm.db")
    mycursor = mysqldb.cursor()
    Email = email_field.get()
    Pass = password_field.get()

    sql = "select * from admin_login where Email = ? and Pass = ?"
    mycursor.execute(sql, [(Email), (Pass)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login success")
        main.destroy()
        call(["python", "admin.py"])
    else:
        messagebox.showinfo("", "Incorrect username or password")
        return True

def ownerLogin():
    mysqldb = sqlite3.connect(database="brm.db")
    mycursor = mysqldb.cursor()
    Email = email_field.get()
    Pass = password_field.get()

    sql = "select * from owner where email = ? and password = ?"
    mycursor.execute(sql, [(Email), (Pass)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login success")
        owner = Toplevel(main)
        owner.geometry("1000x700")
        owner.title("Child Window")

        def closePop():
            owner.destroy()

        def myPost():
            post = Toplevel(main)
            post.geometry("1000x700")
            post.title("Child Window")

            def closePop():
                post.destroy()

            con = sqlite3.connect(database="brm.db")
            cur = con.cursor()
            for x in range(4):
                con = sqlite3.connect(database="brm.db")
                cur = con.cursor()
                Email = email_field.get()
                cur.execute("SELECT image FROM std WHERE email = ?", (Email,))
                row = cur.fetchone()
                nameSql = "SELECT title FROM std WHERE email = ?"
                cur.execute(nameSql, [(Email)])
                titles = cur.fetchall()
                for x in titles:
                    for title in x:
                        img_LabelFrame = ttk.LabelFrame(post, text="")
                        img_LabelFrame.pack()
                        label_photo = Label(img_LabelFrame)
                        label_photo.pack()
                        PostTitle = Label(post, text=title, font=("Arial", 15,))
                        PostTitle.pack()
                        btn = Button(post, text='See more').pack()
                if row:
                    photo = ImageTk.PhotoImage(data=row[0])
                    label_photo.config(image=photo)
                    label_photo.image = photo

        def notification():
            note = Toplevel(main)
            note.geometry("1000x700")
            note.title("Child Window")
            def back():
                note.destroy()
            Title = Label(note, text='Notification', font=('areal', 25, 'bold')).pack(pady=20)

            my_connect = sqlite3.connect(database='brm.db')
            my_conn = my_connect.cursor()
            my_conn.execute("select name from rent where owner = ?",[(Email)])
            takes = my_conn.fetchall()
            for x in takes:
                for take in x:
                     nameLabel = Label(note,text=take + ("rent your home"),font=('areal',15)).pack(pady=10)
                    # my_conn.execute("SELECT title FROM rent where email = ?", [(take)])
                    # results = my_conn.fetchall()
                    # print(results)

            backBtn = Button(note, text="Back", padx=20, font=('areal', 15), bg='#ff0000', fg='#ffffff',
                             command=back)
            backBtn.place(x=50, y=30)

        def amount():
            am = Toplevel(main)
            am.geometry('550x700')
            Email = email_field.get()
            Payment = Label(am, text="Payment", font=('areal', 25, 'bold'), pady=15).grid(row=0, column=2)
            con = sqlite3.connect(database="brm.db")
            cur = con.cursor()
            cur.execute("select id from amount")
            count = cur.fetchall()
            for x in range(len(count)):
                cur.execute("select mainAmount from amount where email = ?", [(Email)])
                mainAmo = cur.fetchall()
                rowCount = 1
                for x in mainAmo:
                    for mainAm in x:
                        mainAmount = Label(am, text=("Payment: " + mainAm), font=('areal', 15), borderwidth=1, relief="solid",padx=10).grid(row=rowCount, column=1)
                        rowCount= rowCount+1
                cur.execute("SELECT ownerAmount FROM amount WHERE email = ?", [(Email)])
                amounts = cur.fetchall()
                rowTest = 1
                for x in amounts:
                    for amount in x:
                        ownerAmount = Label(am, text=("Your amount: " + amount), font=('areal', 15), borderwidth=1, relief="solid",padx=10).grid(row=rowTest,column=2)
                        rowTest = rowTest+1
                cur.execute("SELECT adminAmount FROM amount WHERE email = ?", [(Email)])
                fees = cur.fetchall()
                againTest = 1
                for x in fees:
                    for fee in x:
                        adminAmount = Label(am, text=("Admin amount: " + fee), font=('areal', 15), borderwidth=1, relief="solid",padx=10).grid(row=againTest,column=3)
                        againTest = againTest + 1

        con = sqlite3.connect(database="brm.db")
        cur = con.cursor()
        Email = email_field.get()
        nameSql = "SELECT name FROM owner WHERE email = ?"
        cur.execute(nameSql, [(Email)])
        names = cur.fetchall()
        for x in names:
            for name in x:
                name_show = Label(owner, text=name, font=('areal', 15)).place(x=160, y=380)
                winTitle = Label(owner, text="Welcome " + name, font=('areal', 25, 'bold')).place(x=400, y=20)
        imgSql = "SELECT image FROM owner WHERE email = ?"
        cur.execute(imgSql, [(Email)])
        row = cur.fetchone()
        # photo = ImageTk.PhotoImage(data=row[0])

        img_LabelFrame = ttk.LabelFrame(owner, text="")
        img_LabelFrame.place(x=80, y=110, width=250, height=250)
        # create the label_photo inside img_LabelFrame
        label_photo = Label(img_LabelFrame)
        label_photo.pack()
        if row:
            photo = ImageTk.PhotoImage(data=row[0])
            label_photo.config(image=photo)
            label_photo.image = photo

        # owner catagories
        post_btn = Button(owner, text='My post', font=('areal', 20, 'bold'), width=30, command=myPost).place(x=400,
                                                                                                             y=100)
        notification_btn = Button(owner, text='Notification', font=('areal', 20, 'bold'), width=30,
                                  command=notification).place(x=400,
                                                              y=225)
        amount_btn = Button(owner, text='Amount', font=('areal', 20, 'bold'), width=30, command=amount).place(x=400,
                                                                                                              y=360)
        backBtn = Button(owner, text='Back', font=('areal', 15, 'bold'), padx=10, bg='#ff0000', fg='#ffffff',
                         command=closePop).place(x=880, y=20)
        return True
    else:
        messagebox.showinfo("", "Incorrect username or password")
        return False

def sign_up():
    main.destroy()
    import sign_up

login_label = Label(main, text = "Login", font = ('areal',30,'bold'))
login_label.place(x=300, y=80, anchor='center')

email_label = Label(main,text="Email",font=('areal',15))
email_label.place(x=100,y=145)
email_field = Entry(main, width=30, font=('areal',15))
email_field.place(x=350, y=160, anchor='center')

password_label = Label(main, text = "Password", font = ('areal',15))
password_label.place(x=120, y=240, anchor='center')
password_field = Entry(main, width=30, font=('areal',15))
password_field.place(x=350, y=240, anchor='center')
password_field.config(show='*')

login_btn = Button(main, text='Login', padx=40, font=('areal',18),fg='#ffffff', bg='#15BDF2', command=login)
login_btn.place(x=220, y=360)

admin_btn = Button(main, text='Admin login', padx=5, font=('areal',18),fg='#ffffff', bg='#15BDF2', command=adminLogin)
admin_btn.place(x=220, y=430)

owner_btn = Button(main, text='Owner login', padx=5, font=('areal',18),fg='#ffffff', bg='#15BDF2', command=ownerLogin)
owner_btn.place(x=220, y=500)

signUp_btn = Button(main, text='Signup', padx=10, font=('areal',15),fg='#000000', bg='#00ff00', command=sign_up)
signUp_btn.place(x=460, y=60)

main.geometry('600x700')

main.mainloop()