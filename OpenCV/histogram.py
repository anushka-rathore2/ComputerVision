import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('cat.jpg')
cv.imshow('img',img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

blank = np.zeros((img.shape[:2]),dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(),(img.shape[1]//2 -200,img.shape[0]//2 -200),(img.shape[1]//2 + 200,img.shape[0]//2+200),255,-1)
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),250,255,-1)


# mask = cv.bitwise_and(gray,gray,mask= rectangle)
# cv.imshow('masked', mask)

# gray histogram

# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title('Histogram')
# plt.xlabel('bin')
# plt.ylabel('number of pixels')
# plt.plot(gray_hist)
# plt.show()


# RGB histogram

bgr_mask = cv.bitwise_and(img,img,mask= circle)
cv.imshow('masked', bgr_mask)

colors = ('b','g','r')
plt.figure()
for i,col in enumerate(colors):
    rgb_hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.title('RGB Histogram')
    plt.xlabel('bin')
    plt.ylabel('number of pixels')
    plt.plot(rgb_hist, color = col)
plt.show()


cv.waitKey(0)