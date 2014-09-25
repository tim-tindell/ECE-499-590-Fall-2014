
import diff_drive
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import pygame
import actuator_sim as ser
#-----------------------------------------------------
#--------[ Do not edit above ]------------------------
#-----------------------------------------------------

# Add imports here

import controller_def as ctrl

import keyController_include as ci
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
c = ach.Channel(ci.CONTROLLER_REF_NAME)
c.flush()


print '======================================'
print '============ My Controller ==========='
print '=========== Robert Tindell ==========='
print '========== rtindel2@gmu.edu =========='
print '======================================'

periodTime=0.0
timetochange=0.0
controller = ci.CONTROLLER_REF()
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
	[status, framesize] = t.get(tim, wait=False, last=True)
    else:
	#use the key controller to set the wheels
	[statuss, framesizes] = c.get(controller, wait=False, last=False)
	if controller.diff>0:
		ctrl.rightWheel(r,ref,controller.speed)
		ctrl.leftWheel(r,ref,controller.speed*(1-controller.diff))
	elif controller.diff<0:
		ctrl.rightWheel(r,ref,controller.speed*(1-(-1*controller.diff)))
		ctrl.leftWheel(r,ref,controller.speed)
		
	else:
		ctrl.rightWheel(r,ref,controller.speed)
		ctrl.leftWheel(r,ref,controller.speed)

	print "left: " +str(ref.ref[0])
	print "right: " +str(ref.ref[1])
	periodTime=tim.sim[0]+0.05

#-----------------------------------------------------
#--------[ Do not edit below ]------------------------
#-----------------------------------------------------
