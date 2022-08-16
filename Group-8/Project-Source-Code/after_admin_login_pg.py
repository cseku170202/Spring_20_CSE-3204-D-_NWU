from tkinter import *
from subprocess import call
from tkinter import messagebox
from PIL import ImageTk, Image

win = Tk()
win.title("Admin Mode")
win.configure(bg="#FFE6E8")
win.geometry('950x800')
canv = Canvas(win, width=950, height=800, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rad.jpg"))
canv.create_image(0,0, anchor=NW, image=img)

mylabel1=Label(win, text="Admin-Panel",font='Times 35 bold',fg="#A0522D",bg='white').place(x=355,y=10)

def quit():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
   if response:
      win.destroy()

   else:
      messagebox.showinfo("SYSTEM ALERT", "Canceled")

def ok():
   if ok:
      win.destroy()
      call(['python', "order_show.py"])

      #return True

def ok1():
   if ok1:
      win.destroy()
      call(['python', "edit_employee.py"])

      #return True

def ok2():
   if ok2:
      win.destroy()
      call(['python', "feed_admin_2.py"])

def ok3():
   if ok2:
      win.destroy()
      call(['python', "feed_emp.py"])

def back():
    win.destroy()
    call(['python', "test.py"])



Button(win, text="Show\nOrder-List", command=ok, height=2, width=15, font='Times 18 bold', fg="#A0522D",bg='white').place(x=100, y=100)
Button(win, text="Employee's\nManagement", command=ok1, height=2, width=15, font='Times 18 bold', fg="#A0522D",bg='white').place(x=100, y=200)
Button(win, text="Customer's\nFeedback", command=ok2, height=2, width=15, font='Times 18 bold', fg="#A0522D",bg='white').place(x=100,y=300)
Button(win, text="Employee\nFeedback", command=ok3, height=2, width=15, font='Times 18 bold', fg="#A0522D",bg='white').place(x=100,y=400)
Button(win, text="Back", command=back, height=2, width=15, font='Times 18 bold', fg="#A0522D",bg='white').place(x=100,y=500)
Button(win, font='Time 18 bold', text="Exit", width=14,height=2, command=quit,fg="#A0522D",bg='white').place(x=100,y=600)

win.mainloop()