import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow("img",img)

# average blurring
average = cv.blur(img,(3,3))
cv.imshow('average',average)

# Gaussian Blurring
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gaussian',gaussian)

# Median Blurring
median = cv.medianBlur(img,3)
cv.imshow('median',median)

# bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 35,25)
cv.imshow('bilateral',bilateral)

cv.waitKey(0)