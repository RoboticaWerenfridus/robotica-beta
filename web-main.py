#importing all libraries to setup the Web-app
from flask import Flask, render_template
import time
import RPi.GPIO as GPIO
import yaml

with open("config.yml", "r") as f:
	config = yaml.safe_load(f)

buzzer = config['buzzer']['enabled']
buzzer_pin = config['buzzer']['pin']

motor_controller = config['motors']['controller']
motor_custompins = config['motors']['custom']
motor_r_plus = config['motors']['motor-r+']
motor_l_min = config['motors']['motor-l-']
motor_r_min = config['motors']['motor-r-']
motor_l_plus = config['motors']['motor-l+']

debug_mode = config['settings']['debug']
web_port = config['settings']['port']
web_ip = config['settings']['ip']

anti_crash = config['anti-crash']['enabled']

#Setup GPIO
def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	if (motor_controller == True):
		if (motor_custompins == 'true'):
			GPIO.setup(motor_l_min, GPIO.OUT)
			GPIO.setup(motor_l_plus, GPIO.OUT)
			GPIO.setup(motor_r_min, GPIO.OUT)
			GPIO.setup(motor_r_plus, GPIO.OUT)
		else:
			GPIO.setup(17, GPIO.OUT)
			GPIO.setup(18, GPIO.OUT)
			GPIO.setup(22, GPIO.OUT)
			GPIO.setup(23, GPIO.OUT)
	else:
		if (motor_custompins == True):
			GPIO.setup(motor_l_plus, GPIO.OUT)
			GPIO.setup(motor_r_plus, GPIO.OUT)
			motor_l = motor_l_plus
			motor_r = motor_r_plus
		else:
			GPIO.setup(4, GPIO.OUT)
			GPIO.setup(5, GPIO.OUT)
			motor_l = 4
			motor_r = 5
	if (buzzer == True):
		GPIO.setup(buzzer_pin, GPIO.OUT)

setup()

#Delete and stop all Pins to ensure safe sys exit
def destroy():
	GPIO.output(buzzer_pin, False)
	GPIO.cleanup()

#Math and complicated stuff to play any song using Notes
def play(melody,tempo,pause,pace=0.800):
	
	for i in range(0, len(melody)):		# Play song

		noteDuration = pace/tempo[i]
		buzz(melody[i],noteDuration)	# Change the frequency along the song note

		pauseBetweenNotes = noteDuration * pause
		time.sleep(pauseBetweenNotes)

#Execute notes to the buzzer from above ^^^
def buzz(frequency, length):	 #create the function "buzz" and feed it the pitch and duration)

	if(frequency==0):
		time.sleep(length)
		return
	period = 1.0 / frequency 		 #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
	delayValue = period / 2		 #calcuate the time for half of the wave
	numCycles = int(length * frequency)	 #the number of waves to produce is the duration times the frequency
	
	for i in range(numCycles):		#start a loop from 0 to the variable "cycles" calculated above
		GPIO.output(buzzer_pin, True)	 #set pin 27 to high
		time.sleep(delayValue)		#wait with pin 27 high
		GPIO.output(buzzer_pin, False)		#set pin 27 to low
		time.sleep(delayValue)		#wait with pin 27 low

#Setup the main APP to launch the Wweb-app
app = Flask(__name__)

