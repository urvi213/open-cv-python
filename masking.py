import cv2
import numpy

red = numpy.uint8([[[0,0,255]]]) # unsigned integer 8 bits
hsvred = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print(hsvred)
# read a video file (either takes an existing video or takes from your webcame)
video = cv2.VideoCapture("invisible man video.mp4")
for i in range(60):
    s,bg = video.read() # returns whether video was successful and frame
    #if not s: continue
#cv2.imshow("frame",bg)
#cv2.waitKey(0)

lower_red = numpy.array([100,50,50])
upper_red = numpy.array([200,255,255])

while video.isOpened():
    s,frame = video.read()
    if not s: break
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(frame,lower_red,upper_red)
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3))) # refines mask
    mask2 = cv2.bitwise_not(mask1) # gets opposite of mask1
    result1 = cv2.bitwise_and(bg,bg,mask=mask1)
    result2 = cv2.bitwise_and(frame,frame,mask=mask2)
    final_result = cv2.add(result1,result2)
    cv2.imshow("video",final_result)
    cv2.waitKey(10)
    #cv2.destroyAllWindows()
