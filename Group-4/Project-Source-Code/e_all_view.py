import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from subprocess import call
from tkinter import messagebox

r=tk.Tk()
r.title("View Vehicle Details")
r.geometry("600x300")
r.configure(bg="#C0D7D8")

window_width,window_height=1500,400

screen_width=r.winfo_screenwidth()
screen_height=r.winfo_screenheight()

position_top=int(screen_height/2-window_height/2)
position_right=int(screen_width/2-window_width/2)

r.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')



connect=mysql.connector.connect(host="localhost",user="root",password="",database="vms")
conn=connect.cursor()
conn.execute("select * from vms_info")

rightframe = Frame(r, width=200, height=200, relief=SUNKEN)
rightframe.pack(side=BOTTOM)

tree=ttk.Treeview(rightframe)
tree['show']='headings'

s=ttk.Style(r)
s.theme_use("xpnative")
s.configure(".",font=('Helvetic',11))
s.configure("Treeview.Heading",foreground='red',font=('Helvetic',11))



#define number of columns

tree["columns"]=("type","c_name","model","origin","capasity","color","name","reg","m_date","e_num","c_num","weight","r_date","b_from","price")

#assign the width,minwidth and anchor to the respective columns
tree.column("type",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("c_name",width=110,minwidth=50,anchor=tk.CENTER)
tree.column("model",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("origin",width=100,minwidth=50,anchor=tk.CENTER)
tree.column("capasity",width=100,minwidth=50,anchor=tk.CENTER)
tree.column("color",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("name",width=100,minwidth=50,anchor=tk.CENTER)
tree.column("reg",width=70,minwidth=50,anchor=tk.CENTER)
tree.column("m_date",width=110,minwidth=50,anchor=tk.CENTER)
tree.column("e_num",width=150,minwidth=50,anchor=tk.CENTER)
tree.column("c_num",width=150,minwidth=50,anchor=tk.CENTER)
tree.column("weight",width=50,minwidth=50,anchor=tk.CENTER)
tree.column("r_date",width=100,minwidth=50,anchor=tk.CENTER)
tree.column("b_from",width=70,minwidth=50,anchor=tk.CENTER)
tree.column("price",width=80,minwidth=50,anchor=tk.CENTER)

#assign to the heading name to the respective columns
tree.heading("type",text="Type",anchor=tk.CENTER)
tree.heading("c_name",text="Company name",anchor=tk.CENTER)
tree.heading("model",text="Model",anchor=tk.CENTER)
tree.heading("origin",text="Brand Origin",anchor=tk.CENTER)
tree.heading("capasity",text="Seat Capasity",anchor=tk.CENTER)
tree.heading("color",text="color",anchor=tk.CENTER)
tree.heading("name",text="Owner Name",anchor=tk.CENTER)
tree.heading("reg",text="Reg NO",anchor=tk.CENTER)
tree.heading("m_date",text="Manufact Date",anchor=tk.CENTER)
tree.heading("e_num",text="Engine Number",anchor=tk.CENTER)
tree.heading("c_num",text="Cassis Number",anchor=tk.CENTER)
tree.heading("weight",text="weight",anchor=tk.CENTER)
tree.heading("r_date",text="Reg Date",anchor=tk.CENTER)
tree.heading("b_from",text="Buy from",anchor=tk.CENTER)
tree.heading("price",text="Price",anchor=tk.CENTER)


i=0
for ro in conn:
    tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11],ro[12],ro[13],ro[14]))
    i=i+1

hsb=ttk.Scrollbar(r,orient="vertical")

hsb.configure(command=tree.xview)
tree.configure(yscrollcommand=hsb.set)
#hsb.pack(fill=Y,side=TOP)

tree.pack()


def log_out():
    r.destroy()
    call(["python", "main.py"])

Button(r,text="Log Out",command=log_out,height=2,width=7,bg="#D484B7",font="Times 14 bold").place(x=1400,y=5)

def back():
    r.destroy()
    call(["python", "emp_main.py"])


Button(r,text="Back",command=back,height=2,width=7,bg="#D484B7",font="Times 14 bold").place(x=5,y=5)


def Delete():
    if not tree.selection():
        messagebox.showwarning("Warning", "Select data to delete")
    else:
        result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                        icon="warning")
    if result == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        print(selecteditem[7])
        tree.delete(curItem)
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="vms")
        mycursor = mysqldb.cursor()

        sql = "DELETE FROM vms_info WHERE reg =" +str(selecteditem[7])+ ""
        mycursor.execute(sql)
        mysqldb.commit()
        messagebox.showinfo("information", "Record deleted Successfully")




Button(r,text="Delete",command=Delete,height=2,width=7,bg="#D484B7",font="Times 14 bold").place(x=700,y=100)






r.mainloop()
