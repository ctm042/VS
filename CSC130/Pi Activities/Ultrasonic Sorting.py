import PPi.GPIO as GPIO
from time import sleep, time

#program constants
DEBUG = True
settle_time = 2
calibrations = 5
calibration_delay = 1
trigger_time = 0.00001
speed_of_sound = 343

GPIO.setmode(GPIO.BCM)

#variables for the pins
trig = 18
echo = 19

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def calibrate():
    print("Calibrating...")
    print("Place the sensor a measured distance away from an object")
    known_distance = float(input("What is the measured distance in cm? "))
    print("Getting calibration measurments")
    distance_avg = 0
    for i in range(calibrations):
        distance = getdistance()
        if (DEBUG):
            print("Got {}cm".format(distance))
        distance_avg += distance
        sleep(calibration_delay)
    distance_avg /= calibrations

    if (DEBUG):
        print("average is {}cm".format(distance_avg))

    correction_factor = known_distance / distance_avg

    if(DEBUG):
        print("correction factor is {}".format(correction_factor))

    print("Done")
    print()

    return correction_factor

def getdistance():
    GPIO.output(trig, GPIO.HIGH)
    sleep(trigger_time)
    GPIO.output(trig, GPIO.LOW)

    while(GPIO.input(echo) == GPIO.LOW):
        start = time()
    while(GPIO.input(echo) == GPIO.HIGH):
        stop = time()

    duration = stop - start
    distance = duration * speed_of_sound
    distance = distance / 2
    distance *= 100
    return distance

###main###
#first let the sensor settle
print("Waiting for the sensor to settle. ({}s)...".format(settle_time))
sleep(settle_time)

#next calibrate
correction_factor = calibrate()

#then measure
input("Press Enter to begin"")
print("Getting measurements:")
measures = []

while (True):
    print("Measuring...")
    distance = getdistance() * correction_factor

    sleep(1)
    distance = round(distance, 4)

    print("Distance measured: {}cm".format(distance))
    measures.append(distance)

    i = input("Get another measurement? (Y/n)")
    if (not i in ["yes", "Yes", "YES", "Y", "y", ""]):
        break

#finally clean up
print("Done")
print(measures)
measures.sort()
print(measures)
GPIO.cleanup
        
