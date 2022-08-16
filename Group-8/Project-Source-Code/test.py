import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image

def exit():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
   if response:
      root.destroy()

   else:
      messagebox.showinfo("SYSTEM ALERT", "Canceled")

def back():
    root.destroy()
    call (['python', "main.py"])

def ok():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="rms")
    mycursor= mysqldb.cursor()
    e_id=e1.get()
    e_pass=e2.get()
    root.destroy()

    sql="select * from log_in where id= %s and pass = %s"
    mycursor.execute(sql,[(e_id), (e_pass)])
    results= mycursor.fetchall()

    if results:

        call(['python',"after_admin_login_pg.py"])
        root.quit()
        return True

    else:
        messagebox.showinfo("","incorrect username and password")
        return False

root=Tk()
root.title(" Admin login")
root.configure(bg="#F0FFF0")
root.geometry('950x720')
canv = Canvas(root, width=950, height=720, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rb.jpg"))
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="Admin LogIn",font='Times 35 bold',bg="#3B3131",fg="White").place(x=285,y=10)

global e1
global e2

Label(root,text="Enter Username",font="40",bg="#3B3131",fg="White",width=15,height=2).place(x=60,y=120)
Label(root,text="Enter password",font="40",bg="#3B3131",fg="White",width=15,height=2).place(x=60,y=200)

e1=Entry(root,font=60)
e1.place(x=300,y=130)

e2=Entry(root,font="60")
e2.place(x=300,y=210)
e2.config(show="*")


Button(root,text="Log in",command=ok,width=10,bg="#3B3131",fg="white",font=('vardana',17,'bold'),bd=10, padx=5,pady=5 ).place(x=100,y=300)
Button(root, font=('vardana', 16, 'bold'), text="Back", bg="#3B3131", fg="white", bd=10, padx=10,pady=10, width=10, command=back).place(x=310,y=300)
Button(root, font=('vardana', 16, 'bold'), text="Exit", bg="#3B3131", fg="white", bd=10, padx=10,pady=10, width=10, command=exit).place(x=230,y=400)

root.mainloop()