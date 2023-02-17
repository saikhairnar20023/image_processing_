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
