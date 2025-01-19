import cv2

dogimg = cv2.imread("dog.jpeg",cv2.IMREAD_COLOR)
owlimg =cv2.imread("owl eye.jpeg",cv2.IMREAD_COLOR)

cv2.imshow("dog",dogimg)
cv2.imshow("owl eye",owlimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

grey_dogimg = cv2.imread("dog.jpeg",cv2.IMREAD_GRAYSCALE)
grey_owlimg =cv2.imread("owl eye.jpeg",cv2.IMREAD_GRAYSCALE)

cv2.imshow("grey dog",grey_dogimg)
cv2.imshow("grey owl eye",grey_owlimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

added_img = cv2.add(dogimg,owlimg)
cv2.imshow("added images",added_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

subtracted_img = cv2.subtract(dogimg,owlimg)
cv2.imshow("subtracted images",subtracted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

b, g, r = cv2.split(dogimg)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.waitKey(0)
cv2.destroyAllWindows()         