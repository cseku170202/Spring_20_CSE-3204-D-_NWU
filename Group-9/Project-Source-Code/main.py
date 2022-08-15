from tkinter import *
import subprocess
from PIL import ImageTk, Image
root=Tk()
root.title('T-Shirt Stock Management System')
root['bg']='skyblue3'
root.geometry("1000x600")
def run_program():
    root.destroy()
    subprocess.call(["python", "admin_login.py"])
def run_program1():
    root.destroy()
    subprocess.call(["python", "registration.py"])
#label
Label(root,text="WELCOME TO OUR ONLINE T-SHIRT STORE",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")


# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('home_page.jpg')
image1.thumbnail((1105, 700))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

#Button
Button(root,text="ADMIN",command=run_program,font="ariel 20 bold").place(x=400,y=300)
Button(root,text="USER",command=run_program1,font="ariel 20 bold").place(x=400,y=420)
root.mainloop()