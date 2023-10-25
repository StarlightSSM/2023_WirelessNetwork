#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

seri = serial.Serial(8086, baudrate = brate, timeout = None)
print(seri.name)

a = 1
while a:
    if seri.in_waiting != 0:
        content = seri.readline()
        print(content[:-2].decode())
        a = 0

def interrupt_fired(channel):
    print("interrupt Fired")
    a = 5
    data = [{
        'measurement' : 'pir',
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print(a)
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt_fired)

while(True):
    time.sleep(1)
    a = 1
    data = [{
        'measurement' : 'pir',
        'tags':{
            'VisionUni' : '2410',
        },
        'fields':{
            'pir' : a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print ("Exception" + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print("running influxdb OK")