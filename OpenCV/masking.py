import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
cv.imshow('img',img)

blank = np.zeros((img.shape[:2]),dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(),(img.shape[1]//2 -200,img.shape[0]//2 -200),(img.shape[1]//2 + 200,img.shape[0]//2+200),255,-1)
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),250,255,-1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

shaped_mask = cv.bitwise_or(rectangle,circle)

masked = cv.bitwise_and(img,img,mask= shaped_mask)
cv.imshow('masked', masked)

cv.waitKey(0)