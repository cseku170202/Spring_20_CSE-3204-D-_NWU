from tkinter import *
import sqlite3
from tkinter import messagebox


def find_candidate():
    root = Tk()
    root.title("Job Management System")
    root.geometry("800x700")

    def complete():
        root2 = Tk()
        root2.title("Job Management System")
        root2.geometry("600x500")
        root2.configure(background="red")

        def save():
            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            name1 = user_entry.get()

            c.execute("SELECT * FROM teacher WHERE username = ?", (name1,))
            record = c.fetchall()

            if record == []:
                messagebox.showerror("Error", "There is no username that you entered")
            else:
                c.execute("""UPDATE teacher SET
                            fullname = :rv,
                            e_mail = :em,
                            expected_salary = :es,
                            address = :ads,
                            s_information = :si,
                            phone_no = :pn

                            WHERE username = :oid""",
                          {

                              'rv': full_name.get(),
                              'em': e_mail.get(),
                              'es': expected_salary.get(),
                              'ads': address.get(),
                              'si': s_information.get(),
                              'pn': p_no.get(),

                              'oid': user_entry.get()
                          })

                conn.commit()

                conn.close()
                messagebox.showinfo("Success", "Updated successful")

        full_name_label = Label(root2, text="Full Name", font="times 12", bg="red")
        full_name_label.grid(row=3, column=1, pady=5)
        e_mail_label = Label(root2, text="Job requirement", font="times 12", bg="red")
        e_mail_label.grid(row=6, column=1, pady=5)
        expected_salary_label = Label(root2, text="Expecting Education", font="timesnewroman 12", bg="red")
        expected_salary_label.grid(row=7, column=1, pady=5)
        address_label = Label(root2, text="Expecting certificate", font="timesnewroman 12", bg="red")
        address_label.grid(row=8, column=1, pady=5)
        s_information_label = Label(root2, text="Company address", font="timesnewroman 12", bg="red")
        s_information_label.grid(row=9, column=1, pady=5)
        p_no_label = Label(root2, text="Phone No", font="timesnewroman 12", bg="red")
        p_no_label.grid(row=10, column=1, pady=5)
        username_label = Label(root2, text="Username", font="timesnewroman 10", bg="red")
        username_label.grid(row=4, column=1)

        user_entry = Entry(root2, width=30, borderwidth=5)
        user_entry.grid(row=4, column=2)
        full_name = Entry(root2, width=30, borderwidth=5)
        full_name.grid(row=3, column=2)
        e_mail = Entry(root2, width=30, borderwidth=5)
        e_mail.grid(row=6, column=2)
        expected_salary = Entry(root2, width=30, borderwidth=5)
        expected_salary.grid(row=7, column=2)
        address = Entry(root2, width=30, borderwidth=5)
        address.grid(row=8, column=2)
        s_information = Entry(root2, width=30, borderwidth=5)
        s_information.grid(row=9, column=2)
        p_no = Entry(root2, width=30, borderwidth=5)
        p_no.grid(row=10, column=2)

        save_btn = Button(root2, text="Save", bg="green", font="times 15", command=save)
        save_btn.grid(row=11, column=1, columnspan=3, ipadx=20)

        back = Label(root2, text="         \t\t    ", font="timesnewroman 10", bg="red")
        back.grid(row=0, column=0, pady=(0, 100))

        root2.mainloop()

    label1 = Label(root, text="Candidate List", font="Times_New_Roman 20 bold")
    label1.grid(row=1, column=2, pady=50)
    label2 = Label(root, text="                ", font="Times_New_Roman 20 bold")
    label2.grid(row=1, column=1)

    create_btn = Button(root, text="Complete Your registration", bg="red", font="times 15", command=complete).grid(
        row=0, column=2, pady=20)

    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    c.execute("SELECT * , oid FROM teacher")
    record = c.fetchall()

    count = 0
    print_record = ''
    for records in record:
        print_record += "First Name: " + str(records[0]) + "\n" + "Mail: " + str(
            records[3]) + "\n" + "Expecting Salary: " + str(records[4]) + "\n" + "Education: " + str(
            records[6]) + "\n" + "Present Address: " + str(records[5]) + "\n" + "Phone Number: " + str(
            records[7]) + "\nUser ID: " + str(records[9]) + "\n \n"
        count += 1

    q_label = Label(root, text=print_record, font="timesnewroman 15")
    q_label.grid(row=2, column=2)
    q_label2 = Label(root, text="Total this System: " + str(count), font="timesnewroman 15")
    q_label2.grid(row=3, column=2, pady=50)

    conn.commit()

    conn.close()

    def back_homepage():
        root.destroy()
        homepage()

    back = Button(text="Back to Homepage", font="timesnewroman 10", bg="pink", command=back_homepage)
    back.grid(row=0, column=0)

    root.mainloop()


