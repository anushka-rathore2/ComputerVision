import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# simple thresholding
threshold,thres = cv.threshold(gray,225,255,cv.THRESH_BINARY)
cv.imshow('simple threshold',thres)

# inverse thresholding
threshold,thres_inv = cv.threshold(gray,225,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threshold inverse',thres_inv)

# adaptive thresholding
adaptive_thres = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive thresholding',adaptive_thres)

# inverse thresholding
adaptive_thres = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('adaptive thresholding',adaptive_thres)

# gaussian inverse thresholding
adaptive_gaussian_thres = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('gaussian adaptive thresholding',adaptive_gaussian_thres)

cv.waitKey(0)