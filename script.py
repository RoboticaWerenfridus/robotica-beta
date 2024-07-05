print("created with help from https://aywei.eu")

from vardata import *
from flask import Flask, render_template
import time
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def execute():
	return render_template('index.html')

@app.route('/stop')
def move_stop():
    GPIO.output(17, False)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(23, False)
    return "None"

@app.route('/move-forward')
def move_forward():
    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    return "None"

@app.route('/move-right')
def move_right():
    GPIO.output(17, True)
    GPIO.output(18, False)
    GPIO.output(22, False)
    GPIO.output(23, True)
    return "None"

@app.route('/move-left')
def move_left():	
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(22, True)
    GPIO.output(23, False)
    return "None"

@app.route('/move-back')
def move_back():
    GPIO.output(17, False)
    GPIO.output(18, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    return "None"

@app.route('/honk')
def honk():
    GPIO.output(buzzer_pin, True)
    time.sleep(0.3)
    GPIO.output(buzzer_pin, False)
    time.sleep(0.7)
    GPIO.output(buzzer_pin, True)
    time.sleep(0.9)
    GPIO.output(buzzer_pin, False)
    return "None"

@app.route('/viewcam')
def viewcam():
    play(star_wars_melody, star_wars_tempo, 0.30, 1.2000)
    return "None"
    
if __name__ == "__main__":
	app.run(port=8080, debug=True)
