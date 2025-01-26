import cv2
import numpy as np

eyes = cv2.imread("eyes.jpg",cv2.IMREAD_COLOR)

# circle detection
g_eyes = cv2.cvtColor(eyes,cv2.COLOR_BGR2GRAY) # first you need to convert to grayscale
b_g_eyes = cv2.medianBlur(g_eyes,7) # median blur to get rid of noise
circles = cv2.HoughCircles(b_g_eyes,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=35,minRadius=20,maxRadius=50) # returns list of detected circles
#print(circles)

# show detected circles
if circles is not None:
    ir_circles = np.uint(np.around(circles))
    circles = ir_circles[0] # takes out third list
    for x,y,r in circles: # unpacking values
        cv2.circle(eyes,(x,y),r,color=(255,255,0),thickness=3)
        cv2.circle(eyes,(x,y),radius=5,color=(255,0,0))
        cv2.imshow("circle detection",eyes)
        cv2.waitKey(0)