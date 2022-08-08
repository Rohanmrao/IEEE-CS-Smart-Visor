import cv2
# import numpy as np 

key_kill_val  = ord('q') # this can be changed to any val, here it's the 'q' key

def is_valid(val1,val2):

    if((275 <= val1 <=340) and (190 <= val2 <= 275)): # middle scenario
        return 1
    if((320 <= val1 <= 325) and (130 <= val2 <= 135)): # top scenario
        return 1
    if((290 <= val1 <= 295) and (380 <= val2 <= 385)): # bottom scenario
        return 1
    if((150 <= val1 <= 155) and (250 <= val2 <= 255)): # left scenario
        return 1
    if((460 <= val1  <= 465) and (235 <= val2 <= 240)): # right scenario
        return 1
    
    else:
        return 0

def capture():

    feed = cv2.VideoCapture(0) #zero specifies that a webcam is used
    path='C:/Users/Rohan Mahesh Rao/Desktop/IEEE_CS_Summer/Images/nhb.jpg'
	
    
    while True:

        ret,frame = feed.read() # reading the video frame by frame 
   
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (111,111), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

        cv2.imshow('Frame',frame)
        
        if(is_valid(maxLoc[0],maxLoc[1]) == 1):
            cv2.circle(frame, maxLoc, 40, (0, 255, 255), 3, cv2.LINE_AA)
            cv2.putText(frame, "HIGH BEAM marked by a circle", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0, 0, 255))
            cv2.imshow('Frame',frame)

        if (cv2.waitKey(1) & 0xFF == key_kill_val):
            break
    
    feed.release()
    cv2.destroyAllWindows()
    print("\n\n\n\nVideo feed ended\n")


capture()
