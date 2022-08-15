from sqlalchemy import create_engine
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import subprocess
root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='skyblue'
root.geometry("1100x700")
def run_program():
    root.destroy()
    subprocess.call(["python", "admin_section.py"])
#label
Label(root,text="Insertion",font="ariel 20 bold",bg="blue",fg="white",).pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('insert.jpg')
image1.thumbnail((805, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)


#Combobox
def comboFunction(event):
    print(combo1.get())
    print(combo2.get())
    print(combo3.get())

btn_browse = tk.Button(root, text='Select Image',bg='grey', fg='#ffffff',
                       font=('verdana',16))

def selectPic(): # Image upload and display
    global filename,image
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",filetypes=(("png images", "*.png"), ("jpg images", "*.jpg")))
    image = Image.open(filename)
    image = image.resize((200, 200), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(file=filename)
    lbl_show_pic['image'] = image
    entry_pic_path.insert(0, filename)

btn_browse['command'] = selectPic


def add_data():
    global image, filename
    fob = open(filename, 'rb')  # filename from upload_file()
    fob = fob.read()
    data = (combo1.get(),combo2.get(),combo3.get(),Quantity_entry.get(),Price_entry.get(), fob)  # tuple with data
    my_conn = create_engine("mysql+mysqldb://root:""@localhost/tsms")
    color_code = my_conn.execute("INSERT INTO insertion(color_code,color,size,quantity,price,image) values (%s, %s, %s, %s, %s, %s)", data)
    print("Row Added  = ", color_code.rowcount)  # displayed in console
    messagebox.showinfo("", "Data inserted successfully")
    root.destroy()
    subprocess.call(["python", "admin_section.py"])


Label(root,text="Enter Color Code:",font="5").place(x=560,y=60)
combo1 = ttk.Combobox(root,values=["1","2","3","4"],height=25,width=25)
combo1.place(x=800,y=60)

combo1.set("Select Color Code")
combo1.bind('<<ComboboxSelected>>',comboFunction)


Label(root,text="Enter Color:",font="5").place(x=560,y=100)
combo2 = ttk.Combobox(root,values=["Black","Red","Yellow","Gray"],height=25,width=25)
combo2.place(x=800,y=100)

combo2.set("Select Color")
combo2.bind('<<ComboboxSelected>>',comboFunction)

Label(root,text="Enter Size:",font="5").place(x=560,y=140)
combo3 = ttk.Combobox(root,values=["Large","Medium","Small"],height=25,width=25)
combo3.place(x=800,y=140)

combo3.set("Select Size")
combo3.bind('<<ComboboxSelected>>',comboFunction)

lbl_pic_path = tk.Label(root, text='Image Path:',font=('verdana',16), bg='#FFC0CB')
lbl_show_pic = tk.Label(root, bg='#45aaf2')

Label(root,text="Quantity:",font="20").place(x=560,y=190)
Label(root,text="Price:",font="20").place(x=560,y=240)

#Entry
Quantity_entry=Entry(root,font="10",bd=4)
Quantity_entry.place(x=800,y=190)
Price_entry=Entry(root,font="10",bd=4)
Price_entry.place(x=800,y=240)
entry_pic_path = tk.Entry(root, font=('verdana',16))

#Button
Button(root,text="Insert",command=add_data,font="ariel 20 bold").place(x=900,y=500)
Button(root,text="Back",command=run_program,font="ariel 20 bold").place(x=900,y=600)

lbl_pic_path.place(x=600, y=350)
entry_pic_path.place(x=800, y=350)
lbl_show_pic.place(x=250, y=400)
btn_browse.place(x=800, y=450)

root.mainloop()