import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image

root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='gray'
root.geometry("1300x580")

def run_program():
    root.destroy()
    subprocess.call(["python", "show.py"])

def comboFunction(event):
    print(combo1.get())

def ok():
    color_code = combo1.get()
    price=Price_entry.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root",password="",database="tsms")
    mycursor = mysqldb.cursor()


    try:
       sql="update insertion set price= %s where color_code=%s"
       val =(price,color_code)
       mycursor.execute(sql, val)
       mysqldb.commit()
       messagebox.showinfo("information", "Record Updated Successfully")

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
#label
Label(root,text="Update Data",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('update.jpg')
image1.thumbnail((800, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

Label(root,text="Enter Color Code:",font="5").place(x=850,y=60)
combo1 = ttk.Combobox(root,values=["1","2","3","4"],height=25,width=25)
combo1.place(x=1050,y=60)

combo1.set("Select Color Code")
combo1.bind('<<ComboboxSelected>>',comboFunction)

Label(root,text="Enter Price:",font="20").place(x=850,y=140)

#Entry
Price_entry=Entry(root,font="10",bd=4)
Price_entry.place(x=1050,y=140)

#Button
Button(root,text="Update",command=ok,font="20").place(x=1050,y=230)
Button(root,text="Back",command=run_program,font="20").place(x=1200,y=530)
root.mainloop()