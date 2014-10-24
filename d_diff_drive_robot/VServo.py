import diff_drive
import ach
import sys
import time
from ctypes import *
import socket
import cv2.cv as cv
import cv2
import numpy as np
import controller_def as ctrl
import AngVelChan as angle



ROBOT_CHAN_VIEW   = 'robot-vid-chan'
ROBOT_TIME_CHAN  = 'robot-time'

cv.NamedWindow("frame", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("thresh2", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("img", cv.CV_WINDOW_AUTOSIZE)


newx = 320
newy = 240

nx = 640
ny = 480

dd = diff_drive
tim = dd.H_TIME()

#Initialize channels
v = ach.Channel(ROBOT_CHAN_VIEW)
v.flush()
t = ach.Channel(ROBOT_TIME_CHAN)
t.flush()
a = ach.Channel(angle.CONTROLLER_REF_NAME)
a.flush()
angvel = angle.CONTROLLER_REF()

a.put(angvel)
#get the center of the chosen color
def GetColorCenter(image,color):
	hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
	upper=lower=0
	if color=='blue':
		lower = np.array([110,50,50],np.uint8)
		upper = np.array([130,255,255],np.uint8)
	elif color=='red':
		lower = np.array([0,50,50],np.uint8)
		upper = np.array([50,255,255],np.uint8)
	else:
		lower = np.array([50,50,50],np.uint8)
		upper = np.array([110,255,255],np.uint8)
# Get the threshold of the color chosen
	thresh = cv2.inRange(hsv,lower, upper)
	thresh2 = thresh.copy()

# find contours in the threshold image
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# finding contour with maximum area and store it as best_cnt
	max_area=area=best_cnt=max_area= 0
	try:
		for cnt in contours:
			area = cv2.contourArea(cnt)

		if area > max_area:
			max_area = area
			best_cnt = cnt
		# finding centroids of best_cnt and draw a circle there
		M = cv2.moments(best_cnt)
		cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
		cv2.circle(img,(cx,cy),5,(0, 0, 255),-1)
	except:
		cx=cy=-2

	cv2.imshow('thresh2',thresh2)
	return [cx,cy]
COLOR="blue"
FrameAmount=0
# Main while loop
while True:
	img = np.zeros((newx,newy,3), np.uint8)
	c_image = img.copy()
	vid = cv2.resize(c_image,(newx,newy))
	[status, framesize] = v.get(vid, wait=False, last=True)
	if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
		vid2 = cv2.resize(vid,(nx,ny))
		img = cv2.cvtColor(vid2,cv2.COLOR_BGR2RGB)

		frame = cv2.blur(img,(3,3))
		
		loc=GetColorCenter(frame,COLOR)
		x=float(loc[0])
		print(str(x-newx))
		x=float(x-newx)/newx
		y=float(loc[1])
		y=(y-newy)/newy
		angvel.AngVel=x
		a.put(angvel)
		if(x==0):
			FrameAmount+=1
		else:
			FrameAmount=0
		if FrameAmount>3:
			print "I am looking at the center of" +COLOR+ "ball"
			time.sleep(1)
			#if COLOR=='red':
			#	COLOR="blue"
			#elif COLOR=='blue':
			#	COLOR="green"
			#else:
		#		COLOR="red"
		cv2.imshow("img",img)
		

		cv2.waitKey(10)
		
	else:
		raise ach.AchException( v.result_string(status) )
	[status, framesize] = t.get(tim, wait=False, last=True)
	if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME or status == ach.ACH_STALE_FRAMES:
		pass
	#print 'Sim Time = ', tim.sim[0]
	else:
		raise ach.AchException( v.result_string(status) )
	time.sleep(0.1)

