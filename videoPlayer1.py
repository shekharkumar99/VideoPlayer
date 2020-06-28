import numpy as np
import cv2
import sys

frameInput = 60
displayResolution = 480
color = '' 
cap =''

#User Input check 

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


# Load video using open CV
cap = cv2.VideoCapture(video)

# Set Frames as provided from the command line
cap.set(cv2.CAP_PROP_FPS, frameInput)

# Function to change the resolution 
def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

change_res(displayResolution,displayResolution)

#Function to for segmentation and removing background
# fgbg = cv2.createBackgroundSubtractorMOG2()
# while(1):
#     ret, frame = cap.read()

#     fgmask = fgbg.apply(frame)

while(True):
	ret,frame=cap.read()
	if(color =='monochrome'):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('output',gray)
	else:	
		cv2.imshow('output',frame)
	key = cv2.waitKey(1)
	
	if key == ord('p'):
		cv2.waitKey(-1)
	if
	if(cv2.waitKey(1) & 0xFF == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()