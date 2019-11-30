from easyfacenet.simple import facenet
import numpy as np
import cv2 as cv

np_load_old= np.load
np.load= lambda *a, **k: np_load_old(*a, allow_pickle= True, **k)

face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')
name= ["Adan","Erick","Python","Geras"]

cap=cv.VideoCapture(0)
while True:
        _,frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            face= frame[y-10:y+h+10, x-10:x+w+10]
            cv.imwrite("images/face.jpg", face)

        if cv.waitKey(1) & 0xFF == ord('q'):
            for i in range(4):
                nombre= "images/"+str(name[i])+".jpeg"
                images= ["images/face.jpg", nombre]
                aligned= facenet.align_face(images)
                comparar= facenet.compare(aligned)
                if bool(comparar[0][1]):
                    print(name[i])
                    break
        cv.imshow('frame',frame)
        if cv.waitKey(10) == 27:
                break
cap.release()
cv.destroyAllWindows()

np.load= np_load_old
