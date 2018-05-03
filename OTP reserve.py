from tkinter import *
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import messagebox
import time

# --- Variables Section ------------------------------------------------------------------------------------------------

# --- Function Section -------------------------------------------------------------------------------------------------

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def take_update():
    print("OTP is %s" % e1.get())

def show_entry_fields():
    if otp == '1234':
        messagebox.showinfo("Contact Us", "Your OTP is Accept\nClick OK to continue.")
        take_update()
    else:
        messagebox.showerror("Error", "Your OTP is wrong, Please Re-Enter or contact us")
        print("OTP is %s" % e1.get)

def show_contact():
    messagebox.showinfo("Contact Us",
                        "Tel : 0808894575 \nWebsite : www.smartcarpark.com \nE-mail : tong_ueki@hotmail.com")

def show_qr():
    # time.sleep(30)
    messagebox.showinfo("QR Code",
                        "Your QR Code is :\nScan to see your car details.")

    logo = PhotoImage(file="C:\Users\Tong\Desktop\default_qrcode.png")
    w2 = Label(root, image=logo).grid(row=0, column=1)
    explanation = """Team Geo Zoner"""
    w2 = Label(root, compound=CENTER, fg="Red", bg="black", font="Times 55 bold", text=explanation)
    w2.grid(row=0, column=0)

    mainloop()

# --- Class Section -------------------------------------------------------------------------------------------------

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
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
        tk.Frame.__init__(self, parent, bg="mediumspringgreen")
        self.controller = controller
        label = tk.Label(self, text="Wellcome !!", fg="hot pink", bg="mediumspringgreen", font=("Times", 80, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        lb2 = tk.Label(self, text="Smart Car Park", fg="hot pink", bg="mediumspringgreen", font=("Times", 80, "bold italic"))
        lb2.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="1.Park your car in receive slot, lock your car", bg="mediumspringgreen",
                         font=("Times", 35, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="2.Push a ready button and come back to monitor", bg="mediumspringgreen",
                         font=("Times", 35, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        lb2 = tk.Label(self, text="@Smart Car Park by sinister_30n4", bg="mediumspringgreen",
                       font=("Times", 10, "bold italic"))
        lb2.pack(side="bottom")

        button1 = tk.Button(self, text="Car Deposit", bd=15, font=("Times", 100, "bold italic"), bg="dodgerblue",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Retake Car", bd=15, font=("Times", 100, "bold italic"), bg="coral",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack(pady=(10, 10))
        button2.pack(pady=(10, 10))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Car Deposit", bg="lightskyblue", font=("Times", 100, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="Direction", bg="lightskyblue", font=("Times", 80, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="1.Install Smart Car Park & Scanner application", bg="lightskyblue", font=("Times", 40, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="2.click OK", bg="lightskyblue", font=("Times", 40, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="3.Scan QR Code with Smart Car Park", bg="lightskyblue", font=("Times", 40, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="OK", font=("Times", 15, "bold"), bd=10, bg="tomato", height=3,
                           width=15, command=show_qr)
        button.pack(pady=(10, 10))

        button = tk.Button(self, text="Go to the start page", font=("Times", 15, "bold"), bd=10, bg="tomato", height=3,
                           width=15, command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightskyblue")
        self.controller = controller
        label = tk.Label(self, text="Please enter your OTP number", bg="salmon", font=("Times", 80, "bold italic"))
        label.pack(side="top", fill="x", pady=10)

        e1 = Entry(self, width=20, bd=5, font=("Times", 50, "bold italic"), justify=CENTER)
        e1.pack(pady=(10, 10))

        tk.Button(self, text='Submit', font=("Times", 20, "bold italic"), command= show_entry_fields,
                           bd=10, bg="limegreen", height=5, width=30).pack(pady=(10, 10))
        tk.Button(self, text='Contact Us', font=("Times", 20, "bold italic"), command=show_contact,
                           bd=10, bg="mediumspringgreen",height=5, width=30).pack(pady=(10, 100))

        button = tk.Button(self, text="Go to the start page", font=("Times", 15, "bold"), bd=10, bg="tomato",height=5, width=30,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


# --- Main Section -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app = SampleApp()
    app.title("Smart Car Park.")
    app.mainloop()
