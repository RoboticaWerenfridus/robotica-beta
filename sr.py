import RPi.GPIO as GPIO
import time
import curses

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define motor pins
MOTOR1A = 5
MOTOR1B = 6
MOTOR2A = 16
MOTOR2B = 12

# Set motor pins as outputs
GPIO.setup(MOTOR1A, GPIO.OUT)
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR2A, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)

# Initialize curses for keyboard input
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
stdscr.timeout(100)

# Function to stop motors
def stop_motors():
    GPIO.output(MOTOR1A, False)
    GPIO.output(MOTOR1B, False)
    GPIO.output(MOTOR2A, False)
    GPIO.output(MOTOR2B, False)

# Main loop for reading keyboard inputs
try:
    while True:
        char = stdscr.getch()
        if char == ord('w'):  # Move forward
            GPIO.output(MOTOR1A, True)
            GPIO.output(MOTOR1B, False)
            GPIO.output(MOTOR2A, True)
            GPIO.output(MOTOR2B, False)
        elif char == ord('a'):  # Turn left
            GPIO.output(MOTOR1A, False)
            GPIO.output(MOTOR1B, True)
            GPIO.output(MOTOR2A, True)
            GPIO.output(MOTOR2B, False)
        elif char == ord('s'):  # Move backward
            GPIO.output(MOTOR1A, False)
            GPIO.output(MOTOR1B, True)
            GPIO.output(MOTOR2A, False)
            GPIO.output(MOTOR2B, True)
        elif char == ord('d'):  # Turn right
            GPIO.output(MOTOR1A, True)
            GPIO.output(MOTOR1B, False)
            GPIO.output(MOTOR2A, False)
            GPIO.output(MOTOR2B, True)
        else:  # Stop motors for any other key
            stop_motors()

finally:
    # Clean up GPIO and curses
    stop_motors()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
