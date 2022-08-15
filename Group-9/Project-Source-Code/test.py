import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call


def ok():
    mysqldb = mysql.connector.connect(host="localhost",user="root",password="",database="vms")
    mycursor= mysqldb.cursor()
    e_id=e1.get()
    e_pass=e2.get()

    sql="select * from log_in where id = %s and pass = %s"
    mycursor.execute(sql,[(e_id), (e_pass)])
    results= mycursor.fetchall()
    if results:

        call(['python',"emp_main.py"])
        root.quit()
        return True

    else:
        messagebox.showinfo("error","incorrect username and password")
        return False

root=Tk()
root.title("login")
#root.geometry("600x400")
root.configure(bg="pink")

window_width,window_height=600,400

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

mylabel1=Label(root, text="\n  Welcome To MMS T shirt  \n stock Management System   \n\n\ncustomer Log in Here",font=200,bg="#90EE90")
mylabel1.pack()

global e1
global e2

Label(root,text="Enter User Id",font="40",bg="#90EE90").place(x=50,y=120)
Label(root,text="Enter password",font="40",bg="#90EE90").place(x=50,y=200)

e1=Entry(root,font=40,bg="gray")
e1.place(x=280,y=120)

e2=Entry(root,font="40",bg="gray")
e2.place(x=280,y=200)
e2.config(show="*")

def back():
    call(["python", "main.py"])
    root.destroy()

Button(root,text="back",command=back,height=2,width=7,bg="#8bb16b",font=90).place(x=5,y=5)

Button(root,text="Log in",command=ok,height=4,width=18,bg="#8bb16b",font=90).place(x=200,y=290)

root.mainloop()