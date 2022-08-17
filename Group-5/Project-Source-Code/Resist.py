from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error

root = Tk()
root['bg']='#0b5377'
root.title("Register Form")

width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# =======================================VARIABLES=====================================
USER = StringVar()
PASS = StringVar()
NAME = StringVar()
ADDRESS = StringVar()


# =======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = mysql.connector.connect(host='localhost',
                                   database='db',
                                   user='root',
                                   password='')
    cursor = conn.cursor()


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Register():
    Database()
    if USER.get == "" or PASS.get() == "" or NAME.get() == "" or ADDRESS.get == "":
        lbl_result.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `user` WHERE `user` = %s", [USER.get()])
        if cursor.fetchone() is not None:
            lbl_result.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `user` (user, pass, name, address) VALUES(%s, %s, %s, %s)",
                           (str(USER.get()), str(PASS.get()), str(NAME.get()), str(ADDRESS.get())))
            conn.commit()
            USER.set("")
            PASS.set("")
            NAME.set("")
            ADDRESS.set("")
            lbl_result.config(text="Successfully Created!", fg="green")
        cursor.close()
        conn.close()


# =====================================FRAMES====================================
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)

# =====================================LABEL WIDGETS=============================
lbl_title = Label(TitleFrame, text="Register Form", bg="Orange",font=('arial', 18), bd=1, width=640)
lbl_title.pack()
lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
lbl_username.grid(row=1)
lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
lbl_password.grid(row=2)
lbl_firstname = Label(RegisterFrame, text="Name:", font=('arial', 18), bd=18)
lbl_firstname.grid(row=3)
lbl_lastname = Label(RegisterFrame, text="Address:", font=('arial', 18), bd=18)
lbl_lastname.grid(row=4)
lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
lbl_result.grid(row=5, columnspan=2)

# =======================================ENTRY WIDGETS===========================
user = Entry(RegisterFrame, font=('arial', 20), textvariable=USER, width=15)
user.grid(row=1, column=1)
pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=PASS, width=15, show="*")
pass1.grid(row=2, column=1)
name = Entry(RegisterFrame, font=('arial', 20), textvariable=NAME, width=15)
name.grid(row=3, column=1)
address = Entry(RegisterFrame, font=('arial', 20), textvariable=ADDRESS, width=15)
address.grid(row=4, column=1)
# ========================================BUTTON WIDGETS=========================
btn_register = Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
btn_register.grid(row=6, columnspan=2)
# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()