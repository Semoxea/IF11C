# import modules
import time
import RPi.GPIO as GPIO

# setup pins
GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
Out = [8, 10, 16, 18]
In = [3, 5, 7, 11]
ChangeFlagOld = [0, 0, 0, 0]
ChangeFlagNew = [0, 0, 0, 0]
GPIO.setup(32, GPIO.OUT)

for x in In:
    GPIO.setup(x, GPIO.IN)
for y in Out:
    GPIO.setup(y, GPIO.OUT)


def printChanges():
    print(ChangeFlagOld)
    for j in range(len(ChangeFlagOld)):
        if ChangeFlagOld[j] != ChangeFlagNew[j]:
            print("Aenderungen erkannt")
            GPIO.output(32, GPIO.HIGH)
            ChangeFlagOld[j] = ChangeFlagNew[j]

while True:
    GPIO.output(32, GPIO.LOW)
    for i in range(len(In)):
        if GPIO.input(In[i]) == GPIO.HIGH:
            GPIO.output(Out[i], GPIO.HIGH)
            ChangeFlagNew[i] = 1
        else:
            GPIO.output(Out[i], GPIO.LOW)
            ChangeFlagNew[i] = 0
    printChanges()
    time.sleep(1)
