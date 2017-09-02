#!/usr/bin/python2.7
from video_card import MyDisp
from mylogger import LoggerNew
import argparse
import logging
import sys
import time
import OPi.GPIO as GPIO
from flask import Flask, jsonify, abort, make_response, request, url_for
#from flask_httpauth import HTTPBasicAuth
import json

class Multiplexor():
    def __init__(self, pin0, pin1, pin2, pin3, e_pin, el_pin):
        self.a_pins = {0: pin0, 1: pin1, 2: pin2, 3: pin3}
        self.e_pin = e_pin
        self.el_pin = el_pin
        self.q_pins = []
        self._clear_q_pins()
        self._init_addr_pins()
        self._init_drive_pins()

    def _clear_q_pins(self):
        for i in range(16):
            if len(self.q_pins) < (i+1):
                self.q_pins.append(0)
            else:
                self.q_pins[i] = 0

    def _init_drive_pins(self):
        GPIO.setup(self.e_pin, GPIO.OUT)
        GPIO.setup(self.el_pin, GPIO.OUT)

        GPIO.output(self.e_pin, GPIO.HIGH)
        GPIO.output(self.el_pin, GPIO.HIGH)

    def _latch_pin(self):
        GPIO.output(self.el_pin, GPIO.HIGH)
        GPIO.output(self.el_pin, GPIO.LOW)
        GPIO.output(self.el_pin, GPIO.HIGH)

    def _init_addr_pins(self):
        for i in range(4):
            GPIO.setup(self.a_pins[i], GPIO.OUT)

    def _set_addr(self, addr):
        for i in range(4):
            GPIO.output(self.a_pins[i], [GPIO.LOW, GPIO.HIGH][(addr + 1) >> i & 1])

    def set_pin(self, pin):
        self.q_pins[pin] = 1
        GPIO.output(self.e_pin, GPIO.HIGH)
        self._set_addr(pin)
        GPIO.output(self.e_pin, GPIO.LOW)
        self._latch_pin()

    def reset_pin(self, pin):
        self.q_pins[pin] = 0
        GPIO.output(self.e_pin, GPIO.HIGH)
        self._latch_pin()
        i = 0
        for _pin in self.q_pins[:]:
            if _pin == 1:
                self.set_pin(i)
            i += 1



def main(log):
    log.info("Starting")
    log.info("Init display")
    disp = MyDisp(128, 64, 0)

    disp.draw_text("Roman Grekov")
    disp.draw_text_x_y(0, 25, "Molodets")

    log.info("Setup GPIO")
    led_gpio = 7
    GPIO.setmode(GPIO.BOARD)
    mux = Multiplexor(18, 12, 26, 24, 22, 16)
    mux.set_pin(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Main script')
    parser.add_argument('-l', '--logfile', help='Full path to log file')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                                    help='Verbose output')
    cmd_args = parser.parse_args()
    if cmd_args.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    log = LoggerNew("polivalka", level=level)
    sys.exit(main(log))
