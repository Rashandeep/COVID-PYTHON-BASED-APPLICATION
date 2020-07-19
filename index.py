# DO ALL THE IMPORTS

# IMPORT FOR GUI
import tkinter as tk
from tkinter import messagebox

# IMPORT FOR DISPLAYING DATE AND TIME
import time
import datetime as dt

# IMPORT FOR CALENDER
import calendar

import threading

# IMPORT FOR DISPLAYING IMAGE ON TKINTER
from PIL import ImageTk,Image

# IMPORT FOR SENDING MAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#IMPORTING THE FILES
import case
import navbar
import database
import hyperlink


# FUNCTION TO REFRESH DATA
def refresh():
    newdata=case.get_corona_detail_of_india()
    print("Refreshing..")
    mainlabel['text'] = newdata

# FUNCTION FOR DISPLAYING DYNAMIC TIME
time1 = ''
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

# FUNCTION TO OPEN ABOUT WINDOW
def about_me():
    about_window=tk.Toplevel(root)
    about_window.geometry('500x640')
    about_window.title('ABOUT ME')
    about_window.config(bg="white")
    about_window.resizable(0,0)

    # DISPLAYING HEADING
    myname=tk.Label(about_window, text="RASHANDEEP SINGH", width=20, fg="black", font=("bold",15), relief="solid")
    myname.place(x=150,y=20)

    # DISPLAYING IMAGE
    panel = tk.Label(about_window, image = img_about, relief="solid")
    panel.place(x=150,y=90)

    # DISPLAYNIG PORTFOLIO LABEL
    myfolio=tk.Label(about_window, text=navbar.about(), width=40, fg="black", font=("bold",15), relief="solid")
    myfolio.place(x=32,y=370)

    # DISPLAYING LINK BUTTONS
    tk.Button(about_window,text="Instagram", width=14, bg='medium purple',fg="black", command=hyperlink.insta).place(x=100, y=490)
    tk.Button(about_window,text="Linkedin", width=14, bg='blue',fg="black", command=hyperlink.linkedin).place(x=300, y=490)
    tk.Button(about_window,text="Github", width=14, bg='lightgrey',fg="black", command=hyperlink.github).place(x=100, y=570)
    tk.Button(about_window,text="Go Back", width=14, bg='brown',fg="black", command=lambda: about_window.destroy()).place(x=300, y=570)

# FUNCTION TO OPEN VIEW DATA WINDOW
def view_data():
    view_window=tk.Toplevel(root)
    view_window.geometry('500x640')
    view_window.title('VIEW DATA')
    view_window.resizable(0,0)

    # DISPLAYING HEADING
    view_head=tk.Label(view_window, text="VIEW DATA", width=20, fg="black", font=("bold",15), relief="solid")
    view_head.place(x=150,y=30)

    # DISPLAYING NOTE LABEL
    view_note=tk.Label(view_window, text="Date should be in form- Mon, Jul 13 2020\n This app contains data from Mon, Jul 13 2020",fg="red", font=("bold",9))
    view_note.place(x=135,y=70)

    # FUNCTION FOR CALENDER
    def cal():
        y = e1.get()
        m = e2.get()
        try:
            cal_x = calendar.month(int(y),int(m),w = 2, l = 1)
            messagebox.showinfo("Calender", cal_x)
        except:
            messagebox.showinfo("Calender", "Enter proper details")

    label1 = tk.Label(view_window, text="Year:")
    label1.place(x=70, y=120)

    e1 = tk.Entry(view_window, width="10")
    e1.place(x=110, y=120)

    label2 = tk.Label(view_window, text="Month:")
    label2.place(x=210, y=120)

    e2 = tk.Entry(view_window, width="10")
    e2.place(x=255, y=120)

    button = tk.Button(view_window, text="Show Calender",command=cal)
    button.place(x=350, y=120)

    # DISPLAYING TEXT-Enter Date
    view_date=tk.Label(view_window, text="Enter Date", width=20, font=("bold",10))
    view_date.place(x=40,y=170)

    # DISPLAYING ENRTY BOX
    view_ans=tk.Entry(view_window, width=20)
    view_ans.place(x=200, y=170)

    # FUNCTION TO VIEW DATA
    def seecase():
        database.cur.execute('SELECT * FROM tracker WHERE date= ?',(view_ans.get(), ) )
        row=database.cur.fetchone()

        if row is None:
            messagebox.showinfo("information","Data doesnot exist or it should be in form- \nMon, Jul 13 2020")
        else:
            date=row[0]
            active=row[1]
            cured=row[2]
            deaths=row[3]
            migrated=row[4]

            view_date1 = tk.Label(view_window, text="Date", fg='black', font=("bold", 20))
            view_date1.place(x=120, y=280)
            view_date = tk.Label(view_window, text=date, fg='green', font=("bold", 20))
            view_date.place(x=200, y=280)

            view_active1 = tk.Label(view_window, text="Active Cases", fg='black', font=("bold", 20))
            view_active1.place(x=120, y=330)
            view_active = tk.Label(view_window, text=active, fg='green', font=("bold", 20))
            view_active.place(x=290, y=330)

            view_cured1 = tk.Label(view_window, text="Cured Cases", fg='black', font=("bold", 20))
            view_cured1.place(x=120, y=380)
            view_cured = tk.Label(view_window, text=cured, fg='green', font=("bold", 20))
            view_cured.place(x=290, y=380)

            view_deaths1 = tk.Label(view_window, text="Deaths", fg='black', font=("bold", 20))
            view_deaths1.place(x=120, y=430)
            view_deaths = tk.Label(view_window, text=deaths, fg='green', font=("bold", 20))
            view_deaths.place(x=290, y=430)

            view_migrated1 = tk.Label(view_window, text="Migrated Cases", fg='black', font=("bold", 20))
            view_migrated1.place(x=120, y=480)
            view_migrated = tk.Label(view_window, text=migrated, fg='green', font=("bold", 20))
            view_migrated.place(x=330, y=480)

    tk.Button(view_window,text="View", width=14, bg='green',fg="white", command=seecase).place(x=210, y=220)
    tk.Button(view_window,text="Go Back", width=14, bg='brown',fg="white", command=lambda: view_window.destroy()).place(x=210, y=560)

