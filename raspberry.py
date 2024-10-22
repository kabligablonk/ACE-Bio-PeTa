import RPi.GPIO as GPIO
import time

# note to me: put the LEDs on pinout 17, 27, 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_dow=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_dow=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_dow=GPIO.PUD_UP)

# global variable dictionary index
dictionary_index = 1

if dictionary_index < 1:
    dictionary_index = 1

def increment():
    dictionary_index += 1
    return dictionary_index


def decrement():
    dictionary_index -= 1
    return dictionary_index
