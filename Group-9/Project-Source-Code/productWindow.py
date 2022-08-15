import os
from tkinter import *
from PIL import ImageTk, Image
import subprocess
import mysql.connector

root = Tk()
root.title('Products')
frame1 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(expand=1, anchor='w')
image1 = Image.open('ryan-hoffman-u6n1HrW0sdQ-unsplash.jpg')
image1.thumbnail((100, 100))
i1 = ImageTk.PhotoImage(image1)

Label(frame1, image=i1).grid(row=0, column=0)
Label(frame1, text='Price: ').grid(row=1, column=0)
Label(frame1, text='Quantity: ').grid(row=2, column=0)
# Label(frame1, text='Order: ').grid(row=3, column=0)
def openOrderWindow(tShirtInfo):
    #subprocess.call(["python", "orderwindow.py"],env=os.environ)

    username=os.environ['USERNAME']
    subprocess.call(["C:\\Users\\"+username+"\\PycharmProjects\\pythonProject\\venv\\Scripts\\python.exe","orderWindow.py", tShirtInfo])

Button(frame1,text="Order",command=lambda : openOrderWindow("red,1,800"),font="20").grid(row=3, column=0)

#
frame2 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
frame2.pack(fill='x', expand=1, side='right')
image2 = Image.open('blacktshirt.jpg')
image2.thumbnail((100, 100))
i2 = ImageTk.PhotoImage(image2)  # .grid(row=0,column=0)
Label(frame2, image=i2).grid(row=0, column=0)
Label(frame2, text='Price: ').grid(row=1, column=0)
Label(frame2, text='Quantity: ').grid(row=2, column=0)
# Label(frame2, text='Order: ').grid(row=3, column=0)
Button(frame2,text="Order",command=lambda : openOrderWindow("black,1,750"),font="20").grid(row=3, column=0)
#
frame3 = LabelFrame(root, borderwidth=0, labelanchor='n', padx=20, pady=20)
frame3.pack(fill='x', expand=1)
image3 = Image.open('redtshirt.jpg')
image3.thumbnail((100, 100))
i3 = ImageTk.PhotoImage(image3)  # .grid(row=0,column=0)
Label(frame3, image=i3).grid(row=0, column=0)
Label(frame3, text='Price: ').grid(row=1, column=0)
Label(frame3, text='Quantity: ').grid(row=2, column=0)
# Label(frame3, text='Order: ').grid(row=3, column=0)
Button(frame3,text="Order",command=lambda : openOrderWindow("red,1,850"),font="20").grid(row=3, column=0)

window1 = Toplevel()
framew1 = LabelFrame(window1, borderwidth=0, labelanchor='n', padx=20, pady=20)
# frame1.pack(fill='both',expand=1,side='left')
framew1.pack(expand=1, anchor='w')
imagew1 = Image.open('a1.png')
imagew1.thumbnail((100, 100))
iw1 = ImageTk.PhotoImage(imagew1)

Label(framew1, image=iw1).grid(row=0, column=0)
Label(framew1, text='Price: ').grid(row=1, column=0)
Label(framew1, text='Quantity: ').grid(row=2, column=0)
# Label(framew1, text='Order: ').grid(row=3, column=0)
Button(framew1,text="Order",command=lambda : openOrderWindow("green,1,600"),font="20").grid(row=3, column=0)
#
framew2 = LabelFrame(window1, borderwidth=0, labelanchor='n', padx=20, pady=20)
framew2.pack(fill='x', expand=1, side='right')
imagew2 = Image.open('b1.png')
imagew2.thumbnail((100, 100))
iw2 = ImageTk.PhotoImage(imagew2)  # .grid(row=0,column=0)
Label(framew2, image=iw2).grid(row=0, column=0)
Label(framew2, text='Price: ').grid(row=1, column=0)
Label(framew2, text='Quantity: ').grid(row=2, column=0)
# Label(framew2, text='Order: ').grid(row=3, column=0)
Button(framew2,text="Order",command=lambda : openOrderWindow("gray,1,400"),font="20").grid(row=3, column=0)
#
framew3 = LabelFrame(window1, borderwidth=0, labelanchor='n', padx=20, pady=20)
framew3.pack(fill='x', expand=1)
imagew3 = Image.open('c1.png')
imagew3.thumbnail((100, 100))
iw3 = ImageTk.PhotoImage(imagew3)  # .grid(row=0,column=0)
Label(framew3, image=iw3).grid(row=0, column=0)
Label(framew3, text='Price: ').grid(row=1, column=0)
Label(framew3, text='Quantity: ').grid(row=2, column=0)

# Label(framew3, text='Order: ').grid(row=3, column=0)
Button(framew3,text="Order",command=lambda : openOrderWindow("red,1,700"),font="20").grid(row=3, column=0)
root.mainloop()

