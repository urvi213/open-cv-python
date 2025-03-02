import cv2
import os
# xml - extensible markup language (not a coding language, a form of storing data. in web platfroms you can transfer data with it )

mainfolder_name = "eyes"
#]subfolder_name = "urvi"
#path = os.path.join(mainfolder_name,subfolder_name)
if not os.path.isdir(mainfolder_name):
    os.makedirs(mainfolder_name)

new_width = 200
new_height = 120
video  = cv2.VideoCapture(0) # 0 is primary webcam (external would be 1)
classifier  = cv2.CascadeClassifier("haarcascade_eye.xml")

i = 0
while i < 30: # we are capturing 30 pictures
    s,frame = video.read()
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detected = classifier.detectMultiScale(grayframe,1.2,4)
    #print(detected) [[x,y,w,h],[],[]]

    for x,y,width,height in detected:
        cv2.rectangle(frame,(x,y),(x+width,y+height),color=(255,0,0),thickness=4)

        eye = grayframe[y:y+height,x:x+width]
        eye = cv2.resize(eye,(new_width,new_height))
        cv2.imwrite(  os.path.join(mainfolder_name,"{}.png".format(i)),  eye)
        i += 1

        cv2.imshow("captured video",frame)
        cv2.waitKey(10)