
import socket
import json
import threading
import RPi.GPIO as gpio
import time

# Robot Motor Setup
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
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

def move_robot(direction):
    if direction == "forward":
        set_motor_speed(motor1_forward_pwm, 100)
        set_motor_speed(motor2_forward_pwm, 100)
    elif direction == "backward":
        set_motor_speed(motor1_backward_pwm, 100)
        set_motor_speed(motor2_backward_pwm, 100)
    elif direction == "left":
        set_motor_speed(motor1_backward_pwm, 100)
        set_motor_speed(motor2_forward_pwm, 100)
    elif direction == "right":
        set_motor_speed(motor1_forward_pwm, 100)
        set_motor_speed(motor2_backward_pwm, 100)
    elif direction == "stop":
        set_motor_speed(motor1_forward_pwm, 0)
        set_motor_speed(motor1_backward_pwm, 0)
        set_motor_speed(motor2_forward_pwm, 0)
        set_motor_speed(motor2_backward_pwm, 0)

def client_connect():
    username = "robot1"
    password = "password123"
    server_ip = "reddot.roboticawerenfridus.nl"
    port = 6026

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, port))
    
    credentials = json.dumps({"username": username, "password": password})
    s.send(credentials.encode())
    response = s.recv(1024).decode()
    print("Server Response:", response)
    
    if response == "Authenticated":
        while True:
            command = s.recv(1024).decode()
            if command:
                print("Command Received:", command)
                move_robot(command)
    s.close()

if __name__ == "__main__":
    client_thread = threading.Thread(target=client_connect)
    client_thread.start()
