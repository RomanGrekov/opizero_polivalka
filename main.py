#!/usr/bin/python2.7
from video_card import MyDisp
from mylogger import LoggerNew
import argparse
import logging
import sys
from time import gmtime, strftime, sleep
from flask import Flask, jsonify, abort, make_response, request, url_for
#from flask_httpauth import HTTPBasicAuth
import json
from multiplexor import Multiplexor


def main(log):
    log.info("Starting")
    log.info("Init display")
    disp = MyDisp(128, 64, 0)

    disp.draw_text("Test")

    log.info("Setup GPIO")
    with Multiplexor(log, 11, 13, 16, 12, 15, 19) as mux:
        while True:
	    disp.clean_line(25)
            disp.draw_text_x_y(0, 25, strftime("%H:%M:%S", gmtime()))
            mux.set_pin(0)
            sleep(1)
            mux.reset_pin()
            mux.set_pin(1)
            sleep(1)
            mux.reset_pin()

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
