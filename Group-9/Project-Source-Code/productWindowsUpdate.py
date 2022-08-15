from tkinter import *
from PIL import ImageTk, Image
import subprocess
from tkinter import Tk

root = Tk()
root.title('T-Shirt Stock Management System')
# image=Image.open('C:\\Users\\asmau\\Desktop\\images\\bg1.jpeg')
image=Image.open('bl1.jpg')
bck_end=ImageTk.PhotoImage
root['bg']='gray'
root.geometry("1000x600")
Label(root,text="Home Page",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")
canvas=Canvas(width=1000,height=600)
canvas.pack()
# photo=PhotoImage(file='C:\\Users\\asmau\\Desktop\\images\\bg1.jpeg')
photo=PhotoImage(file='c1.png')
canvas.create_image(100,100,image=photo,anchor=NW)

def run_program():
    root.destroy()
    subprocess.call(["python", "admin_login.py"])
def run_program1():
    root.destroy()
    subprocess.call(["python", "registration.py"])
#label

#Button
Button(root,text="ADMIN",command=run_program,font="20").place(x=100,y=230)
Button(root,text="USER",command=run_program1,font="20").place(x=340,y=230)
root.mainloop()