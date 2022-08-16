import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
import tkinter as tk
from PIL import ImageTk, Image
import tkinter
user = Tk()

def show():
    user.destroy()
    import all_rent

def post():
    user.destroy()
    import post

def back():
    user.destroy()
    import main

user.geometry('1000x700')
user_frame = LabelFrame(user, width=1300, padx=20, pady=10, bg='#ffffff', border=0)
user_frame.grid(pady=40)

logo_label = Label(user_frame, text='Logo', font=('areal', 25, 'bold'), bg='#ffffff')
logo_label.grid(row=0, column=1, padx=20)

title_label = Label(user_frame, text='Building Rent Management System', font=('areal', 15), padx=300, bg='#ffffff')
title_label.grid(row=0, column=2)

room_clicked = StringVar()
room_clicked.set('Room quantity')

#card 1

frame1 = Frame(user, bg ='#ffffff', bd=10, width=250, height=280).place(x=85, y=200)

canvas = Canvas(user, width= 245, height= 150)
canvas.place(x=85, y=200)

family_img1 = Image.open("img/family.jpg")

resized_image1 = family_img1.resize((250,150), Image.ANTIALIAS)
new_image1 = ImageTk.PhotoImage(resized_image1)

canvas.create_image(0,0, anchor=NW, image=new_image1)

heading_label1 = Label(frame1, text='Family building rent', font=('areal', 13), fg='#000000', bg='#ffffff')
heading_label1.place(x=130, y=365)

family_btn = Button(frame1, text='Show more', padx=8, pady=5, font=('areal',12), command=show)
family_btn.place(x=160, y=410)

#card 2

frame2 = Frame(user, bg ='#ffffff', bd=10, width=250, height=280).place(x=385, y=200)

canvas2 = Canvas(user, width = 245, height= 150)
canvas2.place(x=385, y=200)

family_img2 = Image.open("img/officeRent.jpg")

resized_image2 = family_img2.resize((250,150), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resized_image2)

canvas2.create_image(0,0, anchor=NW, image=new_image2)

heading_label2 = Label(frame2, text='Office building rent', font=('areal', 13), fg='#000000', bg='#ffffff')
heading_label2.place(x=435, y=365)

family_btn2 = Button(frame2, text='Show more', padx=8, pady=5, font=('areal',12), command=show)
family_btn2.place(x=465, y=410)

#card 3
frame3 = Frame(user, bg ='#ffffff', bd=10, width=250, height=280).place(x=685, y=200)

canvas3 = Canvas(user, width= 245, height= 150)
canvas3.place(x=685, y=200)

family_img3 = Image.open("img/bachalor.jpg")

resized_image3 = family_img3.resize((250,150), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image3)

canvas3.create_image(0,0, anchor=NW, image=new_image)

heading_label3 = Label(frame3, text='Bachelor building rent', font=('areal', 13), fg='#000000', bg='#ffffff')
heading_label3.place(x=735, y=365)

family_btn3 = Button(frame3, text='Show more', padx=8, pady=5, font=('areal',12), command=show)
family_btn3.place(x=765, y=410)

backBtn = Button(user, text="Back", padx=20, font=('areal',15),bg='#ff0000',fg='#ffffff', command=back)
backBtn.place(x=490, y=530)

user.mainloop()