import cv2
import numpy

red = numpy.uint8([[[0,0,255]]])
hsvred = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print(hsvred)
# read a video file (either takes an existing video or takes from your webcame)
video = cv2.VideoCapture("invisible man video.mp4")
for i in range(60):
    s,bg = video.read() # returns whether video was successful and frame
    if not s: continue
cv2.imshow("frame",bg)
cv2.waitKey(0)