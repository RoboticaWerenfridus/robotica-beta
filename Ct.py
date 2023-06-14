import RPi.GPIO as gpio

import sys

import pygame

gpio.setwarnings(False)

# Define the GPIO pins for motor control

pin1 = 17

pin2 = 18

pin3 = 22

pin4 = 23

# Initialize the GPIO pins

gpio.setmode(gpio.BCM)

gpio.setup(pin1, gpio.OUT)

gpio.setup(pin2, gpio.OUT)

gpio.setup(pin3, gpio.OUT)

gpio.setup(pin4, gpio.OUT)

def stop():

    gpio.output(pin1, False)

    gpio.output(pin2, False)

    gpio.output(pin3, False)

    gpio.output(pin4, False)

def move(joystick):

    # Get the joystick values

    x_axis = joystick.get_axis(0)

    y_axis = joystick.get_axis(1)

    # Determine the direction based on joystick values

    if y_axis < -0.5:

        # Move forward

        gpio.output(pin1, True)

        gpio.output(pin2, False)

        gpio.output(pin3, True)

        gpio.output(pin4, False)

    elif y_axis > 0.5:

        # Move backward

        gpio.output(pin1, False)

        gpio.output(pin2, True)

        gpio.output(pin3, False)

        gpio.output(pin4, True)

    elif x_axis < -0.5:

        # Turn left

        gpio.output(pin1, False)

        gpio.output(pin2, True)

        gpio.output(pin3, True)

        gpio.output(pin4, False)

    elif x_axis > 0.5:

        # Turn right

        gpio.output(pin1, True)

        gpio.output(pin2, False)

        gpio.output(pin3, False)

        gpio.output(pin4, True)

    else:

        # Stop

        stop()

def main():

    # Initialize Pygame

    pygame.init()

    # Initialize the joystick module

    pygame.joystick.init()

    # Check for any connected joysticks

    if pygame.joystick.get_count() == 0:

        print("No joysticks found.")

        return

    # Get the first joystick

    joystick = pygame.joystick.Joystick(0)

    joystick.init()

    try:

        while True:

            # Process Pygame events

            for event in pygame.event.get():

                if event.type == pygame.JOYAXISMOTION:

                    # Joystick movement detected

                    move(joystick)

                elif event.type == pygame.JOYBUTTONUP:

                    # Joystick button released

                    stop()

                elif event.type == pygame.QUIT:

                    # Quit event detected

                    stop()

                    pygame.quit()

                    sys.exit()

    except KeyboardInterrupt:

        # Handle Ctrl+C interruption

        stop()

        pygame.quit()

        sys.exit()

if __name__ == '__main__':

    main()


