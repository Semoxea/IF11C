# import modules
import RPi.GPIO as GPIO   
import time               

# disable warnings
GPIO.setwarnings(False)
# setup pins
GPIO.setmode(GPIO.BOARD)  

ButtonPortNumbers = [3, 5, 7]
LEDPortNumbers = [8, 10, 16, 18, 22, 24, 26, 32]
#LEDPortNumbers = [32, 26, 24, 22, 18, 16, 10, 8]

# Setup Ports
for PortNr in ButtonPortNumbers:
    GPIO.setup(PortNr, GPIO.IN)
for PortNr in LEDPortNumbers:
    GPIO.setup(PortNr, GPIO.OUT)    

Dauer = 0.2
rechtslauf = True
aktPort = 0

while True: 
    # auf kleiner als damit letzter pin auch angeleuchtet wird
    if(aktPort > len(LEDPortNumbers)-1 and rechtslauf==True):
        aktPort = 0
    elif(aktPort < 0 and rechtslauf != True):
        aktPort = len(LEDPortNumbers)-1
    
    if (GPIO.input(5) == GPIO.HIGH):
        rechtslauf = False
    elif (GPIO.input(7) == GPIO.HIGH):
        rechtslauf = True
    elif(GPIO.input(3) == GPIO.HIGH):
        quit()
    elif(rechtslauf == True):
        GPIO.output(LEDPortNumbers[aktPort], GPIO.HIGH)
        time.sleep(Dauer)
        GPIO.output(LEDPortNumbers[aktPort], GPIO.LOW)
        aktPort += 1
    elif(rechtslauf != True):
        GPIO.output(LEDPortNumbers[aktPort], GPIO.HIGH)
        time.sleep(Dauer)
        GPIO.output(LEDPortNumbers[aktPort], GPIO.LOW)
        aktPort -= 1
    

        

