from tkinter import*
from PIL import ImageTk, Image
from subprocess import call
root = Tk()
root.title("Details")
root.geometry("1350x700+0+0")



Label(text="University ",font=("goudly old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

M_Frame=LabelFrame(root,text="Menu",font=("times new roman",15),bg="white")
M_Frame.place(x=10,y=70,width=1340,height=80)
def Open():
    call(["python", "personal.py"])
btn_course=Button(M_Frame,text="Personal Info",command=Open,font=("goudly old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=20,y=5,width=200,height=40)
def Open():
    call(["python", "Resist.py"])
btn_Student=Button(M_Frame,text="Registration", command=Open,font=("goudly old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=240,y=5,width=200,height=40)
def Open():
    call(["python", "report.py"])
btn_Result=Button(M_Frame,text="Result", command=Open,font=("goudly old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=460,y=5,width=200,height=40)
def Open():
    call(["python", "main.py"])
btn_View=Button(M_Frame,text="Exit",command=root.destroy,font=("goudly old style",20,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=700,y=5,width=200,height=40)


bg_img=Image.open("science-1182713_960_720.jpg")
bg_img=ImageTk.PhotoImage(bg_img)
lbl_bg=Label(root,image=bg_img).place(x=350,y=180,width=1000,height=300)


footer=Label(text="SRMS-Student management result\ncontact Us for any technical Issue: 0165025768",font=("goudly old style",12),bg="#262626",fg="white").place(x=0,y=650,relwidth=1,height=60)




root.mainloop()