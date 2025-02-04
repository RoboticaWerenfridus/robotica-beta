import socket
import json
import RPi.GPIO as gpio

# Server details
SERVER_IP = "reddot.roboticawerenfridus.nl"
SERVER_PORT = 6026
USERNAME = "robot1"
PASSWORD = "password123"

# GPIO setup
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)  # Motor 1 forward
gpio.setup(18, gpio.OUT)  # Motor 1 backward
gpio.setup(22, gpio.OUT)  # Motor 2 forward
gpio.setup(23, gpio.OUT)  # Motor 2 backward
gpio.setwarnings(False)

# Configure PWM for smooth movement
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

def move(x, y):
    """
    Convert x and y coordinates from the red dot into PWM values for motor movement.
    - Pushing up (y > 0) moves both motors forward.
    - Pulling down (y < 0) moves both motors backward.
    - Moving right (x > 0) turns the robot right (left motor moves forward, right motor moves backward).
    - Moving left (x < 0) turns the robot left (right motor moves forward, left motor moves backward).
    """
    speed = abs(y) * 100  # Convert y-axis movement into speed (0-100%)

    if y > 0:  # Forward
        set_motor_speed(motor1_forward_pwm, speed)
        set_motor_speed(motor2_forward_pwm, speed)
        set_motor_speed(motor1_backward_pwm, 0)
        set_motor_speed(motor2_backward_pwm, 0)
    elif y < 0:  # Backward
        set_motor_speed(motor1_backward_pwm, speed)
        set_motor_speed(motor2_backward_pwm, speed)
        set_motor_speed(motor1_forward_pwm, 0)
        set_motor_speed(motor2_forward_pwm, 0)
    elif x > 0:  # Right turn
        set_motor_speed(motor1_forward_pwm, speed)
        set_motor_speed(motor2_backward_pwm, speed)
        set_motor_speed(motor1_backward_pwm, 0)
        set_motor_speed(motor2_forward_pwm, 0)
    elif x < 0:  # Left turn
        set_motor_speed(motor2_forward_pwm, speed)
        set_motor_speed(motor1_backward_pwm, speed)
        set_motor_speed(motor1_forward_pwm, 0)
        set_motor_speed(motor2_backward_pwm, 0)
    else:  # Stop when no input
        set_motor_speed(motor1_forward_pwm, 0)
        set_motor_speed(motor1_backward_pwm, 0)
        set_motor_speed(motor2_forward_pwm, 0)
        set_motor_speed(motor2_backward_pwm, 0)

try:
    # Connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    # Send authentication data
    auth_data = json.dumps({"username": USERNAME, "password": PASSWORD})
    client.send(auth_data.encode())

    while True:
        # Receive movement command
        data = client.recv(1024).decode()
        if not data:
            break
        movement = json.loads(data)
        move(movement["x"], movement["y"])

except Exception as e:
    print(f"Connection error: {e}")
finally:
    client.close()
    gpio.cleanup()
