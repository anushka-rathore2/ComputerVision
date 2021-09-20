import cv2 as cv
img = cv.imread('cat.jpg')
cv.imshow('img',img)

#Converting Image to grayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray ',gray)

# # blur
blur = cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)


# Edge Cascade
# canny = cv.Canny(img,125,175)
canny = cv.Canny(blur,50,175) # for fine or less edges
cv.imshow('canny',canny)

# dialate
dilated =cv.dilate(canny,(7,7),iterations = 3)
cv.imshow('dilated',dilated)

# eroded
eroded = cv.erode(dilated,(7,7),iterations = 3)
cv.imshow('Eroded',eroded)

# Resize
# resize = cv.resize(img,(500,500), interpolation=cv.INTER_AREA) #liner & Cubic
# cv.imshow('resized',resize)

# #cropping
# cropped = img[50:200,100:500]
# cv.imshow('cropped',cropped)
cv.waitKey(0)