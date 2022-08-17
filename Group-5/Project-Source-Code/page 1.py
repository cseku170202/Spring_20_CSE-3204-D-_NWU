from tkinter import *
import tkinter as tk
from subprocess import call
from PIL import ImageTk, Image
import tkinter.font as tkFont

app = tk.Tk()
app.title('Log')
app.geometry("600x500")
frame = Frame(app)
frame.pack(pady=200,padx=200)
frame = Frame(app, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("exam-studying-wallpaper-preview.jpg"))
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
    call(["python", "Student log.py"])
buttonExample1 = tk.Button(app,
                           text="Student",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound="c",
                           command=Open)
buttonExample1.pack(side=tk.LEFT)
def Open():
    call(["python", "Admin log in.py"])
buttonExample2 = tk.Button(app,
                           text="Admin",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound=tk.CENTER,
                           command=Open)
buttonExample2.pack(side=tk.RIGHT)



app.mainloop()
