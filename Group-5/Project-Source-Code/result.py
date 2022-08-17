from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

# contrast border thumbnail
ws = Tk()
ws.title("Simple Photo Editor")
ws.geometry("640x640")


# create functions
def selected():
    global image_path, image
    image_path = filedialog.askopenfilename(initialdir=os.getcwd())
    image = Image.open(image_path)
    image.thumbnail((350, 350))
    # imgg = img.filter(ImageFilter.BoxBlur(0))
    image1 = ImageTk.PhotoImage(image)
    canvas2.create_image(300, 210, image=image1)
    canvas2.image = image1


def blur(event):
    global image_path, image1, imgg
    for m in range(0, v1.get() + 1):
        image = Image.open(image_path)
        image.thumbnail((350, 350))
        imgg = image.filter(ImageFilter.BoxBlur(m))
        image1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 210, image=image1)
        canvas2.image = image1


def brightness(event):
    global image_path, image2, image3
    for m in range(0, v2.get() + 1):
        image = Image.open(image_path)
        image.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(image)
        image2 = imgg.enhance(m)
        image3 = ImageTk.PhotoImage(image2)
        canvas2.create_image(300, 210, image=image3)
        canvas2.image = image3


def contrast(event):
    global image_path, image4, image5
    for m in range(0, v3.get() + 1):
        image = Image.open(image_path)
        image.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(image)
        image4 = imgg.enhance(m)
        image5 = ImageTk.PhotoImage(image4)
        canvas2.create_image(300, 210, image=image5)
        canvas2.image = image5


def rotate_image(event):
    global image_path, image6, image7
    image = Image.open(image_path)
    image.thumbnail((350, 350))
    image6 = image.rotate(int(Rotate_combo.get()))
    image7 = ImageTk.PhotoImage(image6)
    canvas2.create_image(300, 210, image=image7)
    canvas2.image = image7


def flip_image(event):
    global image_path, image8, image9
    image = Image.open(image_path)
    image.thumbnail((350, 350))
    if Flip_combo.get() == "FLIP LEFT TO RIGHT":
        image8 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif Flip_combo.get() == "FLIP TOP TO BOTTOM":
        image8 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image9 = ImageTk.PhotoImage(image8)
    canvas2.create_image(300, 210, image=image9)
    canvas2.image = image9


def image_border(event):
    global image_path, image10, image11
    image = Image.open(image_path)
    image.thumbnail((350, 350))
    image10 = ImageOps.expand(image, border=int(Border_combo.get()), fill=95)
    image11 = ImageTk.PhotoImage(image10)
    canvas2.create_image(300, 210, image=image11)
    canvas2.image = image11


image1 = None
image3 = None
image5 = None
image7 = None
image9 = None
image11 = None


def save():
    global image_path, imgg, image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11
    # file=None
    ext = image_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if canvas2.image == image1:
            imgg.save(file)
        elif canvas2.image == image3:
            image2.save(file)
        elif canvas2.image == image5:
            image4.save(file)
        elif canvas2.image == image7:
            image6.save(file)
        elif canvas2.image == image9:
            image8.save(file)
        elif canvas2.image == image11:
            image10.save(file)
        # create labels, scales and comboboxes


blurr = Label(ws, text="Blur:", font=("ariel 17 bold"), width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale = ttk.Scale(ws, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale.place(x=150, y=10)
bright = Label(ws, text="Brightness:", font=("ariel 17 bold"))
bright.place(x=8, y=50)
v2 = IntVar()
Scale1 = ttk.Scale(ws, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
Scale1.place(x=150, y=55)
contrast = Label(ws, text="Contrast:", font=("ariel 17 bold"))
contrast.place(x=35, y=92)
v3 = IntVar()
Scale2 = ttk.Scale(ws, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast)
Scale2.place(x=150, y=100)
Rotate = Label(ws, text="Rotate:", font=("ariel 17 bold"))
Rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
Rotate_combo = ttk.Combobox(ws, values=values, font=('ariel 10 bold'))
Rotate_combo.place(x=460, y=15)
Rotate_combo.bind("<<ComboboxSelected>>", rotate_image)
Flip = Label(ws, text="Flip:", font=("ariel 17 bold"))
Flip.place(x=400, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
Flip_combo = ttk.Combobox(ws, values=values1, font=('ariel 10 bold'))
Flip_combo.place(x=460, y=57)
Flip_combo.bind("<<ComboboxSelected>>", flip_image)
border = Label(ws, text="Add border:", font=("ariel 17 bold"))
border.place(x=320, y=92)
values2 = [i for i in range(10, 45, 5)]
Border_combo = ttk.Combobox(ws, values=values2, font=("ariel 10 bold"))
Border_combo.place(x=460, y=99)
Border_combo.bind("<<ComboboxSelected>>", image_border)
# create canvas to display image
canvas2 = Canvas(ws, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)
# create buttons
button1 = Button(ws, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                 command=selected)
button1.place(x=100, y=595)
button2 = Button(ws, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
button2.place(x=280, y=595)
button3 = Button(ws, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE,
                 command=ws.destroy)
button3.place(x=460, y=595)
ws.mainloop()
