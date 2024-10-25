import RPi.GPIO as GPIO
import time

#Define the GPIO18 pin number
increment_button = 18
decrement_button = 23
submit_button = 24

# Setup the GPIO pin as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(increment_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(decrement_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(submit_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

dictionary_index = 1

def increment(dictionary_index=None):
    dictionary_index += 1
    return dictionary_index

def decrement(dictionary_index=None):
    dictionary_index -= 1
    return dictionary_index

def submit(dictionary_index=None):
    return dictionary_index


try:
    while True:
        if not GPIO.input(increment_button):
            print("Increment button pressed")
            increment()
            time.sleep(0.2)
        if not GPIO.input(decrement_button):
            print("Decrement button pressed")
            decrement()
            time.sleep(0.2)
        if not GPIO.input(submit_button):
            print("Submit button pressed")
            submit()
            time.sleep(0.2)

except KeyboardInterrupt:
    print("Ending task, cleaning up")
    GPIO.cleanup()