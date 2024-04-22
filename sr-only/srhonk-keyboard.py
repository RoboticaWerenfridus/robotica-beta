import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(4, gpio.OUT)  # Setup GPIO pin 4 for the horn
gpio.setwarnings(False)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(4, gpio.OUT)

def forward(tf):
    gpio.output(17, True)
    gpio.output(18, False)
    gpio.output(22, True)
    gpio.output(23, False)
    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    gpio.output(17, False)
    gpio.output(18, True)
    gpio.output(22, True)
    gpio.output(23, False)
    time.sleep(tf)
    gpio.cleanup()

def right(tf):
    gpio.output(17, True)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(23, True)
    time.sleep(tf)
    gpio.cleanup()

def back(tf):
    gpio.output(17, False)
    gpio.output(18, True)
    gpio.output(22, False)
    gpio.output(23, True)
    time.sleep(tf)
    gpio.cleanup()

def stop(tf):
    gpio.output(17, False)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(4, False)  # Make sure the horn is turned off
    time.sleep(tf)
    sys.exit()

def horn_on():
    gpio.output(4, True)

def horn_off():
    gpio.output(4, False)

def key_input(event):
    init()
    print('key:', event.char)
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)
    elif key_press.lower() == 'q':
        stop(sleep_time)
    elif key_press.lower() == 's':
        back(sleep_time)
    elif key_press.lower() == 't':
        # You can add code for the 'toenter' function here
        pass
    elif key_press.lower() == 'h':
        horn_on()  # Turn on the horn
    elif key_press.lower() == 'j':
        horn_off()  # Turn off the horn
    else:
        pass

gpio.output(17, False)
gpio.output(18, False)
gpio.output(22, False)
gpio.output(23, False)
gpio.output(4, False)  # Make sure the horn is initially off
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
