#!/usr/bin/python2.7
from video_card import MyDisp
from mylogger import LoggerNew
import argparse
import logging
import sys
import time
import OPi.GPIO as GPIO
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
import json

def main(log):
    log.info("Starting")
    log.info("Init display")
    disp = MyDisp(128, 64, 0)

    disp.draw_text("Roman Grekov")
    disp.draw_text_x_y(0, 25, "Molodets")

    log.info("Setup GPIO")
    led_gpio = 7
    #GPIO.setmode(GPIO.SUNXI)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_gpio, GPIO.OUT)
    while True:
        GPIO.output(led_gpio, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_gpio, GPIO.LOW)
        time.sleep(1)

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
