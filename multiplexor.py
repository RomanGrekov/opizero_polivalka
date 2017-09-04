#!/usr/bin/python2.7
import OPi.GPIO as GPIO
import time


class Multiplexor():
    def __init__(self, log, pin0, pin1, pin2, pin3, e_pin, el_pin):
        self.log = log
        self.a_pins = {0: pin0, 1: pin1, 2: pin2, 3: pin3}
        self.e_pin = e_pin
        self.el_pin = el_pin
        self._init_mode()
        self._init_addr_pins()
        self._init_drive_pins()
        GPIO.output(self.el_pin, GPIO.HIGH)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        GPIO.cleanup()

    def _init_mode(self):
        GPIO.setmode(GPIO.BOARD)

    def _init_drive_pins(self):
        GPIO.setup(self.e_pin, GPIO.OUT)
        GPIO.setup(self.el_pin, GPIO.OUT)

        GPIO.output(self.e_pin, GPIO.HIGH)
        GPIO.output(self.el_pin, GPIO.HIGH)

    def _init_addr_pins(self):
        for i in range(4):
            GPIO.setup(self.a_pins[i], GPIO.OUT)

    def _set_addr(self, addr):
        for i in range(4):
            state = [GPIO.LOW, GPIO.HIGH][(addr) >> i & 1]
            self.log.debug("Set pin %s(%s) to state %s" % (i, self.a_pins[i], state))
            GPIO.output(self.a_pins[i], state)

    def set_pin(self, pin):
        self.log.info("Set pin %s" % pin)
        GPIO.output(self.e_pin, GPIO.HIGH)
        self._set_addr(pin)
        GPIO.output(self.e_pin, GPIO.LOW)

    def reset_pin(self):
        self.log.info("Reset pins")
        GPIO.output(self.e_pin, GPIO.HIGH)

