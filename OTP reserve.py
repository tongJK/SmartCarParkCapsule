''' OTP Reserve , Smart Car Park Project Bt Sinister30n4 '''

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
from picamera import PiCamera
from time import sleep
import tkinter as tk
import MySQLdb
import time
import smbus


# --- Variables Section ------------------------------------------------------------------------------------------------
otp = None
sotp = None
bus = smbus.SMBus(1)
address = 0x04
camera = PiCamera()
filename = ''
# --- Function Section -------------------------------------------------------------------------------------------------

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def take_photo():
    global filename
    filename = ('%s.PNG' % (picname))
    #filename = datetime.now().strftime('%Y-%m-%d %H:%M:%S.jpg')
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/home/pi/SCPpic/{0}".format(filename))
    camera.stop_preview()

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
            pidx = row[1]
            tcx = row[2]
            tbx = row[3]
            sotp = row[4]
            uidx = row[5]


            if (otp == sotp):
                
              state + 1
              
              sql1 = "DELETE FROM carstatus WHERE park_id = '%s'" % (pidx)
              cursor.execute(sql1)

              sql2 = "UPDATE user SET park_id = '-' WHERE park_id = '%s'" % (pidx)
              cursor.execute(sql2)

              sql3 = "UPDATE park SET park_status = '%s' WHERE park_id = '%s' " % ('Empty', pidx)
              cursor.execute(sql3)

              sql4 = "DELETE FROM payment WHERE park_id = '%s'" % (pidx)
              cursor.execute(sql4)

              sql5 = "DELETE FROM paymentlist WHERE park_id = '%s'" % (pidx)
              cursor.execute(sql5)

              messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")


              print ("park_id=%s " % \
                    (pidx))

              if (pidx == 'A01') :
                   floor = 51
              elif (pidx == 'A02') :
                   floor = 52
              elif (pidx == 'A03') :
                   floor = 53
              elif (pidx == 'A04') :
                   floor = 54
              elif (pidx == 'A05') :
                   floor = 55
              elif (pidx == 'A06') :
                   floor = 56
              elif (pidx == 'A07') :
                   floor = 57
              elif (pidx == 'A08') :
                   floor = 58
              elif (pidx == 'B01') :
                   floor = 61
              elif (pidx == 'B02') :
                   floor = 62
              elif (pidx == 'B03') :
                   floor = 63
              elif (pidx == 'B04') :
                   floor = 64
              elif (pidx == 'B05') :
                   floor = 65
              elif (pidx == 'B06') :
                   floor = 66
              elif (pidx == 'B07') :
                   floor = 67
              elif (pidx == 'B08') :
                   floor = 68
              elif (pidx == 'C01') :
                   floor = 71
              elif (pidx == 'C02') :
                   floor = 72
              elif (pidx == 'C03') :
                   floor = 73
              elif (pidx == 'C04') :
                   floor = 74
              elif (pidx == 'C05') :
                   floor = 75
              elif (pidx == 'C06') :
                   floor = 76
              elif (pidx == 'C07') :
                   floor = 77
              elif (pidx == 'C08') :
                   floor = 78
              elif (pidx == 'D01') :
                   floor = 81
              elif (pidx == 'D02') :
                   floor = 82
              elif (pidx == 'D03') :
                   floor = 83
              elif (pidx == 'D04') :
                   floor = 84
              elif (pidx == 'D05') :
                   floor = 85
              elif (pidx == 'D06') :
                   floor = 86
              elif (pidx == 'D07') :
                   floor = 87
              elif (pidx == 'D08') :
                   floor = 88
                               
              else :
                   floor = None 
                           

              if (floor == None) :
                  print ("Sorry, Our park is FULL!!!")
              else :
                  frr = floor/10
                  sll = floor%10
                  print ("Floor : %d Slot : %d " % \
                     (frr,sll))

              # I2C section ------------------------------------------------------------------------------------

              data_list = list(chr(floor))
              
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
    print(" ---------------------------------------- ")

    
    db.commit()
    db.close()
    


