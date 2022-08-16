from tkinter import *
from tkinter import messagebox, filedialog, ttk
import sqlite3
from PIL import Image, ImageTk
from io import BytesIO

post = Tk()
post.geometry('950x700')

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

def cancel():
    post.destroy()
    import user

con = sqlite3.connect(database="brm.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS std (name TEXT, photo BLOB )")

var_name = StringVar()
var_photo = Variable()

# def uploadImg():
#     filename = filedialog.askopenfilename(initialdir="/", title="Select an Image", filetype=(("jpeg files", "*.jpg"), ("PNG  files", "*.png")))
#     image = Image.open(filename)  # Read the Image
#
#     resize_image = image.resize((200, 150))
#     show_img = ImageTk.PhotoImage(resize_image)
#     # show the resized image
#     label_photo.config(image=show_img)
#     label_photo.image = show_img
#     # save the image data into var_photo
#     outfile = BytesIO()
#     resize_image.save(outfile, "PNG")
#     var_photo.set(outfile.getvalue())

def add():
    con = sqlite3.connect(database="brm.db")
    cur = con.cursor()
    try:
        if var_name.get() == "":
            messagebox.showerror("Error", "Title is Required")
        else:
            cur.execute("select * from std where title =? ", (var_name.get(),))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "Title is already exists")
            else:
                cur.execute("insert into std (image,title,address,contact,payment_method,definition,turms1,turms2,turms3,rent) values (?,?,?,?,?,?,?,?,?,?)", (
                    var_photo.get(),
                    title_field.get(),
                    address_field.get(),
                    contact_field.get(),
                    payment_clicked.get(),
                    definition_field.get(),
                    turms1_field.get(),
                    turms2_field.get(),
                    turms3_field.get(),
                    rent_field.get()
                ))
            con.commit()
            messagebox.showinfo("Success", "Posted Successfully")
    except Exception as ex:
        messagebox.showerror("Error", f"Error duo to {str(ex)}")

back_btn = Button(post, text='Back', padx=10, font=('areal',10),fg='#ffffff', bg='#ff0000', command=cancel)
back_btn.place(x=60, y=50)

login_label = Label(post, text = "Post", font = ('areal',30,'bold'))
login_label.place(x=430, y=50)

bl_Name = Label(post, text="Image", font=("Arial", 15,'bold')).place(x=80, y=145)
img_LabelFrame = ttk.LabelFrame(post, text="")
img_LabelFrame.place(x=155, y=90, width=250, height=150)
img_LabelFrame
label_photo = Label(img_LabelFrame)
label_photo.pack()

btn_upload_img = Button(text="Chose file", font=('areal',12), bg="#dddddd", command=post_data).place(x=200, y=250, width=150, height=40)

title = Label(post, text = "Title", font = ('areal',15,'bold'))
title.place(x=80, y=310)
title_field = Entry(post,textvariable=var_name, width=22, font=('areal',15))
title_field.place(x=280, y=320, anchor='center')

address = Label(post, text = "Address", font = ('areal',15,'bold'))
address.place(x=75, y=385)
address_field = Entry(post, width=22, font=('areal',15))
address_field.place(x=280, y=400, anchor='center')

email_label = Label(post, text = "Email", font = ('areal',15,'bold')).place(x=475, y=135)
email_field = Entry(post, width=22, font=('areal',15)).place(x=580, y=135)

contact = Label(post, text = "Contact", font = ('areal',15,'bold'))
contact.place(x=475, y=220)
contact_field = Entry(post, width=22, font=('areal',15))
contact_field.place(x=700, y=235, anchor='center')

definition = Label(post, text = "Definition", font = ('areal',15,'bold'))
definition.place(x=475, y=305)
definition_field = Entry(post, width=22, font=('areal',15))
definition_field.place(x=700, y=320, anchor='center')

payment_clicked = StringVar()
payment_clicked.set('Select payment method')
payment = OptionMenu(post, payment_clicked, 'Bkash', 'Nagad', 'Bank payment', 'Card', 'Hand cash')
payment.config(font=('areal',12))
payment.place(x=580, y=380)

turms1 = Label(post, text = "Turms1", font = ('areal',15,'bold'))
turms1.place(x=70, y=465)
turms1_field = Entry(post, width=22, font=('areal',15))
turms1_field.place(x=280, y=480, anchor='center')

turms2 = Label(post, text = "Turms2", font = ('areal',15,'bold'))
turms2.place(x=485, y=465)
turms2_field = Entry(post, width=22, font=('areal',15))
turms2_field.place(x=700, y=480, anchor='center')

rentLabel = Label(post, text = "Rent", font = ('areal',15,'bold'))
rentLabel.place(x=490, y=555)
rent_field = Entry(post, width=22, font=('areal',15))
rent_field.place(x=700, y=570, anchor='center')

turms3 = Label(post, text = "Turms3", font = ('areal',15,'bold'))
turms3.place(x=70, y=555)
turms3_field = Entry(post, width=22, font=('areal',15))
turms3_field.place(x=280, y=570, anchor='center')

rent_btn = Button(post, text='Post', padx=30, font=('areal',15),fg='#ffffff', bg='#15BDF2', command=add)
rent_btn.place(x=430, y=610)

post.mainloop()