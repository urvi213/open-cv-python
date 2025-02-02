import cv2
import os
from PIL import Image

img_names = []

path = "C:/Users/aanya/Downloads/things for coding/open cv/video collage"
os.chdir(path) # changes directory
#print(os.listdir(".")) # "." means currecnt path, this functions lists names of things in path
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img_names.append(file)

video_name = "collage.avi"
video = cv2.VideoWriter(video_name,0,0.5,(1600,1200))
for image in img_names:
    to_write = cv2.imread(os.path.join(path,image))
    video.write(to_write)