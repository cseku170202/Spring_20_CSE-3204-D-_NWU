from tkinter import *

import subprocess
def run_program():
    subprocess.call(["python", "Home.py"])
    screen.destroy()
screen = Tk()
screen.title("Colour code")
screen.geometry("500x500")
#label
Label(screen,text="Colour Choice",font="ariel 20 bold",bg="brown",fg="white",).pack(fill="both")
Label(screen,text="Colour code Enter:",font="20").place(x=40,y=80)

Label(screen,text="Colour Red:001",font="ariel 16 bold ",bg="green",fg="red").place(x=80,y=170)
Label(screen,text="Colour Black:002",font="ariel 16 bold ",bg="green",fg="black").place(x=80,y=200)
Label(screen,text="Colour White:003",font="ariel 16 bold ",bg="green",fg="white").place(x=80,y=230)
Label(screen,text="Colour Blue:004",font="ariel 16 bold",bg="green",fg="blue").place(x=80,y=260)


#Entry
Phone_entry=Entry(screen,font="10",bd=4)
Phone_entry.place(x=200,y=80)
#Button
Button(screen, text='Back',command=run_program,font="20").place(x=385,y=355)
mainloop()
