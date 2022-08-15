from tkinter import *
import subprocess

def run_program():
    screen.destroy()
    subprocess.call(["python", "Home.py"])

def run_program1():
    subprocess.call(["python", "registration.py"])

def run_program2():
    subprocess.call(["python", "login.py"])

screen=Tk()
screen.title("T-Shirt Stock Management System")
screen.geometry("600x600")
#label
Label(screen,text="T-Shirt Stock Management System",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

Button(screen,text="Already have an account",command=run_program2,font="ariel 20",bg="green",fg="black").place(x=100,y=120)
Button(screen,text="Creat a new account",command=run_program1,font="ariel 20",bg="green",fg="black").place(x=100,y=250)

Button(screen, text='Back',command=run_program,font="30").place(x=385,y=355)

mainloop()