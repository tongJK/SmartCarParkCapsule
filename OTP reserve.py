''' OTP Reserve , Smart Car Park Project Bt Sinister30n4 '''

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
import MySQLdb
import time
import smbus


# --- Variables Section ------------------------------------------------------------------------------------------------
otp = None
sotp = None
bus = smbus.SMBus(1)
address = 0x04
# --- Function Section -------------------------------------------------------------------------------------------------

def writeNumber(value):
    bus.write_byte(address, value)
    return -1


def take_update(name):

    global otp
    global  sotp
    state = 1

    otp = e1.get()
    name = e1.get()
    e1.delete(0, 'end')

    # database connect section ------------------------------------------------------------------------------------

    # Open database connection
    db = MySQLdb.connect("172.26.0.21", "s5735512160_556", "9OrpLgX6", "s5735512160_556")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT *FROM paymentlist WHERE status = '%s'" % ('success')
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            ridx = row[0]
            uidx = row[1]
            tcx = row[2]
            tbx = row[3]
            sotp = row[4]
            pidx = row[5]

            if (otp == sotp):
                
              state +1
              
              sql1 = "DELETE FROM carstatus WHERE park_id = '%s'" % (pidx)
              cursor.execute(sql1)

              sql2 = "UPDATE user SET park_id = '-' WHERE park_id = '%s'" % (pidx)
              cursor.execute(sql2)

              sq3 = "UPDATE park SET park_status = '%s' WHERE park_id = '%s' " % ('Empty', pidx)
              cursor.execute(sq3)

              messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")
              res = 90

              # I2C section ------------------------------------------------------------------------------------

              data_list = list(chr(res))
              for i in data_list:
                   # Sends to the Slaves
                   writeNumber(ord(i))
                   time.sleep(.1)

            else:
              state = state-1
               

            print("\nOTP from user is %s" % otp)
            print("OTP from server is %s" % sotp)
            

    except:
        print ("Error: unable to fecth data")

            
    if(state < 0):
        messagebox.showerror("Error", "Your OTP is wrong, Please Re-Enter or contact us")
    else:
        state = state
    print ("SOTP DONE!!!")

    
    db.commit()
    db.close()
    


def take_res(namet):

    global otpt
    global  sotpt

    otpt = e2.get()
    namet = e2.get()
    e2.delete(0, 'end')

    # database connect section ------------------------------------------------------------------------------------

    # Open database connection
    db = MySQLdb.connect("172.26.0.21", "s5735512160_556", "9OrpLgX6", "s5735512160_556")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT *FROM reserve WHERE reserve_status = '%s'" % ('success')
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
            sotpt = row[4]
            stx = row[5]

            if (otpt == sotpt):
                
              state = 1
              sql1 = "SELECT *FROM online_reserve WHERE status = '%s'" % ('success')
              try:
                  # Execute the SQL command
                  cursor.execute(sql)
                  # Fetch all the rows in a list of lists.
                  results = cursor.fetchall()
                  for row in results:
                    idx = row[0]
                    ptx = row[1]
                    pex = row[2]
                    pbx = row[3]
                    qtx = row[4]
                    ress = row[5]

              except:
                    print ("Error: unable to fecth data")

              sql2 = "UPDATE online_reserve SET reserve_total = '%s' " % (ress-1)
              cursor.execute(sql2)

              messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")
              res = 90

              # I2C section ------------------------------------------------------------------------------------

              data_list = list(chr(res))
              for i in data_list:
                   # Sends to the Slaves
                   writeNumber(ord(i))
                   time.sleep(.1)

            else:
              state = 0

            print("\nReserve from user is %s" % otpt)
            print("Reserve from server is %s" % sotpt)
            

    except:
        print ("Error: unable to fecth data")

            
    print ("SOTP DONE!!!")

    
    db.commit()
    db.close()
  


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
        #for F in (StartPage, PageOne, PageTwo, PageQR):
        for F in (StartPage, PageOne, PageTwo, PageRes,PageQR):
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
        label = tk.Label(self, text="Welcome !!", fg="hot pink", bg="lightskyblue", font=("Times", 60, "bold italic"))
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
        button2 = tk.Button(self, text="Reservations", bd=15, font=("Times", 70, "bold italic"), bg="mediumspringgreen",
                            command=lambda: controller.show_frame("PageRes"))
        button3 = tk.Button(self, text="Retake Car", bd=15, font=("Times", 70, "bold italic"), bg="coral",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack(pady=(10, 10))
        button2.pack(pady=(10, 10))
        button3.pack(pady=(10, 10))


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
        button.pack(pady=(10, 50))

        button = tk.Button(self, text="Get Smart Car App", font=("Times", 20, "bold"), bd=10, bg="tomato", height=2,
                           width=15, command=show_link)
        button.pack(side=RIGHT)


        button = tk.Button(self, text="Go to the start page", font=("Times", 20, "bold"), bd=10, bg="tomato", height=2,
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
        e1.bind("<Return>", (lambda event: take_update(e1.get())))

        tk.Button(self, text='Submit', font=("Times", 20, "bold italic"), command=take_update,
                  bd=10, bg="limegreen", height=5, width=30).pack(pady=(10, 10))
        tk.Button(self, text='Contact Us', font=("Times", 20, "bold italic"), command=show_contact,
                  bd=10, bg="mediumspringgreen", height=5, width=20).pack(pady=(10, 100))

        button = tk.Button(self, text="Go to the start page", font=("Times", 15, "bold"), bd=10, bg="tomato", height=5,
                           width=30,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageRes(tk.Frame):

    def __init__(self, parent, controller):
        global e2
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Please enter your Reservation Code", bg="lightskyblue", font=("Times", 50, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        e2 = Entry(self, width=20, bd=5, font=("Times", 40, "bold italic"), justify=CENTER)
        e2.pack(pady=(10, 10))
        e2.bind("<Return>", (lambda event: take_res(e2.get())))

        tk.Button(self, text='Submit', font=("Times", 20, "bold italic"), command=take_res,
                  bd=10, bg="limegreen", height=5, width=30).pack(pady=(10, 10))
        tk.Button(self, text='Contact Us', font=("Times", 20, "bold italic"), command=show_contact,
                  bd=10, bg="mediumspringgreen", height=5, width=20).pack(pady=(10, 100))

        button = tk.Button(self, text="Go to the start page", font=("Times", 15, "bold"), bd=10, bg="tomato", height=5,
                           width=30,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageQR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Your QR Code is below", bg="lightskyblue", font=("Times", 50, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="(Scan with Smart Car Park App for register or login)", bg="lightskyblue",
                         font=("Times", 40, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=550, y=300)

        button = tk.Button(self, text="Click when Done", font=("Times", 30, "bold"), bd=10, bg="tomato", height=4,
                           width=20, command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=(450, 10))

# --- Main Section -------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = SampleApp()
    app.title("Smart Car Park.")
    app.mainloop()
