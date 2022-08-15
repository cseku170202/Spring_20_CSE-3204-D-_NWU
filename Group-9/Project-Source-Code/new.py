import tkinter  as tk
from tkinter import *
from sqlalchemy import create_engine
import io
from PIL import Image, ImageTk
my_w = tk.Tk() # parent window
my_w.geometry("600x700") # size as width height
my_w.title("www.plus2net.com")  # Adding a title
# database connection
my_conn = create_engine("mysql+mysqldb://root:""@localhost/tsms")
my_row=my_conn.execute("SELECT * FROM insertion limit 0,4")
# Column headers  row 0
l1=Label(my_w, text='code')
l1.grid(row=0,column=1)
l2=Label(my_w, text='color')
l2.grid(row=0,column=2)
l3=Label(my_w, text='size')
l3.grid(row=0,column=3)
l4=Label(my_w, text='quantity')
l4.grid(row=0,column=4)
l5=Label(my_w, text='price')
l5.grid(row=0,column=5)
i=1 # data starts from row 1
images = [] # to manage garbage collection.
for color_code in my_row:
    stream = io.BytesIO(color_code[2])
    img=Image.open(stream)
    img = ImageTk.PhotoImage(img)
    e = Label(my_w, text=color_code[0])
    e.grid(row=i,column=1,ipadx=20)
    e = Label(my_w, text=color_code[1])
    e.grid(row=i,column=2,ipadx=60)
    e = Label(my_w, image=img)
    e.grid(row=i, column=3,ipady=7)
    images.append(img) # garbage collection
    i=i+1
my_w.mainloop()