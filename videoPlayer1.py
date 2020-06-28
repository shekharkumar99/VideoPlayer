import numpy as np
import cv2
import sys

frameInput = 5
displayResolution = 1280
color = 'color' 
if(len(sys.argv)<2):
	video = '/Users/shekharkumar/Documents/Python/assets/video_2.mp4'
elif(len(sys.argv)==2):
	video = sys.argv[1]
	frameInput = sys.argv[2]
elif(len(sys.argv)==3):
	video = sys.argv[1]
	frameInput = sys.argv[2]
	displayResolution = sys.argv[3]
elif(len(sys.argv)==4):
	video = sys.argv[1]
	frameInput = sys.argv[2]
	displayResolution = sys.argv[3]
	color = sys.argv[4]

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

cap = cv2.VideoCapture(video)
cap.set(cv2.CAP_PROP_FPS, frameInput)
change_res(displayResolution,displayResolution)
# fgbg = cv2.createBackgroundSubtractorMOG2()
# while(1):
#     ret, frame = cap.read()

#     fgmask = fgbg.apply(frame)

while(True):
	ret,frame=cap.read()
	if(color =='monochrome'):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('output',frame)
	else:	
		cv2.imshow('output',frame)
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()