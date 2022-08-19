from tkinter import*
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
from tkinter import ttk


def start_admin():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1200x630")

    bg = PhotoImage(file="F:/finalproject/admin.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)

    def log_in():

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        username_admin = entry1.get()
        userpass_admin = entry2.get()

        c.execute("SELECT * FROM admin_login WHERE username= ? AND password=?", (username_admin,userpass_admin,))
        record = c.fetchall()

        if record == []:
            messagebox.showerror("Error", "Username or Password was Incorrect")
        else:
            root.destroy()
            admin_page()

    label2 = Label(root, text="Admin Login Page", font="timesnewroman 15 bold", padx=20, pady=20,fg="blue")
    label2.grid(row=1, column=4, pady=30, padx=(100,0))

    entry1 = Entry(root, width=30, borderwidth=5)
    entry1.grid(row=3, column=3, pady=(20,3))
    entry2 = Entry(root, width=30, borderwidth=5)
    entry2.grid(row=4, column=3, pady=3)

    label1 = Label(root, text="Username: ", font="timesnewroman 12", fg="blue")
    label1.grid(row=3, column=2)
    label3 = Label(root, text="Password: ", font="timesnewroman 12", fg="blue")
    label3.grid(row=4, column=2)

    btn = Button(root, text="Login", bg="green", borderwidth=5, pady=5, padx=5,
                 font="times 12 bold", command=log_in)
    btn.grid(row=6, column=2, ipadx=25, columnspan=2, pady=30)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        homepage()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    root.mainloop()


def admin_page():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("980x620")

    my_pi = Image.open("administrator.png")
    resize = my_pi.resize((400, 400))
    new_pi = ImageTk.PhotoImage(resize)

    btn = Label(root, image=new_pi)
    btn.grid(row=1,column=4)

    def block():
        root.destroy()
        blk_user()

    def change_pass():
        root3 = Tk()
        root3.title("Tuition Management System")
        root3.geometry("520x380")
        root3.configure(background="aqua")


        def info():
            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            username_admin = user_entry.get()

            c.execute("SELECT * FROM admin_login WHERE username= ?", (username_admin,))
            record = c.fetchall()

            if record == []:
                messagebox.showerror("Error", "There is no username that you entered")
            else:
                if pass_entry.get() == con_pass_entry.get():
                    c.execute("""UPDATE admin_login SET
                                    password = :rv

                                    WHERE username = :oid""",
                              {
                                  'rv': pass_entry.get(),
                                  'oid': user_entry.get()
                              })
                    root3.destroy()
                    messagebox.showinfo("Successful", "Password Change Successfully")

                    conn.commit()
                    conn.close()
                else:
                    messagebox.showerror("Error", "Two password does not matched")

        title = Label(root3, text="Change Password", font="times 20", bg="aqua")
        title.grid(row=0, column=0, pady=20, columnspan=2, padx=(30, 0))

        user_label = Label(root3, text="Enter username", font="times 15", bg="aqua")
        user_label.grid(row=1, column=0, pady=(30, 5), padx=(20, 10))
        pass_label = Label(root3, text="Enter new password", font="times 15", bg="aqua")
        pass_label.grid(row=2, column=0, pady=5, padx=(20, 10))
        con_label = Label(root3, text="Enter new password again", font="times 15", bg="aqua")
        con_label.grid(row=3, column=0, pady=5, padx=(20, 10))

        user_entry = Entry(root3, width=30)
        user_entry.grid(row=1, column=1, pady=(30,0))
        pass_entry = Entry(root3, width=30)
        pass_entry.grid(row=2, column=1)
        con_pass_entry = Entry(root3, width=30)
        con_pass_entry.grid(row=3, column=1)

        save_btn = Button(root3, text="Save", bg="maroon", font="times 15", fg="white", command=info)
        save_btn.grid(row=4, column=0, columnspan=2, pady=30, ipadx=35)

        root3.mainloop()

    def add_admin():
        root2 = Tk()
        root2.title("Tuition Management System")
        root2.geometry("420x380")
        root2.configure(background="aqua")

        def save():
            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            c.execute("INSERT INTO admin_login VALUES(:username, :password)",

                      {
                          'username': user_entry.get(),
                          'password': pass_entry.get()
                      })

            root2.destroy()
            messagebox.showinfo("Successful", "Added a admin Successfully")

            conn.commit()
            conn.close()

        title = Label(root2, text="Add a new admin", font="times 20", bg="aqua")
        title.grid(row=0, column=0, pady=20, columnspan=2, padx=(30,0))

        user_label = Label(root2, text="Enter username", font="times 15", bg="aqua")
        user_label.grid(row=1, column=0, pady=(30,20), padx=(20,10))
        pass_label = Label(root2, text="Enter password", font="times 15", bg="aqua")
        pass_label.grid(row=2, column=0, pady=5, padx=(20,10))

        user_entry = Entry(root2, width=30)
        user_entry.grid(row=1, column=1)
        pass_entry = Entry(root2, width=30)
        pass_entry.grid(row=2, column=1)

        create_btn = Button(root2, text="Create", bg="maroon", font="times 15", fg="white", command=save)
        create_btn.grid(row=3, column=0, columnspan=2, pady=30, ipadx=35)


        root2.mainloop()

    change_pass_btn = Button(root, text="Change Password", pady=5, padx=5, bg="#00FFFF", font="times 15", command=change_pass)
    change_pass_btn.grid(row=2, column=2, ipadx=15, pady=20)
    block_btn = Button(root, text="Block a user", pady=5, padx=5, bg="#00FFFF", font="times 15", command=block)
    block_btn.grid(row=2, column=5, ipadx=25, pady=20)
    add_btn = Button(root, text="Add new admin", pady=5, padx=5, bg="#00FFFF", font="times 15", command=add_admin)
    add_btn.grid(row=2, column=4, ipadx=22, pady=20)

    title = Label(root, text="Admin :)", font="times 30 bold", fg="#000080").grid(row=1, column=4, pady=(320,0), ipadx=20)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        start_admin()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)


    root.mainloop()


