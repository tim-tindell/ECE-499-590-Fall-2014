print '======================================'
print '=========== Key Controller ==========='
print '=========== Robert Tindell ==========='
print '========== rtindel2@gmu.edu =========='
print '======================================'

import keyController_include as ci
import ach
import sys
import time
import numpy as np
from ctypes import *
import curses
# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
c = ach.Channel(ci.CONTROLLER_REF_NAME)
#s.flush()
#r.flush()

# feed-forward will now be refered to as "state"
controller = ci.CONTROLLER_REF()

c.put(controller)
#init the command line to do what we want
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()
key = ''
try:
	while key != ord('q'):

		[statuss, framesizes] = c.get(controller, wait=False, last=True)
		stdscr.addstr(5,0,'diff=                                       ')
		stdscr.addstr(5,0,'diff= '+str(controller.diff))
		stdscr.addstr(7,0,'speed=                                      ')
		stdscr.addstr(7,0,'speed= '+str(controller.speed))
		key = stdscr.getch()
		#print key
		#stdscr.addch(20,25,key)
		stdscr.refresh()
		#w
		if key == 119: 
			controller.speed+=0.05
		#s
		elif key == 115: 
			controller.speed-=0.05
		

		#a
		if key == 97: 
			controller.diff-=0.05

		#d
		elif key == 100: 
			controller.diff+=0.05
		#Make sure values dont go above 1 or below -1
		if controller.speed>1:
			controller.speed=1
		if controller.speed<-1:
			controller.speed=-1
		if controller.diff>1:
			controller.diff=1
		if controller.diff<-1:
			controller.diff=-1
		c.put(controller)
	curses.endwin()
except:
	curses.endwin()

