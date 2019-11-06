from time import sleep
import threading
from rotary_encoder import RotaryEncoder
import RPi.GPIO as GPIO

def update(r):
    r.update()

def display(r):
    prev = r.get_value()
    while True:
        value = r.get_value() 
        if value != prev:
            print(value)
            prev = value
        sleep(0.01)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    r = RotaryEncoder()
    t1 = threading.Thread(target=update, kwargs={"r":r})
    t2 = threading.Thread(target=display, kwargs={"r":r})
    t1.start()
    t2.start()
