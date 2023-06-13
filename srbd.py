import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
from bluedot import BlueDot

bd = BlueDot()
 
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setwarnings(False)

init()

def forward(tf):
    gpio.output(17, True)
    gpio.output(18, False)
    gpio.output(22, True)
    gpio.output(23, False)
    time.sleep(tf)
    
def left(tf):
    ggpio.output(17, False)
    gpio.output(18, True)
    gpio.output(22, True)
    gpio.output(23, False)
    time.sleep(tf)
     
def right(tf):
    gpio.output(17, True)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(23, True)
    time.sleep(tf)
    
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
    sys.exit()
    time.sleep(tf)
    
def move(pos):
    init()
    sleep_time = 0.030
    
    if pos.top:
        forward(sleep_time)
    elif pos.left:
        left(sleep_time)
    elif pos.right:
        right(sleep_time)
    elif pos.bottom:
        back(sleep_time)

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setwarnings(False)
    
def stop1():
    init()
    gpio.output(17, False)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(23, False)

gpio.output(17, False)
gpio.output(18, False)
gpio.output(22, False)
gpio.output(23, False)
bd.when_pressed = move
bd.when_released = stop1
command = tk.Tk()
command.mainloop()

        

