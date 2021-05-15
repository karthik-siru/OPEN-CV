import cv2 as cv
import numpy as np


blank = np.zeros((500,500), dtype = "uint8")

cv.imshow("Blank",blank)

# let's draw some figures on that blank image and perform  bitwise operations

circle =  cv.circle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2) , 200 , 255, -1)
cv.imshow("Circle", circle)

rectangle =  cv.rectangle(blank.copy(),(blank.shape[1]//2 , blank.shape[0]//2),(blank.shape[1]//2 + 200 , blank.shape[0]//2+200), 255, -1)
cv.imshow("rectangle", rectangle)

# Bitwsie and 

bitwise_and =  cv.bitwise_and(circle, rectangle)
cv.imshow("Bitwise_and", bitwise_and)

# Bitwise or 

bitwise_or =  cv.bitwise_or(circle, rectangle)
cv.imshow("Bitwise_Or ", bitwise_or)

# Bitwise xor

bitwise_xor =  cv.bitwise_xor(circle, rectangle)
cv.imshow("Bitwise_Xor", bitwise_xor)

# Bitwise not

bitwise_not =  cv.bitwise_not(rectangle)
cv.imshow("bitwise _not",  bitwise_not)

cv.waitKey(0)