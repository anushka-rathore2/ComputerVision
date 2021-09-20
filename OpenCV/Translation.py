import cv2 as cv
import numpy as np
img = cv.imread('cat.jpg')
cv.imshow("img",img)

# # Translation - shifting images along x & y axis

# def translate(img,x,y):
#     transMAT = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMAT,dimensions)

# # left = -x
# # up = -y
# # right = +x
# # down = +y 

# translated = translate(img,-100,100)
# cv.imshow('translated', translated)

# Rotation

def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    dimension = (height,width)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(img,-90)  #negative value for clockwise rotation
cv.imshow('rotated',rotated)

# rotated_rot = rotate(rotated,-45)  #black region stays
# cv.imshow('rotated_rot',rotated_rot)


cv.waitKey(0)