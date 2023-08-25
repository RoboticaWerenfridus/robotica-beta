import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)  # Motor 1 forward
gpio.setup(18, gpio.OUT)  # Motor 1 backward
gpio.setup(22, gpio.OUT)  # Motor 2 forward
gpio.setup(23, gpio.OUT)  # Motor 2 backward
gpio.setwarnings(False)

# Configure PWM for both motors
motor1_forward_pwm = gpio.PWM(17, 100)  # Using GPIO 17 for motor 1 forward PWM
motor1_backward_pwm = gpio.PWM(18, 100)  # Using GPIO 18 for motor 1 backward PWM
motor2_forward_pwm = gpio.PWM(22, 100)  # Using GPIO 22 for motor 2 forward PWM
motor2_backward_pwm = gpio.PWM(23, 100)  # Using GPIO 23 for motor 2 backward PWM

motor1_forward_pwm.start(0)  # Start with 0% duty cycle
motor1_backward_pwm.start(0)  # Start with 0% duty cycle
motor2_forward_pwm.start(0)  # Start with 0% duty cycle
motor2_backward_pwm.start(0)  # Start with 0% duty cycle

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(18, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)

def set_motor_speed(motor_pwm, speed_percent):
    motor_pwm.ChangeDutyCycle(speed_percent)

def forward(tf):
    set_motor_speed(motor1_forward_pwm, speed_motor1)
    set_motor_speed(motor2_forward_pwm, speed_motor2)
    time.sleep(tf)
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor1_backward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)
    set_motor_speed(motor2_backward_pwm, 0)

def backward(tf):
    set_motor_speed(motor1_backward_pwm, speed_motor1)
    set_motor_speed(motor2_backward_pwm, speed_motor2)
    time.sleep(tf)
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor1_backward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)
    set_motor_speed(motor2_backward_pwm, 0)

def right(tf):
    set_motor_speed(motor1_forward_pwm, speed_motor1)
    set_motor_speed(motor2_backward_pwm, speed_motor2)
    time.sleep(tf)
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor1_backward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)
    set_motor_speed(motor2_backward_pwm, 0)

def left(tf):
    set_motor_speed(motor1_backward_pwm, speed_motor1)
    set_motor_speed(motor2_forward_pwm, speed_motor2)
    time.sleep(tf)
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor1_backward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)
    set_motor_speed(motor2_backward_pwm, 0)

def stop(tf):
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor1_backward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)
    set_motor_speed(motor2_backward_pwm, 0)
    sys.exit()
    time.sleep(tf)

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
        backward(sleep_time)
    else:
        pass

# Set your desired speeds (1 to 100)
speed_motor1 = 100
speed_motor2 = 98

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
