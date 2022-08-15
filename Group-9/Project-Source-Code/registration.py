from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector
import subprocess
from PIL import ImageTk, Image

def run_program2():
    root.destroy()
    subprocess.call(["python", "login.py"])

def run_program():
    root.destroy()
    subprocess.call(["python", "main.py"])

def insert():
    name=name_entry.get()
    age=age_entry.get()
    address=address_entry.get()
    phone=Phone_entry.get()
    password=Password_entry.get()

    if(name=="" or age=="" or address=="" or phone=="" or password==""):
        MessageBox.showinfo("insert status","All field are required to fill")
    else:
        con=mysql.connector.connect(host="localhost",user="root",password="",db="t_shirt")
        cursor=con.cursor()
        cursor.execute("insert into customer_info values('"+name+"',  '"+age+"', '"+address+"', '"+phone+"', '"+password+"')")
        cursor.execute("commit")
        MessageBox.showinfo("insert status", "successfully insert")
        name_entry.delete(0,'end')
        age_entry.delete(0,'end')
        address_entry.delete(0,'end')
        Phone_entry.delete(0,'end')
        Password_entry.delete(0,'end')
        root.destroy()
        subprocess.call(["python","search.py"])
        con.close()

root = Tk()
root.title("Customer Registration")
root.geometry("810x570")

#label
Label(root,text="Customer Registration Form",font="ariel 20 bold",bg="deepskyblue",fg="black").pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('registration_image.png')
image1.thumbnail((805, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

canvas = Canvas(width=500,height=500,bg='skyblue')
canvas.pack()
photo = PhotoImage(file='')

Label(root,text="Name:",font="20").place(x=500,y=70)
Label(root,text="Age:",font="20").place(x=500,y=110)
Label(root,text="Address:",font="20").place(x=500,y=150)
Label(root,text="Phone No:",font="20").place(x=500,y=190)
Label(root,text="Password:",font="20").place(x=500,y=230)
#Entry
name_entry=Entry(root,font="10",bd=4,bg="white")
name_entry.place(x=600,y=70)
age_entry=Entry(root,font="10",bd=4,bg="white")
age_entry.place(x=600,y=110)
address_entry=Entry(root,font="10",bd=4,bg="white")
address_entry.place(x=600,y=150)
Phone_entry=Entry(root,font="10",bd=4,bg="white")
Phone_entry.place(x=600,y=190)
Password_entry=Entry(root,font="10",bd=4,bg="white")
Password_entry.place(x=600,y=230)
Password_entry.config(show="*")
#Button
#Button(root,text="Clear",font="ariel 20 bold").place(x=1165,y=230)
Button(root,text="Sign up",command=insert,font="ariel 18 bold",bg='skyblue').place(x=500,y=300)
Button(root,text=' Back ',command=run_program,font="ariel 19 bold",bg='skyblue').place(x=500,y=490)
Button(root,text="Already have an account",command=run_program2,font="ariel 15",bg='skyblue').place(x=500,y=360)
mainloop()