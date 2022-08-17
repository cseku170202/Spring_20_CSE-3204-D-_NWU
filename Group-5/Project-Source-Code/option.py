from tkinter import *
import tkinter as tk
from subprocess import call
from PIL import ImageTk, Image
import tkinter.font as tkFont

app = tk.Tk()
app.title('Log')
app.geometry("800x500")
frame = Frame(app)
frame.pack(pady=200,padx=200)
frame = Frame(app, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("bb.jpg"))
label = Label(frame, image = img)
label.pack()



def decreaseSize():
    buttonExample1.configure(height=100,
                             width=100)


def increaseSize():
    buttonExample2.configure(height=400,
                             width=400)


pixelVirtual = tk.PhotoImage(width=1, height=1)
def Open():
    call(["python", "sregis.py"])
buttonExample1 = tk.Button(app,
                           text="Add student details",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound="c",
                           bg="#A5A52A",
                           command=Open)
buttonExample1.pack(side=tk.LEFT)
def Open():
    call(["python", "search.py"])
buttonExample2 = tk.Button(app,
                           text="Search student Information",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound=tk.CENTER,
                           bg="#A5A52A",
                           command=Open)
buttonExample2.pack(side=tk.TOP)
def Open():
    call(["python", "resultadd.py"])
buttonExample3 = tk.Button(app,
                           text="Student result add",
                           image=pixelVirtual,
                           width=200,
                           height=100,
                           compound=tk.CENTER,
                           bg="#A5A52A",
                           command=Open)
buttonExample3.place(x=10, y=20)



app.mainloop()
