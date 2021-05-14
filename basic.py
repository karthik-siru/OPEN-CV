import cv2 as cv 

img = cv.imread("taj.jpg")
cv.imshow("tower", img)

# gray_scale :

gray= cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("gray" ,gray)


#blur

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT )
cv.imshow("BLUR", blur)

#edge -detection 

edges = cv.Canny(img, 125 ,150)
cv.imshow('edges', edges )


#dilated 

dilated = cv.dilate(edges , (3,3) , iterations = 2 )
cv.imshow("Dilated", dilated )

#resize 

resized = cv.resize(img, (500, 500) , interpolation=cv.INTER_CUBIC)
cv.imshow("Resized ", resized )


#cropped 

# since the image is an array ,i can slice them to get desired piece 

cropped = img[100:300 , 200 : 500]
cv.imshow("Cropped", cropped )

cv.waitKey(0)