def start_student():

    root = Tk()
    root.title("Tuition Management System")
    root.geometry("900x650")
    root.configure(background='orchid')

    bg = PhotoImage(file="F:/finalproject/student.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)

    label2 = Label(root, text="Student Login Page", font="timesnewroman 15 bold", padx=20, pady=20,fg="blue")
    label2.grid(row=1, column=2,pady=30)

    global user
    global password

    user = StringVar()
    password = StringVar()
    entry1 = Entry(root, textvariable=user, width=30, borderwidth=5)
    entry1.grid(row=3, column=2,pady=3)
    entry2 = Entry(root, textvariable=password, width=30, borderwidth=5)
    entry2.grid(row=4, column=2,pady=3)

    label1 = Label(root, text="Username: ", font="timesnewroman 12",fg="blue")
    label1.grid(row=3, column=1)
    label3 = Label(root, text="Password: ", font="timesnewroman 12",fg="blue")
    label3.grid(row=4, column=1)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=5, column=1)

    def std_dp():
        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        name = user.get()
        password1 = password.get()

        c.execute("SELECT * FROM student WHERE username = ? AND password = ?", (name, password1))
        record = c.fetchall()

        conn.commit()

        conn.close()

        if(record == []):
            messagebox.showerror("Error","Username or Password was Incorrect")
        else:
            root.destroy()
            std_profile()

    def s_std():
        root.destroy()
        std_signup()

    btn = Button(root, text="        Login        ", bg="green", borderwidth=5, pady=5, padx=5,
                 font="timesnewroman 10 bold",command=std_dp)
    btn.grid(row=6, column=1, columnspan=5)
    btn2 = Button(root, text="        Create an Account        ", bg="green", borderwidth=5, pady=5, padx=5,
                  font="timesnewroman 10 bold", command=s_std)
    btn2.grid(row=8, column=2, padx=20)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=7, column=1)

    label14 = Label(root, text="New to Tuition Management System?", font="timesnewroman 12",fg="blue")
    label14.grid(row=8, column=1, padx=20)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        homepage()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    root.mainloop()


def start_teacher():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1100x600")

    bg = PhotoImage(file="F:/finalproject/teacher.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)

    def pro_tcr():

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        name = username.get()
        password2 = passtcr.get()

        c.execute("SELECT * FROM teacher WHERE username= ? AND password = ?", (name, password2))
        record = c.fetchall()

        conn.commit()
        conn.close()

        if(record == []):
            messagebox.showerror("Error","Username or Password was Incorrect")
        else:
            root.destroy()
            tcr_pro()

    def s_tcr():
        root.destroy()
        tcr_signup()

    label2 = Label(root, text="Teacher Login Page", font="timesnewroman 15 bold", padx=20, pady=20,fg="red")
    label2.grid(row=1, column=2,pady=30)

    global username
    global passtcr

    username = StringVar()
    passtcr = StringVar()
    usernameEntry = Entry(root, textvariable=username, width=30, borderwidth=5).grid(row=3, column=2,pady=3)
    entry2 = Entry(root, textvariable=passtcr, width=30, borderwidth=5)
    entry2.grid(row=4, column=2, pady=3)

    label1 = Label(root, text="Username: ", font="timesnewroman 12",fg="red")
    label1.grid(row=3, column=1)
    label3 = Label(root, text="Password: ", font="timesnewroman 12",fg="red")
    label3.grid(row=4, column=1)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=5, column=1)

    btn = Button(root, text="        Login        ", bg="green", borderwidth=5, pady=5, padx=5,
                 font="timesnewroman 10 bold", command=pro_tcr)
    btn.grid(row=6, column=1, columnspan=5)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=7, column=1)

    label14 = Label(root, text="New to Tuition Management System?", font="timesnewroman 12",fg="red")
    label14.grid(row=8, column=1,padx=50)

    btn2 = Button(root, text="        Create an Account        ", bg="green", borderwidth=5, pady=5, padx=5,
                  font="timesnewroman 10 bold",command=s_tcr)
    btn2.grid(row=8, column=2, columnspan=5)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        homepage()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    root.mainloop()


def show_std():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1880x1000")

    bg = PhotoImage(file="F:/finalproject/std.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0,relheight=1)


    def rsubmit():
        if entry_id.get() == '' or entry_rvw.get() == '' or entry_username.get() == "":
            messagebox.showerror("Send Unsuccessful", "Field must not be empty")

        else:

            g = "good"
            b = "bad"
            m = "medium"

            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            name1 = entry_username.get()
            name2 = entry_id.get()

            c.execute("SELECT * FROM teacher WHERE username = ?", (name1,))
            record = c.fetchall()

            c.execute("SELECT * FROM student WHERE username = ?", (name2,))
            record2 = c.fetchall()

            if record == []:
                messagebox.showerror("Failed",
                                     "You are not a registered Teacher. If you want to review a Student you should signup first.")
            elif record2 == []:
                messagebox.showerror("Failed",
                                     "There is no student of this username")
            #elif rv.get() != g or rv.get() != b or rv.get() != m:
                #messagebox.showerror("Failed", "Review not Matched")

            else:
                c.execute("INSERT INTO review2 VALUES (:give, :take, :review)",
                          {
                              'give': entry_username.get(),
                              'take': entry_id.get(),
                              'review': entry_rvw.get()
                          })
                messagebox.showinfo("Succussful", "Send Successfully")

            name3 = entry_id.get()

            c.execute("SELECT * FROM review2 WHERE take = ?", (name3,))
            record3 = c.fetchall()
            print(record3)

            g = 0
            b = 0
            m = 0
            for recors in record3:
                if recors[2] == "good":
                    g = g + 1
                elif recors[2] == "bad":
                    b = b + 1
                else:
                    m = m + 1

            if g > b:
                if g > m:
                    c.execute("""UPDATE student SET
                                        review = :rv

                                        WHERE username = :oid""",
                              {
                                  'rv': "good",
                                  'oid': entry_id.get()
                              })
            elif g == b:
                c.execute("""UPDATE student SET
                                        review = :rv

                                        WHERE username = :oid""",
                          {
                              'rv': "medium",
                              'oid': entry_id.get()
                          })
            elif b > m:
                c.execute("""UPDATE student SET
                                        review = :rv

                                        WHERE username = :oid""",
                          {
                              'rv': "bad",
                              'oid': entry_id.get()
                          })
            else:
                c.execute("""UPDATE student SET
                                        review = :rv

                                        WHERE username = :oid""",
                          {
                              'rv': "medium",
                              'oid': entry_id.get()
                          })

            conn.commit()

            conn.close()


    label1 = Label(root, text="Student List", font="Times_New_Roman 20 bold")
    label1.grid(row=0, column=3, pady=30,padx=(160,0))
    label2 = Label(root, text="                ", font="Times_New_Roman 20 bold")
    label2.grid(row=1, column=4)
    label3 = Label(root, text="Enter Student Username", font="Times_New_Roman 12")
    label3.grid(row=6, column=3,padx=5,ipadx=12)
    label4 = Label(root, text="Enter your review\nMust be good, bad or medium", font="Times_New_Roman 12")
    label4.grid(row=8, column=3, padx=5)
    label5 = Label(root, text="Review Section", font="Times_New_Roman 20 bold",fg="blue")
    label5.grid(row=4, column=3, columnspan=2,pady=10, ipadx=20)
    label4 = Label(root, text="Enter your Username", font="Times_New_Roman 12")
    label4.grid(row=7, column=3, padx=5)

    rv = StringVar()

    entry_id = Entry(root, width=30, borderwidth=5)
    entry_id.grid(row=6, column=3, pady=3, columnspan=2, padx=(280,0))
    entry_username = Entry(root, width=30, borderwidth=5)
    entry_username.grid(row=7, column=3, pady=3, padx=(410,0))
    entry_rvw = Entry(root, textvariable=rv, width=30, borderwidth=5)
    entry_rvw.grid(row=8, column=3, pady=3, padx=(410, 0))

    review_btn = Button(root, text="Submit", font="times 15 bold", bg="orchid", command=rsubmit)
    review_btn.grid(row=9, columnspan=2, column=3, ipadx=30, pady=20,padx=(20,0))

    my_tree = ttk.Treeview(root)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="aqua",
                    foreground="black",
                    rowheight=30,
                    fieldbackgound="red"

                    )
    style.map('Treeview',
              background=[('selected', 'green')])

    # define column
    my_tree['columns'] = ("Name", "username", "class", "group1", "interested_sub", "p_address", "phone_no", "review")

    # format
    my_tree.column("#0", width=0, minwidth=NO)
    my_tree.column("Name", anchor=CENTER, width=120)
    my_tree.column("username", anchor=CENTER, width=100)
    my_tree.column("class", anchor=CENTER, width=100)
    my_tree.column("group1", anchor=CENTER, width=100)
    my_tree.column("interested_sub", anchor=CENTER, width=120)
    my_tree.column("p_address", anchor=CENTER, width=100)
    my_tree.column("phone_no", anchor=CENTER, width=100)
    my_tree.column("review", anchor=CENTER, width=100)

    # hedding
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Name", text="Full Name", anchor=CENTER)
    my_tree.heading("username", text="Username", anchor=CENTER)
    my_tree.heading("class", text="Class", anchor=CENTER)
    my_tree.heading("group1", text="Group", anchor=CENTER)
    my_tree.heading("interested_sub", text="Interested Subjects", anchor=CENTER)
    my_tree.heading("p_address", text="Present Address", anchor=CENTER)
    my_tree.heading("phone_no", text="Phone Number", anchor=CENTER)
    my_tree.heading("review", text="Average Review", anchor=CENTER)

    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    c.execute("SELECT * , oid FROM student")
    data = c.fetchall()

    count = 0

    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[3], record[4], record[5], record[6], record[7], record[8]))
        count += 1

    my_tree.grid(row=3, column=3, padx=(250,0))

    '''conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    c.execute("SELECT * , oid FROM student")
    record = c.fetchall()

    count = 0
    print_record = ''
      for records in record:
        print_record += str(records[0]) + "\t\t" + str(records[3]) + "\t" + str(records[4])+ "\t" + str(records[5]) + "\t" + str(records[6]) + "\t" + str(records[7]) + "\t" + str(records[8]) + "\t" + str(records[9]) + "\n"
        count += 1

    for records in record:
        print_record += "Username: " + str(records[1]) + "\nCLass: " + str(records[3]) + "\nGroup: " + str(records[4])+ "\nInterested Subjects: " + str(records[5]) + "\nPresent Address: " + str(records[6]) + "\nPhone Number: " + str(records[7]) + "\n" + "Average Review: " + str(records[8]) + "\n\n"
        count += 1

    #q_label = Label(root, text="Full Name\tClass\tGroup\tInterested Subjects\tPresent Address\tPhone Number", font="times 10 bold")
    #q_label.grid(row=2, column=0)
    q_label = Label(root, text=print_record, font="times 12")
    q_label.grid(row=3, column=2, padx=(250,0))
    q_label2 = Label(root, text="Total Students is this System: "+str(count), font="timesnewroman 12")
    q_label2.grid(row=4, column=2,pady=10, padx=(250,0))

    conn.commit()

    conn.close()'''

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        homepage()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    def refresh():
        root.destroy()
        show_std()

    my_pic3 = Image.open("refresh.png")
    resized3 = my_pic3.resize((50, 50))
    new_pic3 = ImageTk.PhotoImage(resized3)

    refresh_btn = Button(root, image=new_pic3, command=refresh)
    refresh_btn.grid(row=0, column=2)

    root.mainloop()


