# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:33:18 2023

@author: Sai khairnar
"""

import cv2

img1 = cv2.imread("C:/Users/ABC/Documents/image_processing_programs/Data/flower.jpg")
print(img1)
cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()


#Image conversion project colored image into grayscale.
#import image from user
path = input("Enter the Path and name of an image===")
print("You Enter this===",path)


#Now read image 
img1 = cv2.imread(path,0) #convert image into grayscale
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,0)#it accept 3 parameters 0,-1,1
cv2.imshow("converted image==",img1)
k = cv2.waitKey()
if k == ord("s"):
    cv2.imwrite("C:/Users/ABC/Documents/image_processing_programs/Data/flower.jpg",img1)
else:
    cv2.destroyAllWndows()