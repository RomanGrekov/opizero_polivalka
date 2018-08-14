#!/usr/bin/env python

import subprocess
import sys
import time

def perform_bash(action):
    pipe = subprocess.Popen(action,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)
    (stdout, stderr) = pipe.communicate()
    retcode = pipe.returncode
    return (retcode, stdout, stderr)

class PWM():
    def __init__(self):
	self.f = 1
	self.clock = 50000

    def setup(self):
	retcode = self._set(1, "run")
	if retcode:
	    return retcode
	retcode = self._set(4, "prescale")
	if retcode:
	    return retcode

    def stop(self):
	retcode = self._set(0, "run")

    def calc_f(self):
	return (self.clock / self.f)

    def change_f(self, val):
	print "F: %s" % val
	self.f = val
	cycle = self.calc_f()
	retcode = self._set(cycle, "entirecycles")
	return retcode

    def change_dr(self, val):
	print "DR: %s" % val
	cycle = self.calc_f()
	dr = cycle - (cycle / 100 * val)
	retcode = self._set(dr, "activecycles")
	return retcode
	
    def _set(self, val, dest):
	(retcode, stdout, stderr) = perform_bash("echo %s > /sys/class/pwm-sunxi-opi0/pwm0/%s" % (val, dest))
	if not retcode:
	    return 0
	else:
	    print stderr
	    return retcode

    def _get(self, dest):
	(retcode, stdout, stderr) = perform_bash("cat /sys/class/pwm-sunxi-opi0/pwm0/%s" % dest)
	if retcode:
	    print stderr
        return retcode, stdout.rstrip()
	

if __name__ == '__main__':     # Program start from here
    try:
	pwm = PWM()
	retcode = pwm.setup()
	if retcode:
	    raise KeyboardInterrupt	
	retcode = pwm.change_f(int(sys.argv[1]))
	if retcode:
	    raise KeyboardInterrupt	
	retcode = pwm.change_dr(int(sys.argv[2]))
	if retcode:
	    raise KeyboardInterrupt	
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pwm.stop()

