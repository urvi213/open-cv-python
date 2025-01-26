import cv2

dog = cv2.imread("dog.jpeg",cv2.IMREAD_COLOR)

# drawing line
cv2.line(dog,(0,0),(500,500),color=(100,100,200),thickness=10) # doesnt return, it writes
cv2.imshow("line drawing",dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# drawing rectangle
cv2.rectangle(dog,(10,10),(60,100),color=(255,100,134),thickness=5)
cv2.imshow("rectangle drawing",dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filled rectangle
cv2.rectangle(dog,(70,50),(160,100),color=(255,100,134),thickness=-1)
cv2.imshow("filled rectangle drawing",dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# circle
cv2.circle(dog,(100,100),50,color=(20,30,40),thickness=2)
cv2.imshow("circle drawing",dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# filled circle
cv2.circle(dog,(150,150),20,color=(100,30,40),thickness=-2)
cv2.imshow("filled circle drawing",dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# writing
cv2.putText(dog,text="writing onto dog",org=(20,20),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255),thickness=1)
cv2.imshow("writing onto image",dog)
cv2.waitKey(0)
cv2.destroyAllWindows()