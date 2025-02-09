import cv2
import numpy as np

array = np.zeros((1,1))
img = cv2.imread("blobs.jpg",cv2.IMREAD_COLOR)
blob_params = cv2.SimpleBlobDetector_Params()
blob_params.filterByArea = True
blob_params.minArea = 100
blob_params.filterByCircularity = True
blob_params.minCircularity = 0.3
blob_params.filterByConvexity = True 
blob_params.minConvexity = 0.8
blob_params.filterByInertia = True
blob_params.minInertiaRatio = 0.1
blob_params.maxInertiaRatio = 0.7
detector = cv2.SimpleBlobDetector_create(blob_params)

keypoints = detector.detect(img)
#detected_img = cv2.drawKeypoints(img,keypoints,array,(214,2,242),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.putText(img,"number of detected ellipses: "+str(len(keypoints)),(100,100),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(214,2,242))
drawn_img = cv2.drawKeypoints(img,keypoints,array,(100,100,100),cv2.DRAW_MATCHES_FLAGS_DEFAULT)
cv2.imshow("blob ellipse detection",drawn_img)
cv2.waitKey(0)
cv2.destroyAllWindows()