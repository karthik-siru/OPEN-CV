import cv2 as cv
import numpy as np 

img = cv.imread("taj.jpg")

cv.imshow("Taj", img)

#------------- Translation ------------

def translate (img, x, y ):
    dimensions  = ( img.shape[1], img.shape[0] )
    transMat = np.float32([[1,0,x],[0,1,y]])
    return cv.warpAffine(img ,transMat , dimensions )

# Translated image 

# +x --> right 
# -x --> left
# +y --> down
# -y --> up 

translated = translate(img,100,100)
cv.imshow("Translated_Image", translated )


#--------------- Rotation ---------------

# +ve angle - anti clock wise
# -ve angle - clock wise

# if there is no image , the portions will be black . 

def rotate_frame(img , angle, rotation_point= None ):
    (width , height) = (img.shape[1], img.shape[0])
   
    if rotation_point== None :
        rotation_point = (width//2 , height//2)

    rotMat =  cv.getRotationMatrix2D(rotation_point , angle , 1.0)

    return cv.warpAffine(img, rotMat, (width , height) )


rotated = rotate_frame(img, 45 )
cv.imshow("Rotated_image",rotated )

# so , if you think , we  can get the original from the rotated one , by rotating it back .. you are wrong 

rotated_back = rotate_frame(rotated  , -45)
cv.imshow("Rotated_back", rotated_back)

# looks cool though 

#--------------- Resizing -------------

resized = cv.resize(img , (300,500) , interpolation = cv.INTER_CUBIC  )

cv.imshow("Resized _image", resized )


#--------------- Fliping ---------------

flip =  cv.flip(img , 1)
cv.imshow("Flip", flip )

# if you look closely , they are mirror images of each other ( img and flip  )

# flipcodes :

# 0   - vertical flip
# 1   - horizantal flip
# -1  - reversed mirror image 

reverse_mirror  =  cv.flip(img , -1)

cv.imshow('Flipcode ** -1', reverse_mirror )

cv.waitKey(0)