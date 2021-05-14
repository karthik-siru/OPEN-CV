import cv2 as cv
import numpy as np 

img = cv.imread("taj.jpg")

cv.imshow("Original", img)

blank = np.zeros(img.shape , dtype = "uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale ", gray)

# let's blur this image for better contour detection 

blur = cv.GaussianBlur(gray , (5,5), cv.BORDER_DEFAULT)
cv.imshow("Gray_blur", blur)

#---------------------  THRESHOLD _ FUNCTION -----------------------

# another way to draw contours is to use threshold fucntion ..

# threshold function is just a simple function , it take the gray picture as input .. 
# The method returns two outputs. The first is the threshold that was used and
# the second output is the thresholded image.
# if the darkness value is greater than 125, it will make 255.
# if the darkness value is less than 125, it will make 0 . 
# and returns the corresponding matrix of changed function 

# the 4th argument is thresh_binary can have various modes also 

ret , thresh = cv.threshold(gray , 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh_image ", thresh )

ret1 , thresh1 = cv.threshold(gray , 125, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh_image_Binary_Inverse ", thresh1 )

ret2 , thresh2 = cv.threshold(gray , 125, 255, cv.THRESH_TOZERO)
cv.imshow("Thresh_image_to zero ", thresh2 )

ret3 , thresh3 = cv.threshold(gray , 125, 255, cv.THRESH_TOZERO_INV)
cv.imshow("Thresh_image_to_zero_inverse  ", thresh3 )


#--------------------------------------------------------------------------

canny =  cv.Canny(gray, 125, 175)
cv.imshow("Edges detection", canny)

contours , heirarchy = cv.findContours(thresh  , cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours), " contours  found ")

#--------------------------contours and heirarchy ------------------------

    # findcontours takes  canny ( edge detection images ) and two modes 

    # cv.RETR_LIST       --  all contours 
    # cv.RETR_EXTERNAL   --  computes only external contours 
    

    # cv.CHAIN_APPROX_SIMPLE  --- finds only the simple contours 
    # cv.CHAIN_APPROX_NONE    --- it is little bit complex and finds everything . 

#-------------------------------------------------------------------------

cv.drawContours(blank, contours , -1 , (255,0,100), 2)
cv.imshow("Contours_Drawn", blank )

cv.waitKey(0)