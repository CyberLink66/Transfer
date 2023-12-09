import RPi.GPIO
import time

x = False
y = 0
z = 0
ZV = 1
LOW = GPIO.LOW
HIGH = GPIO.HIGH

def setup():
    global ledPins, pin1, pin2
    ledPins = [17, 27, 22, 23, 24, 6, 12, 13, 16, 20]
    pin1 = 18
    pin2 = 19

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(ledPins, GPIO.OUT)


def turnOn():
    GPIO.output(pin2, HIGH)
    print(f"Status: {y} / {z, ZV} / {x}")

def turnOff():
    GPIO.output(pin2, LOW)
    print(f"Status: {y} / {z, ZV} / {x}")



def goUp():
    for c in range(z):
        GPIO.output(ledPins[c], LOW)


def goDown():
    for c in range(z):
        GPIO.output(ledPins[c], HIGH)


try:
    setup()
    while True:

        y = GPIO.input(pin1)

        if y == 1 and not x:
            x = True
            z += ZV

            if z < 0:
                z = 0
            elif z > len(ledPins):
                z = len(ledPins)

            turnOn()
            goUp()
            time.sleep(0.2)

        elif y == 1 and x:
            x = False
            turnOff()
            time.sleep(0.2)


except KeyboardInterrupt:
    GPIO.cleanup()