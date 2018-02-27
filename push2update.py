#Smart Car Park Capsule By sinister_30N4
#!/usr/bin/python

import MySQLdb
from picamera import PiCamera
from datetime import datetime
from time import sleep
from gpiozero import Button

camera = PiCamera()
button = Button(14)

flag = 0
filename = ''

def take_photo():
    global filename
    filename = datetime.now().strftime('%Y-%m-%d %H:%M:%S.jpg')
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture("/home/pi/SCPpic/{0}".format(filename))
    camera.stop_preview()
    print("Old Flag = ",flag)
    print("Now flag = ",flag + 1)
    take_update()


def take_update():
    # Open database connection
    db = MySQLdb.connect("172.26.0.21","s5735512160_556","9OrpLgX6","s5735512160_556" )

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
               position = 11
    elif (park_id == 'A02') :
               position = 12
    elif (park_id == 'A03') :
               position = 13
    elif (park_id == 'A04') :
               position = 14
    elif (park_id == 'A05') :
               position = 15
    elif (park_id == 'A06') :
               position = 16
    elif (park_id == 'A07') :
               position = 17
    elif (park_id == 'A08') :
               position = 18
    elif (park_id == 'B01') :
               position = 21
    elif (park_id == 'B02') :
               position = 22
    elif (park_id == 'B03') :
               position = 23
    elif (park_id == 'B04') :
               position = 24
    elif (park_id == 'B05') :
               position = 25
    elif (park_id == 'B06') :
               position = 26
    elif (park_id == 'B07') :
               position = 27
    elif (park_id == 'B08') :
               position = 28
    elif (park_id == 'C01') :
               position = 31
    elif (park_id == 'C02') :
               position = 32
    elif (park_id == 'C03') :
               position = 33
    elif (park_id == 'C04') :
               position = 34
    elif (park_id == 'C05') :
               position = 35
    elif (park_id == 'C06') :
               position = 36
    elif (park_id == 'C07') :
               position = 37
    elif (park_id == 'C08') :
               position = 38
    elif (park_id == 'D01') :
               position = 41
    elif (park_id == 'D02') :
               position = 42
    elif (park_id == 'D03') :
               position = 43
    elif (park_id == 'D04') :
               position = 44
    elif (park_id == 'D05') :
               position = 45
    elif (park_id == 'D06') :
               position = 46
    elif (park_id == 'D07') :
               position = 47
    elif (park_id == 'D08') :
               position = 48
           
    print ("position = %d" % \
                  (position))


    sql = "UPDATE park SET park_status = '%s' WHERE park_id = '%s' " % ('Busy', park_id)
    cursor.execute(sql)
    db.commit()
    
    print ("Now Slot %s is  = %s" % \
                (park_id,'Busy'))

    db.close()


button.when_pressed = take_photo
flag = 0

