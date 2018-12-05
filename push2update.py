#Smart Car Park Capsule By sinister_30N4
#!/usr/bin/python

import MySQLdb
import smbus
import time
from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button


bus = smbus.SMBus(1)
address = 0x04
camera = PiCamera()
button = Button(14)

filename = ''
position = 2
floor = 0
slot = 0

def take_photo():
    global filename
    filename = ('%s.PNG' % (park_id))
    #filename = datetime.now().strftime('%Y-%m-%d %H:%M:%S.jpg')
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/home/pi/SCPpic/{0}".format(filename))
    camera.stop_preview()


def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

def take_update():
    global park_id
    # Open database connection
    db = MySQLdb.connect("172.26.0.21","s5735512160_556","9OrpLgX6","s5735512160_556" )
    #db = MySQLdb.connect("172.0.1.1","s5735512160_556","9OrpLgX6","s5735512160_556" )
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT *FROM park WHERE park_status = '%s'" % ('Empty')
    try:
       # Execute the SQL command
       cursor.execute(sql)
       # Fetch all the rows in a list of lists.
       results = cursor.fetchall()
       for row in results:
          park_id = row[0]
          park_status = row[1]
      
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
           

    if (floor == None) :
        print ("Sorry, Our park is FULL!!!")
    else :
        frr = floor/10
        sll = floor%10
        print ("Floor : %d Slot : %d " % \
                  (frr,sll))

        global nowtime
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        #sql = "UPDATE park SET park_status = '%s' WHERE park_id = '%s' " % ('Busy', park_id)
        #cursor.execute(sql)

        sql1 = "INSERT INTO carstatus(park_id, car_pic, time_in) \
                 VALUES ('%s', '%s', '%s' )" % \
       ( park_id, park_id,nowtime)
        cursor.execute(sql1)

        sql2 = "INSERT INTO payment(park_id, time_in, amount) \
                 VALUES ('%s', '%s', %d )" % \
       ( park_id,nowtime, 0)
        cursor.execute(sql2)

        
        db.commit()


    
        print ("Now Slot %s is  = %s" % \
                    (park_id,'Busy'))
        print(" ---------------------------------------- ")

        db.close()

        data_list = list(chr(floor))
        for i in data_list:
            #Sends to the Slaves
            writeNumber(ord(i))
            time.sleep(.1)


    take_photo()

button.when_pressed = take_update
print ("Ready !!")

while True:  
    sleep (1)
