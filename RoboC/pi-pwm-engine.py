import RPi.GPIO as gpio
import time
import sys
import pygame

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.setwarnings(False)

motor1_forward_pwm = gpio.PWM(17, 100)
motor1_backward_pwm = gpio.PWM(18, 100)
motor2_forward_pwm = gpio.PWM(22, 100)
motor2_backward_pwm = gpio.PWM(23, 100)

motor1_forward_pwm.start(0)
motor1_backward_pwm.start(0)
motor2_forward_pwm.start(0)
motor2_backward_pwm.start(0)

def set_motor_speed(motor_pwm, speed_percent):
    motor_pwm.ChangeDutyCycle(speed_percent)

def stop_motors():
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor1_backward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)
    set_motor_speed(motor2_backward_pwm, 0)

def button_L_1():
    print("Joystick button left!")
def button_L_2():
def button_L_3():
def button_R_1():
def button_R_2():
def button_R_3():

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

max_speed = 100

try:
    while True:
        #setup information like battery, controller type, axes, etc.
        draw_text("Controllers: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)
        for joystick in joysticks:
            draw_text("Battery Level: " + str(joystick.get_power_level()), font, pygame.Color("azure"), 10, 35)
            draw_text("Controller Type: " + str(joystick.get_name()), font, pygame.Color("azure"), 10, 60)
            draw_text("Number of axes: " + str(joystick.get_numaxes()), font, pygame.Color("azure"), 10, 85)
        #detect button press on any of the buttons
        for joystick in joysticks:
            if joystick.get_button(7):
                button_L_1()
        pygame.event.pump()
        
        #move motors with PWM setup using joystick input
        axis_x = joystick.get_axis(0)  # Get X-axis value of joystick
        axis_y = -joystick.get_axis(1)  # Get Y-axis value of joystick and invert
        
        speed_motor1 = int(axis_y * max_speed) + int(axis_x * max_speed)
        speed_motor2 = int(axis_y * max_speed) - int(axis_x * max_speed)
        
        # Map motor speeds to valid duty cycle range
        speed_motor1_dc = max(0, min(abs(speed_motor1), 100))  # Limit to 0-100
        speed_motor2_dc = max(0, min(abs(speed_motor2), 100))  # Limit to 0-100
        
        if speed_motor1 > 0:
            set_motor_speed(motor1_forward_pwm, speed_motor1_dc)
            set_motor_speed(motor1_backward_pwm, 0)
        else:
            set_motor_speed(motor1_forward_pwm, 0)
            set_motor_speed(motor1_backward_pwm, speed_motor1_dc)
            
        if speed_motor2 > 0:
            set_motor_speed(motor2_forward_pwm, speed_motor2_dc)
            set_motor_speed(motor2_backward_pwm, 0)
        else:
            set_motor_speed(motor2_forward_pwm, 0)
            set_motor_speed(motor2_backward_pwm, speed_motor2_dc)
        
        time.sleep(0.05)

except KeyboardInterrupt:
    stop_motors()
    joystick.quit()
    pygame.quit()
    sys.exit()
