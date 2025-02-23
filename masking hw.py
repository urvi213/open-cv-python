import cv2
import numpy

pink = numpy.uint8([[[199,78,242]]])
hsv_pink = cv2.cvtColor(pink,cv2.COLOR_BGR2HSV)
print("hi",hsv_pink) #[[[158 173 242]]]

video  = cv2.VideoCapture("masking hw video.mov")
for i in range(60):
    s, bg = video.read()

lower_pink = numpy.array([80,122,150])
upper_pink = numpy.array([228,255,255])

while video.isOpened():
    s,frame = video.read()
    if not s: break
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv_frame,lower_pink,upper_pink)
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3)))
    mask2 = cv2.bitwise_not(mask1)
    result1 = cv2.bitwise_and(bg,bg,mask=mask1)
    result2 = cv2.bitwise_and(frame,frame,mask=mask2)
    final_result = cv2.add(result1,result2)
    cv2.imshow("video",final_result)
    key = cv2.waitKey(20)
    if key == 27: break