submit_pressed = False
dictionary_index = 1

""" import RPi.GPIO as GPIO
import time
import main

# Button and LED locations
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

# LED pins
led_pins = [5, 6, 13, 19, 26, 12, 16, 20]

# global variable dictionary index
dictionary_index = 1
submit_pressed = False

def increment():
    global dictionary_index
    dictionary_index += 1
    led_on_off()
    return dictionary_index

def decrement():
    global dictionary_index
    if dictionary_index > 1:
        dictionary_index -= 1
        led_on_off()
        return dictionary_index

def submit():
    global submit_pressed
    submit_pressed = True
    led_on_off()

while True:
    if GPIO.input(17) == GPIO.LOW:
        increment()
    elif GPIO.input(27) == GPIO.LOW:
        decrement()
    elif GPIO.input(22) == GPIO.LOW:
        submit()
        break
    time.sleep(0.1)

def led_on_off():
    # Turn off all LEDs first
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
    # Turn on LEDs based on the current dictionary_index
    for i in range(dictionary_index):
        if i < len(led_pins):  # Ensure we don't exceed the number of available LEDs
            GPIO.output(led_pins[i], GPIO.HIGH)

GPIO.cleanup """