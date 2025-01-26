import cv2
import numpy as np

eye = cv2.imread("owl eye.jpeg",cv2.IMREAD_COLOR)

resized = cv2.resize(eye,(200,400))
cv2.imshow("resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((15,15))
eroded = cv2.erode(eye,kernel)
cv2.imshow("eroded",eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

constant_border = cv2.copyMakeBorder(eye,50,50,20,20,cv2.BORDER_CONSTANT,value=(300,300,100))
cv2.imshow("constant border",constant_border)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflected_border = cv2.copyMakeBorder(eye,20,20,50,50,cv2.BORDER_REFLECT)
cv2.imshow("reflected border",reflected_border)
cv2.waitKey(0)
cv2.destroyAllWindows()

gaussian_blur = cv2.GaussianBlur(eye,(9,9),0) # () kernel size - bigger number, more blurry; sigmaX - standard division - how big is value for average x direction (sigmaY takes value of sigmaX)
cv2.imshow("gaussian blurred",gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

median_blur = cv2.medianBlur(eye,7)
cv2.imshow("median blurred",median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

bilateral_blur = cv2.bilateralFilter(eye,20,200,200) # image; diameter (how long is pixel neighbourhood); sigmaColour (standard deviation in colourspace - how large is range of mixed colours); sigmaSpace (how far will pixels mix)
cv2.imshow("bilateral blurred",bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

greyscale = cv2.cvtColor(eye,cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale",greyscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows,columns = eye.shape[0:2]
rotation_matrix = cv2.getRotationMatrix2D((rows/2,columns/2),45,1) 
rotated = cv2.warpAffine(eye,rotation_matrix,(rows,columns))
cv2.imshow("rotated",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges = cv2.Canny(eye,100,200) # 2 values - second is almost twice than first (lower is more precise)
cv2.imshow("edges",edges)  
cv2.waitKey(0)
cv2.destroyAllWindows()