#Main notes given here:
notes = {
	'B0' : 31,
	'C1' : 33, 'CS1' : 35,
	'D1' : 37, 'DS1' : 39,
	'EB1' : 39,
	'E1' : 41,
	'F1' : 44, 'FS1' : 46,
	'G1' : 49, 'GS1' : 52,
	'A1' : 55, 'AS1' : 58,
	'BB1' : 58,
	'B1' : 62,
	'C2' : 65, 'CS2' : 69,
	'D2' : 73, 'DS2' : 78,
	'EB2' : 78,
	'E2' : 82,
	'F2' : 87, 'FS2' : 93,
	'G2' : 98, 'GS2' : 104,
	'A2' : 110, 'AS2' : 117,
	'BB2' : 123,
	'B2' : 123,
	'C3' : 131, 'CS3' : 139,
	'D3' : 147, 'DS3' : 156,
	'EB3' : 156,
	'E3' : 165,
	'F3' : 175, 'FS3' : 185,
	'G3' : 196, 'GS3' : 208,
	'A3' : 220, 'AS3' : 233,
	'BB3' : 233,
	'B3' : 247,
	'C4' : 262, 'CS4' : 277,
	'D4' : 294, 'DS4' : 311,
	'EB4' : 311,
	'E4' : 330,
	'F4' : 349, 'FS4' : 370,
	'G4' : 392, 'GS4' : 415,
	'A4' : 440, 'AS4' : 466,
	'BB4' : 466,
	'B4' : 494,
	'C5' : 523, 'CS5' : 554,
	'D5' : 587, 'DS5' : 622,
	'EB5' : 622,
	'E5' : 659,
	'F5' : 698, 'FS5' : 740,
	'G5' : 784, 'GS5' : 831,
	'A5' : 880, 'AS5' : 932,
	'BB5' : 932,
	'B5' : 988,
	'C6' : 1047, 'CS6' : 1109,
	'D6' : 1175, 'DS6' : 1245,
	'EB6' : 1245,
	'E6' : 1319,
	'F6' : 1397, 'FS6' : 1480,
	'G6' : 1568, 'GS6' : 1661,
	'A6' : 1760, 'AS6' : 1865,
	'BB6' : 1865,
	'B6' : 1976,
	'C7' : 2093, 'CS7' : 2217,
	'D7' : 2349, 'DS7' : 2489,
	'EB7' : 2489,
	'E7' : 2637,
	'F7' : 2794, 'FS7' : 2960,
	'G7' : 3136, 'GS7' : 3322,
	'A7' : 3520, 'AS7' : 3729,
	'BB7' : 3729,
	'B7' : 3951,
	'C8' : 4186, 'CS8' : 4435,
	'D8' : 4699, 'DS8' : 4978
}


#Mario Melody & Tempo to play it to the buzzer
melody = [
  notes['E7'], notes['E7'], 0, notes['E7'],
  0, notes['C7'], notes['E7'], 0,
  notes['G7'], 0, 0,  0,
  notes['G6'], 0, 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0,
 
  notes['C7'], 0, 0, notes['G6'],
  0, 0, notes['E6'], 0,
  0, notes['A6'], 0, notes['B6'],
  0, notes['AS6'], notes['A6'], 0,
 
  notes['G6'], notes['E7'], notes['G7'],
  notes['A7'], 0, notes['F7'], notes['G7'],
  0, notes['E7'], 0, notes['C7'],
  notes['D7'], notes['B6'], 0, 0
]
tempo = [
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
 
  9, 9, 9,
  12, 12, 12, 12,
  12, 12, 12, 12,
  12, 12, 12, 12,
]
#Final Countdown Melody & Tempo to play

