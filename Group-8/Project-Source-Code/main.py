from tkinter import *
from subprocess import call
from tkinter import messagebox
from PIL import ImageTk, Image
import Image

win = Tk()
win.title("Restuarent Management System")
win.configure(bg="#F0FFF0")
win.geometry('900x875')
canv = Canvas(win, width=900, height=675, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rbg.webp"))
canv.create_image(0,0, anchor=NW, image=img)

mylabel=Label(win, text="Let's Ketchup",font='Times 30 bold',bg="black",fg="white").place(x=310,y=10)
mylabel1=Label(win, text="Contact Us\nPhone Number:0152284562\nAddress:76,Munshiganj,Khulna",font='Times 20 bold',bg="#F0FFF0",fg="black").place(x=220,y=690)

def quit():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
   if response:
      win.destroy()

   else:
      messagebox.showinfo("SYSTEM ALERT", "Canceled")

def ok():
   if ok:
      win.destroy()
      call(['python', "test.py"])

      return True

def ok1():
   if ok1:
      win.destroy()
      call(['python', "prac.py"])

      return True

def ok2():
   if ok2:
      win.destroy()
      call(['python', "new_menu.py"])

      return True

def ok3():
   if ok3:
      win.destroy()
      call(['python', "feed.py"])

      return True

def ok4():
   if ok4:
      win.destroy()
      call(['python', "menus.py"])

Button(win, text="Admin log in", command=ok, height=2, width=15, font='Times 18 bold', bg="#F0E68C").place(x=100, y=100)
Button(win, text="Employee log in", command=ok1, height=2, width=15, font='Times 18 bold', bg="#F0E68C").place(x=100, y=200)
Button(win, text="Menu", command=ok2, height=2, width=15, font='Times 18 bold', bg="#F5DEB3").place(x=100, y=300)
Button(win, text="Feedback", command=ok3, height=2, width=15, font='Times 18 bold', bg="#696969",fg='white').place(x=100,y=400)
Button(win, text="Exit", command=quit, height=2, width=15, font='Times 18 bold', bg="#6D6968",fg='white').place(x=100,y=600)
Button(win, text="Menu Image", command=ok4, height=2, width=15, font='Times 18 bold', bg="#6D6968",fg='white').place(x=100,y=500)

win.mainloop()
