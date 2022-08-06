import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image


def ok():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="vms")
    mycursor= mysqldb.cursor()
    e_id = e1.get()
    e_pass = e2.get()

    sql="select * from own_log where id = %s and pass = %s"
    mycursor.execute(sql,[(e_id), (e_pass)])
    results= mycursor.fetchall()
    if results:
        root.destroy()
        call(['python',"own_main.py"])

        return True

    else:
        messagebox.showinfo("","incorrect username and password")
        return False

root=Tk()
root.title("login")
root.configure(bg="#ADD8E6")
root.resizable(False, False)
window_width,window_height=1450,750

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')


canv = Canvas(root, width=750, height=750, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("log3.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="Welcome To Khulna BRTA \n Vehicle Management System \n\n\nOwner Log in Here",font='Times 18 bold',bg="#ADD8E6").place(x=950,y=0)
#mylabel1.pack()

global e1
global e2

Label(root,text="Enter User Name",font="Times 18 bold",bg="#ADD8E6").place(x=900,y=250)
Label(root,text="Enter Registration NO",font="Times 18 bold",bg="#ADD8E6").place(x=900,y=350)

e1=Entry(root,font="Times 18 bold")
e1.place(x=1150,y=250)

e2=Entry(root,font="Times 18 bold")
e2.place(x=1150,y=350)
e2.config(show="*")

reg=e2.get()

def back():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Back",command=back,height=4,width=18,bg="#A1ABEC",font="Times 18 bold").place(x=800,y=500)

Button(root,text="Log in",command=ok,height=4,width=18,bg="#A1ABEC",font="Times 18 bold").place(x=1150,y=500)

root.mainloop()