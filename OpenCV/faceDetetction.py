import cv2 as cv

img = cv.imread('peoples.jpg')
# cv.imshow('Person',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('haars_cascade.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
print("faces detected ", len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2,None)
cv.imshow('faces detected', img)

cv.waitKey(0)