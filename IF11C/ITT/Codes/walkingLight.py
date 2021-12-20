# import modules
import time
import RPi.GPIO as GPIO

# setup pins
GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
Out = [16,12,7,8,25,24,23,18]
In = [5, 6, 13, 19]

directionRight = True
duration = 0.2
current = 0

for x in In:
    GPIO.setup(x, GPIO.IN)
for y in Out:
    GPIO.setup(y, GPIO.OUT)

def runLeft():
    for i in range(len(Out)):
        GPIO.output(Out[len(Out)-(i+1)], GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(Out[len(Out)-(i+1)], GPIO.LOW)

def runRight():
    if(current != (len(Out)-1)):
        GPIO.output(Out[current], GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(Out[current], GPIO.LOW)
    else:
        GPIO.output(Out[current], GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(Out[current], GPIO.LOW)

def quit():
    if GPIO.input(5) == GPIO.HIGH:
        exit()

while True: 
    if directionRight:
        runRight()

    
