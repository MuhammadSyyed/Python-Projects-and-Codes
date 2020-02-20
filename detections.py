import numpy as np
import cv2
import sqlite3

detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

roc = cv2.createLBPHFaceRecognizer();
roc.load("recognizer\\LearningData.yml")
iD = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)

def getrecord(iD):
    conn= sqlite3.connect('facebase.db')
    cmd = "SELECT * FROM People WHERE iD = "+str(iD)
    cursor = conn.execute(cmd)
    record = None
    for row in cursor:
        record = row
    conn.close()
    return record
    
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),852)
        iD,conf = roc.predict(gray[y:y+h,x:x+h])

        record = getrecord(iD)
        if record != None:
            cv2.cv.PutText(cv2.cv.fromarray(img),"NAME:  "+str(record[1]),(x,y+h+30),font,(0,252,252));
            cv2.cv.PutText(cv2.cv.fromarray(img),"AGE:  "+str(record[2]),(x,y+h+60),font,(252,252,0));
            cv2.cv.PutText(cv2.cv.fromarray(img),"GENDER:  "+str(record[3]),(x,y+h+90),font,(252,252,252));
            cv2.cv.PutText(cv2.cv.fromarray(img),"EMAIL:  "+str(record[4]),(x,y+h+120),font,52);

        
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
    
cap.release()
cv2.destroyAllWindows()
