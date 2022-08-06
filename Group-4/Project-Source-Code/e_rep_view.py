import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from subprocess import call
from tkinter import messagebox

r=tk.Tk()
r.title("View Vehicle Details")
r.geometry("600x300")
r.configure(bg="#E6EFF0")

window_width,window_height=800,400

screen_width=r.winfo_screenwidth()
screen_height=r.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

r.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')



connect=mysql.connector.connect(host="localhost",user="root",password="",database="vms")
conn=connect.cursor()
conn.execute("select * from rep")

rightframe = Frame(r, width=200, height=200, relief=SUNKEN)
rightframe.pack(side=BOTTOM)

tree=ttk.Treeview(rightframe)
tree['show']='headings'

s=ttk.Style(r)
s.theme_use("xpnative")
s.configure(".",font=('Helvetic',11))
s.configure("Treeview.Heading",foreground='red',font=('Helvetic',11))



#define number of columns

tree["columns"]=("reg","claim_det")

#assign the width,minwidth and anchor to the respective columns
tree.column("reg",width=100,minwidth=50,anchor=tk.CENTER)
tree.column("claim_det",width=410,minwidth=50,anchor=tk.CENTER)


#assign to the heading name to the respective columns
tree.heading("reg",text="REG No",anchor=tk.CENTER)
tree.heading("claim_det",text="REPORT DETAILS",anchor=tk.CENTER)


i=0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1]))
    i=i+1

hsb=ttk.Scrollbar(r,orient="vertical")

hsb.configure(command=tree.xview)
tree.configure(yscrollcommand=hsb.set)
#hsb.pack(fill=Y,side=TOP)

tree.pack()


def log_out():
    r.destroy()
    call(["python", "main.py"])

Button(r,text="Log Out",command=log_out,height=2,width=7,bg="#738D8F",font="Times 14 bold").place(x=700,y=5)

def back():
    r.destroy()
    call(["python", "emp_main.py"])


Button(r,text="Back",command=back,height=2,width=7,bg="#738D8F",font="Times 14 bold").place(x=5,y=5)


def Delete():
    # open database
    #Database()
    if not tree.selection():
        messagebox.showwarning("Warning", "Select data to delete")
    else:
        result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                        icon="warning")
    if result == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        #reg=selecteditem[8]
        print(selecteditem[0])
        tree.delete(curItem)
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
        mycursor = mysqldb.cursor()

        sql = "DELETE FROM rep WHERE reg =" +str(selecteditem[0])+ ""
        mycursor.execute(sql)
        mysqldb.commit()
        messagebox.showinfo("information", "Record deleted Successfully")




Button(r,text="Delete",command=Delete,height=2,width=7,bg="#738D8F",font="Times 14 bold").place(x=350,y=5)






r.mainloop()
