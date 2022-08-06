from tkinter import *
from subprocess import call
from tkinter import messagebox
from tkinter.font import BOLD

from PIL import ImageTk, Image
root = Tk()
root.title("Main Dashboard")
root.configure(bg="#90EE90")

# root.geometry("1120x718")
root.resizable(False, False)
window_width,window_height=1120,718

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

canv = Canvas(root, width=1120, height=718, bg='white')
canv.place(x=0,y=0)

img = ImageTk.PhotoImage(Image.open("i1.jpg"))  # PIL solution
canv.create_image(0,0, anchor=NW, image=img)

#mylabel1=Label(root, text="Welcome To Khulna BRTA \n Vehicle Management System",font='Times 35 bold',bg="#fff2e5").place(x=500,y=2)
canv.create_text(730, 70, text="Welcome To Khulna BRTA \n Vehicle Management System", fill="black", font='Times 35 bold')
canv.pack()
#mylabel1.configure(font=("Helvetica",BOLD, 18))


def emp():
    root.destroy()
    call(["python", "emp_log_in.py"])

def ser():
    root.destroy()
    call(["python", "ser_log_in.py"])

def own():
    root.destroy()
    call(["python", "own_log_in.py"])

def exit_window():

    response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
    if response:
        root.destroy()


    else:
        messagebox.showinfo("SYSTEM ALERT", "Canceled")




Button(root,text="Employee Log in",command=emp,height=4,width=18,font='Times 18 bold',bg="#8f8d5b").place(x=710,y=180)
Button(root,text="Sergeant Log in",command=ser,height=4,width=18,font='Times 18 bold',bg="#8f8d5b").place(x=750,y=315)
Button(root,text="Owner Log in",command=own,height=4,width=18,font='Times 18 bold',bg="#8f8d5b").place(x=790,y=450)
Button(root,text="Exit",command=exit_window,height=3,width=9,font='Times 18 bold',bg="#8f8d5b").place(x=800,y=600)

root.mainloop()