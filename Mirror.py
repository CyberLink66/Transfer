import RPi.GPIO as GPIO
import time

cP = [6, 5, 25, 24, 23, 27, 17]     #Contolling-Pins für die 7seg-Digit
üLP = 26                            #Pin der überwachungs- LED
bP = 20                             #Input-Pin des Button

y = 0                               #Zusatnd des Button am GPIO20  (0/1)
x = False                           #Zusand der LED (True/False)
z = 0                               #Zähler, welcher die Einschaltzyklen der LED dokumentiert (0-9)
ZV = 1                              #Zählervariable, welche entscheidet ob hoch oder runter gezählt wird (1/-1)

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(cP, GPIO.OUT)
    GPIO.setup(ledP, GPIO.OUT)
    GPIO.setup(bP, GPIO.IN)

def end():
    GPIO.cleanup()

def Statusmeldung():
    print(f"Status: {y} / {x}")

def zuordnung():
    EINS = [5, 25]
    ZWEI = [6, 5, 17, 23, 24]
    DREI = [6, 5, 17, 25, 24]
    VIER = [27, 5, 17, 25]
    FUNF = [6, 27, 17, 25, 24]
    SECHS = [6, 27, 17, 23, 25, 24]
    SIEBEN = [6, 5, 25]
    ACHT = cP
    NEUN = [6, 27, 5, 17, 25, 24]
    NULL = [6, 27, 5, 23, 25, 24]

def turnOn():
    x = True
    GPIO.output(üLP, GPIO.HIGH)
    Statusmeldung()

def turnOff():
    GPIO.output(üLP, LOW)
    x = False
    Statusmeldung()

def testFor():
    if z == 9:
        ZV = (-1)
    if z == 0:
        ZV = 1

def showC():
    if z == 0:
        GPIO.output(NULL, GPIO.LOW)
    if z == 1:
        GPIO.output(EINS, GPIO.LOW)
    if z == 2:
        GPIO.output(ZWEI, GPIO.LOW)
    if z == 3:
        GPIO.output(DREI, GPIO.LOW)
    if z == 4:
        GPIO.output(VIER, GPIO.LOW)
    if z == 5:
        GPIO.output(FUNF, GPIO.LOW)
    if z == 6:
        GPIO.output(SECHS, GPIO.LOW)
    if z == 7:
        GPIO.output(SIEBEN, GPIO.LOW)
    if z == 8:
        GPIO.output(ACHT, GPIO.LOW)
    if z == 9:
        GPIO.output(NEUN, GPIO.LOW)


if __name__ == "__main__":
    print("Starting...")
    try:
        while True:
            y = GPIO.input(bP)

            if y == 1 and not x:
                turnOn()
                showC()
                z += ZV
                testFor()
                time.sleep(0.2)
            elif y == 1 and x:
                turnOff()
                showC()
                z += ZV
                testFor()
                time.sleep(0.2)

    except KeyboardInterrupt:
        end()
