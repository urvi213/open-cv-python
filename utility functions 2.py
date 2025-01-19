import cv2
import numpy as np

dog = cv2.imread("dog.jpeg",cv2.IMREAD_COLOR)

"""# resizing an image
resized_dog = cv2.resize(dog,(400,200))
cv2.imshow("resized dog",resized_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# erosion on an image - requires a kernel (a numpy/np array)
kernel = np.ones((5,5)) # creates an array with 5 rows and 5 columns - each item's value is 1
#print(kernel)
# [[1. 1. 1. 1. 1.] 
 #[1. 1. 1. 1. 1.] 
 #[1. 1. 1. 1. 1.] 
 #[1. 1. 1. 1. 1.] 
 #[1. 1. 1. 1. 1.]]
eroded_dog = cv2.erode(dog,kernel)
cv2.imshow("eroded dog",eroded_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# putting a border
bordered_dog = cv2.copyMakeBorder(dog,10,10,10,10,cv2.BORDER_CONSTANT,value=(200,200,100))
cv2.imshow("with a border",bordered_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# new style
other_bordered_dog = cv2.copyMakeBorder(dog,50,50,50,50,cv2.BORDER_REFLECT)
cv2.imshow("with a border",other_bordered_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# blurring an image
gblurred_dog = cv2.GaussianBlur(dog,(7,7),0) # uses mean of surrounding pixels
cv2.imshow("blurred",gblurred_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# median blur
mblurred_dog = cv2.medianBlur(dog,7) # uses median of surrounding pixels
cv2.imshow("median blurred",mblurred_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# bilateral blur
b_blurred_dog = cv2.bilateralFilter(dog,18,220,220)
cv2.imshow("bilateral blurred",b_blurred_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

# changing colourspace after youve read an image: bgr to grayscale
grey_dog = cv2.cvtColor(dog,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey dog",grey_dog)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

# rotating an image - you need rotation matrix
r,c = dog.shape[0:2] # doesnt include 2 so the values are 0 and 1 (rows and columns)
rotation_matrix = cv2.getRotationMatrix2D((c/2,r/2),45,1)
rotated_image = cv2.warpAffine(dog,rotation_matrix,(r,c))
cv2.imshow("rotated 45 degrees",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# edge detection
edges = cv2.Canny(dog,50,90)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()