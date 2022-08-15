from tkinter import *
import subprocess

from PIL import ImageTk, Image

root=Tk()
root.title('T-Shirt Stock Management System')
root['bg']='gray'
root.geometry("1100x450")

def run_program1():
    root.destroy()
    subprocess.call(["python", "insert.py"])
def run_program2():
    root.destroy()
    subprocess.call(["python", "showproduct.py"])
def run_program5():
    root.destroy()
    subprocess.call(["python", "main.py"])

    # label
    Label(root, text="Admin Login", font="ariel 20 bold", bg="blue", fg="white", ).pack(fill="both")


#label
Label(root,text="Admin Section",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="chocolate3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('admi_s.jpg')
image1.thumbnail((805, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)


#Button
Button(root,text="Insert",command=run_program1,font="ariel 20 bold").place(x=650,y=120)
Button(root,text="Show",command=run_program2,font="ariel 20 bold").place(x=800,y=220)
Button(root,text="Back",command=run_program5,font="ariel 20 bold").place(x=900,y=350)
root.mainloop()