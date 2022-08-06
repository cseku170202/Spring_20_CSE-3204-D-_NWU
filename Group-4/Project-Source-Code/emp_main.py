import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image


root=Tk()
root.title("Dashboard")
root.configure(bg="#ed3b87")
root.resizable(False, False)

window_width,window_height=1220,514

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

canv = Canvas(root, width=620, height=514, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("emp-1.png"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(root, text="Welcome To Khulna BRTA \n Vehicle Management System \n\n Employee Dashboard",font="Times 18 bold",bg="#ed3b87",fg="white").place(x=750,y=5)
#mylabel1.pack()

def emp1():
    root.destroy()
    call(["python", "e_insert.py"])

def emp2():
    root.destroy()
    call(["python", "e_view.py"])

def emp3():
    root.destroy()
    call(["python", "e_cng.py"])

def emp4():
    root.destroy()
    call(["python", "e_delete.py"])

def emp5():
    root.destroy()
    call(["python", "e_all_view.py"])
def emp6():
    root.destroy()
    call(["python", "e_rep_view.py"])


Button(root,text="Register a New Vehicle",command=emp1,height=2,width=18,bg="#afc7e7",font="Times 18 bold").place(x=650,y=200)
Button(root,text="View Vehicle Information",command=emp2,height=2,width=20,bg="#afc7e7",font="Times 18 bold").place(x=930,y=200)
Button(root,text="Chenge Owner Name",command=emp3,height=2,width=18,bg="#afc7e7",font="Times 18 bold").place(x=650,y=300)
Button(root,text="Delete Vehicle Information",command=emp4,height=2,width=20,bg="#afc7e7",font="Times 18 bold").place(x=930,y=300)
Button(root,text="View All Information",command=emp5,height=2,width=20,bg="#afc7e7",font="Times 18 bold").place(x=930,y=400)
Button(root,text="Check Report",command=emp6,height=2,width=18,bg="#afc7e7",font="Times 18 bold").place(x=650,y=400)

def log_out():
    root.destroy()
    call(["python", "main.py"])

Button(root,text="Log Out",command=log_out,height=2,width=7,bg="#afc7e7",font="Times 18 bold").place(x=1090,y=50)


root.mainloop()