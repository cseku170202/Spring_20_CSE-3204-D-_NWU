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

    sql="select * from log_in where id = %s and pass = %s"
    mycursor.execute(sql,[(e_id), (e_pass)])
    results= mycursor.fetchall()
    if results:

        root.destroy()
        call(['python',"emp_main.py"])

        return True

    else:
        messagebox.showinfo("","incorrect username and password")
        return False

root=Tk()
root.title("login")
#root.geometry("600x400")
root.configure(bg="#90EE90")
root.resizable(False, False)
window_width,window_height=696,464

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

canv = Canvas(root, width=696, height=464, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("i3.jpg"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

#mylabel1=Label(root, text="\n Welcome To Khulna BRTA \n Vehicle Management System",font="Times 18 bold",bg="#98A493",fg="white").place(x=380,y=5)
canv.create_text(530, 40, text="Welcome To Khulna BRTA \n Vehicle Management System", fill="black", font='Times 18 bold')
canv.pack()
#mylabel1.pack()

global e1
global e2

#Label(root,text="Enter User Id",font="Times 18 bold",bg="#1e455b",fg="white").place(x=200,y=220)
canv.create_text(300, 230, text="Enter User Id", fill="white", font='Times 18 bold')
canv.pack()
canv.create_text(300, 315, text="Enter password", fill="white", font='Times 18 bold')
canv.pack()
#Label(root,text="Enter password",font="Times 18 bold",bg="#1e455b",fg="white").place(x=200,y=300)

e1=Entry(root,font="Times 18 bold",bg="gray",fg="white")
e1.place(x=400,y=220)

e2=Entry(root,font="Times 18 bold",bg="gray",fg="white")
e2.place(x=400,y=300)
e2.config(show="*")

def back():
    root.destroy()
    call(["python", "main.py"])


Button(root,text="Back",command=back,height=2,width=8,bg="#6577B3",fg="white",font="Times 18 bold").place(x=5,y=390)

Button(root,text="Log in",command=ok,height=2,width=8,bg="#6577B3",fg="white",font="Times 18 bold").place(x=550,y=390)

root.mainloop()