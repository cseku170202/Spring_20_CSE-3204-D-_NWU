from tkinter import ttk
from tkinter import *
import subprocess
from PIL import ImageTk, Image

root = Tk()
root.title("T-Shirt Stock Management System")
root['bg']='skyblue3'
root.geometry("1000x550")

def run_program():
    root.destroy()
    subprocess.call(["python", "main.py"])

def run_program1():
    root.destroy()
    subprocess.call(["python", "product1.py"])
def run_program2():
    root.destroy()
    subprocess.call(["python", "product2.py"])
def run_program3():
    root.destroy()
    subprocess.call(["python", "product3.py"])
def run_program4():
    root.destroy()
    subprocess.call(["python", "product4.py"])

def comboFunction(event):
    print(combo1.get())

def checkcmbo():
    if combo1.get() == "Black":
        root.destroy()
        subprocess.call(["python", "product1.py"])

    elif combo1.get() == "Red":
        root.destroy()
        subprocess.call(["python", "product2.py"])

    elif combo1.get() == "Yellow":
        root.destroy()
        subprocess.call(["python", "product3.py"])

    elif combo1.get() == "Gray":
        root.destroy()
        subprocess.call(["python", "product4.py"])

    else:
        print("error")


#label
Label(root,text="Search T-Shirt",font="ariel 20 bold",bg="deepskyblue",fg="black").pack(fill="both")

# Frame left
frame1 = LabelFrame(root, labelanchor='n',height=450,bg="skyblue3")
# frame1.pack(fill='both',expand=1,side='left')
frame1.pack(fill="both")
image1 = Image.open('search.jpg')
image1.thumbnail((805, 805))
i1 = ImageTk.PhotoImage(image1,size="300")
Label(frame1, image=i1).grid(row=0, column=0)

Label(root,text="Color search here:",font="5").place(x=600,y=76)

combo1 = ttk.Combobox(root,values=["Black","Red","Yellow","Gray"],height=25,width=25)
# combo1.pack(padx=20,pady=40)
combo1.place(x=800,y=80)

combo1.set("Select Color Code")
combo1.bind('<<ComboboxSelected>>',comboFunction)

#Button
Button(root,text="Search",command=checkcmbo,font="ariel 19 bold",bg='skyblue').place(x=800,y=150)
Button(root,text="  Back  ",command=run_program,font="ariel 19 bold",bg='skyblue').place(x=880,y=305)
Button(root,text="1",command=run_program1,font="20",bg='black',fg='white').place(x=650,y=400)
Button(root,text="2",command=run_program2,font="20",bg='red',fg='white').place(x=750,y=400)
Button(root,text="3",command=run_program3,font="20",bg='yellow',fg='white').place(x=850,y=400)
Button(root,text="4",command=run_program4,font="20",bg='gray',fg='white').place(x=950,y=400)

root.mainloop()
