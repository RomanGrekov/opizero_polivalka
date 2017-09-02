#!/usr/bin/python2.7

import logging
import sys

class LoggerNew():
    def __init__(self, name, logfile=None, level=10):
        self.name = name
        self.logfile = logfile
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not logfile:
            self.fh = logging.StreamHandler(sys.stdout)
        else:
            self.fh = logging.FileHandler(logfile)
        # add the handlers to the logger
        self.logger.addHandler(self.fh)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s',
                                      "%b %-2d %H:%M:%S")
        self.fh.setFormatter(formatter)

    def write(self, msg, logger):
        try:
            logger(u'%s' % msg)
        except Exception as err:
            logger(u'%s' % err)

    def error(self, msg):
        self.write(msg, self.logger.error)

    def info(self, msg):
        self.write(msg, self.logger.info)

    def debug(self, msg):
        self.write(msg, self.logger.debug)

    def change_name(self, name):
        self.__init__(name, self.logfile)

    def close(self):
        self.logger.removeHandler(self.fh)

    def set_level(self, level):
        self.logger.setLevel(level)

    def change_level(self, level):
        self.logger.setLevel(level)

    def __del__(self):
        self.close()
