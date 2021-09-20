import cv2 as cv
# read image
img = cv.imread(r'D:\backup\OpenCV\cat.jpg')
cv.imshow('cat',img)
cv.waitKey(0)

#########################################################################

#read Video
# capture = cv.VideoCapture('OneDrive\Desktop\OpenCV\dog.mp4')
# capture = cv.VideoCapture(0) #for webcam
# while True:
#    isTrue, frame = capture.read()
#    cv.imshow('Video', frame)

#    if cv.waitKey(20) & 0xFF == ord('d'):
#        break

# capture.realease()
# cv.destroyAllWindows()

###########################################################################

#rescale video

# capture = cv.VideoCapture('OneDrive\Desktop\OpenCV\dog.mp4')
# method works for image, video, live video
# def rescaleFrame(frame,scale=0.75):
#     width  = int(frame.shape[1] * scale)
#     height  = int(frame.shape[0] * scale)
#     dimensions = (width,height)

#     return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

# while True:
#    isTrue, frame = capture.read()
#    frame_resized = rescaleFrame(frame)  #default
#    frame_resized = rescaleFrame(frame,2)
#    cv.imshow('Video', frame_resized)

#    if cv.waitKey(20) & 0xFF == ord('d'):
#        break

# capture.realease()
# cv.destroyAllWindows()

###########################################################################
#rescale image

img = cv.imread('OneDrive\Desktop\OpenCV\cat.jpg')
def rescaleFrame(frame,scale=0.75):
    width  = int(frame.shape[1] /scale)
    height  = int(frame.shape[0] / scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA)

img_resized = rescaleFrame(img,4)
cv.imshow('cat',img_resized)
cv.waitKey(0)

############################################################################

#resize image  - method1

# capture = cv.VideoCapture(0)

# #method works for live video only
# capture.set(cv.CAP_PROP_FRAME_WIDTH, 1080)
# capture.set(cv.CAP_PROP_FRAME_HEIGHT, 720)  

# while True:
    
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#        break

# capture.realease()
# cv.destroyAllWindows()

#############################################################################

#Resize video - method2 - by function

# capture = cv.VideoCapture(0)
# #method works for live video only
# def changeRes(width,height):
#     capture.set(3,width)
#     capture.set(4,height)    

# changeRes(1080,720)

# while True:
    
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#        break

# capture.realease()
# cv.destroyAllWindows()

##########################################################################