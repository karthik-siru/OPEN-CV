import cv2 as cv
import numpy as np

img =  cv.imread("dog.jpg")
cv.imshow("Dog", img)

blank = np.zeros(img.shape[:2], dtype = "uint8")
cv.imshow("Blank",blank)

# let's create a mask shape and mask it on dog image

circle =  cv.circle(blank.copy(), (blank.shape[1]//2 , blank.shape[0]//2), 150 , 255, -1)
cv.imshow("Circle", circle)

# Circle mask

circle_mask = cv.bitwise_and(img, img, mask = circle )
cv.imshow("Circle_masked", circle_mask)

# Rectangle_mask

rectangle = cv.rectangle(blank.copy(),(blank.shape[1]//2 , blank.shape[0]//2) , (blank.shape[1]//2 +200 , blank.shape[0]//2 + 200) ,255 , -1)
cv.imshow("rectangle", rectangle)

rectangle_mask = cv.bitwise_and(img,img, mask = rectangle)
cv.imshow("Rectangle_Mask", rectangle_mask)

# let's create a weiird mask 

xor_ = cv.bitwise_xor(circle , rectangle)
or_ =  cv.bitwise_or(circle,rectangle)

weird = cv.bitwise_and(xor_ , or_)

# Mask it to the image

weird_mask = cv.bitwise_and(img , img , mask = weird)
cv.imshow("Weird_Masked_Image", weird_mask)

cv.waitKey(0) # waits until 0 is entered .