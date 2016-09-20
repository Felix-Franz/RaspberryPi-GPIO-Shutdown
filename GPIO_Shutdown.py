# Written by Felix Franz (20.9.2016)
# Uses Pin 3 and GND Pin (if P3 connected to GND --> Shutdown)
# To change which pin is used: Just change the number behind GPIO_Pin
# Run with python GPIO_Shutdown.py (put this command with path to file in /etc/rc.local to start this automatically after booting)

import RPi.GPIO as GPIO
import time
import os

# Pin, that shoud be connected to GND (Feel free to change it)
GPIO_Pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

input_state = True
while (input_state):
    input_state = GPIO.input(GPIO_Pin)
    time.sleep(0.2)

print('GPIO: Shutting down system...')
time.sleep(1)
os.system("poweroff -p")