final_countdown_melody = [
	notes['A3'],notes['E5'],notes['D5'],notes['E5'],notes['A4'],
	notes['F3'],notes['F5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['D3'],notes['F5'],notes['E5'],notes['F5'],notes['A4'],
	notes['G3'],0,notes['D5'],notes['C5'],notes['D5'],notes['C5'],notes['B4'],notes['D5'],
	notes['C5'],notes['A3'],notes['E5'],notes['D5'],notes['E5'],notes['A4'],
	notes['F3'],notes['F5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['D3'],notes['F5'],notes['E5'],notes['F5'],notes['A4'],
	notes['G3'],0,notes['D5'],notes['C5'],notes['D5'],notes['C5'],notes['B4'],notes['D5'],
	notes['C5'],notes['B4'],notes['C5'],notes['D5'],notes['C5'],notes['D5'],
	notes['E5'],notes['D5'],notes['C5'],notes['B4'],notes['A4'],notes['F5'],
	notes['E5'],notes['E5'],notes['F5'],notes['E5'],notes['D5'],
	notes['E5'],
]

final_countdown_tempo = [
	1,16,16,4,4,
	1,16,16,8,8,4,
	1,16,16,4,4,
	2,4,16,16,8,8,8,8,
	4,4,16,16,4,4,
	1,16,16,8,8,4,
	1,16,16,4,4,
	2,4,16,16,8,8,8,8,
	4,16,16,4,16,16,
	8,8,8,8,4,4,
	2,8,4,16,16,
	1,
]

#Adventure Time Melody & Tempo to play
adventure_time_melody = [
	notes['D5'], 
	notes['G5'], notes['G5'], notes['G5'], notes['G5'], notes['FS5'],
	notes['FS5'], notes['E5'], notes['D5'], notes['E5'], notes['D5'], notes['D5'],
	notes['C5'], notes['B5'], notes['A5'], notes['G4'],  
	0, notes['C5'], notes['B5'], notes['A5'], notes['G4'], 0,  
	notes['G5'], 0, notes['G5'], notes['G5'], 0, notes['G5'], 
	notes['FS5'], 0, notes['E5'], notes['E5'], notes['D5'], notes['D5'], 
	notes['C5'], notes['C5'], notes['C5'], notes['D5'], 
	notes['D5'], notes['A5'], notes['B5'], notes['A5'], notes['G4'], 
	notes['G5']
  ]
adventure_time_tempo = [
	24,
	24, 12, 12, 12, 24,
	12, 24, 24, 24, 12, 24,
	12, 12, 12, 12,
	24, 12, 24, 24, 12, 24,  
	24, 24, 24, 12, 24, 12, 
	24, 24, 24, 12, 12, 24, 
	8, 24, 24, 8, 
	8, 24, 12, 24, 24, 
	12 
  ]

#Star Wars Darth Vader Melody & Tempo to play
star_wars_melody = [ 
			notes['G4'], notes['G4'], notes['G4'], 
			notes['EB4'], 0, notes['BB4'], notes['G4'], 
			notes['EB4'], 0, notes['BB4'], notes['G4'], 0,

			notes['D4'], notes['D4'], notes['D4'], 
			notes['EB4'], 0, notes['BB3'], notes['FS3'],
			notes['EB3'], 0, notes['BB3'], notes['G3'], 0,

			notes['G4'], 0, notes['G3'], notes['G3'], 0,
			notes['G4'], 0, notes['FS4'], notes['F4'], 
			notes['E4'], notes['EB4'], notes['E4'], 0,
			notes['GS3'], notes['CS3'], 0, 

			notes['C3'], notes['B3'], notes['BB3'], notes['A3'], notes['BB3'], 0,
			notes['EB3'], notes['FS3'], notes['EB3'], notes['FS3'], 
			notes['BB3'], 0, notes['G3'], notes['BB3'], notes['D4'], 0,


			notes['G4'], 0, notes['G3'], notes['G3'], 0,
			notes['G4'], 0, notes['FS4'], notes['F4'], 
			notes['E4'], notes['EB4'], notes['E4'], 0,
			notes['GS3'], notes['CS3'], 0, 

			notes['C3'], notes['B3'], notes['BB3'], notes['A3'], notes['BB3'], 0,

			notes['EB3'], notes['FS3'], notes['EB3'],  
			notes['BB3'], notes['G3'], notes['EB3'], 0, notes['BB3'], notes['G3'],
			]


star_wars_tempo = [
			2, 2, 2, 
			4, 8, 6, 2, 
			4, 8, 6, 2, 8,

			2, 2, 2,
			4, 8, 6, 2,
			4, 8, 6, 2, 8,

			2, 16, 4, 4, 8,
			2, 8, 4, 6,
			6, 4, 4, 8,
			4, 2, 8, 
			4, 4, 6, 4, 2, 8,
			4, 2, 4, 4, 
			2, 8, 4, 6, 2, 8,

			2, 16, 4, 4, 8,
			2, 8, 4, 6,
			6, 4, 4, 8,
			4, 2, 8, 
			4, 4, 6, 4, 2, 8,
			4, 2, 2, 
			4, 2, 4, 8, 4, 2,
			]
#TT Little Star Melody & Tempo to play
twinkle_twinkle_melody = [
	notes['C4'], notes['C4'], notes['G4'], notes['G4'], notes['A4'], notes['A4'], notes['G4'],
	notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'], notes['D4'], notes['C4'],
	
	notes['G4'], notes['G4'], notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'],
	notes['G4'], notes['G4'], notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'],
	
	notes['C4'], notes['C4'], notes['G4'], notes['G4'], notes['A4'], notes['A4'], notes['G4'],
	notes['F4'], notes['F4'], notes['E4'], notes['E4'], notes['D4'], notes['D4'], notes['C4'],
]

twinkle_twinkle_tempo = [
	4,4,4,4,4,4,2,
	4,4,4,4,4,4,2,
	
	4,4,4,4,4,4,2,
	4,4,4,4,4,4,2,
	
	4,4,4,4,4,4,2,
	4,4,4,4,4,4,2,
]

#Crazy Frog Melody & Tempo to play
crazy_frog_melody = [
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],0,
	
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],0,
	
	
	notes['A3'], notes['G3'], notes['E3'], notes['D3'],
	
	notes['A4'], notes['C5'], notes['A4'], notes['A4'], notes['D5'], notes['A4'], notes['G4'], 
	notes['A4'], notes['E5'], notes['A4'], notes['A4'], notes['F5'], notes['E5'], notes['C5'],
	notes['A4'], notes['E5'], notes['A5'], notes['A4'], notes['G4'], notes['G4'], notes['E4'], notes['B4'], 
	notes['A4'],
]

