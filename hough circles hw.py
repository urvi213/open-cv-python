import cv2
import numpy as np
img = cv2.imread("pacman ghost hw.png",cv2.IMREAD_COLOR)

g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bg_img = cv2.medianBlur(g_img,7)
circles = cv2.HoughCircles(bg_img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=35,minRadius=10,maxRadius=40)

if circles is not None:
    ir_circles = np.uint(np.around(circles))
    circles = ir_circles[0]
    for x,y,r in circles: # unpacking values
        cv2.circle(img,(x,y),r,color=(255,255,0),thickness=3)
        cv2.circle(img,(x,y),radius=5,color=(255,0,0))
        cv2.imshow("circle detection",img)
        cv2.waitKey(0)