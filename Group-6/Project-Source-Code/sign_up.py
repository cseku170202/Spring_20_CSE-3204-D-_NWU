from tkinter import *
from tkinter import messagebox, ttk, filedialog
from subprocess import call
import sqlite3
from io import BytesIO
from PIL import Image,ImageTk

sign = Tk()

def submitact():
    mysqldb = sqlite3.connect(database="brm.db")
    mycursor = mysqldb.cursor()
    Image = var_photo.get(),
    Name = var_name.get(),
    Email = email_field.get(),
    Pass = password_field.get()
    try:
        if (Email == "" or Pass == "" or Image == "" or Name == ""):
            messagebox.showinfo("", "Please fill the fields")
        else:
            cur.execute(
                "insert into owner (image,name,email,password) values (?,?,?,?)",
                (
                    var_photo.get(),
                    var_name.get(),
                    email_field.get(),
                    password_field.get(),
                ))
            con.commit()
            messagebox.showinfo("Success", "Signup Successfully")
    except Exception as ex:
        messagebox.showerror("Error", f"Error duo to {str(ex)}")
        sign.destroy()
        import main
    return Name

def user():
    sign.destroy()
    import main

def post_data():
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetype=(("jpeg files", "*.jpg"), ("PNG  files", "*.png")))
    image = Image.open(filename)  # Read the Image

    resize_image = image.resize((200, 150))
    show_img = ImageTk.PhotoImage(resize_image)
    # show the resized image
    label_photo.config(image=show_img)
    label_photo.image = show_img
    # save the image data into var_photo
    outfile = BytesIO()
    resize_image.save(outfile, "PNG")
    var_photo.set(outfile.getvalue())

con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT, photo BLOB )")

var_name = StringVar()
var_photo = Variable()

back_btn = Button(sign, text='Back', padx=15, font=('areal',10), fg='#ffffff', bg='#ff0000', command=user)
back_btn.place(x=20, y=20)

signUp_label = Label(sign, text = "Sign up", font = ('areal',30,'bold'))
signUp_label.place(x=300, y=80, anchor='center')

bl_Name = Label(sign, text="Image", font=("Arial", 15)).place(x=80, y=280)
img_LabelFrame = ttk.LabelFrame(sign, text="")
img_LabelFrame.place(x=200, y=220, width=200, height=150)
img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()

btn_upload_img = Button(text="Chose file", font=('areal',12), bg="#dddddd", command=post_data).place(x=200, y=400, width=150, height=40)

name_label = Label(sign,text='Name',font=('areal',15)).place(x=100,y=145)
name_field = Entry(sign, textvariable=var_name, width=30, font=('areal',15)).place(x=183,y=150)
email_label = Label(sign,text="Email",font=('areal',15))
email_label.place(x=100,y=490)
email_field = Entry(sign, width=30, font=('areal',15))
email_field.place(x=350, y=505, anchor='center')

password_label = Label(sign, text = "Password", font = ('areal',15))
password_label.place(x=120, y=580, anchor='center')
password_field = Entry(sign, width=30, font=('areal',15))
password_field.place(x=350, y=580, anchor='center')
password_field.config(show='*')

signUp_btn = Button(sign, text='Signup', padx=25, font=('areal',18),fg='#ffffff', bg='#15BDF2', command=submitact)
signUp_btn.place(x=220, y=660)

sign.geometry('600x800')

sign.mainloop()