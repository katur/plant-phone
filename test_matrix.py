import RPi.GPIO as GPIO

from config import COLUMNS, ROWS

COL_1_PIN = COLUMNS[1]['pi_pin']
ROW_1_PIN = ROWS[1]['pi_pin']

GPIO.setmode(GPIO.BOARD)


def get_key():
    # Set all columns as output low
    for i in COLUMNS:
        pin = COLUMNS[i]['pi_pin']
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    # Set all rows as input
    for i in ROWS:
        pin = ROWS[i]['pi_pin']
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Scan rows for pushed key/button
    # A valid key press should set "rowVal"  between 0 and 3.
    row_hit = None
    for i in ROWS:
        pin = ROWS[i]['pi_pin']
        if GPIO.input(pin) == 0:
            row_hit = pin

    if not row_hit:
        return

    # Convert columns to input
    for i in COLUMNS:
        pin = COLUMNS[i]['pi_pin']
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # Switch the row hit from scan to output
    GPIO.setup(row_hit, GPIO.OUT)
    GPIO.output(row_hit, GPIO.HIGH)

    # Scan columns for still-pushed key/button
    col_hit = None
    for i in COLUMNS:
        pin = COLUMNS[i]['pi_pin']
        if GPIO.input(pin) == 1:
            col_hit = pin

    # if colVal is not 0 thru 2 then no button was pressed and we can exit
    if not col_hit:
        return

    # Return the value of the key pressed
    return (row_hit, col_hit)


if __name__ == '__main__':
    # Loop while waiting for a keypress
    coordinate = None
    while True:
        coordinate = get_key()
        if coordinate:
            print coordinate
            break
