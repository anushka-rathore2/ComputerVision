import numpy as np
import cv2 as cv
import os

people =[]
for i in os.listdir(r'C:\Users\mraks\OneDrive\Desktop\data\data'):
    people.append(i)

haar_cascade = cv.CascadeClassifier('haars_cascade.xml')

# features = np.load('features.npy',allow_pickle= True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\mraks\OneDrive\Desktop\data\testData\TEST\TP\TPT4.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Person',gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print('label =', people[label],' with a confidence of',confidence)

    cv.putText(img, str(people[label]),(20,20), cv.FONT_HERSHEY_TRIPLEX,0.5, (0,0,255), 1)
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0))

cv.imshow('Detected face', img)
cv.waitKey(0)