import cv2
img1 = cv2.imread("house.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("mountains.jpg",cv2.IMREAD_COLOR)

cv2.imshow("house",img1)
cv2.imshow("mountains",img2)
cv2.waitKey(0)
 
# adding images
added_img = cv2.add(img1,img2)
cv2.imshow("added",added_img) # pixel values are both added
cv2.waitKey(0)

# weighted addition # giving mroe weight to one image
weighted = cv2.addWeighted(img1,0.2,img2,1,0)
cv2.imshow("weighted",weighted) 
cv2.waitKey(0)

# subtraction
subtracted = cv2.subtract(img1,img2)
cv2.imshow("subtracted",subtracted) 
cv2.waitKey(0)