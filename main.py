#!/usr/bin/python2.7
from video_card import MyDisp
from mylogger import LoggerNew
import argparse
import logging
import sys
import time
from flask import Flask, jsonify, abort, make_response, request, url_for
#from flask_httpauth import HTTPBasicAuth
import json
from multiplexor import Multiplexor


def main(log):
    log.info("Starting")
    log.info("Init display")
    disp = MyDisp(128, 64, 0)

    disp.draw_text("Roman Grekov")
    disp.draw_text_x_y(0, 25, "Molodets")

    log.info("Setup GPIO")
    with Multiplexor(log, 18, 12, 26, 24, 22, 16) as mux:
        while True:
            mux.set_pin(0)
            time.sleep(1)
            mux.set_pin(2)
            time.sleep(1)

            mux.set_pin(0)
            time.sleep(0.2)
            mux.reset_pin()
            time.sleep(0.2)
            mux.set_pin(0)
            time.sleep(0.2)
            mux.reset_pin()
            time.sleep(0.2)
            mux.set_pin(0)
            time.sleep(0.2)
            mux.reset_pin()
            time.sleep(0.2)

            

    return 0

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
    try:
        retcode = main(log)
    except Exception as err:
        log.error(err)
        retcode = 1
    sys.exit(retcode)
