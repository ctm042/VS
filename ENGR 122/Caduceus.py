import RPi.GPIO as gpio
from num2words import num2words
from subprocess import call
from time import sleep
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)


# Set column pins
COLUMNS = [8,10,12,16,18,22,24,26,32,36,38,40,37]
for column in COLUMNS :
    gpio.setup(column, gpio.OUT)

# Set row pins
ROWS = [11,13,15,19]
for row in ROWS :
    gpio.setup(row, gpio.IN, pull_up_down=gpio.PUD_DOWN)

# E1
gpio.setup(13, gpio.IN)
gpio.setup(15, gpio.IN)

# E2
gpio.setup(19, gpio.IN)
gpio.setup(21, gpio.IN)

# E3
gpio.setup(23, gpio.IN)
gpio.setup(29, gpio.IN)

# Prime the encoders
laststate1 = gpio.input(13)
laststate2 = gpio.input(19)
laststate3 = gpio.input(23)

volume = 100
pitch = 50
speed = 180

lastcoord = []


keymap = [
    [   "Esc",     "M1",    "M2",   "M3",   "M4",   "M5",   "M6",   "L1",   "L2",   "L3",   "R1",   "R2",   "R3"    ],
    [   "`",       "Q",     "W",    "E",    "R",    "T",    "F1",   "Y",    "U",    "I",    "O",    "P",    "Back"  ],
    [   "Tab",     "A",     "S",    "D",    "F",    "G",    "F2",   "H",    "J",    "K",    "L",    ";",    "Return"],
    [   "LShift",  "Z",     "X",    "C",    "V",    "B",    "Space","N",    "M",    ",",    ".",    "/",    "RShift"]
]

# Power each column one at a time, check for powered rows for each. Return any true cases. 
def keyscan():
    coords = []
    global lastcoord
    for column in COLUMNS:
        gpio.output(column, gpio.HIGH)
        for row in ROWS:
            if (gpio.input(row)):    
                coords = [row, column]
        gpio.output(column, gpio.LOW)
    if (lastcoord != coords):
        lastcoord = coords
        return coords
    return []

# Takes the cases from keyscan, converts them into a string, check for special keys, and append to result.
def constructor():
    global volume
    global pitch
    global speed

    result = ""
    while(True):
        coords = []

        while len(coords) != 2 :
            keycoords = keyscan()
            if keycoords != [] : coords = keycoords

            encodercoords = encoderscan()
            if encodercoords != [] : coords = encodercoords

        row =(ROWS.index(coords[0]))
        column = (COLUMNS.index(coords[1]))
        
        key = keymap[row][column]

        #print(f"Pressed {key} at {column},{row}")

        # Modifiers
        if key == "Esc":
            result += ""#uh
        elif key == "Back":
            result = result[:-1]
        elif key == "Tab":
            result += ""#uh
        elif key == "Return":
            return result
        elif key == "LShift":
            result += ""#swap key map / definitions?
        elif key == "RShift":
            result += ""#swap key map / definitions?
        elif key == "Space":
            result += " "
        
        # Macros
        elif key == "M1":
            macro1()
        elif key == "M2":
            macro2()
        elif key == "M3":
            macro3()
        elif key == "M4":
            macro4()
        elif key == "M5":
            macro5()
        elif key == "M6":
            macro6()
        
        # Function
        elif key == "F1":
            result += ""#swap?
        elif key == "F2":
            result += ""#swap?

        # Rotary Encoders
        elif key == "L1":
            if volume > 0: volume -= 5
        elif key == "L2":
            if pitch > 0: pitch -= 2
        elif key == "L3":
            if speed > 80: speed -= 10
        elif key == "R1":
            if volume < 200: volume += 5
        elif key == "R2":
            if pitch < 98: pitch += 2
        elif key == "R3":
            if speed < 400: speed += 10

        # Alphas
        else:
            result += key

        print(result)

# Encoder Dedoder
def encoderscan():
    global laststate1
    global laststate2
    global laststate3
    active1, rotation1, laststate1 = decoder(13,15,laststate1)
    active2, rotation2, laststate2 = decoder(19,21,laststate2)
    active3, rotation3, laststate3 = decoder(23,29,laststate3)
    if ((active1) & (rotation1 == "l")): return [0,7]
    if ((active1) & (rotation1 == "r")): return [0,10]
    if ((active2) & (rotation2 == "l")): return [0,8]
    if ((active2) & (rotation2 == "r")): return [0,11]
    if ((active3) & (rotation3 == "l")): return [0,9]
    if ((active3) & (rotation3 == "r")): return [0,12]
    return []

def decoder(pin1,pin2,last):
    if gpio.input(pin1) != last:
        if gpio.input(pin1) != gpio.input(pin2):
            return True, "r", gpio.input(pin1)
        else : return True, "l", gpio.input(pin1)
    else : return False, "", gpio.input(pin1)


# Custom macros
def macro1():
    voice = "m1"

def macro2():
    voice = "m5"

def macro3():
    voice = "f1"

def macro4():
    voice = "f4"

def macro5():
    language = "en"

def macro6():
    language = "es"
        

# Takes string from constructor and converts it to tts.
def tts():
    string = constructor()
    #print("have string, now speaking")
    beg = "espeak "
    vol = f"-a{volume} "
    pit = f"-p{pitch} "
    spe = f"-s{speed} "
    voi = f"-v{language}+{voice} "
    end = " 2>/dev/null"
    call([beg+vol+pit+spe+string+end], shell=True)


# 
while True:
    tts()
    
    
