import cv2
import numpy as np

array = np.zeros((1,1))

img = cv2.imread("blobs.jpg",cv2.IMREAD_COLOR)
blob_params = cv2.SimpleBlobDetector_Params()
blob_params.filterByArea = True # to avoid detection of tiny dots
blob_params.minArea = 100
blob_params.filterByCircularity = True # Circularity = 4*pi*Area/(perimeter)^2 (circle returns 1)
blob_params.minCircularity = 0.9
blob_params.filterByConvexity = True # cirlce has a high convexity
blob_params.minConvexity = 0.8
blob_params.filterByInertia = True # objects similar to circle has large inertia (circle=1,ellipse=0.7ish,line=0)
blob_params.minInertiaRatio = 0.7
detector = cv2.SimpleBlobDetector_create(blob_params)

keypoints = detector.detect(img) # returns keypoints
print(keypoints) # (< cv2.KeyPoint 0000012209182310>, < cv2.KeyPoint 0000012200F0F090>, < cv2.KeyPoint 0000012200F0ECA0>, < cv2.KeyPoint 0000012200EDA2B0>, < cv2.KeyPoint 0000012200E
detected_img = cv2.drawKeypoints(img,keypoints,array,(214,2,242),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.putText(detected_img,str(len(keypoints)),(100,100),fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(214,2,242))

cv2.imshow("blob circle detection",detected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()