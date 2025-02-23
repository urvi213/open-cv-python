import cv2
import os
# xml - extensible markup language (not a coding language, a form of storing data. in web platfroms you can transfer data with it )

mainfolder_name = "faces"
subfolder_name = "urvi"
path = os.path.join(mainfolder_name,subfolder_name)
if not os.path.isdir(path):
    os.makedirs(path)
    print("made")

new_width = 100
new_height = 120
video  = cv2.VideoCapture(0) # 0 is primary webcam (external would be 1)
classifier  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

i = 0
while i < 30: # we are capturing 30 pictures
    s,frame = video.read()
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detected = classifier.detectMultiScale(grayframe,1.2,4)
    #print(detected) [[x,y,w,h],[],[]]

    for x,y,width,height in detected:
        cv2.rectangle(frame,(x,y),(x+width,y+height),color=(255,0,0),thickness=4)

        face = grayframe[y:y+height,x:x+width]
        face = cv2.resize(face,(new_width,new_height))
        cv2.imwrite(  os.path.join(path,"{}.png".format(i)),  face)
        i += 1

        cv2.imshow("captured video",frame)
        cv2.waitKey(10)