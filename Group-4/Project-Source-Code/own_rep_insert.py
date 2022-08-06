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

    response = messagebox.askyesno('SYSTEM ALERT', 'Are you sure you want to INSERT?')
    if response:
        try:
            sql = "insert into rep(reg,claim_det) values(%s,%s)"
            val = (e_id, e_pass)
            mycursor.execute(sql, val)
            mysqldb.commit()
            messagebox.showinfo("Information", "Case Record Successfully")
        except EXCEPTION as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")
    e1.delete(0, END)
    e2.delete(0, END)


root=Tk()
root.title("Report")
root.configure(bg="#B2C6D7")

window_width,window_height=800,380

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

canv = Canvas(root, width=400, height=380, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("cas1.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="Welcome To Khulna BRTA \n Vehicle Management System \n\n\nReport A Problem Here",font="Times 12 bold",bg="#B2C6D7").place(x=490,y=0)
#mylabel1.pack()

global e1
global e2

Label(root,text="Enter Registration No",font="Times 12 bold",bg="#B2C6D7").place(x=420,y=120)
Label(root,text="Enter Your Report Details",font="Times 12 bold",bg="#B2C6D7").place(x=420,y=200)

e1=Entry(root,font="Times 12 bold",bg="gray",fg="white")
e1.place(x=600,y=120)

e2=Entry(root,font="Times 12 bold",bg="gray",fg="white")
e2.place(x=600,y=200)


reg=e2.get()

def back():
    root.destroy()
    call(["python", "own_main.py"])

Button(root,text="Back",command=back,height=2,width=7,bg="#5093CA",font="Times 12 bold").place(x=5,y=5)

Button(root,text="Submit Report",command=ok,height=4,width=18,bg="#5093CA",font="Times 12 bold").place(x=600,y=290)

root.mainloop()