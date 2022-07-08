# open cv solution 
import cv2
import numpy as np 
from time import sleep

key_kill_val  = ord('q') # this can be changed to any val, here it's the 'q' key

def capture():

    #feed = cv2.VideoCapture(0) #zero specifies that a webcam is used
    path='C:/Users/Rohan Mahesh Rao/Desktop/IEEE_CS_Summer/Images/nhb.jpg'
	
    
    while True:

        #ret,frame = feed.read() # reading the video frame by frame 
        frame = cv2.imread(path)
        hsv_vid = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #converting to grayscale
    
        sensitivity = 142
        lower_white = np.array([0,0,255-sensitivity])
        upper_white = np.array([255,sensitivity,255])
        white_mask = cv2.inRange(frame,lower_white,upper_white)

        #contour to track white color goes below- 
        contours, hierarchy = cv2.findContours(white_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 40000):
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y),(x + w, y + h),(0, 0, 255), 2)
                cv2.putText(frame, "HIGH BEAM", (x, y),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255))


        res = cv2.bitwise_and(frame,frame, mask= white_mask)

        cv2.imshow("Mask cam", res)
        cv2.imshow("Livecam", frame) # display processed video

        if (cv2.waitKey(1) & 0xFF == key_kill_val):
            break

    #feed.release()
    cv2.destroyAllWindows()
    print("\n\n\n\nVideo feed ended\n")


capture()
