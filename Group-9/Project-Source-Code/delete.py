import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
from PIL import ImageTk, Image
root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='gray'
root.geometry("1200x500")



def run_program():
    root.destroy()
    subprocess.call(["python", "show.py"])

def comboFunction(event):
    print(combo1.get())

def ok():
    color_code = combo1.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root",password="",database="tsms")
    mycursor = mysqldb.cursor()


    try:
       sql = "delete from insertion where color_code=%s"
       val =(color_code,)
       mycursor.execute(sql, val)
       mysqldb.commit()

       print(mycursor.rowcount);
       messagebox.showinfo("", "Data delete successfully")

       root.destroy()
       subprocess.call(["python", "admin_section.py"])


    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
#label
Label(root,text="Delete Data",font="ariel 20 bold",bg='#f40f6e',fg="white",).pack(fill="both")
# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg='#f40f6e')
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('delet1.jpg')
image1.thumbnail((805, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

Label(root,text="Enter Color Code:",font="5").place(x=500,y=60)
combo1 = ttk.Combobox(root,values=["1","2","3","4"],height=25,width=25)
# combo1.pack(padx=10,pady=20)
combo1.place(x=700,y=62)

combo1.set("Select Color Code")
combo1.bind('<<ComboboxSelected>>',comboFunction)


#Button
Button(root,text="Delete",command=ok,font="ariel 20 bold").place(x=970,y=230)
Button(root,text="Back",command=run_program,font="ariel 20 bold").place(x=1070,y=430)
root.mainloop()