crazy_frog_tempo = [
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,4,
	
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,4,
	
	8,4,4,4,
	
	2,4,4,8,4,4,4,
	2,4,4,8,4,4,4,
	4,4,4,8,4,8,4,4,
	1,
]

#Main Web-App
@app.route('/')
def execute():
	return render_template('main.html')

@app.route('/<cmd>')
def command(cmd=None):
	response = "Performing {} ...".format(cmd.capitalize())
	if cmd == '^^^':
		camera_command = "X"
		if (motor_controller == True):
			if (motor_custompins == 'true'):
				GPIO.output(motor_l_min, True)
				GPIO.output(motor_l_plus, False)
				GPIO.output(motor_r_min, True)
				GPIO.output(motor_r_plus, False)
			else:
				GPIO.output(17, True)
				GPIO.output(18, False)
				GPIO.output(22, True)
				GPIO.output(23, False)
		else:
			GPIO.output(motor_l, True)
			GPIO.output(motor_r, True)
	elif cmd == '<))':
		camera_command = "X"
		if (buzzer == True):
			GPIO.output(buzzer_pin, True)
			time.sleep(0.3)
			GPIO.output(buzzer_pin, False)
			time.sleep(0.7)
			GPIO.output(buzzer_pin, True)
			time.sleep(0.9)
			GPIO.output(buzzer_pin, False)
		else:
			response = "Buzzer is disabled!".format(cmd.capitalize())
	elif cmd == 'X':
		camera_command = "X"
		if (motor_controller == True):
			if (motor_custompins == 'true'):
				GPIO.output(motor_l_min, False)
				GPIO.output(motor_l_plus, False)
				GPIO.output(motor_r_min, False)
				GPIO.output(motor_r_plus, False)
			else:
				GPIO.output(17, False)
				GPIO.output(18, False)
				GPIO.output(22, False)
				GPIO.output(23, False)
		else:
			GPIO.output(motor_l, False)
			GPIO.output(motor_r, False)
	elif cmd == '<<<':
		camera_command = "X"
		if (motor_controller == True):
			if (motor_custompins == 'true'):
				GPIO.output(motor_l_min, False)
				GPIO.output(motor_l_plus, True)
				GPIO.output(motor_r_min, True)
				GPIO.output(motor_r_plus, False)
			else:
				GPIO.output(17, False)
				GPIO.output(18, True)
				GPIO.output(22, True)
				GPIO.output(23, False)
		else:
			GPIO.output(motor_l, False)
			GPIO.output(motor_r, True)
	elif cmd == '>>>':
		camera_command = "X"
		if (motor_controller == True):
			if (motor_custompins == 'true'):
				GPIO.output(motor_l_min, True)
				GPIO.output(motor_l_plus, False)
				GPIO.output(motor_r_min, False)
				GPIO.output(motor_r_plus, True)
			else:
				GPIO.output(17, True)
				GPIO.output(18, False)
				GPIO.output(22, False)
				GPIO.output(23, True)
		else:
			GPIO.output(motor_l, True)
			GPIO.output(motor_r, False)
	elif cmd == 'VVV':
		camera_command = "X"
		if (motor_controller == True):
			if (motor_custompins == 'true'):
				GPIO.output(motor_l_min, False)
				GPIO.output(motor_l_plus, True)
				GPIO.output(motor_r_min, False)
				GPIO.output(motor_r_plus, True)
			else:
				GPIO.output(17, False)
				GPIO.output(18, True)
				GPIO.output(22, False)
				GPIO.output(23, True)
		else:
			response = "Option is not available without a Motor Controller!"
	elif cmd == 'The-Final-Countdown':
		camera_command = "X"
		if buzzer == False:
			response = "Option is not available with the Buzzer disabled!"
		else:
			play(final_countdown_melody, final_countdown_tempo, 0.30, 1.2000)
			response = "Played The Final Countdown by The Buzzer 3000"
	elif cmd == 'Star-Wars-Theme':
		camera_command = "X"
		if buzzer == False:
			response = "Option is not available with the Buzzer disabled!"
		else:
			play(star_wars_melody, star_wars_tempo, 0.30, 1.2000)
			response = "Played Star Wars Theme Song by Darthbuzzer"
	elif cmd == 'Adventure-Time':
		camera_command = "X"
		if buzzer == False:
			response = "Option is not available with the Buzzer disabled!"
		else:
			play(adventure_time_melody, adventure_time_tempo, 1.3, 1.500)
			response = "Played Adventure Time by Dora the Buzzerrr"
	elif cmd == 'TT-Little-Star':
		camera_command = "X"
		if buzzer == False:
			response = "Option is not available with the Buzzer disabled!"
		else:
			play(twinkle_twinkle_melody, twinkle_twinkle_tempo, 0.50, 1.000)
			response = "Played Twinkle, Twinkle little star by the elf that buzzez too hard"
	elif cmd == 'Crazy-Frog':
		camera_command = "X"
		if buzzer == False:
			response = "Option is not available with the Buzzer disabled!"
		else:
			play(crazy_frog_melody, crazy_frog_tempo, 0.30, 0.900)
			response = "Played Crazzyy Frog by Crazzzzyyyy Buzzzzzzzzzer"
	elif cmd == 'Mario-Ultimate-Theme':
		camera_command = "X"
		if buzzer == False:
			response = "Option is not available with the Buzzer disabled!"
		else:
			play(melody, tempo, 1.3, 0.800)
			response = "Played Mario Theme by Lubuzzer"
	else:
		camera_command = cmd[0].upper()
		response = "Performing {} ...".format(cmd.capitalize())
	return response, 200, {'Content-Type': 'text/plain'}
if __name__ == "__main__":
	app.run(host=web_ip, port=web_port, debug=debug_mode)