def take_res(namet):

    global otpt
    global sotpt
    global picname

    otpt = e2.get()
    namet = e2.get()
    e2.delete(0, 'end')

    # database connect section ------------------------------------------------------------------------------------

    # Open database connection
    db = MySQLdb.connect("172.26.0.21", "s5735512160_556", "9OrpLgX6", "s5735512160_556")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql6 = "SELECT *FROM reserve WHERE reserve_status = '%s'" % ('success')
    try:
        # Execute the SQL command
        cursor.execute(sql6)
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
              sql1 = "SELECT *FROM online_reserve " 
              try:
                  # Execute the SQL command
                  cursor.execute(sql1)
                  # Fetch all the rows in a list of lists.
                  resultsi = cursor.fetchall()
                  for rowi in resultsi:
                    idxi = rowi[0]
                    ptxi = rowi[1]
                    pexi = rowi[2]
                    pbxi = rowi[3]
                    qtxi = rowi[4]
                    ress = rowi[5]

                    sql7 = "SELECT *FROM park WHERE park_status = '%s'" % ('Empty')
                    try:
                       # Execute the SQL command
                       cursor.execute(sql7)
                       # Fetch all the rows in a list of lists.
                       resultsy = cursor.fetchall()
                       for rowy in resultsy:
                          park_id = rowy[0]
                          park_status = rowy[1]
                      
                    except:
                       print ("Error: unable to fecth data")

                    print ("park_id=%s --- park_status = %s" % \
                                (park_id,park_status))

                    if (park_id == 'A01') :
                               floor = 11
                    elif (park_id == 'A02') :
                               floor = 12
                    elif (park_id == 'A03') :
                               floor = 13
                    elif (park_id == 'A04') :
                               floor = 14
                    elif (park_id == 'A05') :
                               floor = 15
                    elif (park_id == 'A06') :
                               floor = 16
                    elif (park_id == 'A07') :
                               floor = 17
                    elif (park_id == 'A08') :
                               floor = 18
                    elif (park_id == 'B01') :
                               floor = 21
                    elif (park_id == 'B02') :
                               floor = 22
                    elif (park_id == 'B03') :
                               floor = 23
                    elif (park_id == 'B04') :
                               floor = 24
                    elif (park_id == 'B05') :
                               floor = 25
                    elif (park_id == 'B06') :
                               floor = 26
                    elif (park_id == 'B07') :
                               floor = 27
                    elif (park_id == 'B08') :
                               floor = 28
                    elif (park_id == 'C01') :
                               floor = 31
                    elif (park_id == 'C02') :
                               floor = 32
                    elif (park_id == 'C03') :
                               floor = 33
                    elif (park_id == 'C04') :
                               floor = 34
                    elif (park_id == 'C05') :
                               floor = 35
                    elif (park_id == 'C06') :
                               floor = 36
                    elif (park_id == 'C07') :
                               floor = 37
                    elif (park_id == 'C08') :
                               floor = 38
                    elif (park_id == 'D01') :
                               floor = 41
                    elif (park_id == 'D02') :
                               floor = 42
                    elif (park_id == 'D03') :
                               floor = 43
                    elif (park_id == 'D04') :
                               floor = 44
                    elif (park_id == 'D05') :
                               floor = 45
                    elif (park_id == 'D06') :
                               floor = 46
                    elif (park_id == 'D07') :
                               floor = 47
                    elif (park_id == 'D08') :
                               floor = 48
                               
                    else :
                               floor = None 
                           

                    picname = park_id
                    take_photo()
                    
                    if (floor == None) :
                        print ("Sorry, Our park is FULL!!!")
                    else :
                        frr = floor/10
                        sll = floor%10
                        print ("Floor : %d Slot : %d " % \
                                  (frr,sll))

                        global nowtime
                        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


                        sql8 = "INSERT INTO carstatus(park_id, car_pic, time_in) \
                                 VALUES ('%s', '%s', '%s' )" % \
                       ( park_id, park_id,nowtime)
                        cursor.execute(sql8)

                        sql9 = "INSERT INTO payment(park_id, time_in, amount) \
                                 VALUES ('%s', '%s', %d )" % \
                       ( park_id,nowtime, 0)
                        cursor.execute(sql9)

                        sql10 = "DELETE FROM reserve WHERE otp = '%s'" % (otpt)
                        cursor.execute(sql10)

    
                        print ("Now Slot %s is  = %s" % \
                                    (park_id,'Busy'))
                        

                        data_list = list(chr(floor))
                        for i in data_list:
                            #Sends to the Slaves
                            writeNumber(ord(i))
                            time.sleep(.1)


              except:
                    print ("Error: in inner fecth data ")

              
              messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")

              sql11 = "UPDATE online_reserve SET park_empty = '%s', reserve_total = '%s' " % ((pexi+1),(ress-1))
              cursor.execute(sql11)


            else:
              state = 0
              messagebox.showerror("Error", "Your OTP is wrong, Please Re-Enter or contact us")

            print("\nReserve from user is %s" % otpt)
            print("Reserve from server is %s" % sotpt)
            

    except:
        print ("Error: unable to fecth data")
      
    #take_photo()

    print ("SOTP DONE!!!")
    print(" ---------------------------------------- ")

    
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
        label = tk.Label(self, text="Welcome !!", fg="hot pink", bg="lightskyblue", font=("Times", 70, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        lb2 = tk.Label(self, text="Smart Car Park", fg="hot pink", bg="lightskyblue", font=("Times", 70, "bold italic"))
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


        button1 = tk.Button(self, text="Car Deposit", bd=15, font=("Times", 50, "bold italic"), bg="dodgerblue",
                            command=lambda: controller.show_frame("PageOne"))

        button2 = tk.Button(self, text="Reservations", bd=15, font=("Times", 50, "bold italic"), bg="mediumspringgreen",
                            command=lambda: controller.show_frame("PageRes"))
        button3 = tk.Button(self, text="Retake Car", bd=15, font=("Times", 50, "bold italic"), bg="coral",
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

        button = tk.Button(self, text="Click when Done", font=("Times", 20, "bold"), bd=10, bg="tomato", height=3,
                           width=20, command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=(450, 10))

# --- Main Section -------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = SampleApp()
    app.title("Smart Car Park.")
    app.mainloop()
