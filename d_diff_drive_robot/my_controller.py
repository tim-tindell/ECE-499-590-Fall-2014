#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*
# Copyright (c) 2014, Daniel M. Lofaro <dan (at) danLofaro (dot) com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# */
import diff_drive
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np

import actuator_sim as ser
#-----------------------------------------------------
#--------[ Do not edit above ]------------------------
#-----------------------------------------------------

# Add imports here

import controller_def as ctrl


#-----------------------------------------------------
#--------[ Do not edit below ]------------------------
#-----------------------------------------------------
dd = diff_drive
ref = dd.H_REF()
tim = dd.H_TIME()

ROBOT_DIFF_DRIVE_CHAN   = 'robot-diff-drive'
ROBOT_CHAN_VIEW   = 'robot-vid-chan'
ROBOT_TIME_CHAN  = 'robot-time'
# CV setup 
r = ach.Channel(ROBOT_DIFF_DRIVE_CHAN)
r.flush()
t = ach.Channel(ROBOT_TIME_CHAN)
t.flush()

i=0


print '======================================'
print '============= Robot-View ============='
print '========== Daniel M. Lofaro =========='
print '========= dan@danLofaro.com =========='
print '======================================'

periodTime=0.0
timetochange=0.0
#State0 is rotate clockwise, State1 is rotate counterclockwise, State2 is move in square
state=2
mag=1
x=0
slow=1
while True:
    [status, framesize] = t.get(tim, wait=False, last=True)
    if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
        pass
        #print 'Sim Time = ', tim.sim[0]
    else:
        raise ach.AchException( v.result_string(status) )

#-----------------------------------------------------
#--------[ Do not edit above ]------------------------
#-----------------------------------------------------
    # Main Loop
    # Def:
    # tim.sim[0] = Sim Time
    #Will Update every 0.05 seconds(20 hz) SimTime
    
    while(periodTime-tim.sim[0]>0):
	pass
    else:
        #rotate
	if(state==0):
		ctrl.rotate(r,ref,-mag)
	elif(state==1):
		ctrl.rotate(r,ref,mag)
	elif(state==2):
		if(timetochange==0):
			timetochange=tim.sim[0]+5
			print timetochange
		#go straight		
		elif(x==0 and timetochange-tim.sim[0]<=0):
			mag=1
			ctrl.straight(r,ref,mag)
			x=2
			timetochange=tim.sim[0]+5
			print "Go Straight"
		#turn
		elif(x==1 and timetochange-tim.sim[0]<=0):
			mag=0.25
			ctrl.rotate(r,ref,-mag)
			x=3
			timetochange=tim.sim[0]+5.0
			print "Turning"
		#slow down
		elif((x==2 or x==3)and timetochange-tim.sim[0]<=0):
			if(mag-(0.05*slow)<=0):
				if x==2:
					x=1
					slow=1
				if x==3:
					x=0
					slow=1
			else:
				if x==2:
					ctrl.straight(r,ref,mag-0.05*slow)
				elif x==3:
					ctrl.rotate(r,ref,-1*(mag-0.05*slow))
				slow=slow+1
				timetochange=tim.sim[0]+0.5
			
				print "stop "+str(x)+"mag: "+str(mag-0.05*slow)
	

#-----------------------------------------------------
#--------[ Do not edit below ]------------------------
#-----------------------------------------------------
