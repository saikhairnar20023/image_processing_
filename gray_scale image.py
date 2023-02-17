# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:41:34 2023

@author: Sai khairnar
"""

import cv2


img1 = cv2.imread("C:/Users/ABC/Documents/image_processing_programs/Data/flower.jpg",0)
print(img1)
cv2.imshow("gray_scale_image",img1)
cv2.waitKey(5000)
cv2.destroyAllWindows()
