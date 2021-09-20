import cv2 as cv
import numpy as np
# blank image
blank = np.zeros((500,500,3),dtype ='uint8')
# cv.imshow('Blank', blank)

# paint the image with colour
# blank[:] = 0,0,255
# cv.imshow('Blank', blank)

# paint a particular portion
# blank[200:300,300:400] = 0,0,255
# cv.imshow('Blank', blank)

# draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,255,255),thickness=2)
# cv.rectangle(blank,(0,0),(250,500),(0,255,255),thickness=cv.FILLED)
# cv.rectangle(blank,(0,0),(250,500),(0,255,255),thickness=-1)
# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,255),thickness=cv.FILLED)
# cv.imshow('Blank', blank)

# Draw a circle
# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(255,0,0),thickness =-1)
# cv.imshow('Blank', blank)

# Draw a line
# cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,0,0),thickness =3)
# cv.imshow('Blank', blank)

# Write text
cv.putText(blank,'Hello',(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),thickness = 2)
cv.imshow('Blank', blank)
cv.waitKey(0)
