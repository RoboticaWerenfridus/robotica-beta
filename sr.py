import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(8, gpio.OUT)
gpio.setwarnings(False)


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(8, gpio.OUT)

def forward(tf):
    gpio.output(5, True)
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()
    
def left(tf):
    gpio.output(6, True)
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()
    
def right(tf):
    gpio.output(5, True)
    gpio.output(8, True)
    time.sleep(tf)
    gpio.cleanup()
    
def back(tf):
    gpio.output(6, True)
    gpio.output(8, True)
    time.sleep(tf)
    gpio.cleanup()
    
def stop(tf):
    gpio.output(5, False)
    gpio.output(6, False)
    gpio.output(7, False)
    gpio.output(8, False)
    sys.exit()
    time.sleep(tf)
    
def key_input(event):
    init()
    print ('key:'), event.char
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
    else:
        pass

gpio.output(5, False)
gpio.output(6, False)
gpio.output(7, False)
gpio.output(8, False)
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()

