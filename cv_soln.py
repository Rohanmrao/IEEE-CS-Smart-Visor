# open cv solution 
import cv2
import numpy as np 
from time import sleep

key_kill_val  = ord('q') # this can be changed to any val, here it's the 'q' key

def capture():

    feed = cv2.VideoCapture(0) #zero specifies that a webcam is used
    path='C:/Users/Rohan Mahesh Rao/Desktop/IEEE_CS_Summer/Images/nhb.jpg'
	
    
    while True:

        ret,frame = feed.read() # reading the video frame by frame 
   
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (111,111), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
        cv2.circle(frame, maxLoc, 40, (0, 255, 255), 3, cv2.LINE_AA)
        cv2.putText(frame, "HIGH BEAM marked by a circle", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255))
        cv2.imshow('Frame',frame)
      
        if (cv2.waitKey(1) & 0xFF == key_kill_val):
            break
    
    gray = cv2.GaussianBlur(gray, (111,111), 0)
    #comparing direct pixel values now ,after applying a blur filter
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    #here we're interested in only the max value of the largest array returned
    
    cv2.circle(frame, maxLoc, 40, (0, 0, 255), 3, cv2.LINE_AA)
    cv2.waitKey(0)

    feed.release()
    cv2.destroyAllWindows()
    print("\n\n\n\nVideo feed ended\n")


capture()