def find_jobholder():
    root = Tk()
    root.title("Job Management System")
    root.geometry("800x700")

    def complete():
        root2 = Tk()
        root2.title("Job Management System")
        root2.geometry("600x500")
        root2.configure(background="red")

        def save():
            conn = sqlite3.connect('tms.db')
            c = conn.cursor()

            name1 = user_entry.get()

            c.execute("SELECT * FROM student WHERE username = ?", (name1,))
            record = c.fetchall()

            if record == []:
                messagebox.showerror("Error", "There is no username that you entered")
            else:
                c.execute("""UPDATE student SET
                            fullname = :rv,
                            class = :em,
                            group1 = :es,
                            interested_sub = :ads,
                            p_address = :si,
                            phone_no = :pn

                            WHERE username = :oid""",
                          {

                              'rv': full_name.get(),
                              'em': e_mail.get(),
                              'es': expected_salary.get(),
                              'ads': address.get(),
                              'si': s_information.get(),
                              'pn': p_no.get(),

                              'oid': user_entry.get()
                          })

                conn.commit()

                conn.close()
                messagebox.showinfo("Success", "Updated successful")

        full_name_label = Label(root2, text="Full Name", font="times 12", bg="red")
        full_name_label.grid(row=3, column=1, pady=5)
        e_mail_label = Label(root2, text="Mail", font="times 12", bg="red")
        e_mail_label.grid(row=6, column=1, pady=5)
        expected_salary_label = Label(root2, text="Expecting Salary", font="timesnewroman 12", bg="red")
        expected_salary_label.grid(row=7, column=1, pady=5)
        address_label = Label(root2, text="Address", font="timesnewroman 12", bg="red")
        address_label.grid(row=8, column=1, pady=5)
        s_information_label = Label(root2, text="Education", font="timesnewroman 12", bg="red")
        s_information_label.grid(row=9, column=1, pady=5)
        p_no_label = Label(root2, text="Phone No", font="timesnewroman 12", bg="red")
        p_no_label.grid(row=10, column=1, pady=5)
        username_label = Label(root2, text="Username", font="timesnewroman 10", bg="red")
        username_label.grid(row=4, column=1)

        user_entry = Entry(root2, width=30, borderwidth=5)
        user_entry.grid(row=4, column=2)
        full_name = Entry(root2, width=30, borderwidth=5)
        full_name.grid(row=3, column=2)
        e_mail = Entry(root2, width=30, borderwidth=5)
        e_mail.grid(row=6, column=2)
        expected_salary = Entry(root2, width=30, borderwidth=5)
        expected_salary.grid(row=7, column=2)
        address = Entry(root2, width=30, borderwidth=5)
        address.grid(row=8, column=2)
        s_information = Entry(root2, width=30, borderwidth=5)
        s_information.grid(row=9, column=2)
        p_no = Entry(root2, width=30, borderwidth=5)
        p_no.grid(row=10, column=2)

        save_btn = Button(root2, text="Save", bg="green", font="times 15", command=save)
        save_btn.grid(row=11, column=1, columnspan=3, ipadx=20)

        back = Label(root2, text="         \t\t    ", font="timesnewroman 10", bg="red")
        back.grid(row=0, column=0, pady=(0, 100))

        root2.mainloop()

    label1 = Label(root, text="Job List", font="Times_New_Roman 20 bold")
    label1.grid(row=1, column=2, pady=50)
    label2 = Label(root, text="                ", font="Times_New_Roman 20 bold")
    label2.grid(row=1, column=1)

    conn = sqlite3.connect('tms.db')
    c = conn.cursor()

    c.execute("SELECT * , oid FROM student")
    record = c.fetchall()

    count = 0
    print_record = ''
    for records in record:
        print_record += "First Name: " + str(records[0]) + "\nLast Name: " + str(
            records[1]) + "\n" + "Job Requrement: " + str(records[3]) + "\n" + "Expecting Education: " + str(
            records[4]) + "\n" + "Expecting certificate: " + str(records[5]) + "\n" + "Company Address: " + str(
            records[6]) + "\n" + "Phone Number: " + str(records[7]) + "\nUser ID: " + str(records[9]) + "\n \n"
        count += 1

    q_label = Label(root, text=print_record, font="timesnewroman 15")
    q_label.grid(row=2, column=2)
    q_label2 = Label(root, text="Total this System: " + str(count), font="timesnewroman 15")
    q_label2.grid(row=3, column=2, pady=50)

    create_btn = Button(root, text="Complete Your registration", bg="red", font="times 15", command=complete).grid(
        row=0, column=2, pady=20)

    conn.commit()

    conn.close()

    def back_homepage():
        root.destroy()
        homepage()

    back = Button(text="Back to Homepage", font="timesnewroman 10", bg="pink", command=back_homepage)
    back.grid(row=0, column=0)

    root.mainloop()


