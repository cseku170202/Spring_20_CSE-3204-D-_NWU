import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from subprocess import call
from tkinter import messagebox
from PIL import ImageTk, Image
import Image

r = tk.Tk()
r.title("Show Customer's Feedback")
r.geometry("600x300")
r.configure(bg="#36013F")

canv = Canvas(r, width=950, height=600, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("rbb.jpg"))
canv.create_image(0,0, anchor=NW, image=img)

window_width, window_height = 950, 600

screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

r.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

def quit():
   response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
   if response:
      r.destroy()


   else:
      messagebox.showinfo("SYSTEM ALERT", "Canceled")


def back():
    r.destroy()
    call(['python', "after_admin_login_pg.py"])

tree = ttk.Treeview(r)
tree['show'] = 'headings'

s = ttk.Style(r)
s.theme_use("xpnative")
s.configure(".", font=('Helvetic', 11))
s.configure("Treeview.Heading", foreground='red', font=('Helvetic', 11))

# define number of columns

tree["columns"] = ("name", "mail", "comment")

# assign the width,minwidth and anchor to the respective columns
tree.column("name", width=150, minwidth=50, anchor=tk.CENTER)
tree.column("mail", width=300, minwidth=50, anchor=tk.CENTER)
tree.column("comment", width=250, minwidth=50, anchor=tk.CENTER)

# assign to the heading name to the respective columns
tree.heading("name", text="Customer Name", anchor=tk.CENTER)
tree.heading("mail", text=" Email", anchor=tk.CENTER)
tree.heading("comment", text="Comments", anchor=tk.CENTER)

connect = mysql.connector.connect(host="localhost", user="root", password="", database="rms")
conn = connect.cursor()
conn.execute("SELECT * FROM `feedback`")
i = 0
for ro in conn:
    tree.insert('', i, text="", values=(
    ro[0], ro[1], ro[2]))
    i = i + 1

hsb = ttk.Scrollbar(r, orient="horizontal")

hsb.configure(command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

tree.pack()

#mylabel=Label(r, text="Show Feedback",font='Times 30 bold').place(x=315,y=0)

Button(r, text="Exit", command=quit, height=1, width=7, font='Times 20 bold',bg='#463E3F',fg='white').place(x=855,y=500)
Button(r, text="Back", command=back, height=1, width=7, font='Times 20 bold',bg='#B6B6B4',fg='black').place(x=1,y=500)

r.mainloop()