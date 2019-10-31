import cv2
import os

'''
Snagged this from a medium article and modified it for our purposes. It takes a given MP4 file that is in the
videos folder and creates a new directory in the images folder. It then takes a frame capture every 0.5 seconds.
Just import the module to your code (must have your python file in src/) and then call the function passing the 
filename you want to convert (e.g/ "Cars.mp4")
'''

def getFrame(sec, count, vidcap, image_directory):
	    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
	    hasFrames, image = vidcap.read()
	    if hasFrames:
	        cv2.imwrite(image_directory + "/image"+str(count)+".jpg", image)     # save frame as JPG file
	    return hasFrames

def getVideoFrames(videoFileName):
	video_path = os.getcwd()[0:-3] + "videos/{}".format(videoFileName)
	vidcap = cv2.VideoCapture(video_path)
	image_directory = os.getcwd()[0:-3] + "images/{}".format(videoFileName[:-4])
	if not os.path.exists(image_directory):
		os.makedirs(image_directory)

	sec = 0
	frameRate = 0.5 #//it will capture image in each 0.5 second
	count=1
	success = getFrame(sec, count, vidcap, image_directory)
	while success:
	    count = count + 1
	    sec = sec + frameRate
	    sec = round(sec, 2)
	    success = getFrame(sec, count, vidcap, image_directory)