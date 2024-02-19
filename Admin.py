from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import datetime as dt
import time
import sqlite3
import webbrowser
import random
import string

dashboard = Tk()
dashboard.title("Travel MS")
dashboard.configure(background="green")
dashboard.geometry('1360x750')

titleLabel = Label(dashboard, text="TRAVEL MANAGEMENT SYSTEM",
                   bg="blue", fg="orange", relief=RIDGE, bd=5,
                   width=1350, font=("Rockwell Extra Bold", 29, "bold"))
titleLabel.pack()

# ====================== COMPANY LOGO ==================================================

global newimage
myimage = Image.open("pictures/Marto.jpg")
resized = myimage.resize((80, 45), Image.ANTIALIAS)
newimage = ImageTk.PhotoImage(resized)

# ======================= OTHER IMAGES ================================================

myimage = Image.open("pictures/forgot-password-icon-17.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
password = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/add_usrer.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
adduser = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/account-i.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
viewuser = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/edit_user.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
removeusers = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/exit_2.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
logouts = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/checklist-icon-blue-blue-checklist-document-19.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
viewcustomer = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/reports.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
report = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/report-icon-14.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
viewreport = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/home_1.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
addstage = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/door-exit-log-out-logout-sign-out-icon--8.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
removestage = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/account_edit_1.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
updatestage = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/viewstage.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
viewstage = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/help-icon-6.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
help1 = ImageTk.PhotoImage(resized)

myimage = Image.open("pictures/about_1.png")
resized = myimage.resize((80, 70), Image.ANTIALIAS)
abouts = ImageTk.PhotoImage(resized)

# ======================= IMAGE LABELS ===========================================

img = Label(dashboard, image=newimage, bd=0)
img.place(x=5, y=4)

img1 = Label(dashboard, image=newimage, bd=0)
img1.place(x=1280, y=4)


myimagelogo = Image.open("pictures/exit_3.png")
resizedlogo = myimage.resize((130, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resizedlogo)


# ======================= Basic label details ===============================================

Motto = Label(dashboard, text="Offering Best & Quality services",
              bd=5, padx=20, bg="blue", fg="Orange", font=('Verdana', 22, 'bold'))
Motto.place(x=5, y=115)


Clock = Label(dashboard, bd=5, padx=20, bg="darkblue", fg="Orange",
              font=('Verdana', 19, 'bold'))
Clock.place(x=3, y=60)

Clock1 = Label(dashboard, bd=5, padx=20, bg="blue", fg="White",
               font=('elephant', 16, 'bold'))
Clock1.place(x=1050, y=10)


# =======================CLOCK AND DATES===============================================
def digitalclock():
    current = time.strftime("%a, %H:%M:%S %p")
    Clock.config(text=current)
    Clock.after(1000, digitalclock)


digitalclock()


def liveclock():
    current = time.strftime("%H:%M:%S %p")
    Clock1.config(text=current)
    Clock1.after(1000, liveclock)


liveclock()

date = dt.datetime.now()
format_date = f"{date:%d/%m/%Y}"  # f"{date:%a, %d, %b, %Y}"
format_date1 = f"{date:%d %b, %Y}"

# ------------------------------Welcome and date MODULES---------------------------------
welcome = Label(dashboard, text="Welcome Back  DANIEL !", pady=2, bg="Blue",
                fg="yellow", font=('Verdana', 20, 'bold'))
welcome.place(x=900, y=60)

welcomeDate = Label(dashboard, text=format_date1, padx=25, pady=2, bg="DarkBlue",
                    fg="yellow", font=('Verdana', 20, 'bold'))
welcomeDate.place(x=340, y=60)

logged = Label(dashboard, text="You are logged in as Admin", pady=2, bg="Blue",
               fg="yellow", font=('Constantia', 16, 'bold'))
logged.place(x=900, y=105)

logged = Label(dashboard, text="Mombasa Express Shuttle", pady=2, bg="green",
               fg="yellow", font=('Edwardian Script ITC', 23, 'bold'))
logged.place(x=900, y=137)

img2 = Label(dashboard, image=logo, bd=0)
img2.place(x=700, y=60)

# ============================ Functionalities ==========================================


def addusers():
    idno = IntVar()
    name = StringVar()
    phone = IntVar()
    username = StringVar()
    pass1 = StringVar()
    pass2 = StringVar()
    usertype = StringVar()

    def save():
        if name.get() == "" or idno.get() == "" or phone.get() == "" or pass1.get() == "":
            messagebox.showerror("Error", "You Must fill all the fields", parent=users)
        elif pass1.get() != pass2.get():
            messagebox.showerror("Error", "Passwords do not match!", parent=users)
            pass1entry.delete(0, END)
            pass2entry.delete(0, END)
        else:
            if usertype.get() == "Admin":
                connection = sqlite3.connect("TMS.db")
                cursor = connection.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS Admins(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            Name TEXT NOT NULL,
                            ID_NO INTEGER NOT NULL,
                            PHONE INTEGER NOT NULL,
                            USERNAME TEXT NOT NULL,
                            PASSWORD TEXT NOT NULL,
                            USERTYPE TEXT NOT NULL
                            )''')
                insert = "INSERT INTO Admins(" \
                         "Name," \
                         "ID_NO," \
                         "PHONE," \
                         "USERNAME," \
                         "PASSWORD," \
                         "USERTYPE" \
                         ") VALUES(?,?,?,?,?,?)"
                VAL = (name.get(),
                       idno.get(),
                       phone.get(),
                       username.get(),
                       pass1.get(),
                       usertype.get()
                       )
                cursor.execute(insert, VAL)
                connection.commit()
                connection.close()
                messagebox.showinfo("Success", "New Admin saved!", parent=users)
                nameEntry.delete(0, END)
                identry.delete(0, END)
                phoneentry.delete(0, END)
                usernameentry.delete(0, END)
                pass1entry.delete(0, END)
                pass2entry.delete(0, END)

            else:
                connection = sqlite3.connect("TMS.db")
                cursor = connection.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                                            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                            Name TEXT NOT NULL,
                                            ID_NO INTEGER NOT NULL,
                                            PHONE INTEGER NOT NULL,
                                            USERNAME TEXT NOT NULL,
                                            PASSWORD TEXT NOT NULL,
                                            USERTYPE TEXT NOT NULL
                                            )''')
                insert = "INSERT INTO Users(" \
                         "Name," \
                         "ID_NO," \
                         "PHONE," \
                         "USERNAME," \
                         "PASSWORD," \
                         "USERTYPE" \
                         ") VALUES(?,?,?,?,?,?)"
                VAL = (name.get(),
                       idno.get(),
                       phone.get(),
                       username.get(),
                       pass1.get(),
                       usertype.get()
                       )
                cursor.execute(insert, VAL)
                connection.commit()
                connection.close()
                messagebox.showinfo("Success", "New User saved!", parent=users)
                nameEntry.delete(0, END)
                identry.delete(0, END)
                phoneentry.delete(0, END)
                usernameentry.delete(0, END)
                pass1entry.delete(0, END)
                pass2entry.delete(0, END)

    users = Toplevel(dashboard, bd=3, relief=RIDGE)
    users.title("Add System Users")
    users.configure(background="LimeGreen")
    users.geometry('450x380')
    x = dashboard.winfo_x()
    y = dashboard.winfo_y()
    users.geometry("+%d+%d" % (x + 400, y + 250))
    users.wm_transient(dashboard)

    Details = LabelFrame(users, text="Add Users", fg="Red", bd=5, bg="darkblue",
                         font=('Verdana', 14, 'bold'))
    Details.place(x=40, y=30)

    namelabel = Label(Details, text="Name:", bg="darkblue",
                      fg="yellow", font=('Verdana', 14, 'bold'))
    namelabel.grid(row=0, column=0, sticky=W)

    nameEntry = Entry(Details, textvariable=name, bg="lightblue", bd=5,
                          fg="black", width=15, font=('Verdana', 15, 'bold'))
    nameEntry.grid(row=0, column=1)

    idlabel = Label(Details, text="ID NO:", bg="darkblue",
                    fg="yellow", font=('Verdana', 14, 'bold'))
    idlabel.grid(row=1, column=0, sticky=W)

    identry = Entry(Details, textvariable=idno, bg="lightblue", bd=5,
                    fg="black", width=15, font=('Verdana', 15, 'bold'))
    identry.grid(row=1, column=1)

    phonelabel = Label(Details, text="Phone :", bg="darkblue",
                       fg="yellow", font=('Verdana', 14, 'bold'))
    phonelabel.grid(row=2, column=0, sticky=W)

    phoneentry = Entry(Details, textvariable=phone, bg="lightblue", bd=5,
                       fg="black", width=15, font=('Verdana', 15, 'bold'))
    phoneentry.grid(row=2, column=1)

    usernamelabel = Label(Details, text="Username :", bg="darkblue",
                          fg="yellow", font=('Verdana', 14, 'bold'))
    usernamelabel.grid(row=3, column=0, sticky=W)

    usernameentry = Entry(Details, textvariable=username, bg="lightblue", bd=5,
                          fg="black", width=15, font=('Verdana', 15, 'bold'))
    usernameentry.grid(row=3, column=1)

    pass1label = Label(Details, text="Password 1:", bg="darkblue",
                          fg="yellow", font=('Verdana', 14, 'bold'))
    pass1label.grid(row=4, column=0, sticky=W)

    pass1entry = Entry(Details, textvariable=pass1, show="*", bg="lightblue", bd=5,
                       fg="black", width=15, font=('Verdana', 15, 'bold'))
    pass1entry.grid(row=4, column=1)

    pass2label = Label(Details, text="Confirm :", bg="darkblue",
                       fg="yellow", font=('Verdana', 15, 'bold'))
    pass2label.grid(row=5, column=0, sticky=W)

    pass2entry = Entry(Details, textvariable=pass2, show="*", bg="lightblue", bd=5,
                       fg="black", width=15, font=('Verdana', 15, 'bold'))
    pass2entry.grid(row=5, column=1)

    usertypelabel = Label(Details, text="Usertype :", bg="darkblue",
                          fg="yellow", font=('Verdana', 15, 'bold'))
    usertypelabel.grid(row=6, column=0, sticky=W)

    usertypeentry = ttk.Combobox(Details, textvariable=usertype, width=15,
                                 font=('Verdana', 15, 'bold'))
    usertypeentry['value'] = ["Admin", "User"]
    usertypeentry.current(0)
    usertypeentry.configure(state="readonly")
    usertypeentry.grid(row=6, column=1)

    addbutton = Button(users, text="Save User", bd=3, fg="White",
                       bg="Green", relief=RAISED, command=save,
                       font=('Rockwell Extra Bold', 14, "bold"))
    addbutton.place(x=150, y=330)

    users.mainloop()


def addlocations():
    location = StringVar()
    dest = StringVar()

    def save():
        if location.get() == "" or dest.get() == "":
            messagebox.showerror("Error", "You Must fill all the fields", parent=form)
        else:
            connection = sqlite3.connect("TMS.db")
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Destinations(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    Dest TEXT NOT NULL,
                    Destt TEXT NOT NULL 
                    )''')
            insert = "INSERT INTO Destinations(" \
                     "Dest," \
                     "Destt" \
                     ") VALUES(?,?)"
            VAL = (location.get(),
                   dest.get())
            cursor.execute(insert, VAL)
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "New Destination Added!", parent=form)
            locationEntry.delete(0, END)
            desttentry.delete(0, END)

    form = Toplevel(dashboard, bd=3, relief=RIDGE)
    form.title("New Route")
    form.configure(background="LimeGreen")
    form.geometry('350x200')
    x = dashboard.winfo_x()
    y = dashboard.winfo_y()
    form.geometry("+%d+%d" % (x+400, y+250))
    form.wm_transient(dashboard)

    Details = LabelFrame(form, text="Add New Route", fg="Red", bd=5,bg="darkblue",
                         font=('Verdana', 14, 'bold'))
    Details.place(x=25, y=30)

    locationLabel = Label(Details, text="Dest1:", bg="darkblue",
                           fg="yellow", font=('Verdana', 14, 'bold'))
    locationLabel.grid(row=0, column=0, sticky=W)

    locationEntry = Entry(Details, textvariable=location, bg="lightblue", bd=5,
                      fg="black", width=15, font=('Verdana', 14))
    locationEntry.grid(row=0, column=1)

    desttlabel = Label(Details, text="Dest2:", bg="darkblue",
                          fg="yellow", font=('Verdana', 14, 'bold'))
    desttlabel .grid(row=1, column=0, sticky=W)

    desttentry = Entry(Details, textvariable=dest, bg="lightblue", bd=5,
                          fg="black", width=15, font=('Verdana', 14))
    desttentry.grid(row=1, column=1)

    addbutton = Button(form, text="Save", bd=3, fg="White",
                       bg="Green", relief=RAISED, command=save,
                       font=('Rockwell Extra Bold', 14, "bold"))
    addbutton.place(x=110, y=130)

    form.mainloop()


# ============================ Actions Frame =============================================
actionsFrame = LabelFrame(dashboard, text="Options", cursor="arrow",
                          bg="MediumSpringGreen",
                          bd=5, fg="black", width=1340, height=520,
                          relief=SUNKEN, font=('Constantia', 18, 'bold'))
actionsFrame.place(x=13, y=170)

# ================================= ACTIONS ==============================================

changepass = Button(actionsFrame, text="Change Password", bg="blue",
                    activebackground="orangered", cursor="hand2", fg="yellow",
                    font=('Constantia', 18, 'bold'))
changepass.place(x=110, y=10)

addusers = Button(actionsFrame, text="Add User", command=addusers, bg="blue",
                  activebackground="orangered", cursor="hand2", fg="yellow",
                  font=('Constantia', 18, 'bold'))
addusers.place(x=110, y=110)

viewusers = Button(actionsFrame, text="View Users", bg="blue",
                   activebackground="orangered", cursor="hand2", fg="yellow",
                   font=('Constantia', 18, 'bold'))
viewusers.place(x=110, y=210)

removeuser = Button(actionsFrame, text="Remove User", bg="blue",
                    activebackground="orangered", cursor="hand2", fg="yellow",
                    font=('Constantia', 18, 'bold'))
removeuser.place(x=110, y=310)

logout = Button(actionsFrame, text="Log Out", bg="red",
                activebackground="white", cursor="hand2",
                fg="white", font=('Constantia', 18, 'bold'))
logout.place(x=110, y=410)

viewcustomers = Button(actionsFrame, text="View Customers", bg="blue",
                       activebackground="orangered", cursor="hand2", fg="yellow",
                       font=('Constantia', 18, 'bold'))
viewcustomers.place(x=520, y=10)

reports = Button(actionsFrame, text="Generate Reports", bg="blue",
                 activebackground="orangered", cursor="hand2", fg="yellow",
                 font=('Constantia', 18, 'bold'))
reports.place(x=520, y=110)

viewreports = Button(actionsFrame, text="View Reports", bg="blue",
                     activebackground="orangered", cursor="hand2", fg="yellow",
                     font=('Constantia', 18, 'bold'))
viewreports.place(x=520, y=210)

addstages = Button(actionsFrame, text="Add Route", bg="blue",
                   activebackground="orangered", cursor="hand2", fg="yellow",
                   command=addlocations, font=('Constantia', 18, 'bold'))
addstages.place(x=520, y=310)

removestages = Button(actionsFrame, text="Remove Route", bg="blue",
                      activebackground="orangered", cursor="hand2", fg="yellow",
                      font=('Constantia', 18, 'bold'))
removestages.place(x=520, y=410)

updatestages = Button(actionsFrame, text="Update Stations", bg="blue",
                      activebackground="orangered", cursor="hand2", fg="yellow",
                      font=('Constantia', 18, 'bold'))
updatestages.place(x=920, y=10)

updatestages = Button(actionsFrame, text="View Stations", bg="blue",
                      activebackground="orangered", cursor="hand2", fg="yellow",
                      font=('Constantia', 18, 'bold'))
updatestages.place(x=920, y=110)

helpbtn = Button(actionsFrame, text="Help/Support", bg="blue",
                 activebackground="orangered", cursor="hand2", fg="yellow",
                 font=('Constantia', 18, 'bold'))
helpbtn.place(x=920, y=210)

about = Button(actionsFrame, text="About", bg="blue",
               activebackground="orangered", cursor="hand2", fg="yellow",
               font=('Constantia', 18, 'bold'))
about.place(x=920, y=310)

# ============================ Link =======================================================


def callback(url):
    webbrowser.open_new_tab(url)


link = Label(actionsFrame, text="www.d-techtechnologies.com",
             fg="blue", bg="MediumSpringGreen", cursor="hand2", font=('Helveticabold', 15))
link.place(x=750, y=460)

link.bind("<Button-1>", lambda e: callback("https://www.d-techtechnologies.com"))

# ============================ ICON LABELS==================================================
img3 = Label(actionsFrame, image=password, bd=0, bg="MediumSpringGreen")
img3.place(x=20, y=3)

img4 = Label(actionsFrame, image=adduser, bd=0, bg="MediumSpringGreen")
img4.place(x=20, y=100)

img5 = Label(actionsFrame, image=viewuser, bd=0, bg="MediumSpringGreen")
img5.place(x=20, y=200)

img6 = Label(actionsFrame, image=removeusers, bd=0, bg="MediumSpringGreen")
img6.place(x=20, y=300)

img7 = Label(actionsFrame, image=logouts, bd=0, bg="MediumSpringGreen")
img7.place(x=20, y=400)

img8 = Label(actionsFrame, image=viewcustomer, bd=0, bg="MediumSpringGreen")
img8.place(x=430, y=3)

img9 = Label(actionsFrame, image=report, bd=0, bg="MediumSpringGreen")
img9.place(x=430, y=100)

img10 = Label(actionsFrame, image=viewreport, bd=0, bg="MediumSpringGreen")
img10.place(x=430, y=200)

img11 = Label(actionsFrame, image=addstage, bd=0, bg="MediumSpringGreen")
img11.place(x=430, y=300)

img12 = Label(actionsFrame, image=removestage, bd=0, bg="MediumSpringGreen")
img12.place(x=430, y=400)

img13 = Label(actionsFrame, image=updatestage, bd=0, bg="MediumSpringGreen")
img13.place(x=830, y=3)

img14 = Label(actionsFrame, image=viewstage, bd=0, bg="MediumSpringGreen")
img14.place(x=830, y=100)

img13 = Label(actionsFrame, image=help1, bd=0, bg="MediumSpringGreen")
img13.place(x=830, y=200)

img14 = Label(actionsFrame, image=abouts, bd=0, bg="MediumSpringGreen")
img14.place(x=830, y=300)


dashboard.mainloop()
