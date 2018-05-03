''' OTP Reserve , Smart Car Park Project Bt Sinister30n4 '''

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import MySQLdb
import time


# --- Variables Section ------------------------------------------------------------------------------------------------
otp = None
sotp = None
# --- Function Section -------------------------------------------------------------------------------------------------

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def take_update():
    global sotp

    # database connect section ------------------------------------------------------------------------------------

    # Open database connection
    db = MySQLdb.connect("172.26.0.21", "s5735512160_556", "9OrpLgX6", "s5735512160_556")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT *FROM paymentlist WHERE otp = '%s'" % ('Empty')
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            idx = row[0]
            pidx = row[1]
            phx = row[2]
            amtx = row[3]
            sotp = row[4]
            stx = row[5]

            # if (e1.get() == sotp):
            #  messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")

            # else:
            #  messagebox.showerror("Error", "Your OTP is wrong, Please Re-Enter or contact us")

            # print("OTP from server is %s" % sotp)
            if (e1.get() == sotp):
                res = 90

                # I2C section ------------------------------------------------------------------------------------

                data_list = list(chr(res))
                for i in data_list:
                    # Sends to the Slaves
                    writeNumber(ord(i))
                    time.sleep(.1)

            else:
                res = None

    except:
        print ("Error: unable to fecth data")

    db.commit()
    db.close()

def show_entry_fields(name):
    global otp
    global  sotp

    name = e1.get()
    otp = e1.get()
    e1.delete(0, 'end')


    if otp == '1234':
        messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")
        take_update()
    else:
        messagebox.showerror("Error", "Your OTP is wrong, Please Re-Enter or contact us")

def show_contact():
    messagebox.showinfo("Contact Us",
                        "Tel : 0808894575 \nWebsite : www.smartcarpark.com \nE-mail : smartcarpark@hotmail.com")

def show_link():
    messagebox.showinfo("Smart Car App",
                        'Android : https://play.google.com/store/apps/SmartCarParkApp '
                        '\n\n\nIOS : https://www.apple.com/th/ios/app-store/SmartCarParkApp ')



# --- Class Section ----------------------------------------------------------------------------------------------------

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageQR):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Wellcome !!", fg="hot pink", bg="lightskyblue", font=("Times", 60, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        lb2 = tk.Label(self, text="Smart Car Park", fg="hot pink", bg="lightskyblue", font=("Times", 60, "bold italic"))
        lb2.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="1.Park your car in receive slot, lock your car", bg="lightskyblue",
                         font=("Times", 35, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="2.Push a ready button and come back to monitor", bg="lightskyblue",
                         font=("Times", 35, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        lb2 = tk.Label(self, text="@Smart Car Park by sinister_30n4", bg="lightskyblue",
                       font=("Times", 10, "bold italic"))
        lb2.pack(side="bottom")


        button1 = tk.Button(self, text="Car Deposit", bd=15, font=("Times", 70, "bold italic"), bg="dodgerblue",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Retake Car", bd=15, font=("Times", 70, "bold italic"), bg="coral",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack(pady=(10, 10))
        button2.pack(pady=(10, 10))


class PageOne(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Car Deposit", bg="lightskyblue", font=("Times", 60, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="Direction", bg="lightskyblue", font=("Times", 60, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="1.Install Smart Car Park & Scanner application", bg="lightskyblue", font=("Times", 30, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="2.click 'Get QR Code' button and wait a moment", bg="lightskyblue", font=("Times", 30, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="3.Scan QR Code with Smart Car Park", bg="lightskyblue", font=("Times", 30, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Get QR Code", bd=15, font=("Times", 60, "bold italic"), bg="dodgerblue",
                            command=lambda: time.sleep(10) & controller.show_frame("PageQR"))
        button.pack(pady=(10, 10))

        button = tk.Button(self, text="Get Smart Car App", font=("Times", 15, "bold"), bd=10, bg="tomato", height=2,
                           width=15, command=show_link)
        button.pack(side=RIGHT)


        button = tk.Button(self, text="Go to the start page", font=("Times", 15, "bold"), bd=10, bg="tomato", height=2,
                           width=15, command=lambda:controller.show_frame("StartPage"))
        button.pack(side=RIGHT)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        global e1
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Please enter your OTP number", bg="lightskyblue", font=("Times", 50, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        e1 = Entry(self, width=20, bd=5, font=("Times", 40, "bold italic"), justify=CENTER)
        e1.pack(pady=(10, 10))
        e1.bind("<Return>", (lambda event: show_entry_fields(e1.get())))

        tk.Button(self, text='Submit', font=("Times", 15, "bold italic"), command=show_entry_fields,
                  bd=10, bg="limegreen", height=5, width=30).pack(pady=(10, 10))
        tk.Button(self, text='Contact Us', font=("Times", 15, "bold italic"), command=show_contact,
                  bd=10, bg="mediumspringgreen", height=5, width=20).pack(pady=(10, 100))

        button = tk.Button(self, text="Go to the start page", font=("Times", 10, "bold"), bd=10, bg="tomato", height=5,
                           width=30,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageQR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Your QR Code is below", bg="lightskyblue", font=("Times", 40, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="(Scan with Smart Car Park App for register or login)", bg="lightskyblue",
                         font=("Times", 30, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=300, y=200)

        button = tk.Button(self, text="Click when Done", font=("Times", 20, "bold"), bd=10, bg="tomato", height=5,
                           width=20, command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=(450, 10))

# --- Main Section -------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = SampleApp()
    app.title("Smart Car Park.")
    app.mainloop()
