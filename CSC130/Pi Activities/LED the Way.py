import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
gpio.setup(16,gpio.IN, pull_up_down = gpio.PUD_DOWN)

try:
    while(True):
        if (gpio.input(16)==gpio.HIGH):
            gpio.output(17,gpio.HIGH)
            sleep(.1)
            gpio.output(17,gpio.LOW)
            sleep(.1)
        else:
            gpio.output(17,gpio.HIGH)
            sleep(.5)
            gpio.output(17,gpio.LOW)
            sleep(.5)
except KeyboardInterrupt:
    gpio.cleanup()
