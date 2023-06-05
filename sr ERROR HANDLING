import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

def init():
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(17, gpio.OUT)
        gpio.setup(18, gpio.OUT)
        gpio.setup(22, gpio.OUT)
        gpio.setup(23, gpio.OUT)
    except gpio.GPIOError as e:
        print("Error initializing GPIO:", e)
        sys.exit(1)

def forward(tf):
    try:
        gpio.output(17, True)
        gpio.output(18, False)
        gpio.output(22, True)
        gpio.output(23, False)
        time.sleep(tf)
        gpio.cleanup()
    except gpio.GPIOError as e:
        print("Error controlling motors:", e)
        gpio.cleanup()
        sys.exit(1)
    
def left(tf):
    try:
        gpio.output(17, False)
        gpio.output(18, True)
        gpio.output(22, True)
        gpio.output(23, False)
        time.sleep(tf)
        gpio.cleanup()
    except gpio.GPIOError as e:
        print("Error controlling motors:", e)
        gpio.cleanup()
        sys.exit(1)
    
def right(tf):
    try:
        gpio.output(17, True)
        gpio.output(18, False)
        gpio.output(22, False)
        gpio.output(23, True)
        time.sleep(tf)
        gpio.cleanup()
    except gpio.GPIOError as e:
        print("Error controlling motors:", e)
        gpio.cleanup()
        sys.exit(1)
    
def back(tf):
    try:
        gpio.output(17, False)
        gpio.output(18, True)
        gpio.output(22, False)
        gpio.output(23, True)
        time.sleep(tf)
        gpio.cleanup()
    except gpio.GPIOError as e:
        print("Error controlling motors:", e)
        gpio.cleanup()
        sys.exit(1)
    
def stop(tf):
    try:
        gpio.output(17, False)
        gpio.output(18, False)
        gpio.output(22, False)
        gpio.output(23, False)
        time.sleep(tf)
        gpio.cleanup()
        sys.exit()
    except gpio.GPIOError as e:
        print("Error controlling motors:", e)
        gpio.cleanup()
        sys.exit(1)
    
def key_input(event):
    init()
    print('key:', event.char)
    key_press = event.char
    sleep_time = 0.030
    
    try:
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
        else:
            pass
    except Exception as e:
        print("Error:", e)
        gpio.cleanup()

try:
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    
    command = tk.Tk()
    command.bind('<KeyPress>', key_input)
    command.mainloop()
    
except gpio.GPIOError as e:
    print("GPIO error:", e)
    sys.exit(1)
except tk.TclError as e:
    print("Tkinter error:", e)
    sys.exit(1)
except Exception as e:
    print("Error:", e)
   
