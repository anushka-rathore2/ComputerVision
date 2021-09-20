import cv2 as cv
import numpy as np
img = cv.imread('cat.jpg')
cv.imshow("img",img)

blank = np.zeros((1000,1000,3),dtype ='uint8')
cv.imshow('blank',blank)

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

ret, thres = cv.threshold(blur,125,255,cv.THRESH_BINARY)
cv.imshow('thres',thres)

canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours), 'found')

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('contours drawn',blank)

cv.waitKey(0)