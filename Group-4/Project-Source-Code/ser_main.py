import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image


root=Tk()
root.title("Sergent Dashboard")
root.configure(bg="#afc7e7")

window_width,window_height=1220,514
root.resizable(False, False)
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

canv = Canvas(root, width=620, height=514, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("emp-1.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="Welcome To Khulna BRTA \n Vehicle Management System  \n\nSergeant Dashboard",font="Times 23 bold",bg="#afc7e7",fg="white").place(x=750,y=5)
#mylabel1.pack()

def emp2():
    root.destroy()
    call(["python", "ser_view.py"])

def emp3():
    root.destroy()
    call(["python", "ser_view_all_case.py"])

def emp4():
    root.destroy()
    call(["python", "ser_new_case.py"])



Button(root,text="View Vehicle Information",command=emp2,height=3,width=21,bg="#ee4579",font="Times 18 bold").place(x=650,y=160)
Button(root,text="Sergent All Cases",command=emp3,height=3,width=21,bg="#ee4579",font="Times 18 bold").place(x=900,y=285)
Button(root,text="New Case File",command=emp4,height=3,width=21,bg="#ee4579",font="Times 18 bold").place(x=650,y=400)

def log_out():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Log Out",command=log_out,height=2,width=7,bg="#ee4579",font="Times 11 bold").place(x=1090,y=450)


root.mainloop()