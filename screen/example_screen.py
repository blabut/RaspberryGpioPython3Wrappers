from screen import Screen
import RPi.GPIO as GPIO


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    screen = Screen()
    screen.clear()
    screen.display("Hello world!")