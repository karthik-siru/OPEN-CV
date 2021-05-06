import cv2 as cv


# reading the image

img =  cv.imread('1.jpg') #collects the image in large matrix ,(if the image size is larger than the monitor size , it will show thw possible cropped image )

cv.imshow('Cats',img) # we can keep , anything in  the first slot , whereas , second is either image or video matrix .

# below line -- the pop up window will stay , untill you press any key from the keyboard

cv.waitKey(0) 


# reading the video


Capture =  cv.VideoCapture(0)  # We can input , the video file path  , instead of number 

# Number implies , the connected cameras to the computer . 0-webcam , 1-second camera connected to the computer and so on .. 

# the below loop will read the video frame by frame .

while True :
    isTrue , frame = Capture.read()

    cv.imshow('video', frame) # shows each frame in new popup window 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

Capture.release()
cv.destroyAllWindows()