import cv2 as cv 


def Resize_frame (frame , scale = 0.75):

   # works for photo  , video , live videos . 

    width  = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation= cv.INTER_AREA )


def Change_resolution(width , height):

    # this function is for  live video

    Capture.set(3,width)
    Capture.set(4,height)




img = cv.imread('2.jpg')  # reads the image 

cv.imshow('Dog', img)  #shows the image without resizing 

resized_Image =  Resize_frame(img , scale = 0.30)  # resizing the image 

cv.imshow('resized image of dog ',resized_Image)  # showing the resized image 

cv.waitKey(0) # wait, untill closing the window . 


#__________________________________________________VIDEO-CAPTURE_____________________________________________



# let's do it for video :

Capture = cv.VideoCapture('video.mp4')

# but there is an issue , if the video ran out of frames , it will raise an exception . 

while True :

    is_True , frame = Capture.read() # reads the video , frame by frame . 

    resized_frame = Resize_frame(frame , scale = 0.30) # resized frame is stored in resized_frame variable . 

    cv.imshow('video', frame) # displays the frames 

    cv.imshow('resized_video' , resized_frame)

    if cv.waitKey(0): # waits untill key d is pressed . 
        break 

Capture.release() # this is to release  the capture device . 
cv.destroyAllWindows()