def show_tcr():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1840x1000")

    bg = PhotoImage(file="F:/finalproject/tcr.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=200, y=160, relwidth=1, relheight=1)

    def rsubmit():
        if entry_id.get() == '' or entry_rvw.get() == '' or entry_username.get() == "":
            messagebox.showerror("Send Unsuccessful", "Fields Must not be empty")

        else:

            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            name1 = entry_username.get()
            name2 = entry_id.get()

            c.execute("SELECT * FROM student WHERE username = ?", (name1,))
            record = c.fetchall()

            c.execute("SELECT * FROM teacher WHERE username = ?", (name2,))
            record2 = c.fetchall()

            if record == [] :
                messagebox.showerror("Failed","You are not a registered Student. If you want to review a teacher you should signup first.")
            elif record2 == []:
                messagebox.showerror("Failed",
                                     "There is no teacher of this username")
            #elif rb.get() != "good" or rb.get() != "bad" or rb.get() != 'medium':
                #messagebox.showerror("Failed", "Review not Matched")
            else:
                c.execute("INSERT INTO review2 VALUES (:give, :take, :review)",
                          {
                              'give': entry_username.get(),
                              'take': entry_id.get(),
                              'review': entry_rvw.get()
                          })
                messagebox.showinfo("Succussful", "Send Successfully")

            name3 = entry_id.get()

            c.execute("SELECT * FROM review2 WHERE take = ?", (name3,))
            record3 = c.fetchall()

            g = 0
            b = 0
            m = 0
            for recors in record3:
                if recors[2] == "good":
                    g = g + 1
                elif recors[2] == "bad":
                    b = b + 1
                else:
                    m = m + 1

            if g > b :
                if g > m :
                    c.execute("""UPDATE teacher SET
                            review = :rv

                            WHERE username = :oid""",
                      {
                          'rv': "good",
                          'oid': entry_id.get()
                      })
            elif g == b:
                c.execute("""UPDATE student SET
                                        review = :rv

                                        WHERE username = :oid""",
                          {
                              'rv': "medium",
                              'oid': entry_id.get()
                          })
            elif b > m:
                c.execute("""UPDATE teacher SET
                            review = :rv

                            WHERE username = :oid""",
                      {
                          'rv': "bad",
                          'oid': entry_id.get()
                      })
            else:
                c.execute("""UPDATE teacher SET
                            review = :rv

                            WHERE username = :oid""",
                      {
                          'rv': "medium",
                          'oid': entry_id.get()
                      })

            conn.commit()

            conn.close()


    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    label1 = Label(root, text="Teacher List", font="Times_New_Roman 20 bold")
    label1.grid(row=0, column=3,padx=(200,0), pady=30)
    label3 = Label(root, text="Enter Teacher Username", font="Times_New_Roman 12")
    label3.grid(row=5, column=3,padx=5,ipadx=12)
    label4 = Label(root, text="Enter your review\nMust be good, bad or medium", font="Times_New_Roman 12")
    label4.grid(row=7, column=3, padx=5)
    label5 = Label(root, text="Review Section", font="Times_New_Roman 20 bold",fg="blue")
    label5.grid(row=4, column=3, columnspan=2,pady=10, ipadx=20, padx=(150,0))
    label6 = Label(root, text="Input Your username", font="Times_New_Roman 12")
    label6.grid(row=6, column=3, padx=5)

    rb = StringVar()

    entry_id = Entry(root, width=30, borderwidth=5)
    entry_id.grid(row=5, column=3, pady=3, columnspan=2, padx=(410,0))
    entry_rvw = Entry(root,textvariable=rb, width=30, borderwidth=5)
    entry_rvw.grid(row=7, column=3,columnspan=2, pady=3, padx=(410,0))
    entry_username = Entry(root, width=30, borderwidth=5)
    entry_username.grid(row=6, column=3,columnspan=2, pady=3, padx=(410,0))

    review_btn = Button(root, text="Submit", font="times 15 bold", bg="orchid", command=rsubmit)
    review_btn.grid(row=8, columnspan=3, column=3, ipadx=30, pady=20, padx=(200,0))



    my_tree = ttk.Treeview(root)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background="aqua",
                    foreground="black",
                    rowheight=30,
                    fieldbackgound="red"


                    )
    style.map('Treeview',
              background=[('selected', 'green')])

    # define column
    my_tree['columns'] = ("Name", "username", "class", "group1", "interested_sub", "p_address", "phone_no", "review")

    # format
    my_tree.column("#0", width=0, minwidth=NO)
    my_tree.column("Name", anchor=CENTER, width=120)
    my_tree.column("username", anchor=CENTER, width=100)
    my_tree.column("class", anchor=CENTER, width=100)
    my_tree.column("group1", anchor=CENTER, width=100)
    my_tree.column("interested_sub", anchor=CENTER, width=120)
    my_tree.column("p_address", anchor=CENTER, width=120)
    my_tree.column("phone_no", anchor=CENTER, width=100)
    my_tree.column("review", anchor=CENTER, width=100)

    # hedding
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("Name", text="Full Name", anchor=CENTER)
    my_tree.heading("username", text="Username", anchor=CENTER)
    my_tree.heading("class", text="E-mail", anchor=CENTER)
    my_tree.heading("group1", text="Expected Salary", anchor=CENTER)
    my_tree.heading("interested_sub", text="Address", anchor=CENTER)
    my_tree.heading("p_address", text="Studies Information", anchor=CENTER)
    my_tree.heading("phone_no", text="Phone Number", anchor=CENTER)
    my_tree.heading("review", text="Average Review", anchor=CENTER)

    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    c.execute("SELECT * , oid FROM teacher")
    data = c.fetchall()

    count = 0

    for record in data:
        my_tree.insert(parent='', index='end', iid=count, text="",
                       values=(record[0], record[1], record[3], record[4], record[5], record[6], record[7], record[8]))
        count += 1

    my_tree.grid(row=3, column=3, padx=(250,0))

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        homepage()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    def refresh():
        root.destroy()
        show_tcr()

    my_pic3 = Image.open("refresh.png")
    resized3 = my_pic3.resize((50, 50))
    new_pic3 = ImageTk.PhotoImage(resized3)

    refresh_btn = Button(root, image=new_pic3, command=refresh)
    refresh_btn.grid(row=0, column=2)


    root.mainloop()


