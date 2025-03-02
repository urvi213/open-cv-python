### pip install opencv-contrib-python #### 


import cv2
import os
import numpy as np

WIDTH =100
HEIGHT = 120

mainfolder = "faces"
#print(list(os.walk(mainfolder))) # [('faces', ['urvi'], []), ('faces\\urvi', [], ['0.png', '1.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png', '19.png', '2.png', '20.png', '21.png', '22.png', '23.png', '24.png', '25.png', '26.png', '27.png', '28.png', '29.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png'])]
# root, subdirectory (subfolders), files
# machine learning is all maths.

images = []
names = {}
labels = [] # trains machine

counter = 0
for root,subdirectories,files in list(os.walk(mainfolder)):
    for subdirectory in subdirectories:
        names[counter] = subdirectory
        path = os.path.join(mainfolder,subdirectory)
        for file in os.listdir(path):
            images.append(cv2.imread(os.path.join(path,file),cv2.IMREAD_GRAYSCALE)) 
            labels.append(counter)  #creates list like [0,0,0,0,1,1,1,1,2,2,2,2] (but with 30 of each)
        counter+=1
 
print(names)
print("")
print(labels)

images = np.array(images) # array() takes list and turns it into array
labels = np.array(labels)

model = cv2.face.LBPHFaceRecognizer_create() # local binary patterns histogram
model.train(images,labels)

video = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    s,picture = video.read()
    if not s: continue # restarts loop
    gray_picture = cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)
    detected = detector.detectMultiScale(gray_picture,1.2,4)
    for x,y,width,height in detected:
        cv2.rectangle(picture,(x,y),(x+width,y+height),color=(0,255,255))
        face = gray_picture[x:x+width,y:y+height] # slicing up picture
        face = cv2.resize(face,(WIDTH,HEIGHT))
        prediction = model.predict(face) # returns an item from labels
        cv2.putText(picture,names[prediction[0]],(x,y-20),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255))
        #print(prediction)
    cv2.imshow("camera",picture)
    key = cv2.waitKey(10)
    if key == 27: break