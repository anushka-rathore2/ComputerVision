import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# Sobel
sobelx =  cv.Sobel(gray,cv.CV_64F,1,0)
sobely =  cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_and(sobelx,sobely)

cv.imshow("sobel x",sobelx)
cv.imshow("sobel y",sobely)
cv.imshow("Combined sobel",combined_sobel)

canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)