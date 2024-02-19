# importing required modules
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import datetime as dt
import time
import random
import string
import sqlite3

dashboard = Tk()
dashboard.title("Travel MS")
dashboard.configure(background="light blue")
dashboard.geometry('1360x750')

titleLabel = Label(dashboard, text="TRAVEL  MANAGEMENT  SYSTEM",
                   bg="blue", fg="orangered", relief=RIDGE, bd=5,
                   width=1350, font=("Rockwell Extra Bold", 29, "bold"))
titleLabel.pack()

# ---------------------COMPANY LOGO-------------------------

global newimage
myimage = Image.open("pictures/Marto.jpg")
resized = myimage.resize((80, 45), Image.ANTIALIAS)
newimage = ImageTk.PhotoImage(resized)

img = Label(dashboard, image=newimage, bd=0)
img.place(x=5, y=4)

img2 = Label(dashboard, image=newimage, bd=0)
img2.place(x=1280, y=4)

myimagelogo = Image.open("pictures/Marto.jpg")
resizedlogo = myimage.resize((320, 350), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(resizedlogo)

# ---------------------------------Frames------------------------------------------------------

CDFrame = Frame(dashboard,bd=3, highlightcolor="blue",
                bg="MediumSpringGreen", padx=20, relief=RIDGE)
CDFrame.place(x=3, y=62, width=800, height=640)

DDFrame = Frame(dashboard, bd=3, highlightcolor="blue",
                bg="lightgreen", padx=20, relief=RIDGE)
DDFrame.place(x=810, y=62, width=550, height=640)

# --------------------------------------- Variables -------------------------------------
ref_var = StringVar()
name_var = StringVar()
post_var = IntVar()
phone_var = IntVar()
date_var = StringVar()
bus_var = StringVar()
driver_var = StringVar()
from_var = StringVar()
to_var = StringVar()
tax_var = StringVar()
total_var = IntVar()
searchC_var = StringVar()
searchText_var = StringVar()
cost_var = IntVar()
Current = StringVar()
# --------------------------------------- End ofVariables ------------------------------------
# --------------------------------------- Button Functionalities-------------------------------


def refrence_no():
    ref_length = 8
    for n in range(ref_length):
        ref_string = string.ascii_letters + string.digits
        reference = "".join(random.choice(ref_string))
        RefNoEntry.insert(END, reference)


# ================================== Button functionalities =================================

def reset():
    ref_length1 = 8
    for n in range(ref_length1):
        ref_strings = string.ascii_letters + string.digits
        ref_no = "".join(random.sample(ref_strings, ref_length1))
        ref_var.set(ref_no)
    name_var.set("")
    post_var.set("")
    phone_var.set("")
    bus_var.set("")
    driver_var.set("")
    cost_var.set("")
    tax_var.set("")
    total_var.set("")


def refresh():
    ref_length1 = 8
    for n in range(ref_length1):
        ref_strings = string.ascii_letters + string.digits
        ref_no = "".join(random.sample(ref_strings, ref_length1))
        ref_var.set(ref_no)
    name_var.set("")
    post_var.set("")
    phone_var.set("")
    bus_var.set("")
    driver_var.set("")
    cost_var.set("")
    tax_var.set("")
    to_var.set("")
    total_var.set("")


def iquit():
    iexit = messagebox.askyesno("Quit Sytem!!", "Are You Sure  Quit??")
    if iexit > 0:
        dashboard.destroy()
        return


def iprint():
    if name_var.get() == "" or phone_var.get() == "":
        messagebox.showerror("Error", "All fields must be filled!!")
    else:
        connection = sqlite3.connect("TMS.db")
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Records(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    RefNo TEXT NOT NULL,
                    Name TEXT NOT NULL,
                    PostCode INTEGER NOT NULL,
                    Phone INTEGER NOT NULL,
                    Date TEXT NOT NULL,
                    BusNo TEXT NOT NULL,
                    Driver TEXT NOT NULL,
                    FromW TEXT NOT NULL,
                    ToW TEXT NOT NULL,
                    Total TEXT NOT NULL,
                    Time TEXT NOT NULL  
                    )''')
        insert = "INSERT INTO Records(" \
                 "RefNo," \
                 "Name," \
                 "PostCode," \
                 "Phone," \
                 "Date," \
                 "BusNo," \
                 "Driver," \
                 "FromW," \
                 "ToW," \
                 "Total," \
                 "Time) VALUES(?,?,?,?,?,?,?,?,?,?,?)"
        VAL = (ref_var.get(),
               name_var.get(),
               post_var.get(),
               phone_var.get(),
               date_var.get(),
               bus_var.get(),
               driver_var.get(),
               from_var.get(),
               to_var.get(),
               total_var.get(),
               Current.get()
               )
        cursor.execute(insert, VAL)
        connection.commit()
        display()
        connection.close()
        messagebox.showinfo("Success", "Record saved successfully", parent=dashboard)


def update():
    if records.selection():
        connect = sqlite3.connect('TMS.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Records set"
                       " RefNo=?,"
                       " Name=?,"
                       " PostCode=?, "
                       " Phone=?, "
                       " Date=?, "
                       " BusNo=?, "
                       " Driver=?, "
                       " FromW=?, "
                       " ToW=?, "
                       " Total=? "
                       "WHERE ID=?",(
            ref_var.get(),
            name_var.get(),
            post_var.get(),
            phone_var.get(),
            date_var.get(),
            bus_var.get(),
            driver_var.get(),
            from_var.get(),
            to_var.get(),
            total_var.get(),
            ID
        ))

        connect.commit()
        display()
        connect.close()
        messagebox.showinfo("Success", "Update Successful")
    else:
        messagebox.showerror("ERROR","Please Select the record you want to update")

def delete():
    if records.selection():
        warn = messagebox.askquestion("Delete", "Are you sure to delete this record?",
                                      icon="warning")
        if warn == 'yes':
            connect = sqlite3.connect('TMS.db')
            cursor = connect.cursor()
            cursor.execute("DELETE from Records WHERE ID=%d" % row[0])
            connect.commit()
            display()
            connect.close()
        else:
            display()
    else:
        messagebox.showerror("Error", "Please select a record to delete")

def display():
    connect = sqlite3.connect('TMS.db')
    cursor = connect.cursor()
    cursor.execute("select * from Records")
    row = cursor.fetchall()
    if len(row) != 0:
        records.delete(*records.get_children())
        for i in row:
            records.insert("", END, values=i)
        connect.commit()
    cursor.close()


def get_cursor(ev=""):
    global ID;
    global row;
    cursor_row = records.focus()
    content = records.item(cursor_row)
    row = content["values"]

    ID = row[0]
    ref_var.set(row[1]),
    name_var.set(row[2]),
    post_var.set(row[3]),
    phone_var.set(row[4]),
    date_var.set(row[5])
    bus_var.set(row[6])
    driver_var.set(row[7])
    from_var.set(row[8])
    to_var.set(row[9])
    total_var.set(row[10])

# -------------------------------------label details---------------------------------------

Motto = Label(CDFrame, text="Offering Best & Quality services",
              bd=5, padx=20, bg="darkblue", fg="Orange", font=('Verdana', 18, 'bold'))
Motto.place(x=0, y=5)


Clock = Label(CDFrame, bd=5, padx=20, bg="darkblue", fg="Orange",
              font=('Verdana', 17, 'bold'))
Clock.place(x=490, y=5)

Clock1 = Label(dashboard, bd=5, padx=20, bg="blue", fg="White",
               font=('elephant', 16, 'bold'))
Clock1.place(x=1050, y=10)


def digitalclock():
    Current = time.strftime("%a, %H:%M:%S %p")
    Clock.config(text=Current)
    Clock.after(1000, digitalclock)
digitalclock()


def liveclock():
    Current = time.strftime("%H:%M:%S %p")
    Clock1.config(text=Current)
    Clock1.after(1000,liveclock)
liveclock()

img2 = Label(CDFrame, image=logo, bd=0)
img2.place(x=450, y=50)

date = dt.datetime.now()
format_date = f"{date:%d/%m/%Y}" #f"{date:%a, %d, %b, %Y}"
format_date1 = f"{date:%d %b, %Y}"


# ---------------------------------------Customer details--------------------------------

customerFrame = LabelFrame(CDFrame, text="Customer Details",bd=5, bg="darkblue",
                           fg="Red", font=('Verdana', 14, 'bold'))

customerFrame.place(x=0, y=50, )

RefNo = Label(customerFrame, text="Ref Number  : ", bd=5,
              padx=20, bg="darkblue", fg="Orange",
              font=('Verdana', 14, 'bold'))
RefNo.grid(column=0, row=0, sticky=W)
RefNoEntry = Entry(customerFrame, textvariable=ref_var, bd=2,
                   fg="darkred", font=('Verdana', 12, 'bold'))
refrence_no()
RefNoEntry.configure(state="readonly")
RefNoEntry.grid(column=1, row=0, ipady=4, pady=5)

Name = Label(customerFrame, text="Full Name  : ", bd=5, padx=20,
             bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Name.grid(column=0, row=1, sticky=W)
NameEntry = Entry(customerFrame, bd=2, textvariable=name_var,
                  fg="darkred", font=('Verdana', 12, 'bold'))
NameEntry.grid(column=1, row=1, ipady=4, pady=5)

Post = Label(customerFrame, text="Post Code : ", bd=5,
             padx=20, bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Post.grid(column=0, row=2, sticky=W)
PostEntry = Entry(customerFrame, bd=2, textvariable=post_var,
                  fg="darkred", font=('Verdana', 12, 'bold'))
PostEntry.grid(column=1, row=2, ipady=4, pady=5)

Phone = Label(customerFrame, text="Phone : ", bd=5, padx=20,
              bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Phone.grid(column=0, row=3, sticky=W)
PhoneEntry = Entry(customerFrame, bd=2, textvariable=phone_var,
                   fg="darkred", font=('Verdana', 12, 'bold'))
PhoneEntry.grid(column=1, row=3, ipady=4, pady=5)

Date = Label(customerFrame, text="Date : ", bd=5, padx=20,
             bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Date.grid(column=0, row=4, sticky=W)
DateEntry = Entry(customerFrame, bd=2, textvariable=date_var,
                  fg="darkred", font=('Verdana', 12, 'bold'))
DateEntry.insert(END, format_date)
DateEntry.configure(state="readonly")
DateEntry.grid(column=1, row=4, ipady=4, pady=5)

# -----------------------End Of Customer details----------------------------------------

# -----------------------Travel details-------------------------------------------------

travelDFrame = LabelFrame(CDFrame, text="Travel Details", bd=5,
                          bg="darkblue", fg="Red", font=('Verdana', 14, 'bold'))
travelDFrame.place(x=1, y=330)


Bus = Label(travelDFrame, text="Bus Number : ", bd=5, padx=20,
            bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Bus.grid(column=0, row=0, sticky=W)
BusEntry = Entry(travelDFrame, bd=2, textvariable=bus_var,
                 fg="darkred", font=('Verdana', 12, 'bold'))
BusEntry.grid(column=1, row=0, ipady=4, pady=5)

Driver = Label(travelDFrame, text="Driver : ", bd=5, padx=20,
               bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Driver.grid(column=0, row=1, sticky=W)
DriverEntry = Entry(travelDFrame, bd=2, textvariable=driver_var,
                    fg="darkred", font=('Verdana', 12, 'bold'))
DriverEntry.grid(column=1, row=1, ipady=4, pady=5)

From = Label(travelDFrame, text="From : ", bd=5, padx=20,
             bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
From.grid(column=0, row=2, sticky=W)

connection = sqlite3.connect('TMS.db')
cursor = connection.cursor()
cursor.execute("SELECT dest FROM Destinations")
options = cursor.fetchall()

FromEntry = ttk.Combobox(travelDFrame, textvariable=from_var,
                         width=18, font=('Verdana', 12, 'bold'))
FromEntry['value'] = options
FromEntry.current(0)
FromEntry.configure(state="readonly")
FromEntry.grid(column=1, row=2, ipady=4, pady=5)

cursor = connection.cursor()
cursor.execute("SELECT destt FROM Destinations")
options1 = cursor.fetchall()

To = Label(travelDFrame, text="To : ", bd=5, padx=20, bg="darkblue",
           fg="Orange", font=('Verdana', 14, 'bold'))
To.grid(column=0, row=3, sticky=W)
ToEntry = ttk.Combobox(travelDFrame, textvariable=to_var, width=18,
                       font=('Verdana', 12, 'bold'))
ToEntry['value'] = options1
ToEntry.current(0)
ToEntry.configure(state="readonly")
ToEntry.grid(column=1, row=3, ipady=3, pady=5)


Cost = Label(travelDFrame, text="Cost/Person : ", bd=5, padx=20,
             bg="darkblue", fg="Orange", font=('Verdana', 14, 'bold'))
Cost.grid(column=0, row=4, sticky=W)
CostEntry = Entry(travelDFrame, bd=2, textvariable=cost_var,
                  fg="darkred", font=('Verdana', 12, 'bold'))
CostEntry.grid(column=1, row=4, ipady=4, pady=5)

ResetButton = Button(CDFrame, command=reset, text="RESET", bd=3,
                     fg="OrangeRed", bg="Purple", relief=RAISED,
                     font=('Rockwell Extra Bold', 18, "bold"))
ResetButton.place(x=0, y=580)

ExitButton = Button(CDFrame, text="Quit", command=iquit, bd=3, fg="White", bg="Red",
                    relief=RAISED, font=('Rockwell Extra Bold', 18, "bold"))
ExitButton.place(x=150, y=580)

RefreshButton = Button(CDFrame, text="Refresh", command=refresh, bd=3, fg="White",
                       bg="Green", relief=RAISED,
                       font=('Rockwell Extra Bold', 18, "bold"))
RefreshButton.place(x=280, y=580)

# --------------------------------- Totals ---------------------------------------------

totalsFrame = LabelFrame(CDFrame, text="Total", bd=5, bg="darkblue", fg="Red",
                         font=('Verdana', 14, 'bold'))
totalsFrame.place(x=450, y=405, )

taxPaid = Label(totalsFrame, text="TaxPaid: ", bd=5, padx=20, bg="darkblue",
                fg="Orange", font=('Verdana', 14, 'bold'))
taxPaid.grid(column=0, row=1, sticky=W)
taxPaidEntry = Entry(totalsFrame, bd=2, width=11,  textvariable=tax_var,
                     fg="red", bg="Lightblue", font=('Verdana', 14, 'bold'))
taxPaidEntry.grid(column=1, row=1, ipady=4, pady=6)

Total = Label(totalsFrame, text="Total: ", bd=5, padx=20, bg="darkblue",
              fg="Orange", font=('Verdana', 14, 'bold'))
Total.grid(column=0, row=2, sticky=W)
TotalPaidEntry = Entry(totalsFrame, bd=2,  textvariable=total_var, width=11,
                       fg="red", bg="Lightblue", font=('Verdana', 14, 'bold'))
TotalPaidEntry.grid(column=1, row=2, ipady=4, pady=6)

totalButton = Button(totalsFrame, bd=2, width=8, text="TOTAL", fg="red",
                     relief=RAISED, bg="cadetblue",
                     font=('Rockwell Extra Bold', 16, 'bold'))
totalButton.grid(column=1, row=3, ipady=2, pady=4)

printButton = Button(totalsFrame, bd=2, width=8, command=iprint, text="PRINT",
                     fg="Pink", relief=RAISED, bg="cadetblue",
                     font=('Rockwell Extra Bold', 16, 'bold'))
printButton.grid(column=0, row=3, ipady=2, pady=4)

# ---------------------------------End Of Travel details---------------------------------

# ---------------------------------Welcome and date--------------------------------------
welcome = Label(DDFrame, text="WELCOME! Daniel !", pady=2, bg="DarkBlue",
                fg="OrangeRed", font=('Verdana', 18, 'bold'))
welcome.place(x=0, y=5)

welcomeDate = Label(DDFrame, text=format_date1, padx=25, pady=2, bg="DarkBlue",
                    fg="white", font=('Verdana', 18, 'bold'))
welcomeDate.place(x=290, y=5)


# --------------------------------Records Display----------------------------------------

style = ttk.Style(dashboard)
style.configure("Treeview.Heading", font=('verdana', 11,'bold'), foreground="red")
records = ttk.Treeview(DDFrame, height=200,
                       selectmode=BROWSE,
                       columns=('ID',
                                "Ref NO",
                                "Name",
                                "Code",
                                "Phone",
                                "Date",
                                "Bus No",
                                "Driver",
                                "From",
                                "To",
                                "Cost",
                                "Time"))


X_scroller = Scrollbar(records, orient=HORIZONTAL, command=records.xview)
Y_scroller = Scrollbar(records, orient=VERTICAL, command=records.yview)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)

records.configure(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

records.heading('ID', text='ID', anchor=CENTER)
records.heading('Ref NO', text='Ref No', anchor=CENTER)
records.heading('Name', text='Name', anchor=CENTER)
records.heading('Code', text='Code', anchor=CENTER)
records.heading('Phone', text='Phone', anchor=CENTER)
records.heading('Date', text='Date', anchor=CENTER)
records.heading('Bus No', text='Bus No', anchor=CENTER)
records.heading('Driver', text='Driver', anchor=CENTER)
records.heading('From', text='From', anchor=CENTER)
records.heading('To', text='To', anchor=CENTER)
records.heading('Cost', text='Amount', anchor=CENTER)
records.heading('Time', text='Time', anchor=CENTER)

records.column('#0', width=0, stretch=NO)
records.column('#1', width=40, stretch=NO)
records.column('#2', width=100, stretch=NO)
records.column('#3', width=130, stretch=NO)
records.column('#4', width=100, stretch=NO)
records.column('#5', width=150, stretch=NO)
records.column('#6', width=80, stretch=NO)
records.column('#7', width=80, stretch=NO)
records.column('#8', width=180, stretch=NO)
records.column('#9', width=180, stretch=NO)
records.column('#10', width=150, stretch=NO)
records.column('#11', width=150, stretch=NO)

records.place(y=80, relwidth=1.03, relheight=0.8, relx=0)
display()
records.bind("<ButtonRelease-1>", get_cursor)

# ------------------------------Search bar and buuton------------------------------------

SearchEntry = Entry(DDFrame, bd=2, fg="purple", bg="LightBlue",
                    font=('verdana', 16, 'bold'))
SearchEntry.place(x=180, y=49)

SearchButton = Button(DDFrame, text="Search", bd=1, fg="White",
                      bg="Blue", relief=RAISED, font=('verdana', 11, "bold"))
SearchButton.place(x=450, y=48)

SearchSelect = ttk.Combobox(DDFrame, width=18, font=('Verdana', 14, 'bold'))
SearchSelect['value'] = ('Search By:','Nairobi','Kitale', 'Naivasha',
                         'Kisumu', 'Nakuru', 'Mombasa', 'Kisii', 'Kakamenga',
                         'Garrisa', 'Kilifi', 'Meru',  'Kajiado')
SearchSelect.current(0)
SearchSelect.place(x=0, y=49, width=175)

# --------------------------------Record duplication Buttons---------------------------------
DeleteButton = Button(DDFrame, command=delete, text="DELETE RECD", bd=3,
                      fg="White", bg="Red",relief=RAISED,
                      font=('Rockwell Extra Bold', 14, "bold"))
DeleteButton.place(x=0, y=593)

EditButton = Button(DDFrame, command=update, text="UPDATE", bd=3, fg="White", bg="Green",
                    relief=RAISED, font=('Rockwell Extra Bold', 14, "bold"))
EditButton.place(x=200, y=593)

ShowButton = Button(DDFrame, command=display, text="SHOW ALL", bd=3, fg="White",
                    bg="DarkBlue",relief=RAISED,
                    font=('Rockwell Extra Bold', 14, "bold"))
ShowButton.place(x=350, y=593)


dashboard.update()
dashboard.mainloop()
