import RPi.GPIO as GPIO
import time

# note to me: put the LEDs on pinout 17, 27, 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# global variable dictionary index
dictionary_index = 1
submit_pressed = False

def increment():
    global dictionary_index
        dictionary_index += 1
            return dictionary_index

def decrement():
    global dictionary_index
    if dictionary_index > 1:
        dictionary_index -= 1
        return dictionary_index

def submit():
    global submit_pressed
    submit_pressed = True

while True:
    if GPIO.input(17) == GPIO.LOW:
        increment()
    elif GPIO.input(27) == GPIO.LOW:
        decrement()
    elif GPIO.input(22) == GPIO.LOW:
        submit()
        break
    time.sleep(0.1)
