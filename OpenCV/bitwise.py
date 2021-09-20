import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise and ---->  intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('AND', bitwise_and)

# bitwise or ---->  intersecting regions & non intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('or', bitwise_or)

# bitwise xor ---->  non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('xor', bitwise_xor)

# bitwise not ---->  inverting
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('rectangle not', bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow('circle not', bitwise_not)

cv.waitKey(0)