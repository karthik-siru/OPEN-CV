import cv2 as cv
import numpy as np

# color channels -- so we can divide an image into respective color channels like red , green , blue .

img = cv.imread("taj.jpg")

cv.imshow("Taj", img)

b,g,r = cv.split(img)

# the lighters portions in b,g,r represents the high concentrations  of respective colors 

cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red",r)


# So let's see  how to merge to get back the original image 

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

# but bro.. when we split , we are viewing them as green scale images .. 
# let's see how to visualize them in color spaces 

blank = np.zeros(img.shape[:2], dtype = "uint8")

# we are creating the images using merge function , but we are passing only one argument ..
# and the other two as blank 

blue = cv.merge([b,blank,blank])
green =  cv.merge([blank, g,blank])
red  =  cv.merge ([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

# now  you realise that gray scale images are far better  to know the intensities of color channels 

cv.waitKey(0) # waits until 0 is pressed . 