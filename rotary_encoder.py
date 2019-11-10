from time import sleep
from RPi import GPIO

class RotaryEncoder:
    """
    This class is a wrapper to use rotary encoder connected to a Raspberry Pi.
    It assumes the GPIO mode is set to GPIO.BOARD, and is meant to use in a threaded fashion by launching the update method in a separate thread.
    You can use the clockwise argument to change the direction in which ticks are counted.
    """
    def __init__(self, clk=11, dt=12, clockwise = True):
        self.value = 0
        self.clk = clk
        self.dt = dt
        if clockwise:
            self.clockwise = 1
        else :
            self.clockwise = -1
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
                            value -= self.clockwise*0.5
                    else:
                            value += self.clockwise*0.5
                    if value % 1 == 0:
                        self.value = value      
            clkLastState = clkState
            sleep(0.005)

    def get_value(self):
        return self.value



if __name__ == "__main__":
    import threading
    
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
    
    GPIO.setmode(GPIO.BOARD)
    r = RotaryEncoder(clockwise = True)
    t1 = threading.Thread(target=update, kwargs={"r":r})
    t2 = threading.Thread(target=display, kwargs={"r":r})
    t1.start()
    t2.start()
