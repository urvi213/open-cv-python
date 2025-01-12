import cv2

# load an image
image1 = cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
print(type(image1))#<class 'numpy.ndarray'>

# displaying an image
cv2.imshow("window",image1)

#  holding a window
key_pressed  = cv2.waitKey(0) # either put a time or 0 which is hold till user presses a key
print(key_pressed) # prints a code thats a number
cv2.destroyAllWindows()     

# reading a grayscale image
image1_grayscale = cv2.imread("pikachu.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("grayscale window",image1_grayscale)
cv2.waitKey(0)

# saving a new image
imwrite_status = cv2.imwrite("pikachu grayscale.png",image1_grayscale)
print(imwrite_status)

# splitting colour channels, cv2 uses BGR
b, g , r = cv2.split(image1)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.waitKey(0)