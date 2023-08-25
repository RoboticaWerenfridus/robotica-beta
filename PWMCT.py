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

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

max_speed = 100

try:
    while True:
        pygame.event.pump()
        axis_x = joystick.get_axis(0)  # Get X-axis value of joystick
        axis_y = joystick.get_axis(1)  # Get Y-axis value of joystick
        
        speed_motor1 = int(axis_y * max_speed)  # Calculate speed for motor 1
        speed_motor2 = int(axis_y * max_speed)  # Calculate speed for motor 2
        speed_motor1 += int(axis_x * max_speed)  # Adjust motor 1 speed based on X-axis
        speed_motor2 -= int(axis_x * max_speed)  # Adjust motor 2 speed based on X-axis
        
        # Apply motor speed limits
        speed_motor1 = max(-max_speed, min(speed_motor1, max_speed))
        speed_motor2 = max(-max_speed, min(speed_motor2, max_speed))
        
        if abs(axis_x) > 0.1 or abs(axis_y) > 0.1:
            set_motor_speed(motor1_forward_pwm, speed_motor1)
            set_motor_speed(motor1_backward_pwm, 0)
            set_motor_speed(motor2_forward_pwm, speed_motor2)
            set_motor_speed(motor2_backward_pwm, 0)
        else:
            stop_motors()
        
        time.sleep(0.05)

except KeyboardInterrupt:
    stop_motors()
    joystick.quit()
    pygame.quit()
    sys.exit()
