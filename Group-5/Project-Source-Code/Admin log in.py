import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image

def Ok():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="admin")
    mycursor = mysqldb.cursor()
    uname = e1.get()
    password = e2.get()

    sql = "select * from user where uname = %s and password = %s"
    mycursor.execute(sql, [(uname), (password)])
    results = mycursor.fetchall()

    if results:
        root.destroy()
        call(["python", "option.py"])
        return True
    else:
        messagebox.showinfo("", "Incorrent Username and Password")
        return False


root = Tk()
root.title("Admin Login")
root.geometry("500x400")
frame = Frame(root)
frame.pack(pady=200,padx=200)
frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("person-holds-a-book-over-a-stack-and-turns-the-page.jpg"))
label = Label(frame, image = img)
label.pack()
global e1
global e2

Label(root, text="Admin Login form", font=("Arial", 15, "bold"), bg="#00376b", fg="#FFFCF9").place(x=10, y=10)
Label(root, text="UserName").place(x=10, y=60)
Label(root, text="Password").place(x=10, y=90)

e1 = Entry(root)
e1.place(x=140, y=60)

e2 = Entry(root)
e2.place(x=140, y=90)
e2.config(show="*")

Button(root, text="Login", command=Ok, height=2, width=13).place(x=150, y=120)

root.mainloop()