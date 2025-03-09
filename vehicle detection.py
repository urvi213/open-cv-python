import cv2

video = cv2.VideoCapture("car video.avi")
classifier = cv2.CascadeClassifier("cars xml.xml")

while video.isOpened():
    s,frame = video.read()
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detected = classifier.detectMultiScale(grayframe,1.2,4)
    for x,y,width,height in detected:
        cv2.rectangle(frame,(x,y),(x+width,y+height),color=(255,255,0),thickness=2)
        cv2.imshow("vehicle detection",frame)
        key = cv2.waitKey(10)
        if key == 27: break