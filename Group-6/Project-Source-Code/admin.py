import tkinter
from tkinter import *
import os
import sqlite3
from tkinter import ttk
from tkinter import ttk, messagebox
from tkinter import messagebox, filedialog, ttk
from io import BytesIO
from PIL import ImageTk

admin = Tk()
admin.geometry('1000x700')

def notification():
    admin.destroy()
    import notification

def posts():
    all = Toplevel(admin)
    all.geometry('1020x800')
    # 1
    user_frame = Canvas(all, width=220, border=0, bg='#ffffff')
    user_frame.place(x=100, y=100)
    # Image
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(all, text="")
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
            label = Label(user_frame, text=title1).place(x=75, y=150)
    btn = Button(user_frame, text='See more', command=show1).place(x=85, y=210)

    # 2
    user_frame = Canvas(all, width=220, border=0, bg='#ffffff')
    user_frame.place(x=400, y=100)
    # Image
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 1,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(all, text="")
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
            label = Label(user_frame, text=title2).place(x=80, y=150)
    btn = Button(user_frame, text='See more', command=show1).place(x=85, y=210)

    # 3
    user_frame = Canvas(all, width=220, border=0, bg='#ffffff')
    user_frame.place(x=690, y=100)
    # Image
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 2,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(all, text="")
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
            label = Label(user_frame, text=title3).place(x=82, y=150)
    btn = Button(user_frame, text='See more', command=show1).place(x=85, y=210)

    # 4
    user_frame = Canvas(all, width=220, border=0, bg='#ffffff')
    user_frame.place(x=100, y=400)
    # Image
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 3,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(all, text="")
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
            label = Label(user_frame, text=title4).place(x=82, y=150)
    btn = Button(user_frame, text='See more', command=show1).place(x=85, y=210)

    # 5
    user_frame = Canvas(all, width=220, border=0, bg='#ffffff')
    user_frame.place(x=400, y=400)
    # Image
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 4,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(all, text="")
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
            label = Label(user_frame, text=title5).place(x=80, y=150)
    btn = Button(user_frame, text='See more', command=show1).place(x=85, y=210)

    # 6
    user_frame = Canvas(all, width=220, border=0, bg='#ffffff')
    user_frame.place(x=690, y=400)
    # Image
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    cur.execute("SELECT image FROM std limit 5,1")
    row = cur.fetchone()
    # photo = ImageTk.PhotoImage(data=row[0])
    img_LabelFrame = ttk.LabelFrame(all, text="")
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
            label = Label(user_frame, text=title6).place(x=80, y=150)
    btn = Button(user_frame, text='See more', command=show1).place(x=85, y=210)

    btn = Button(all, text='Back', font=('areal', 10, 'bold'), bg='#ff0000', fg='#ffffff', padx=20,command=back).place(x=20, y=30)

def payment():
    pay = Toplevel(admin)
    pay.geometry('850x350')
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    Payment = Label(pay, text="Payment Distribution", font=('areal', 25,'bold'),pady=15).grid(row=0,column=2)
    cur.execute("select id from amount")
    count = cur.fetchall()
    for x in range(len(count)):
        cur.execute("select mainAmount from amount")
        mainAmo = cur.fetchall()
        rowCount = 1
        for x in mainAmo:
            for mainAm in x:
                mainAmount = Label(pay, text=("Payment: " + mainAm), font=('areal', 15), borderwidth=1, relief="solid").grid(row=rowCount,column=1)
                rowCount = rowCount + 1
        cur.execute("SELECT ownerAmount FROM amount")
        amounts = cur.fetchall()
        rowTest = 1
        for x in amounts:
            for amount in x:
                ownerAmount = Label(pay, text=("Owner amount: " + amount), font=('areal', 15), borderwidth=1, relief="solid").grid(row=rowTest,column=2)
                rowTest = rowTest + 1
        cur.execute("SELECT adminAmount FROM amount")
        fees = cur.fetchall()
        againTest = 1
        for x in fees:
            for fee in x:
                adminAmount = Label(pay, text=("Your amount: " + fee), font=('areal', 15), borderwidth=1, relief="solid").grid(row=againTest,column=3)
                againTest = againTest + 1

showBtn = Button(admin,text="Show posts",font=('areal',20,'bold'),command=posts).place(x=430,y=130)
btnNotification = Button(admin, text='Notification', font=('areal', 20, 'bold'), command=notification).place(x=430, y=230)
payment = Button(admin, text='Payment', font=('areal', 20, 'bold'),padx=20, command=payment).place(x=430, y=330)

def back():
    admin.destroy()
    import main

def booking():
    admin.destroy()
    import booking

