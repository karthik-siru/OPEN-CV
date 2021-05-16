import cv2 as cv

haar_face = cv.CascadeClassifier( 'har_face.xml' )
haar_smile = cv.CascadeClassifier('har_smile.xml')


def detect_faces (img):

        gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces_rect =  haar_face.detectMultiScale(gray , scaleFactor = 1.1 , minNeighbors = 6 )

        for (x,y,w,h)  in faces_rect :

            cv.rectangle(img , (x,y), (x+w,y+h), (0,255,0), 2)

        cv.imshow("Faces detected_Image ", img )


def detect_smile(img):

    gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)

    smile_rect =  haar_smile.detectMultiScale(gray , scaleFactor = 1.1 , minNeighbors = 25 )

    for (x,y,w,h)  in smile_rect :

        cv.rectangle(img , (x,y), (x+w,y+h), (0,255,0), 2)

    cv.imshow("Smiles detected_Image ", img )


Capture =  cv.VideoCapture(0) 

while True :
    isTrue , frame = Capture.read()

    detect_faces(frame)
    detect_smile(frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()