# FUNCTION TO OPEN MAIL WINDOW
def call_mail():
    # print('opening mail window')
    try:
        database.cur.execute('CREATE TABLE email (date TEXT, sender TEXT, subject TEXT, message TEXT)')
    except:
        database.cur.execute('SELECT * FROM email')

    new_window=tk.Toplevel(root)
    new_window.geometry('500x640')
    new_window.title('EMAIL SENDER')
    new_window.resizable(0,0)

    # DISPLAYING HEADING
    Label_0=tk.Label(new_window, text="YOUR MAIL ACCOUNT", width=20, fg="green", font=("bold",15), relief="solid")
    Label_0.place(x=150,y=33)

    # DISPLAYING DATE
    w=tk.Label(new_window, text=format_date, fg="black", bg="lightgrey", width="14")
    w.place(x=0,y=0)

    # DISPLAYING TEXT-Your Email Account
    Label_1=tk.Label(new_window, text="Your Email Account", width=20, font=("bold",10))
    Label_1.place(x=40,y=110)

    # DISPLAYING ENRTY BOX
    emailE=tk.Entry(new_window, width=40)
    emailE.place(x=200, y=110)

    # DISPLAYING TEXT-Your Email Account
    Label_2=tk.Label(new_window, text="Your Password", width=20, font=("bold",10))
    Label_2.place(x=40,y=160)

    # DISPLAYING ENRTY BOX
    passwordE=tk.Entry(new_window, width=40,show="*")
    passwordE.place(x=200, y=160)

    # DISPLAYING  SECOND HEADING
    compose=tk.Label(new_window, text="COMPOSE YOUR MAIL", width=20, fg="green", font=("bold",15), relief="solid")
    compose.place(x=150,y=210)

    # DISPLAYING TEXT-Send To Email
    Label_3=tk.Label(new_window, text="Send To Email", width=20, font=("bold",10))
    Label_3.place(x=40,y=260)

    # DISPLAYING RECIEVER'S MAIL
    senderE=tk.Label(new_window, text="rashandeepsingh@gmail.com" ,width=30, font=("bold",10))
    senderE.place(x=200,y=260)
    t_senderE=senderE.cget("text")

    # DISPLAYING TEXTS-Subject
    Label_4=tk.Label(new_window, text="Subject", width=20, font=("bold",10))
    Label_4.place(x=40,y=310)

    # DISPLAYING ENRTY BOX
    subjectE=tk.Entry(new_window, width=40)
    subjectE.place(x=200, y=310)

    # DISPLAYING TEXT-Message
    Label_5=tk.Label(new_window, text="Message", width=20, font=("bold",10))
    Label_5.place(x=40,y=360)

    # DISPLAYING MESSAGE BOX
    msgbodyE=tk.Text(new_window, width=30, height=10)
    msgbodyE.place(x=200, y=360)

    # FUNCTION TO SEND MAIL
    def sendemail():
        isubmit = tk.messagebox.askyesno("Confirm","Are you sure to submit?") # TO DISPLAY CONFIRM BOX
        if isubmit > 0:
            try:
                mymsg=MIMEMultipart()
                mymsg['From']=emailE.get()
                mymsg['To']=t_senderE
                mymsg['Subject']=subjectE.get()

                mymsg.attach(MIMEText(msgbodyE.get(1.0,'end'), 'plain'))

                server=smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(emailE.get(), passwordE.get())
                text=mymsg.as_string()
                server.sendmail(emailE.get(), t_senderE, text)

                database.cur.execute('''INSERT OR IGNORE INTO email (date, sender, subject, message)
                    VALUES ( ?, ?, ?, ? )''', ( format_date, emailE.get(), subjectE.get(), msgbodyE.get(1.0,'end'), ) )
                database.conn.commit()

                Label_6 = tk.Label(new_window, text="Done!", width=20, fg='green', font=("bold", 15))
                Label_6.place(x=140, y=550)

                server.quit()

            except:
                Label_6 = tk.Label(new_window, text="something went wrong!", width=20, fg='red', font=("bold", 15))
                Label_6.place(x=140, y=550)

    # DISPLAYING SEND BUTTON
    tk.Button(new_window,text="Send", width=14, bg='green',fg="white", command=sendemail).place(x=100, y=590)

    # DISPLAYING QUIT BUTTON
    tk.Button(new_window,text="Go Back", width=14, bg='brown',fg="white", command=lambda: new_window.destroy()).place(x=250, y=590)

