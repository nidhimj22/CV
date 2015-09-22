import numpy as np
import cv2
import argparse

cap = cv2.VideoCapture('input.mp4')

# Capture first frame
ret,frame = cap.read()
	
# setting up init locatn & r,h,c,w - ROI (used to put on car)
r,h,c,w = 200,90,300,120  
ROI_window = (c,r,w,h)

roi_hsv =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
new_mask = cv2.inRange(roi_hsv, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv2.calcHist([roi_hsv],[0],new_mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX) 

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
Threshold = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret ,frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Bck_Pjctn = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift and display on feed
        ret, ROI_window = cv2.meanShift(Bck_Pjctn, ROI_window, Threshold)
        x,y,w,h = ROI_window
        cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',frame)

        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite("Output.jpg",frame)

    else:
        break

cv2.destroyAllWindows()
cap.release()





