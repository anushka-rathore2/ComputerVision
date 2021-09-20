import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('cat.jpg')
cv.imshow('Image', img)

# plt.imshow(img)
# plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

lab  = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)

# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('hsv_bgr',hsv_bgr)

lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr',lab_bgr)

plt.imshow(lab_bgr)
plt.show()

cv.waitKey(0)