#Nathan Schalkwijk #lucas Ewalts
import RPi.GPIO as gpio
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

def forward():
    gpio.output(17, True)
    gpio.output(18, False)
    gpio.output(22, True)
    gpio.output(23, False)
    
def left():
    gpio.output(17, False)
    gpio.output(18, True)
    gpio.output(22, True)
    gpio.output(23, False)
     
def right():
    gpio.output(17, True)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(23, True)
    
def back():
    gpio.output(17, False)
    gpio.output(18, True)
    gpio.output(22, False)
    gpio.output(23, True)
    
def stop():
    gpio.output(17, False)
    gpio.output(18, False)
    gpio.output(22, False)
    gpio.output(23, False)
    sys.exit()
    
def move(pos):
    init()
    
    if pos.top:
        forward()
    elif pos.left:
        left()
    elif pos.right:
        right()
    elif pos.bottom:
        back()

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

        