def start_student():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("950x500")
    root.configure(background='orchid')

    label2 = Label(root, text="Job Holder page", font="timesnewroman 15 bold", padx=20, pady=20, fg="blue", bg="orchid")
    label2.grid(row=1, column=2, pady=30)

    global user

    user = StringVar()
    entry1 = Entry(root, textvariable=user, width=30, borderwidth=5)
    entry1.grid(row=3, column=2, pady=3)
    entry2 = Entry(root, width=30, borderwidth=5)
    entry2.grid(row=4, column=2, pady=3)

    label1 = Label(root, text="Username: ", font="timesnewroman 12", fg="blue", bg="orchid")
    label1.grid(row=3, column=1)
    label3 = Label(root, text="Password: ", font="timesnewroman 12", fg="blue", bg="orchid")
    label3.grid(row=4, column=1)

    label14 = Label(root, text="\n", font="timesnewroman 10", bg="orchid")
    label14.grid(row=5, column=1)

    def std_dp():
        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        name = user.get()

        c.execute("SELECT * FROM student WHERE username = ?", (name,))
        record = c.fetchall()

        conn.commit()

        conn.close()

        if (record == []):
            labelm = Label(root, text="Username or Password was incorrect", font="timesnewroman 10", bg="orchid")
            labelm.grid(row=100, column=100)
        else:
            root.destroy()
            find_candidate()

    def s_std():
        root.destroy()
        std_signup()

    btn = Button(root, text="        Login        ", bg="green", borderwidth=5, pady=5, padx=5,
                 font="timesnewroman 10 bold", command=std_dp)
    btn.grid(row=6, column=1, columnspan=5)
    btn2 = Button(root, text="        Create an Account        ", bg="green", borderwidth=5, pady=5, padx=5,
                  font="timesnewroman 10 bold", command=s_std)
    btn2.grid(row=8, column=2, padx=20)

    label14 = Label(root, text="\n", font="timesnewroman 10", bg="orchid")
    label14.grid(row=7, column=1)

    label14 = Label(root, text="New to BD job?", font="timesnewroman 12", fg="blue", bg="orchid")
    label14.grid(row=8, column=1, padx=20)

    def back_homepage():
        root.destroy()
        homepage()

    back = Button(text="Back to Homepage", font="timesnewroman 10", bg="pink", command=back_homepage)
    back.grid(row=0, column=0)

    root.mainloop()


