from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import mysql.connector
import sys
from PIL import ImageTk, Image

root = Tk()
root.title("Order")
root['bg']='gray'
root.geometry("1200x550")
arguments=sys.argv
tshirtInfo=None
if len(arguments) > 1:
    tshirtInfo=arguments[1].split(',')
    print(tshirtInfo)

def run_program():
    root.destroy()
    subprocess.call(["python", "main.py"])

def insertOrder(color, size, quantity, price):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="t_shirt")
    dbcursor = mydb.cursor()
    sql = "INSERT INTO t_shirt_order (color,size,quantity, price) VALUES (%s, %s,%s,%s)"
    if size == 'Select Size':
        size="Medium"
    val = (color, size, quantity, price)
    dbcursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("", "Data inserted successfully")
    mydb.close()

def run_program():
    #subprocess.call(["python", "admin_section.py"])
    pass
#label
Label(root,text="Add Order",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")
# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('add_order.jpg')
image1.thumbnail((685, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

#Combobox
def comboFunction(event):
    print(colorCombo.get())
    print(combo.get())

Label(root,text="Enter Color:",font="5").place(x=720,y=60)
colorCombo = ttk.Combobox(root,values=["Black","Red","Blue","Yellow","Teal","Green","Gray"],height=25,width=25)
colorCombo.place(x=900,y=63)

#colorCombo.set("Select Color")
colorCombo.set("Select Color")
if tshirtInfo is not None:
    colorCombo.set(tshirtInfo[0])
colorCombo.bind('<<ComboboxSelected>>',comboFunction)

Label(root,text="Enter Size:",font="5").place(x=720,y=100)
combo = ttk.Combobox(root,values=["Small","Medium","Large","Extra large","Extra extra large"],height=25,width=25)
combo.place(x=900,y=100)

combo.set("Select Size")
combo.bind('<<ComboboxSelected>>',comboFunction)

Label(root,text="Quantity:",font="20").place(x=720,y=150)
Label(root,text="Price:",font="20").place(x=720,y=200)

#Entry
quantityText = StringVar()
quantityText.set("1")
Quantity_entry=Entry(root,textvariable=quantityText,font="10",bd=4)
Quantity_entry.place(x=900,y=150)
priceText = StringVar()
priceText.set("0")
if tshirtInfo is not None:
    priceText.set(tshirtInfo[2])
Price_entry=Entry(root,textvariable=priceText,font="10",bd=4)
Price_entry.place(x=900,y=200)


#Button
Button(root,text="Order",command=lambda : insertOrder(colorCombo.get(),combo.get(),quantityText.get(),priceText.get()), font="ariel 20 bold").place(x=950,y=300)
Button(root,text="Back",command=run_program,font="ariel 20 bold").place(x=1080,y=440)
root.mainloop()