# CREATING NAVBAR
# setting switch state:
btnState = False

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        # brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg="green")
        topFrame.config(bg="green")
        # root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        # brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg="green")
        topFrame.config(bg="green")
        # root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True


# CREATING GUI USING TKINTER

root = tk.Tk()
root.geometry("500x640")
root.title("CORONA TRACKER - INDIA")
f = ("poppins", 25, "bold")
root.configure(bg="white")
root.resizable(0,0)

# GUI FOR NAVBAR
# top Navigation bar:
topFrame = tk.Frame(root, bg="green")
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="COVID", font="Bahnschrift 15", bg="green", fg="black", height=2, padx=20)
homeLabel.pack(side="right")

# Navbar button:
navbarBtn = tk.Button(topFrame, text="MENU", bg="green", activebackground="green", bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=15)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="lightgrey", height=250, width=115)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg="green", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# creating buttons in navbar
tk.Button(navRoot, text="View Data", font="BahnschriftLight 15", bg="lightgrey", fg="black", activebackground="lightgrey", activeforeground="green", bd=0, command=view_data).place(x=10, y=80)
tk.Button(navRoot, text="FAQ", font="BahnschriftLight 15", bg="lightgrey", fg="black", activebackground="lightgrey", activeforeground="green", bd=0, command=hyperlink.pdf).place(x=10, y=120)
tk.Button(navRoot, text="About", font="BahnschriftLight 15", bg="lightgrey", fg="black", activebackground="lightgrey", activeforeground="green", bd=0, command=about_me).place(x=10, y=160)
tk.Button(navRoot, text="Exit", font="BahnschriftLight 15", bg="lightgrey", fg="black", activebackground="lightgrey", activeforeground="green", bd=0, command=navbar.quiter).place(x=10, y=200)

# Navbar Close Button:
closeBtn = tk.Button(navRoot,text="CLOSE", bg="green", activebackground="green", bd=0, command=switch)
closeBtn.place(x=50, y=15)


# DISPLAYING IMAGE ON WINDOW
img_about = ImageTk.PhotoImage(Image.open("about.png"))
img = ImageTk.PhotoImage(Image.open("banner.png"))
panel = tk.Label(root, image = img, relief="solid")
panel.place(x=150,y=90)

# DISPLAYING TEXT ON WINDOW
mainlabel = tk.Label(root, text=case.get_corona_detail_of_india(), font=f, bg="white")
mainlabel.place(x=20,y=290)

# DISPLAYING REFRESH BUTTON ON WINDOW
rebtn = tk.Button(root, text="Refresh", width="14", command=refresh, relief="solid")
rebtn.place(x=195,y=480)

# DISPLAYING DATE
date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"
w=tk.Label(root, text=format_date, fg="black", bg="white", width="14" )
w.place(x=195,y=533)

# DISPLAYING DYNAMIC TIME
clock = tk.Label(root, width="14", bg='white')
clock.place(x=195,y=560)
tick()

#DISPLAYING ASK FROM DOCTER BUTTON
btn_mail = tk.Button(root, text="Ask Query From Doctor", width="18", bg="green", fg="white", command=call_mail)
btn_mail.place(x=181,y=600)

# DISPLAYING NAME BADGE
name= tk.Label(root,text='@RASHANDEEP SINGH', font=("poppins", 6), bg='white')
name.place(x=395,y=625)

# CREATE A NEW THREAD
th1 = threading.Thread(target=case.notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()