def blk_user():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1000x700")


    b = PhotoImage(file="F:/finalproject/qq.png")

    mylabel = Label(root, image=b)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)

    def show_student():

        root.geometry("1300x700")

        my_tree = ttk.Treeview(root)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="aqua",
                        foreground="black",
                        rowheight=30,
                        fieldbackgound="red"

                        )
        style.map('Treeview',
                  background=[('selected', 'green')])

        # define column
        my_tree['columns'] = ("username", "class","phone_no", "review")

        my_tree.column("#0", width=0, minwidth=NO)
        my_tree.column("username", anchor=CENTER, width=100)
        my_tree.column("class", anchor=CENTER, width=100)
        my_tree.column("phone_no", anchor=CENTER, width=100)
        my_tree.column("review", anchor=CENTER, width=100)

        # hedding
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("username", text="Username", anchor=CENTER)
        my_tree.heading("class", text="Class", anchor=CENTER)
        my_tree.heading("phone_no", text="Average Review", anchor=CENTER)
        my_tree.heading("review", text="User ID", anchor=CENTER)

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("SELECT * , oid FROM student")
        data = c.fetchall()

        count = 0

        for record in data:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[1], record[3], record[8], record[9]))
            count += 1

        my_tree.grid(row=3, column=2)

    def show_teacher():

        my_tree = ttk.Treeview(root)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="aqua",
                        foreground="black",
                        rowheight=30,
                        fieldbackgound="red"

                        )
        style.map('Treeview',
                  background=[('selected', 'green')])

        # define column
        my_tree['columns'] = ("username", "class", "phone_no", "review")

        # format
        my_tree.column("#0", width=0, minwidth=NO)
        my_tree.column("username", anchor=CENTER, width=100)
        my_tree.column("class", anchor=CENTER, width=100)
        my_tree.column("phone_no", anchor=CENTER, width=100)
        my_tree.column("review", anchor=CENTER, width=100)

        # hedding
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("username", text="Username", anchor=CENTER)
        my_tree.heading("class", text="E-mail", anchor=CENTER)
        my_tree.heading("phone_no", text="Average Review", anchor=CENTER)
        my_tree.heading("review", text="User ID", anchor=CENTER)

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("SELECT * , oid FROM teacher")
        data = c.fetchall()

        count = 0

        for record in data:
            my_tree.insert(parent='', index='end', iid=count, text="",
                           values=( record[1], record[3], record[8], record[9]))
            count += 1

        my_tree.grid(row=3, column=4)


        '''conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("SELECT * , oid FROM teacher")
        record = c.fetchall()

        print_record = ''
        for records in record:
            print_record += "Full Name: " + str(records[0]) + "\n" + "Username: " + str(
                records[1]) + "\n" + "Class: " + str(records[3]) + "\n" + "Phone Number: " + str(
                records[7]) + "\n" + "Review: " + str(records[8]) + "\nUser ID: " + str(records[9]) + "\n\n"

        q_label = Label(root, text=print_record, font="timesnewroman 12")
        q_label.grid(row=3, column=4)

        conn.commit()

        conn.close()'''

    def delete_student():

        ans = messagebox.askokcancel("Conformation","Are you sure you want to delete it?")

        if ans == 0:
            return
        else:
            if (delete1.get() == ''):
                messagebox.showinfo("Delete Unsuccessfull","ID number is Invalid")

            else:
                conn = sqlite3.connect('tms.db')
                c = conn.cursor()

                c.execute("DELETE FROM student WHERE oid = " + delete1.get())
                c.execute("DELETE FROM review2 WHERE oid = " + delete1.get())

                conn.commit()

                conn.close()

                messagebox.showinfo("Congrats","Delete Successful")

    def delete_teacher():

        ans = messagebox.askokcancel("Conformation", "Are you sure you want to delete it?")

        if ans == 0:
            return
        else:
            if (delete2.get() == ''):
                messagebox.showinfo("Delete Unsuccessful", "ID number is Invalid")

            else:

                conn = sqlite3.connect('tms.db')
                c = conn.cursor()

                c.execute("DELETE FROM teacher WHERE  oid = " + delete2.get())

                conn.commit()

                conn.close()

                messagebox.showinfo("Congrats","Delete Successful")

    label2 = Label(root, text="Block User Page", font="timesnewroman 22 bold", pady=10)
    label2.grid(row=1, column=3,pady=30)

    label1 = Label(root, text="Enter User ID: ", pady=10, font="timesnewroman 12")
    label1.grid(row=4, column=1)
    labelr= Label(root, text="Enter User ID: ", pady=10, font="timesnewroman 12")
    labelr.grid(row=4, column=3)

    delete1 = Entry(root, width=30, borderwidth=5)
    delete1.grid(row=4, column=2)
    delete2 = Entry(root, width=30, borderwidth=5)
    delete2.grid(row=4, column=4)

    btn = Button(root, text="Delete", bg="red", font="timesnewroman 12", command=delete_student)
    btn.grid(row=5, column=2)

    btn2 = Button(root, text="Delete", bg="red", font="timesnewroman 12", command=delete_teacher)
    btn2.grid(row=5, column=4)

    show_student_btn = Button(root, text="Show Student", bg="green", font="timesnewroman 12", command=show_student)
    show_student_btn.grid(row=2, column=2)

    #labelf = Label(root, text="                                  ", pady=10, font="timesnewroman 12")
    #labelf.grid(row=1, column=3)

    show_teacher_btn = Button(root, text="Show Teacher", bg="green", font="timesnewroman 12", command=show_teacher)
    show_teacher_btn.grid(row=2, column=4)

    def refresh():
        root.destroy()
        blk_user()

    my_pic3 = Image.open("refresh.png")
    resized3 = my_pic3.resize((50, 50))
    new_pic3 = ImageTk.PhotoImage(resized3)

    refresh_btn = Button(root, image=new_pic3, command=refresh)
    refresh_btn.grid(row=0, column=2)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        admin_page()

    my_pic2 = Image.open("exit (2).png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)


    root.mainloop()


def std_profile():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1020x630")

    def chk_rvw():

        root1 = Tk()
        root1.title("Tuition Management System")
        root1.geometry("400x500")
        root1.configure(background="orchid")

        dp_name = user.get()

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("SELECT * FROM review2 WHERE give= ?", (dp_name,))
        record = c.fetchall()

        print_record = ''
        for records in record:
            print_record += "Username: " + str(records[1])  + "\nReview: " + str(records[2]) + "\n \n"

        q_label = Label(root1, text=print_record, font="timesnewroman 15", bg="orchid")
        q_label.grid(row=1, column=0)
        q_label = Label(root1, text="You send", font="timesnewroman 15", bg="orchid")
        q_label.grid(row=0, column=0)

        c.execute("SELECT * FROM review2 WHERE take= ?", (dp_name,))
        record = c.fetchall()

        print_record = ''
        for records in record:
            print_record += "Username: " + str(records[0]) + "\nReview: " + str(records[2]) + "\n \n"

        q_label = Label(root1, text=print_record, font="timesnewroman 15", bg="orchid")
        q_label.grid(row=1, column=1,padx=10)
        q_label = Label(root1, text="You received", font="timesnewroman 15", bg="orchid")
        q_label.grid(row=0, column=1,padx=10)

        conn.commit()
        conn.close()

        root.mainloop()

    def save_std():

        user_name = name1

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("""UPDATE student SET
                                     fullname =  :first,
                                     username = :user,
                                     password = :pass,
                                     class =:mail,
                                     group1 = :salary,
                                     interested_sub = :address,
                                     p_address = :info,
                                     phone_no = :number

                                    WHERE username = :oid""",
                  {
                      'first': full_name_edits.get(),
                      'user': username_edits.get(),
                      'pass': password_edits.get(),
                      'mail': e_mail_edits.get(),
                      'salary': expected_salary_edits.get(),
                      'address': address_edits.get(),
                      'info': s_information_edits.get(),
                      'number': phone_no_edits.get(),
                      'oid': user_name
                  }
                  )
        conn.commit()

        conn.close()

        root2.destroy()
        messagebox.showinfo("Successful", "Information Saved Successfully")
        root.destroy()
        std_profile()

    def edits():

        global root2

        root2 = Tk()
        root2.title("Tuition Management System")
        root2.geometry("370x450")
        root2.configure(background='orchid')

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        global name1

        name1 = user.get()

        c.execute("SELECT * FROM student WHERE username= ?", (name,))
        records = c.fetchall()

        editl = Label(root2, text="Edit your Information", font="times 12 bold", bg="orchid")
        editl.grid(row=0, column=1, pady=10, columnspan=2)

        full_name_label = Label(root2, text="Full Name", font="timesnewroman 10", bg="orchid")
        full_name_label.grid(row=3, column=1, pady=3)
        username_label = Label(root2, text="Username", font="timesnewroman 10", bg="orchid")
        username_label.grid(row=4, column=1, pady=3)
        password_label = Label(root2, text="Password", font="timesnewroman 10", bg="orchid")
        password_label.grid(row=5, column=1, pady=3)
        e_mail_label = Label(root2, text="Class", font="timesnewroman 10", bg="orchid")
        e_mail_label.grid(row=6, column=1, pady=3)
        expected_salary_label = Label(root2, text="Group", font="timesnewroman 10", bg="orchid")
        expected_salary_label.grid(row=7, column=1, pady=3)
        address_label = Label(root2, text="Interested Subjects", font="timesnewroman 10", bg="orchid")
        address_label.grid(row=8, column=1, pady=3)
        s_information_label = Label(root2, text="Permanent Address", font="timesnewroman 10", bg="orchid")
        s_information_label.grid(row=9, column=1, pady=3)
        phone_no_label = Label(root2, text="Phone Number", font="timesnewroman 10", bg="orchid")
        phone_no_label.grid(row=10, column=1, pady=3)

        global full_name_edits
        global username_edits
        global password_edits
        global e_mail_edits
        global expected_salary_edits
        global address_edits
        global s_information_edits
        global phone_no_edits

        # for entry box

        full_name_edits = Entry(root2, width=30, borderwidth=5)
        full_name_edits .grid(row=3, column=2, pady=3)
        username_edits  = Entry(root2, width=30, borderwidth=5)
        username_edits.grid(row=4, column=2, pady=3)
        password_edits  = Entry(root2, width=30, borderwidth=5)
        password_edits .grid(row=5, column=2, pady=3)
        e_mail_edits  = Entry(root2, width=30, borderwidth=5)
        e_mail_edits.grid(row=6, column=2, pady=3)
        expected_salary_edits  = Entry(root2, width=30, borderwidth=5)
        expected_salary_edits .grid(row=7, column=2, pady=3)
        address_edits  = Entry(root2, width=30, borderwidth=5)
        address_edits .grid(row=8, column=2, pady=3)
        s_information_edits  = Entry(root2, width=30, borderwidth=5)
        s_information_edits .grid(row=9, column=2, pady=3)
        phone_no_edits  = Entry(root2, width=30, borderwidth=5)
        phone_no_edits .grid(row=10, column=2, pady=3)

        save_btn = Button(root2, text="Save Information", font="times 12 bold", bg="green", command=save_std)
        save_btn.grid(row=11, column=1, columnspan=2, ipadx=30, pady=10)

        for record in records:

            full_name_edits.insert(0, record[0])
            username_edits.insert(0, record[1])
            password_edits.insert(0, record[2])
            e_mail_edits.insert(0, record[3])
            expected_salary_edits.insert(0, record[4])
            address_edits.insert(0, record[5])
            s_information_edits.insert(0, record[6])
            phone_no_edits.insert(0, record[7])

        conn.commit()

        conn.close()

        root.mainloop()

    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    label1 = Label(root, text="Student Profile \n \n", font="timesnewroman 15 bold")
    label1.grid(row=1, column=2)

    name = user.get()

    c.execute("SELECT * FROM student WHERE username = ?", (name,))
    record = c.fetchall()

    print_record = ''
    for records in record:
        print_record += "Full Name: " + str(records[0]) + "\n" + "User Name: " + str(records[1]) + "\n" + "Password: " + str(records[2]) + "\n" + "CLass: " + str(records[3]) + "\n" + "Group: " + str(
            records[4]) + "\n" + "Interested Subjects: " + str(records[5]) + "\n" + "Present Address: " + str(
            records[6]) + "\n" + "Phone Number: " + str(records[7]) + "\nReview: " + str(records[8]) + "\n \n"

    q_label = Label(root, text=print_record, font="timesnewroman 15")
    q_label.grid(row=2, column=3)

    conn.commit()

    conn.close()

    my_img = ImageTk.PhotoImage(Image.open("pro.jpg"))
    my_label = Label(image=my_img)
    my_label.grid(row=2, column=1)

    edit_btn = Button(root, text="Edit Information", font="times 15 bold", bg="yellow", command=edits)
    edit_btn.grid(row=3, column=2, columnspan=1, pady=10)
    rvw_btn = Button(root, text="Check Reviews", font="times 15 bold", bg="yellow", command=chk_rvw)
    rvw_btn.grid(row=3, column=3, columnspan=1, pady=10)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        start_student()

    my_pic2 = Image.open("exit (2).png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    root.mainloop()


def tcr_pro():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1000x500")

    def chk_rvw():

        root1 = Tk()
        root1.title("Tuition Management System")
        root1.geometry("400x500")
        root1.configure(background="orchid")

        dp_name = username.get()

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("SELECT * FROM review2 WHERE give= ?", (dp_name,))
        record = c.fetchall()

        print_record = ''
        for records in record:
            print_record += "Username: " + str(records[1])  + "\nReview: " + str(records[2]) + "\n \n"

        q_label = Label(root1, text=print_record, font="timesnewroman 15", bg="orchid")
        q_label.grid(row=1, column=0,padx=10)
        q_label = Label(root1, text="You send", font="timesnewroman 15", bg="orchid")
        q_label.grid(row=0, column=0,padx=10)

        c.execute("SELECT * FROM review2 WHERE take= ?", (dp_name,))
        record = c.fetchall()

        print_record = ''
        for records in record:
            print_record += "Username: " + str(records[0]) + "\nReview: " + str(records[2]) + "\n \n"

        q_label = Label(root1, text=print_record, font="timesnewroman 15", bg="orchid")
        q_label.grid(row=1, column=1,padx=10)
        q_label = Label(root1, text="You received", font="timesnewroman 15",bg="orchid")
        q_label.grid(row=0, column=1,padx=10)

        conn.commit()
        conn.close()

        root.mainloop()

    def save_tcr():

        user_name = name

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute("""UPDATE teacher SET
                                    fullname =  :first,
                                    username = :user,
                                    password = :pass,
                                    e_mail = :mail,
                                    expected_salary = :salary,
                                    address = :address,
                                    s_information = :info,
                                    phone_no = :number

                                    WHERE username = :oid""",
                  {
                      'first': full_name_edit.get(),
                      'user': username_edit.get(),
                      'pass': password_edit.get(),
                      'mail': e_mail_edit.get(),
                      'salary': expected_salary_edit.get(),
                      'address': address_edit.get(),
                      'info': s_information_edit.get(),
                      'number': phone_no_edit.get(),
                      'oid': user_name
                  }
                  )
        conn.commit()

        conn.close()

        root2.destroy()
        messagebox.showinfo("Successful", "Information Saved Successfully")
        root.destroy()
        tcr_pro()

    def edit():

        global root2

        root2 = Tk()
        root2.title("Tuition Management System")
        root2.geometry("370x450")
        root2.configure(background='orchid')

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        global name

        name = username.get()

        c.execute("SELECT * FROM teacher WHERE username= ?", (name,))
        records = c.fetchall()

        editl = Label(root2, text="Edit your Information", font="times 12 bold", bg="orchid")
        editl.grid(row=0, column=1, pady=10, columnspan=2)

        full_name_label = Label(root2, text="Full Name", font="timesnewroman 10", bg="orchid")
        full_name_label.grid(row=3, column=1, pady=3)
        username_label = Label(root2, text="Username", font="timesnewroman 10", bg="orchid")
        username_label.grid(row=4, column=1, pady=3)
        password_label = Label(root2, text="Password", font="timesnewroman 10", bg="orchid")
        password_label.grid(row=5, column=1, pady=3)
        e_mail_label = Label(root2, text="E-mail", font="timesnewroman 10", bg="orchid")
        e_mail_label.grid(row=6, column=1, pady=3)
        expected_salary_label = Label(root2, text="Expected Salary", font="timesnewroman 10", bg="orchid")
        expected_salary_label.grid(row=7, column=1, pady=3)
        address_label = Label(root2, text="Address", font="timesnewroman 10", bg="orchid")
        address_label.grid(row=8, column=1, pady=3)
        s_information_label = Label(root2, text="Studies information", font="timesnewroman 10", bg="orchid")
        s_information_label.grid(row=9, column=1, pady=3)
        phone_no_label = Label(root2, text="Phone Number", font="timesnewroman 10", bg="orchid")
        phone_no_label.grid(row=10, column=1, pady=3)

        global full_name_edit
        global username_edit
        global password_edit
        global e_mail_edit
        global expected_salary_edit
        global address_edit
        global s_information_edit
        global phone_no_edit

        # for entry box

        full_name_edit = Entry(root2, width=30, borderwidth=5)
        full_name_edit .grid(row=3, column=2, pady=3)
        username_edit  = Entry(root2, width=30, borderwidth=5)
        username_edit .grid(row=4, column=2, pady=3)
        password_edit  = Entry(root2, width=30, borderwidth=5)
        password_edit .grid(row=5, column=2, pady=3)
        e_mail_edit  = Entry(root2, width=30, borderwidth=5)
        e_mail_edit .grid(row=6, column=2, pady=3)
        expected_salary_edit  = Entry(root2, width=30, borderwidth=5)
        expected_salary_edit .grid(row=7, column=2, pady=3)
        address_edit  = Entry(root2, width=30, borderwidth=5)
        address_edit .grid(row=8, column=2, pady=3)
        s_information_edit  = Entry(root2, width=30, borderwidth=5)
        s_information_edit .grid(row=9, column=2, pady=3)
        phone_no_edit  = Entry(root2, width=30, borderwidth=5)
        phone_no_edit .grid(row=10, column=2, pady=3)

        save_btn = Button(root2, text="Save Information", font="times 12 bold", bg="green", command=save_tcr)
        save_btn.grid(row=11, column=1, columnspan=2, ipadx=30, pady=10)

        for record in records:

            full_name_edit.insert(0, record[0])
            username_edit.insert(0, record[1])
            password_edit.insert(0, record[2])
            e_mail_edit.insert(0, record[3])
            expected_salary_edit.insert(0, record[4])
            address_edit.insert(0, record[5])
            s_information_edit.insert(0, record[6])
            phone_no_edit.insert(0, record[7])

        conn.commit()

        conn.close()

        root.mainloop()

    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    label1 = Label(root, text="Teacher Profile\n", font="Times_New_Roman 18 bold")
    label1.grid(row=1, column=2)

    name = username.get()
    password2 = passtcr.get()

    c.execute("SELECT * FROM teacher WHERE username= ? AND password = ?", (name, password2))
    record = c.fetchall()

    print_record = ''
    for records in record:

        print_record += "Full Name: " + str(records[0]) + "\n" + "User Name: " + str(
            records[1]) + "\n" + "Password: " + str(records[2]) + "\n" + "E-mail: " + str(
            records[3]) + "\n" + "Expected Salary: " + str(records[4]) + "\n" + "Address: " + str(
            records[5]) + "\n" + "Studies Information: " + str(records[6]) + "\n" + "Phone Number: " + str(
            records[7]) + "\n \n"

    q_label = Label(root, text=print_record, font="timesnewroman 15")
    q_label.grid(row=2, column=3)

    conn.commit()

    conn.close()

    my_img = ImageTk.PhotoImage(Image.open("tcr_pro1.png"))
    my_label = Label(image=my_img)
    my_label.grid(row=2, column=1)

    edit_btn = Button(root, text="Edit Information", font="times 15 bold", bg="yellow", command=edit)
    edit_btn.grid(row=3, column=2, columnspan=1, pady=10)
    edit_btn = Button(root, text="Check Reviews", font="times 15 bold", bg="yellow", command=chk_rvw)
    edit_btn.grid(row=3, column=3, columnspan=1, pady=10)


    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        start_teacher()

    my_pic2 = Image.open("exit (2).png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)
    root.mainloop()


def tcr_signup():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1000x530")
    root.configure(background='orchid')

    bg = PhotoImage(file="F:/finalproject/ww.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)


    def submit():

        if fn.get()=='' or un.get()=='' or pw.get()=='' or gm.get()== '' or es.get()=='' or si.get()=='' or ad.get()=='' or pn.get()=='':
            messagebox.showerror("Failed", "An Information was Empty")
        else:
            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            c.execute(
                "INSERT INTO teacher VALUES (:fullname, :username, :password, :e_mail, :expected_salary, :address, :s_information, :phone_no, :review)",

                {
                    'fullname': full_name.get(),
                    'username': username.get(),
                    'password': password.get(),
                    'e_mail': e_mail.get(),
                    'expected_salary': expected_salary.get(),
                    'address': address.get(),
                    's_information': s_information.get(),
                    'phone_no': phone_no.get(),
                    'review': "No Review yet"

                }

            )
            c.execute("INSERT INTO review VALUES(:username, :review)",

                      {
                          'username': username.get(),
                          'review': ""
                      })

            conn.commit()

            conn.close()

            full_name.delete(0, END)
            username.delete(0, END)
            password.delete(0, END)
            s_information.delete(0, END)
            address.delete(0, END)
            phone_no.delete(0, END)
            e_mail.delete(0, END)
            expected_salary.delete(0, END)

            messagebox.showinfo("Congrats", "Account created Successful")

    label2 = Label(root, text="Teacher Signup Page", font="timesnewroman 15 bold")
    label2.grid(row=1, column=2, columnspan=2, pady=30, padx=(300,0))



    # for label

    full_name_label = Label(root, text="Full Name", font="timesnewroman 10")
    full_name_label.grid(row=3, column=2, padx=(300,10))
    username_label = Label(root, text="Username", font="timesnewroman 10")
    username_label.grid(row=4, column=2, padx=(300,10))
    password_label = Label(root, text="Password", font="timesnewroman 10")
    password_label.grid(row=5, column=2, padx=(300,10))
    e_mail_label = Label(root, text="E-mail", font="timesnewroman 10")
    e_mail_label.grid(row=6, column=2, padx=(300,10))
    expected_salary_label = Label(root, text="Expected Salary", font="timesnewroman 10")
    expected_salary_label.grid(row=7, column=2, padx=(300,10))
    address_label = Label(root, text="Address", font="timesnewroman 10")
    address_label.grid(row=8, column=2, padx=(300,10))
    s_information_label = Label(root, text="Studies information", font="timesnewroman 10")
    s_information_label.grid(row=9, column=2, padx=(300,10))
    phone_no_label = Label(root, text="Phone Number", font="timesnewroman 10")
    phone_no_label.grid(row=10, column=2, padx=(300,10))

    # for entry box

    fn = StringVar()
    un = StringVar()
    pw = StringVar()
    gm = StringVar()
    es = StringVar()
    ad = StringVar()
    si = StringVar()
    pn = StringVar()

    full_name = Entry(root,textvariable=fn, width=30, borderwidth=5)
    full_name.grid(row=3, column=3, pady=3)
    username = Entry(root,textvariable=un, width=30, borderwidth=5)
    username.grid(row=4, column=3, pady=3)
    password = Entry(root,textvariable=pw, width=30, borderwidth=5)
    password.grid(row=5, column=3, pady=3)
    e_mail = Entry(root, textvariable=gm,width=30, borderwidth=5)
    e_mail.grid(row=6, column=3, pady=3)
    expected_salary = Entry(root,textvariable=es, width=30, borderwidth=5)
    expected_salary.grid(row=7, column=3, pady=3)
    address = Entry(root, width=30,textvariable=ad, borderwidth=5)
    address.grid(row=8, column=3, pady=3)
    s_information = Entry(root,textvariable=si, width=30, borderwidth=5)
    s_information.grid(row=9, column=3, pady=3)
    phone_no = Entry(root,textvariable=pn, width=30, borderwidth=5)
    phone_no.grid(row=10, column=3, pady=3)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=11, column=1)

    # for button

    btn2 = Button(root, text="              Create Account            ", bg="green", borderwidth=5, pady=5, padx=5,
                  command=submit)
    btn2.grid(row=12, column=3, columnspan=2)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        homepage()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    root.mainloop()

def std_signup():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1100x600")
    root.configure(background='orchid')

    bg = PhotoImage(file="F:/finalproject/std.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)

    def submit():

        if fn.get()=='' or un.get()=='' or pw.get()=='' or gm.get()== '' or es.get()=='' or si.get()=='' or ad.get()=='' or pn.get()=='':
            messagebox.showerror("Failed", "Information was Empty")
        else:
            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            c.execute(
                "INSERT INTO student VALUES (:fullname, :username, :password, :class, :group1, :interested_sub, :p_address, :phone_no, :review)",

                {
                    'fullname': full_name.get(),
                    'username': username.get(),
                    'password': password.get(),
                    'class': class_.get(),
                    'group1': group1.get(),
                    'interested_sub': i_sub.get(),
                    'p_address': p_address.get(),
                    'phone_no': phone_no.get(),
                    'review': "No Review yet"

                }

            )
            c.execute("INSERT INTO review VALUES(:username, :review)",

                      {
                          'username': username.get(),
                          'review': ""
                      })

            conn.commit()

            conn.close()

            full_name.delete(0, END)
            username.delete(0, END)
            password.delete(0, END)
            class_.delete(0, END)
            i_sub.delete(0, END)
            phone_no.delete(0, END)
            p_address.delete(0, END)
            group1.delete(0, END)

            messagebox.showinfo("Congrats", "Account created Successful")

    label2 = Label(root, text="Student Signup Page", font="timesnewroman 15 bold", padx=20, pady=20)
    label2.grid(row=1, column=2, columnspan=5, pady=20, padx=(300,0))

    full_name_label = Label(root, text="Full Name", font="timesnewroman 10")
    full_name_label.grid(row=3, column=2, padx=(300,10))
    username_label = Label(root, text="Username", font="timesnewroman 10")
    username_label.grid(row=4, column=2, padx=(300,10))
    password_label = Label(root, text="Password", font="timesnewroman 10")
    password_label.grid(row=5, column=2, padx=(300,10))
    class__label = Label(root, text="Class", font="timesnewroman 10")
    class__label.grid(row=6, column=2, padx=(300,10))
    group1_label = Label(root, text="Group", font="timesnewroman 10")
    group1_label.grid(row=7, column=2, padx=(300,10))
    i_sub_label = Label(root, text="Interested Subjects", font="timesnewroman 10")
    i_sub_label.grid(row=8, column=2, padx=(300,10))
    p_address_label = Label(root, text="Present Address", font="timesnewroman 10")
    p_address_label.grid(row=9, column=2, padx=(300,10))
    phone_no_label = Label(root, text="Phone Number", font="timesnewroman 10")
    phone_no_label.grid(row=10, column=2, padx=(300,10))

    fn = StringVar()
    un = StringVar()
    pw = StringVar()
    gm = StringVar()
    es = StringVar()
    ad = StringVar()
    si = StringVar()
    pn = StringVar()

    full_name = Entry(root,textvariable=fn, width=30, borderwidth=5,)
    full_name.grid(row=3, column=3, pady=3)
    username = Entry(root,textvariable=un, width=30, borderwidth=5)
    username.grid(row=4, column=3, pady=3)
    password = Entry(root,textvariable=pw, width=30, borderwidth=5)
    password.grid(row=5, column=3, pady=3)
    class_ = Entry(root,textvariable=gm, width=30, borderwidth=5)
    class_.grid(row=6, column=3, pady=3)
    group1 = Entry(root,textvariable=es, width=30, borderwidth=5)
    group1.grid(row=7, column=3, pady=3)
    i_sub = Entry(root,textvariable=ad, width=30, borderwidth=5)
    i_sub.grid(row=8, column=3, pady=3)
    p_address = Entry(root,textvariable=si, width=30, borderwidth=5)
    p_address.grid(row=9, column=3, pady=3)
    phone_no = Entry(root,textvariable=pn, width=30, borderwidth=5)
    phone_no.grid(row=10, column=3, pady=3)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=11, column=1)

    btn2 = Button(root, text="Create Account", bg="green", borderwidth=5, pady=5, padx=5,
                  command=submit, font="times 12 bold")
    btn2.grid(row=12, column=3, columnspan=2, ipadx=10)

    def back_homepage():
        root.destroy()
        homepage()

    my_pic = Image.open("home-icon-silhouette.png")
    resized = my_pic.resize((50, 50))
    new_pic = ImageTk.PhotoImage(resized)

    home_btn = Button(root, image=new_pic, command=back_homepage)
    home_btn.grid(row=0, column=0)

    def back():
        root.destroy()
        start_student()

    my_pic2 = Image.open("left-arrow.png")
    resized2 = my_pic2.resize((50, 50))
    new_pic2 = ImageTk.PhotoImage(resized2)

    back_btn = Button(root, image=new_pic2, command=back)
    back_btn.grid(row=0, column=1)

    root.mainloop()


def homepage():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("750x630")
    root.configure(background="pink")

    bg = PhotoImage(file="F:/finalproject/rr.png")

    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)

    def admin():
        root.destroy()
        start_admin()

    def teacher():
        root.destroy()
        start_teacher()

    def student():
        root.destroy()
        start_student()

    def showtcr():
        root.destroy()
        show_tcr()

    def showstd():
        root.destroy()
        show_std()

    m_label = Label(root, text="Tuition Management System \n ", font="timesnewroman 15 bold", padx=20,
                    pady=20)
    m_label.grid(row=0, column=2,padx=(30,0))

    querry_btn = Button(root, text="Find Teacher", bg="navy",fg="white", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,command=showtcr)
    querry_btn.grid(row=8, column=3,ipadx=3, padx=(10,0))
    querry_btn2 = Button(root, text="List of Student", bg="navy",fg="white", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=showstd)
    querry_btn2.grid(row=10, column=3, padx=(10,0))

    label1 = Label(root, text="\n Login as ", font="timesnewroman 15 bold", padx=20, pady=20)
    label1.grid(row=5, column=1)
    la = Label(root, text="\nDisplay ", font="timesnewroman 15 bold", padx=20, pady=20)
    la.grid(row=5, column=3)

    label7 = Label(root, text="\n   \n", font="timesnewroman 15 bold", padx=20, pady=20)
    label7.grid(row=4, column=0)
    label8 = Label(root, text="\n")
    label8.grid(row=9, column=1)
    label9 = Label(root, text="\n")
    label9.grid(row=11, column=1)

    querry_btn3 = Button(root, text="Admin Login", bg="navy",fg="white", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=admin)
    querry_btn3.grid(row=8, column=1)
    querry_btn4 = Button(root, text="Student", bg="navy",fg="white", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=student)
    querry_btn4.grid(row=10, column=1,ipadx=15)
    querry_btn5 = Button(root, text="Teacher", bg="navy",fg="white", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=teacher)
    querry_btn5.grid(row=12, column=1,ipadx=13)

    root.mainloop()


homepage()



