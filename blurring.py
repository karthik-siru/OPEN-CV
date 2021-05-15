import cv2 as cv
import numpy as np

img = cv.imread("cat.jpg")

cv.imshow("Cat", img)

#------------------------ Theory ---------------------------
'''
    Let's learn about kernel size . Suppose we choose
    kernel size as (3,3) .. so it will decide the blurring 
    intensity of the center pixel using the surrounding pixels..
    This (3,3) will slide all over the image 

    ex : the given values are intensities of the pixels 
    
            1   2    3 
            3   --   4
            6   2    1

    1)  Average Blurring :

       blurness of the center pixel is the average of all of them 

       (1+2+3+3+4+6+2+1) /8 

    
    2) Gaussian Blur :

       certain weights are given to the surronding pixels and the 
       intensity of the middle is calculated .

    3) Medain Blur :
      
      center pixel intensity will be median of the surrounding one .

    4) Bilateral blur :

      diameter of the blur circle is needed and the pixel intensity is 
      calculated . edges are preserved .. 

'''
#-----------------------------------------------------------

# average blur:

average = cv.blur(img , (7,7))
cv.imshow("Average-Blur", average )

# Gaussian Blur 

# Gaussian blur is far better than average ,it looks natural 

gblur = cv.GaussianBlur(img , (7,7) , 0)
cv.imshow("Gaussian-blur", gblur)

# Median Blur 
''' Medainblur  will automatically selects (n,n ) as kernel size ..
    where n is second parameter . '''

mblur = cv.medianBlur(img , 3) 
cv.imshow("Median-Blur",mblur)

# Bilateral Blur 

bblur = cv.bilateralFilter(img , 5, 15,20)
cv.imshow("bilateral blur", bblur)

#lets see when we increase the diameter size 

bblur2 = cv.bilateralFilter(img, 20, 15 ,20)
cv.imshow("Bilateral-large-diameter", bblur2)

# not much difference noticed , let's play with remaining two parameters

bblur3 = cv.bilateralFilter(img, 10, 35,40)
cv.imshow("Bilateral blur- changed parameters", bblur3)

cv.waitKey(0)