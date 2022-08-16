from tkinter import *
import sqlite3

notification = Tk()
notification.geometry('800x700')

def back():
    notification.destroy()
    import admin

Title = Label(notification,text='Notification',font=('areal',25,'bold')).pack(pady=20)

my_connect = sqlite3.connect(database='brm.db')
my_conn = my_connect.cursor()
my_conn.execute("SELECT name FROM rent")
results = my_conn.fetchall()
for x in results:
    for result in x:
        ownerLabel = Label(notification, text=result + 's home is rented', font=('areal', 15)).pack(pady=5)

backBtn = Button(notification, text="Back", padx=20, font=('areal',15),bg='#ff0000',fg='#ffffff', command=back)
backBtn.place(x=50, y=30)

notification.mainloop()