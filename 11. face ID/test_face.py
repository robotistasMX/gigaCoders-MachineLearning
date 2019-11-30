from easyfacenet.simple import facenet
import numpy as np
import cv2 as cv

# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h), (0,255,0), 2)
        color = frame[y:y+h,x:x+w]
        cv.imwrite( "images/face.jpg", color )
        images = ["images/image1.jpg", "images/image3.jpg", "images/face.jpg"]
        aligned = facenet.align_face(images)
        comparisons = facenet.compare(aligned)

        print("Is image 1 and 3 similar? ", bool(comparisons[0][1]))
        print("Is image 2 and 3 similar? ", bool(comparisons[0][2]))
    cv.imshow('frame', frame)
    #cv.imshow('cara', color)
    if cv.waitKey(10) == 27:
        break 

cap.release()
cv.destroyAllWindows()

# restore np.load for future normal usage
np.load = np_load_old