def start_teacher():
    root = Tk()
    root.title("Tuition Management System")
    root.geometry("1100x500")

    def pro_tcr():

        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        name = username.get()

        c.execute("SELECT * FROM teacher WHERE username= ?", (name,))
        record = c.fetchall()

        conn.commit()
        conn.close()

        if (record == []):
            labelm = Label(root, text="Username or Password was incorrect", font="timesnewroman 10")
            labelm.grid(row=100, column=100)
        else:
            root.destroy()
            find_jobholder()

    def s_tcr():
        root.destroy()
        tcr_signup()

    label2 = Label(root, text="Job Candidate page", font="timesnewroman 15 bold", padx=20, pady=20, fg="red")
    label2.grid(row=1, column=2, pady=30)

    global username

    username = StringVar()
    usernameEntry = Entry(root, textvariable=username, width=30, borderwidth=5).grid(row=3, column=2, pady=3)
    entry2 = Entry(root, width=30, borderwidth=5)
    entry2.grid(row=4, column=2, pady=3)

    label1 = Label(root, text="Username: ", font="timesnewroman 12", fg="red")
    label1.grid(row=3, column=1)
    label3 = Label(root, text="Password: ", font="timesnewroman 12", fg="red")
    label3.grid(row=4, column=1)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=5, column=1)

    btn = Button(root, text="        Login        ", bg="green", borderwidth=5, pady=5, padx=5,
                 font="timesnewroman 10 bold", command=pro_tcr)
    btn.grid(row=6, column=1, columnspan=5)

    label14 = Label(root, text="\n", font="timesnewroman 10")
    label14.grid(row=7, column=1)

    label14 = Label(root, text="New to BD Job?", font="timesnewroman 12", fg="red")
    label14.grid(row=8, column=1, padx=50)

    btn2 = Button(root, text="        Create an Account        ", bg="green", borderwidth=5, pady=5, padx=5,
                  font="timesnewroman 10 bold", command=s_tcr)
    btn2.grid(row=8, column=2, columnspan=5)

    def back_homepage():
        root.destroy()
        homepage()

    back = Button(text="Back to Homepage", font="timesnewroman 10", bg="pink", command=back_homepage)
    back.grid(row=0, column=0)

    root.mainloop()


def tcr_signup():
    root = Tk()
    root.title("SADMAN")
    root.geometry("1000x500")
    root.configure(background='red')

    def submit():
        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute(
            "INSERT INTO student VALUES (:fullname, :username, :password, :e_mail, :expected_salary, :address, :s_information, :phone_no, :review)",

            {
                'fullname': "",
                'username': username.get(),
                'password': password.get(),
                'e_mail': "",
                'expected_salary': "",
                'address': "",
                's_information': "",
                'phone_no': "",
                'review': ""
            }

        )

        conn.commit()

        conn.close()

        username.delete(0, END)
        password.delete(0, END)

    label2 = Label(root, text="\t \t \t \t Job Candidate  \n \n", font="timesnewroman 15 bold", padx=20, pady=20,
                   bg="red")
    label2.grid(row=1, column=1)

    # for label

    username_label = Label(root, text="Username", font="timesnewroman 10", bg="red")
    username_label.grid(row=4, column=1)
    password_label = Label(root, text="Password", font="timesnewroman 10", bg="red")
    password_label.grid(row=5, column=1)

    # for entry box

    username = Entry(root, width=30, borderwidth=5)
    username.grid(row=4, column=2)
    password = Entry(root, width=30, borderwidth=5)
    password.grid(row=5, column=2)

    label14 = Label(root, text="\n", font="timesnewroman 10", bg="red")
    label14.grid(row=11, column=1)

    # for button

    btn2 = Button(root, text="              Create Account            ", bg="yellow", borderwidth=5, pady=5, padx=5,
                  command=submit)
    btn2.grid(row=12, column=1, columnspan=2)

    def back_homepage():
        root.destroy()
        homepage()

    back = Button(text="Back to Homepage", font="timesnewroman 10", bg="yellow", command=back_homepage)
    back.grid(row=0, column=2)

    root.mainloop()


