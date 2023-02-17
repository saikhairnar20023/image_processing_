# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:19:30 2023

@author: Sai khairnar
"""

import cv2

cap = cv2.VideoCapture("C:/Users/ABC/Documents/image_processing_programs/Data/friends.mp4")
print("cap",cap)


while True:
    ret,frame = cap.read()
    cv2.resize(frame,(1200,500))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k= cv2.waitKey(25)
    if k==ord("s") & 0xFF:
        break
   
cap.release()
cv2.destroyAllWindows()

#now capture video from webcam and save into memory

cap = cv2.VideoCapture(0)
print("cap",cap)

#DIVX, XVID , MJPG , X264 , WMV1 , WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#it contain 4 parameter , name, codes , fps , resolution
output = cv2.VideoWriter("C:/Users/ABC/Documents/image_processing_programs/Data",fourcc,20.0,(640,480),0)



while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
       
       gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
       cv2.imshow("frame",frame)
       cv2.imshow("gray",gray)
       output.Write(gray)
       k= cv2.waitKey(1)
       if k==ord("s") & 0xFF:
            break
   
cap.release()
output.release()
cv2.destroyAllWindows()