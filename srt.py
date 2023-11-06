print("Nathan Schalkwijk")
print("Lucas Ewalts")
import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(17, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setup(21, gpio.OUT)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(21, gpio.OUT)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)

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
    gpio.output(21, False)
    sys.exit()
    time.sleep(tf)

def toeter(tf):
    gpio.output(21, True)
    time.sleep(tf)
    gpio.cleanup()
    
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
    elif key_press.lower() == 's':
        back(sleep_time)
    elif key_press.lower() == 't':
        toeter(sleep_time)
    else:
        pass

gpio.output(17, False)
gpio.output(18, False)
gpio.output(22, False)
gpio.output(23, False)
gpio.output(21, False)
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
