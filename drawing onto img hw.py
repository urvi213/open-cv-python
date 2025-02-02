import cv2

img = cv2.imread("owl eye.jpeg",cv2.IMREAD_COLOR)
cv2.rectangle(img,(100,100),(180,180),color=(255, 238, 0),thickness=-1)
cv2.line(img,(80,100),(200,100),thickness=10,color=(214, 2, 242))
cv2.line(img,(80,100),(140,60),thickness=10,color=(214, 2, 242))
cv2.line(img,(200,100),(140,60),thickness=10,color=(214, 2, 242))
cv2.rectangle(img,(140,180),(170,130),color=(214, 2, 242),thickness=-1)

cv2.imshow("drawn onto image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()