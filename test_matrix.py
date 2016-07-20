import RPi.GPIO as GPIO

from config import MATRIX_COLUMNS, MATRIX_ROWS

COL_1_PIN = MATRIX_COLUMNS[1]['pi_pin']
ROW_1_PIN = MATRIX_ROWS[1]['pi_pin']

GPIO.setmode(GPIO.BOARD)
GPIO.setup(COL_1_PIN, GPIO.IN)
GPIO.setup(ROW_1_PIN, GPIO.IN)


while True:
    if GPIO.input(COL_1_PIN) and GPIO.input(ROW_1_PIN):
        print('Button S1 being pressed')
    elif GPIO.input(ROW_1_PIN):
        print('row1')
    elif GPIO.input(COL_1_PIN):
        print('col1')
