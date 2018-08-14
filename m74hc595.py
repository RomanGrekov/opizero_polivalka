#!/usr/bin/python2.7
import OPi.GPIO as GPIO
import time


class M74HC595():
    # ds - serial data input
    # sh_cp - clock input
    # st_cp - latch pins
    def __init__(self, log, oe, mr, ds, sh_cp, st_cp):
        self.log = log
        self.oe = oe
        self.mr = mr
        self.ds = ds
        self.sh_cp = sh_cp
        self.st_cp = st_cp
        self.size = 8
        self.pause = 0
        self.value = 0
        self._init_mode()
        self._init_drive_pins()
        self._set_drive_pins()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        GPIO.cleanup()

    def _init_mode(self):
        self.log.info("Init GPIO board")
        GPIO.setmode(GPIO.BOARD)

    def _init_drive_pins(self):
        self.log.info("Init drive pins")
        GPIO.setup(self.oe, GPIO.OUT)
        GPIO.setup(self.mr, GPIO.OUT)
        GPIO.setup(self.ds, GPIO.OUT)
        GPIO.setup(self.sh_cp, GPIO.OUT)
        GPIO.setup(self.st_cp, GPIO.OUT)

    def _set_drive_pins(self):
        self.log.info("Set drive pins")
        GPIO.output(self.oe, GPIO.LOW)
        GPIO.output(self.mr, GPIO.HIGH)
        GPIO.output(self.ds, GPIO.LOW)
        GPIO.output(self.sh_cp, GPIO.LOW)
        GPIO.output(self.st_cp, GPIO.HIGH)

    def _tick(self):
        GPIO.output(self.sh_cp, GPIO.HIGH)
        time.sleep(self.pause)
        GPIO.output(self.sh_cp, GPIO.LOW)
        time.sleep(self.pause)

    def _latch(self):
        GPIO.output(self.st_cp, GPIO.HIGH)
        time.sleep(self.pause)
        GPIO.output(self.st_cp, GPIO.LOW)
        time.sleep(self.pause)

    def _write(self):
        value = self.value
        for x in range (0, self.size):
            if value & 0x80 == 0x80:
                state = GPIO.HIGH
            else:
                state = GPIO.LOW
            self.log.debug("Set pin %s to state %s" % (x, state))
            GPIO.output(self.ds, state)
            self._tick()
            value = value << 0x01
        self._latch()

    def set_val(self, value):
        self.value = value
        self._write()

    def set_pin(self, pin, state):
        if state != 0 and state != 1:
            self.log.error("Error. State must be 0 or 1")
            return 1
        if self.size >= pin < 0:
            self.log.error("Wrong pin number")
            return 1
        if state:
            self.value = self.value | (state << pin)
        else:
            self.value = self.value & ~(1 << pin)
        self.set_val(self.value)
        return 0
        
            

