from time import sleep
from RPi import GPIO

class RotaryEncoder:
    """
    This class is a wrapper to use rotary encoder connected to a Raspberry Pi.
    It assumes the GPIO mode is set to GPIO.BOARD, and is meant to use in a threaded fashion by launching the update method in a separate thread.
    """
    def __init__(self, clk=11, dt=12):
        self.value = 0
        self.clk = clk
        self.dt = dt
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def update(self):
        clkLastState = GPIO.input(self.clk)
        value = self.value
        while True:
            clkState = GPIO.input(self.clk)
            dtState = GPIO.input(self.dt)
            if clkState != clkLastState:
                    if dtState != clkState:
                            value += 0.5
                    else:
                            value -= 0.5
                    if value % 1 == 0:
                        self.value = value      
            clkLastState = clkState
            sleep(0.005)

    def get_value(self):
        return self.value