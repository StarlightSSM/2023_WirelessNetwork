#!/usr/bin/python

import time
import RPi.GPIO as GPIO

print GPIO.VERSION

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def interrupt_fired(channel):
    print("interrupt fired")
    print(channel)

GPIO.add_event_detect(4, GPIO.FALLING, callback=interrupt_fired)

while (True):
    time.sleep(1)
    print("Timer Fired")