def show1():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 1")
    results = my_conn.fetchall()
    for x in results:
        global result
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

    cur.execute("SELECT rent FROM std  limit 1")
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

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2')
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    condition1 = Label(top, text='Condition 1 will given here')
    condition1.place(x=20, y=550)

    condition2 = Label(top, text='Condition 2 will given here')
    condition2.place(x=20, y=600)

    condition3 = Label(top, text='Condition 3 will given here')
    condition3.place(x=20, y=650)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show2():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 1,1")
    results = my_conn.fetchall()
    for x in results:
        global result
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

    cur.execute("SELECT rent FROM std  limit 1,1")
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

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2')
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    condition1 = Label(top, text='Condition 1 will given here')
    condition1.place(x=20, y=550)

    condition2 = Label(top, text='Condition 2 will given here')
    condition2.place(x=20, y=600)

    condition3 = Label(top, text='Condition 3 will given here')
    condition3.place(x=20, y=650)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show3():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 2,1")
    results = my_conn.fetchall()
    for x in results:
        global result
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

    cur.execute("SELECT rent FROM std  limit 2,1")
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

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2')
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    condition1 = Label(top, text='Condition 1 will given here')
    condition1.place(x=20, y=550)

    condition2 = Label(top, text='Condition 2 will given here')
    condition2.place(x=20, y=600)

    condition3 = Label(top, text='Condition 3 will given here')
    condition3.place(x=20, y=650)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show4():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 3,1")
    results = my_conn.fetchall()
    for x in results:
        global result
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

    cur.execute("SELECT rent FROM std  limit 3,1")
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

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2')
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    condition1 = Label(top, text='Condition 1 will given here')
    condition1.place(x=20, y=550)

    condition2 = Label(top, text='Condition 2 will given here')
    condition2.place(x=20, y=600)

    condition3 = Label(top, text='Condition 3 will given here')
    condition3.place(x=20, y=650)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show5():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()
    my_conn.execute("SELECT title FROM std limit 4,1")
    results = my_conn.fetchall()
    for x in results:
        global result
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

    cur.execute("SELECT rent FROM std  limit 4,1")
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

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2')
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    condition1 = Label(top, text='Condition 1 will given here')
    condition1.place(x=20, y=550)

    condition2 = Label(top, text='Condition 2 will given here')
    condition2.place(x=20, y=600)

    condition3 = Label(top, text='Condition 3 will given here')
    condition3.place(x=20, y=650)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def show6():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
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

    rent_btn = Button(top, text='Rent', font=('areal', 15), padx=25, fg='#ffffff', bg='#15BDF2')
    rent_btn.place(x=540, y=270)

    rent_details = tkinter.Message(top,
                                   text='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry`s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',
                                   width=900)
    rent_details.place(x=20, y=440)

    condition1 = Label(top, text='Condition 1 will given here')
    condition1.place(x=20, y=550)

    condition2 = Label(top, text='Condition 2 will given here')
    condition2.place(x=20, y=600)

    condition3 = Label(top, text='Condition 3 will given here')
    condition3.place(x=20, y=650)

    if row:
        photo = ImageTk.PhotoImage(data=row[0])
        label_photo.config(image=photo)
        label_photo.image = photo

def update1():
    top = Toplevel(admin)
    top.geometry("1000x700")
    top.title("Child Window")
    my_connect = sqlite3.connect(database='brm.db')
    my_conn = my_connect.cursor()

    title = Label(top, text="Title", font=('areal', 15, 'bold'))
    title.place(x=80, y=225)
    title_field = Entry(top, width=22, font=('areal', 15))
    title_field.place(x=280, y=235, anchor='center')

    address = Label(top, text="Address", font=('areal', 15, 'bold'))
    address.place(x=75, y=125)
    address_field = Entry(top, width=22, font=('areal', 15))
    address_field.place(x=280, y=135, anchor='center')

    contact = Label(top, text="Contact", font=('areal', 15, 'bold'))
    contact.place(x=475, y=125)
    contact_field = Entry(top, width=22, font=('areal', 15))
    contact_field.place(x=700, y=150, anchor='center')

    definition = Label(top, text="Definition", font=('areal', 15, 'bold'))
    definition.place(x=475, y=210)
    definition_field = Entry(top, width=22, font=('areal', 15))
    definition_field.place(x=700, y=225, anchor='center')

    payment_clicked = StringVar()
    payment_clicked.set('Select payment method')
    payment = OptionMenu(top, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
    payment.config(font=('areal', 12))
    payment.place(x=580, y=295)

    turms1 = Label(top, text="Turms1", font=('areal', 15, 'bold'))
    turms1.place(x=70, y=400)
    turms1_field = Entry(top, width=22, font=('areal', 15))
    turms1_field.place(x=280, y=420, anchor='center')

    turms2 = Label(top, text="Turms2", font=('areal', 15, 'bold'))
    turms2.place(x=485, y=395)
    turms2_field = Entry(top, width=22, font=('areal', 15))
    turms2_field.place(x=700, y=410, anchor='center')

    rentLabel = Label(top, text="Rent", font=('areal', 15, 'bold'))
    rentLabel.place(x=490, y=470)
    rent_field = Entry(top, width=22, font=('areal', 15))
    rent_field.place(x=700, y=485, anchor='center')

    turms3 = Label(top, text="Turms3", font=('areal', 15, 'bold'))
    turms3.place(x=70, y=475)
    turms3_field = Entry(top, width=22, font=('areal', 15))
    turms3_field.place(x=280, y=490, anchor='center')

    def add():
        con = sqlite3.connect(database="brm.db")
        cur = con.cursor()
        takeTitle = title_field.get()
        try:
            cur.execute(
                "update std set (title = ?,address = ?,contact = ?,payment_method = ?,definition = ?,turms1 = ?,turms2 = ?,turms3 = ?,rent = ? where id = 3",address_field.get(),contact_field.get(),payment_clicked.get(),definition_field.get(),turms1_field.get(),
                    turms2_field.get(),
                    turms3_field.get(),
                    rent_field.get() )
            con.commit()
            messagebox.showinfo("Success", "Posted Successfully")
        except Exception as ex:
            messagebox.showerror("Error", f"Error duo to {str(ex)}")

    rent_btn = Button(top, text='Update', padx=30, font=('areal', 15), fg='#ffffff', bg='#15BDF2', command=add)
    rent_btn.place(x=430, y=580)

pageTitle  = Label(admin,text='Admin',font=('areal',25,'bold')).place(x=460,y=20)



admin.mainloop()