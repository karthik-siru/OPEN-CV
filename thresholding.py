import cv2 as cv
import numpy as np

img = cv.imread("puppies.jpg")
cv.imshow("Puppies", img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)


#---------------------------theory -------------------------
'''
     So , what is thresholding --> binarising the images .

     binary numbers are only two , either 1 or 0 . 

     similarly , we will turn our 'grayscale image'into either pure black 
     or pure white  , by binarising it . 

     two types of thresholding 

     1) Simple Thresholding 

     For move advanced projects , selecting the threshold value manually .
     is not a good option .. hence we need adaptive thresholding . 

     cv.adaptiveThreshold(img  , max_value ,[ cv.ADAPTIVE_THRESH_MEAN_C  , gaussian ], threshold type , kernel size  , bias )

     bias - used for finding central pixel intensity  i.e ( Mean of surrounding - Bias )

     2) Adaptive thresholding 

'''
#----------------------------------------------------------

# 1) Simple Thresholding 

# the second parameter decides the thresholded image .. 

# if  pixel intensity > second parameter  :
#     --> pixel intensity = max_value (third parameter)

# else : 
#     -->  pixel intensity = 0 .


threshold , thresh = cv.threshold(gray, 125 , 255  , cv.THRESH_BINARY  )
cv.imshow("Thresholding_Image ", thresh )

 
# Inverse thresholding 

threshold, inverse_threshold =  cv.threshold(gray ,125 , 255  ,cv.THRESH_BINARY_INV)
cv.imshow("Inverse_Threshold_Image", inverse_threshold)


# 2) Adaptive Thresholding 

adaptive_threshold = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 , 5)
cv.imshow("Mean-Adaptive-Threshold-Image", adaptive_threshold)


# let's see the inverse of thea above 

adaptive_threshold_inv = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY_INV , 11 , 5)
cv.imshow("Mean-Adaptive-Threshold-Image-Inverse", adaptive_threshold_inv)

# gaussian -Adaptive :

gaussian_adaptive_threshold = cv.adaptiveThreshold(gray ,255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C ,cv.THRESH_BINARY , 11, 5)
cv.imshow("Gaussian-Adaptive-Threshold image ", gaussian_adaptive_threshold)


cv.waitKey(0)