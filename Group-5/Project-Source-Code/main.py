from tkinter import *
from subprocess import call
from PIL import ImageTk, Image

root=Tk()
root.title('University registration')
root.geometry('500x500')
Label(text="University registration  ", bg="blue", width="300", height="4", font=("Calibri", 20)).pack()
Label(text="").pack()
Label(text="NN ", bg="blue", width="300", height="80", font=("Calibri", 50)).pack()
Label(text="").pack()
frame = Frame(root)
frame.pack(pady=200,padx=200)
frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("North-Western-University-Logo.png"))
label = Label(frame, image = img)
label.pack()



def Open():
    call(["python", "page 1.py"])
btn=Button(frame,text='Continue',command=Open)
btn.pack()

root.mainloop()
