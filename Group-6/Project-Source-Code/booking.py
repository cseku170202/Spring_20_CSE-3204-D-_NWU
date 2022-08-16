from tkinter import *
import os
import mysql.connector
from tkinter import messagebox
import sqlite3

booking = Tk()
booking.geometry('950x700')

def user():
    booking.destroy()
    import user

def rent():
    mysqldb = sqlite3.connect(database="brm.db")
    mycursor = mysqldb.cursor()
    image = image_field.get()
    title = title_field.get()
    address = address_field.get()
    contact = contact_field.get()
    payment_method = payment_clicked.get()
    definition = definition_field.get()
    sql = "INSERT INTO rent (name, title, address, contact, payment_method, email) VALUES (?, ?, ?, ?, ?, ?)"
    val = (image, title, address, contact, payment_method, definition)
    mycursor.execute(sql, val)
    mysqldb.commit()
    messagebox.showinfo("", "Booking success")

def cancel():
    booking.destroy()
    import all_rent

back_btn = Button(booking, text='Back', padx=10, font=('areal',10),fg='#ffffff', bg='#ff0000', command=cancel)
back_btn.place(x=60, y=50)

login_label = Label(booking, text = "Booking", font = ('areal',30,'bold'))
login_label.place(x=430, y=50)

image = Label(booking, text = "Name", font = ('areal',15,'bold'))
image.place(x=80, y=145)
image_field = Entry(booking, textvariable="Chose file", width=22, font=('areal',15))
image_field.place(x=280, y=160, anchor='center')

title = Label(booking, text = "Title", font = ('areal',15,'bold'))
title.place(x=80, y=215)
title_field = Entry(booking, width=22, font=('areal',15))
title_field.place(x=280, y=230, anchor='center')

address = Label(booking, text = "Address", font = ('areal',15,'bold'))
address.place(x=75, y=305)
address_field = Entry(booking, width=22, font=('areal',15))
address_field.place(x=280, y=320, anchor='center')

contact = Label(booking, text = "Contact", font = ('areal',15,'bold'))
contact.place(x=475, y=125)
contact_field = Entry(booking, width=22, font=('areal',15))
contact_field.place(x=700, y=150, anchor='center')

definition = Label(booking, text = "Email", font = ('areal',15,'bold'))
definition.place(x=475, y=210)
definition_field = Entry(booking, width=22, font=('areal',15))
definition_field.place(x=700, y=225, anchor='center')

payment_clicked = StringVar()
payment_clicked.set('Select payment method')
payment = OptionMenu(booking, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
payment.config(font=('areal',12))
payment.place(x=580, y=295)

rent_btn = Button(booking, text='Rent', padx=30, font=('areal',15),fg='#ffffff', bg='#15BDF2',command=rent)
rent_btn.place(x=430, y=390)

booking.mainloop()