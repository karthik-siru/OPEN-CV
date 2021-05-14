import cv2 as cv

img = cv.imread("taj.jpg")
cv.imshow("BGR ", img )

#---------------Color-Spaces----------------------------------

   # we are not bound to just one color space ( that is BGR ). 

   # BGR IS THE DEFAULT FOR OPEN CV  .

   # There are actually many 

   # 1) GraySCale 
   # 2) RGB
   # 3) HLS
   # 4) LAB

   # let's see , how we can toggle between them . 

#-------------------------------------------------------------

# 1) Grayscale 

gray =  cv.cvtColor(img  , cv.COLOR_BGR2GRAY)
cv.imshow("GRAYSCALE", gray)

# 2) RGB 

rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
cv.imshow("RGB ", rgb)

# 3) HLS 

hls =  cv.cvtColor(img , cv.COLOR_BGR2HLS)
cv.imshow("hls", hls)

# 4) LAB 

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

cv.imshow("lab",lab)

# yeah , I know lab is just like faded look of the original image ;)


cv.waitKey(0)