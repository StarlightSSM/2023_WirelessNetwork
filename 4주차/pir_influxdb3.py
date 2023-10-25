#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
import requests
from influxdb import InfluxDBClient as influxdb
import serial

# Initialize GPIO and PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

# Set up serial communication
brate = 9600  # Baud rate for serial communication
seri = serial.Serial('/dev/ttyS0', baudrate=brate, timeout=None)
print(seri.name)


def interrupt_fired(channel):
    print("interrupt Fired")
    a = 5
    data = [{
        'measurement': 'pir',
        'tags': {
            'VisionUni': '2410',
        },
        'fields': {
            'pir': a,
        }
    }]
    client = None
    try:
        client = influxdb('localhost', 8086, 'root', 'root', 'pir')
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


# Add GPIO event detection
GPIO.add_event_detect(14, GPIO.FALLING, callback=interrupt_fired)

while True:
    time.sleep(1)
    a = 1
    data = [{
        'measurement': 'pir',
        'tags': {
            'VisionUni': '2410',
        },
        'fields': {
            'pir': a,
        }
    }]

    # Read data from serial communication
    if seri.in_waiting != 0:
        content = seri.readline()
        print(content[:-2].decode())
        a = 0

    # Send data to InfluxDB
    client = None
    try:
        client = influxdb('localhost', 8086, 'root', 'root', 'pir')
    except Exception as e:
        print("Exception" + str(e))

    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print("running influxdb OK")
