import os
import serial
import time
import json
from threading import Thread

def startRFCOMM():
    os.system("sudo rfcomm watch hci0")

def handleInput():
    while True:
        input = ser.readline()
        print(input)
        
        try:
            json_object = json.loads(input)
            
            for x in json_object['data']:
                speed = x['speed']
                time = x['time']
                dist = x['dist']
                direction = x['dir']
                print (speed + time + dist + direction)
                
        except (ValueError, KeyError, TypeError):
            print("Error")
                
t = Thread(target = startRFCOMM)
t2 = Thread(target = handleInput)
t.start()

while True:
    try:
        ser = serial.Serial("/dev/rfcomm0")
        if ser.isOpen():
            ser.write(b"Connected")
            t2.start()
            break
    except:
        print("Not yet connected")
        time.sleep(1)
