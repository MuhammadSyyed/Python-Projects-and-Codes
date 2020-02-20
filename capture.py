import numpy as np
import cv2
import sqlite3

detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

#------------------creating A picture taking loop--------------------------------------------------------------------------------------------------------------------------------------------

def inserting(Id,Name,Age,Gender,Email ):
    conn = sqlite3.connect('facebase.db')
    cmd = "SELECT * FROM  People WHERE  ID = "+str(Id)
    cursor = conn.execute(cmd)
    exits = 0
    for row in cursor:
        exits=1
        

    if exits == 1:
        cmd = "UPDATE People SET Name = "+str(Name)+" AND  SET Age="+str(Age)+" AND SET Gender="+str(Gender)+" AND SET Email="+str(Email)+"  WHERE ID="+str(Id)
    else:
        cmd = "INSERT INTO People(Id,Name,Age,Gender,Email) Values("+str(Id)+" , "+str(Name)+" , "+str(Age)+", "+str(Gender)+" , "+str(Email)+")"
        conn.execute(cmd)
        conn.commit()
        conn.close()

id = raw_input('Enter ID:')
name = raw_input('Enter name:')
age = raw_input('Enter Age;')
gender = raw_input('Enter Gender:')
email = raw_input('Enter email;')
inserting(id,name,age,gender,email)
random = 0
#------------------creating A picture taking loop--------------------------------------------------------------------------------------------------------------------------------------------


while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:

        random = random + 1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#------------------- Saving Image-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        cv2.imwrite("dataSet/User."+id +'.'+ str(random) + ".jpg", gray[y:y+h,x:x+w])
        cv2.waitKey(1)

    cv2.imshow('frame',img)
    cv2.waitKey(1)
    if random>60:
        break
    
cap.release()
cv2.destroyAllWindows()
