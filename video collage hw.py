import cv2
import os
from PIL import Image

img_names = []
total_width = 0
total_height = 0

path = "C:/Users/aanya/Downloads/things for coding/open cv/video collage hw"
os.chdir(path) # changes directory
#print(os.listdir(".")) # "." means currecnt path, this functions lists names of things in path
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img_names.append(file)
        image = Image.open(os.path.join(path,file))
        w,h = image.size
        total_height += h
        total_width += w

#print(img_names)
mean_width = total_width//len(img_names)
mean_height = total_height//len(img_names)

for name in img_names:
    image = Image.open(os.path.join(path,name))
    resized_img = image.resize((mean_width,mean_height))
    resized_img.save(name,"JPEG")


video_name = "collage hw.avi"
video = cv2.VideoWriter(video_name,0,1,(mean_width,mean_height))
for image in img_names:
    to_write = cv2.imread(os.path.join(path,image))
    video.write(to_write)
    rotation_matrix = cv2.getRotationMatrix2D((mean_width//2,mean_height//2),45,1)
    rotated_image = cv2.warpAffine(to_write,rotation_matrix,(mean_width,mean_height))
    video.write(rotated_image)
    cv2.imshow("rotation",rotated_image)
    cv2.waitKey(0)
   # cv2.destroyAllWindows()