from tkinter import *
from tkinter import messagebox
from subprocess import call
import sqlite3

main = Tk()

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

def sign_up():
    main.destroy()
    import sign_up

login_label = Label(main, text = "Admin login", font = ('areal',30,'bold'))
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

login_btn = Button(main, text='Login', padx=35, font=('areal',18),fg='#ffffff', bg='#15BDF2', command=login)
login_btn.place(x=220, y=360)

signUp_btn = Button(main, text='Signup', padx=25, font=('areal',18),fg='#ffffff', bg='#15BDF2', command=sign_up)
signUp_btn.place(x=220, y=460)

main.geometry('600x700')

main.mainloop()