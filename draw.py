import cv2 as cv 
import numpy as np

blank =  np.zeros((500 , 500 , 3), dtype =  'uint8')
cv.imshow('blank', blank)


# Painting a solid color :

blank[:] = (0,124,21)

cv.imshow('new color', blank)


# a random shape :

blank[0:200 , 100 : 300] =  (124,125,2)

cv.imshow('new_color 1', blank)



# Drawing shapes with built in methods 

# drawing a line 

cv.line(blank, (0,0) , (250,250) , (0,255,0) , thickness = 2 )
cv.imshow('line', blank)

#drawing a rectangle :

cv.rectangle(blank, (100,100) , (250,250), (0,255,0) ,thickness = cv.FILLED) # thickness parameter -1 to fill color 
cv.imshow('rectangle', blank)


# drawing the circle :

cv.circle(blank , (250,250), 60 , (100,150,120) , thickness = -1)
cv.imshow("circle", blank)


# put text on image :

cv.putText(blank, "hello open cv , I am coming ", (0,250),cv.FONT_HERSHEY_COMPLEX  , 1.0  ,(0,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
