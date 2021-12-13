# import modules
import time
import RPi.GPIO as GPIO

# setup pins
GPIO.setmode(GPIO.BOARD)
Out = [22, 24, 26, 28]
In = [27, 29, 31, 33]

for x in In:
    GPIO.setup(x, GPIO.IN)
    GPIO.setup(x-5, GPIO.OUT)
while True:
    for i in In:
        GPIO.output(i-5, GPIO.input(i))
        time.sleep(1)
