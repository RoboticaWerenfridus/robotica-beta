import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(8, gpio.OUT)
    
def lf(tf):
    gpio.output(5, True)
    time.sleep(tf)
    gpio.cleanup()

def lr(tf):
    gpio.output(6, True)
    time.sleep(tf)
    gpio.cleanup()
    
def rf(tf):
    gpio.output(7, True)
    time.sleep(tf)
    gpio.cleanup()
    
def rr(tf):
    gpio.output(8, True)
    time.sleep(tf)
    gpio.cleanup()
    
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)
    gpio.setup(7, gpio.OUT)
    gpio.setup(8, gpio.OUT)

def stop(tf):
    gpio.output(5, False)
    gpio.output(6, False)
    gpio.output(7, False)
    gpio.output(8, False)
    sys.exit()
    time.sleep(tf)
    
def key_input(event):
    init()
    event.char
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
    elif key_press.lower() == '<escape>':
        stop(sleep_time)
    else:
        pass

init()
gpio.output(5, False)
gpio.output(6, False)
gpio.output(7, False)
gpio.output(8, False)
command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()

