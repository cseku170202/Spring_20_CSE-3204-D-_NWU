import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image


def ok():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="vms")
    mycursor= mysqldb.cursor()
    e_id=e1.get()
    e_pass=e2.get()

    sql="select * from ser_log_in where id = %s and pass = %s"
    mycursor.execute(sql,[(e_id), (e_pass)])
    results= mycursor.fetchall()
    if results:
        root.destroy()
        call(['python',"ser_main.py"])

        return True

    else:
        messagebox.showinfo("","incorrect username and password")
        return False

root=Tk()
root.title("login")
#root.geometry("600x400")
root.configure(bg="#6e89c5")
root.resizable(False, False)

window_width,window_height=900,450

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


canv = Canvas(root, width=450, height=450,)
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("log5.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)



mylabel1=Label(root, text="Welcome To Khulna BRTA \n Vehicle Management System",font='Times 20 bold',bg="#6e89c5").place(x=520,y=5)
#mylabel1.pack()

global e1
global e2

Label(root,text="Enter User Id",font="Times 18 bold",bg="#6e89c5").place(x=480,y=130)
Label(root,text="Enter password",font="Times 18 bold",bg="#6e89c5").place(x=480,y=200)

e1=Entry(root,font="Times 18 bold",bg="gray",fg="white")
e1.place(x=640,y=130)
z=e1.get()

e2=Entry(root,font="Times 18 bold",bg="gray",fg="white")
e2.place(x=645,y=200)
e2.config(show="*")

def back():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Back",command=back,height=3,width=8,bg="#75777D",font="Times 18 bold").place(x=500,y=290)

Button(root,text="Log in",command=ok,height=3,width=8,bg="#75777D",font="Times 18 bold").place(x=700,y=290)

root.mainloop()