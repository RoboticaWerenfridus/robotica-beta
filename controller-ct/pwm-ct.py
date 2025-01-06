import RPi.GPIO as gpio
import time
import sys
import pygame

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)  # Motor 1 forward
gpio.setup(18, gpio.OUT)  # Motor 1 backward
gpio.setup(22, gpio.OUT)  # Motor 2 forward
gpio.setup(23, gpio.OUT)  # Motor 2 backward
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
button_actions = {
    0: "X",  # X button
    3: "Triangle",  # Triangle button
    1: "Circle",  # Circle button
    2: "Square",  # Square button
}

def handle_button_action(button_id):
    # Leave button actions empty (no motor control for buttons)
    action = button_actions.get(button_id)
    if action:
        print(f"Button {action} pressed!")
        # No specific actions for buttons are defined here

# Start the main loop
try:
    while True:
        pygame.event.pump()  # Update the joystick events
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

        # Check if any button is pressed
        for button_id in range(4):  # Only check X, Circle, Square, Triangle buttons
            if joystick.get_button(button_id):
                handle_button_action(button_id)
        
        time.sleep(0.05)

except KeyboardInterrupt:
    stop_motors()
    joystick.quit()
    pygame.quit()
    sys.exit()
