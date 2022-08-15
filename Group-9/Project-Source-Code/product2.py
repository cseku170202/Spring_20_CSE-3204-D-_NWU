import os
from tkinter import *
from PIL import ImageTk, Image
import subprocess
import mysql.connector
root = Tk()
root.title("T-Shirt Stock Management System")
root.geometry("600x400")

def run_program():
    root.destroy()
    subprocess.call(["python", "search.py"])

def run_program3():
    root.destroy()
    subprocess.call(["python", "product3.py"])
def run_program1():
    root.destroy()
    subprocess.call(["python", "product1.py"])


def openOrderWindow(tShirtInfo):
    username=os.environ['USERNAME']
    subprocess.call(["C:\\Users\\"+username+"\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe","orderWindow.py", tShirtInfo])

frame1 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
frame1.pack(fill='x', expand=1, side='right')
image1 = Image.open('r1.jpg')
image1.thumbnail((100, 100))
i1 = ImageTk.PhotoImage(image1)
Label(frame1, image=i1).grid(row=0, column=0)
Label(frame1, text='Price:750 ').grid(row=1, column=0)
Label(frame1, text='Quantity:1 ').grid(row=2, column=0)
Button(frame1,text="Order",command=lambda : openOrderWindow("black,1,750"),font="20").grid(row=3, column=0)
#
frame2 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
frame2.pack(fill='x', expand=1, side='right')
image2 = Image.open('redtshirt.jpg')
image2.thumbnail((150, 150))
i2 = ImageTk.PhotoImage(image2)  # .grid(row=0,column=0)
Label(frame2, image=i2).grid(row=0, column=0)
Label(frame2, text='Price:500 ').grid(row=1, column=0)
Label(frame2, text='Quantity:1 ').grid(row=2, column=0)
Button(frame2,text="Order",command=lambda : openOrderWindow("red,1,500"),font="20").grid(row=3, column=0)
#
frame3 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
frame3.pack(fill='x', expand=1, side='right')
image3 = Image.open('r2.jpg')
image3.thumbnail((100, 100))
i3 = ImageTk.PhotoImage(image3)  # .grid(row=0,column=0)
Label(frame3, image=i3).grid(row=0, column=0)
Label(frame3, text='Price:600 ').grid(row=1, column=0)
Label(frame3, text='Quantity:1 ').grid(row=2, column=0)
Button(frame3,text="Order",command=lambda : openOrderWindow("black,1,600"),font="20").grid(row=3, column=0)
#
frame4 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
frame4.pack(fill='x', expand=1, side='right')
image4 = Image.open('r4.jpg')
image4.thumbnail((100, 100))
i4 = ImageTk.PhotoImage(image4)  # .grid(row=0,column=0)
Label(frame4, image=i4).grid(row=0, column=0)
Label(frame4, text='Price:850 ').grid(row=1, column=0)
Label(frame4, text='Quantity:1 ').grid(row=2, column=0)
Button(frame4, text="Order",command=lambda : openOrderWindow("red,1,850"),font="20").grid(row=3, column=0)
Button(root,text="Next",command=run_program3 ,font="20").place(x=500,y=330)
Button(root,text="Back",command=run_program,font="20").place(x=50,y=330)
Button(root,text="Previous",command=run_program1,font="20").place(x=420,y=330)
root.mainloop()