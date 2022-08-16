import mysql.connector
import base64
from PIL import Image
import io
from tkinter import *
from PIL import ImageTk , Image
from subprocess import call
from tkinter import messagebox

# def exit():
#    response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
#    if response:
#       root.destroy()
#
#    else:
#       messagebox.showinfo("SYSTEM ALERT", "Canceled")

def back():
    root.destroy()
    call(['python', "main.py"])

root = Tk()
root.title("Menu-Management")
root.geometry("1700x900")

mylabel=Label(root, text="Menu-Management",font='Times 35 bold',bg="white").place(x=550,y=0)

canv = Canvas(root, width=400, height=300, bg='white')
canv.place(x=0,y=60)
img = ImageTk.PhotoImage(Image.open("burger.jpg"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)
lbl1=Label(root, text="Burger\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=60,y=370)

canv1 = Canvas(root, width=400, height=300, bg='white')
canv1.place(x=500,y=60)
img1 = ImageTk.PhotoImage(Image.open("pizza.jpg"))  # PIL solution
canv1.create_image(0,0, anchor=NW, image=img1)
lbl2=Label(root, text="Pizza\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=575,y=370)

canv2 = Canvas(root, width=400, height=300, bg='white')
canv2.place(x=1000,y=60)
img2 = ImageTk.PhotoImage(Image.open("french fries.jpg"))  # PIL solution
canv2.create_image(0,0, anchor=NW, image=img2)
lbl3=Label(root, text="French-Fries\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=1075,y=370)

canv3 = Canvas(root, width=400, height=300, bg='white')
canv3.place(x=0,y=440)
img3 = ImageTk.PhotoImage(Image.open("noodles.webp"))  # PIL solution
canv3.create_image(0,0, anchor=NW, image=img3)
lbl4=Label(root, text="Noodles\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=60,y=740)

canv4 = Canvas(root, width=400, height=300, bg='white')
canv4.place(x=500, y=440)
img4 = ImageTk.PhotoImage(Image.open("ice cream.webp"))  # PIL solution
canv4.create_image(0, 0, anchor=NW, image=img4)
lbl5=Label(root, text="Ice-Cream\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=575,y=740)

canv5 = Canvas(root, width=400, height=300, bg='white')
canv5.place(x=1000, y=440)
img5 = ImageTk.PhotoImage(Image.open("drinks.jpg"))  # PIL solution
canv5.create_image(0, 0, anchor=NW, image=img5)
lbl6=Label(root, text="Drinks\n Price:220/=", font="Time 15 bold", bg="white",width=15,height=2).place(x=1075,y=740)

Button(root, font=('vardana', 16, 'bold'), text="Back", bg="white", fg="black", padx=10,pady=10, width=7, command=back).place(x=0,y=0)
#Button(root, font=('vardana', 16, 'bold'), text="Exit", bg="white", fg="red", bd=10, padx=10,pady=10, width=7, command=exit).place(x=1390, y=0)
# Button(root, font=('vardana', 16, 'bold'), text="ADD", bg="white", fg="blue", padx=10,pady=10, width=7).place(x=320,y=0)
# Button(root, font=('vardana', 16, 'bold'), text="UpDate", bg="white", fg="green", padx=10,pady=10, width=7).place(x=1095,y=0)
# Button(root, font=('vardana', 16, 'bold'), text="Delete", bg="white", fg="red",padx=10,pady=10, width=7).place(x=1410,y=0)

# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "",
    database="rms"  # Name of the database
)
cursor = mydb.cursor()
file = open('french fries.jpg', 'rb').read()
file = base64.b64encode(file)

args = ('French Fries', 'Fast Food', '60', file)

query = 'INSERT INTO food_list2 VALUES(%s, %s, %s, %s)'

cursor.execute(query, args)
mydb.commit()

cursor = mydb.cursor()
file = open('burger.jpg', 'rb').read()
file = base64.b64encode(file)

args = ('Burger', 'Fast Food', '120', file)

query = 'INSERT INTO food_list2 VALUES(%s, %s, %s, %s)'

cursor.execute(query, args)
mydb.commit()

cursor = mydb.cursor()
file = open('noodles.webp', 'rb').read()
file = base64.b64encode(file)

args = ('Noodles', 'Fast Food', '80', file)

query = 'INSERT INTO food_list2 VALUES(%s, %s, %s, %s)'

cursor.execute(query, args)
mydb.commit()

cursor = mydb.cursor()
file = open('drinks.jpg', 'rb').read()
file = base64.b64encode(file)

args = ('Drinks', 'drinks', '50', file)

query = 'INSERT INTO food_list2 VALUES(%s, %s, %s, %s)'

cursor.execute(query, args)
mydb.commit()

cursor = mydb.cursor()
file = open('ice cream.webp', 'rb').read()
file = base64.b64encode(file)

args = ('Ice-Cream', 'Desert', '120', file)

query = 'INSERT INTO food_list2 VALUES(%s, %s, %s, %s)'

cursor.execute(query, args)
mydb.commit()

cursor = mydb.cursor()
file = open('pizza.jpg', 'rb').read()
file = base64.b64encode(file)

args = ('Pizza', 'Vegetable', '220', file)

query = 'INSERT INTO food_list2 VALUES(%s, %s, %s, %s)'

cursor.execute(query, args)
mydb.commit()

root.mainloop()