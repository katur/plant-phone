import RPi.GPIO as GPIO
import time


green = 15
yellow = 29 
# green = 16 
# yellow = 18 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.IN)
GPIO.setup(yellow, GPIO.IN)

while True:
    if not GPIO.input(yellow) and not GPIO.input(green):
        print('Button S1 being pressed') 
    elif not (GPIO.input(yellow)):
        print('row1')
    elif not (GPIO.input(green)):
        print('col1')
    else:
        print('\tlalala')
