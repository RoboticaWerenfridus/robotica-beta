import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(8, gpio.OUT)
gpio.setup(9, gpio.OUT)
gpio.setup(10, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)
    
def lf(tf):
    gpio.output(5, True)
    gpio.output(6, True)
    gpio.cleanup()

def lr(tf):
    gpio.output(7, True)
    gpio.output(8, True)
    time.sleep(tf)
    gpio.cleanup()
    
def rf(tf):
    gpio.output(9, True)
    gpio.output(10, True)
    time.sleep(tf)
    gpio.cleanup()
    
def rr(tf):
    gpio.output(11, True)
    gpio.output(12, True)
    time.sleep(tf)
    gpio.cleanup()
    
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(8, gpio.OUT)
    gpio.setup(9, gpio.OUT)
    gpio.setup(10, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(12, gpio.OUT)

def stop(tf):
    gpio.output(5, False)
    gpio.output(6, False)
    gpio.output(7, False)
    gpio.output(8, False)
    gpio.output(9, False)
    gpio.output(10, False)
    gpio.output(11, False)
    gpio.output(12, False)
    sys.exit()
    time.sleep(tf)
    
def key_input(event):
    init()
    print ('key:'), event.char
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == 'w':
        lf(sleep_time)
        rf(sleep_time)
    elif key_press.lower() == 'a':
        lr(sleep_time)
        rf(sleep_time)
    elif key_press.lower() == 's':
        rr(sleep_time)
        lr(sleep_time)
    elif key_press.lower() == 'd':
        rr(sleep_time)
        lf(sleep_time)
    elif key_press.lower() == 'q':
        stop(sleep_time)
    else:
        pass

init()
gpio.output(5, False)
gpio.output(6, False)
gpio.output(7, False)
gpio.output(8, False)
gpio.output(9, False)
gpio.output(10, False)
gpio.output(11, False)
gpio.output(12, False)
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()