def std_signup():
    root = Tk()
    root.title("SADMAN")
    root.geometry("1100x400")
    root.configure(background='red')

    def submit():
        conn = sqlite3.connect('tms.db')
        c = conn.cursor()

        c.execute(
            "INSERT INTO teacher VALUES (:fullname, :username, :password, :class, :group1, :interested_sub, :p_address, :phone_no , :review)",

            {
                'fullname': "",
                'username': username.get(),
                'password': password.get(),
                'class': "",
                'group1': "",
                'interested_sub': "",
                'p_address': "",
                'phone_no': "",
                'review': ""
            }

        )

        conn.commit()
        conn.close()

        username.delete(0, END)
        password.delete(0, END)

    label2 = Label(root, text="\t \t \t \t Job Holder  \n \n", font="timesnewroman 15 bold", padx=20, pady=20,
                   bg="red")
    label2.grid(row=1, column=1)

    username_label = Label(root, text="Username", font="timesnewroman 10", bg="red")
    username_label.grid(row=4, column=1)
    password_label = Label(root, text="Password", font="timesnewroman 10", bg="red")
    password_label.grid(row=5, column=1)

    username = Entry(root, width=30, borderwidth=5)
    username.grid(row=4, column=2, pady=3)
    password = Entry(root, width=30, borderwidth=5)
    password.grid(row=5, column=2, pady=3)

    label14 = Label(root, text="\n", font="timesnewroman 10", bg="red")
    label14.grid(row=11, column=1)

    btn2 = Button(root, text="              Create Account            ", bg="green", borderwidth=5, pady=5, padx=5,
                  command=submit)
    btn2.grid(row=12, column=1, columnspan=2)

    def back_homepage():
        root.destroy()
        homepage()

    back = Button(text="Back to Homepage", font="timesnewroman 10", bg="yellow", command=back_homepage)
    back.grid(row=0, column=2)

    root.mainloop()


def homepage():
    root = Tk()
    root.title("SADMAN")
    root.geometry("550x300")
    root.configure(background='black')

    def teacher():
        root.destroy()
        start_teacher()

    def student():
        root.destroy()
        start_student()

    def candidate():
        root.destroy()
        find_candidate()

    def jobholder():
        root.destroy()
        find_jobholder()

    m_label = Label(root, text="BD JOB", bg="blue", font="times 20 bold", pady=20)
    m_label.grid(row=0, column=2, ipadx=30, pady=30)

    querry_btn4 = Button(root, text="Job Candidate", bg="wheat", font="timesnewroman 12 ", pady=5, padx=5,
                         borderwidth=5,
                         command=teacher)
    querry_btn4.grid(row=1, column=1, padx=30)
    querry_btn5 = Button(root, text="Job Holder", bg="wheat", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=student)
    querry_btn5.grid(row=1, column=3, padx=30, ipadx=20)
    '''querry_btn6 = Button(root, text="Find Candidate", bg="wheat", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=candidate)
    querry_btn6.grid(row=8, column=3, padx=10)
    querry_btn7 = Button(root, text="Find job ", bg="wheat", font="timesnewroman 12 ", pady=5, padx=5, borderwidth=5,
                         command=jobholder)
    querry_btn7.grid(row=8, column=4, padx=10)'''

    root.mainloop()


homepage()

