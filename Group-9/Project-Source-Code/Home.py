from tkinter import *
import subprocess
def run_program():
    screen.destroy()
    subprocess.call(["python", "2nd_page.py"])

screen=Tk()
screen.title("T-Shirt Stock Management System")
screen.geometry("600x600")
#label
Label(screen,text="T-Shirt Stock Management System",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

Button(screen,text="Admin",command=run_program,font="ariel 30",bg="green",fg="black").place(x=115,y=205)
Button(screen,text="User",command=run_program,font="ariel 30",bg="green",fg="black").place(x=385,y=205)

mainloop()