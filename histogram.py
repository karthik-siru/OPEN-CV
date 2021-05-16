import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

# ---------------------Theory ---------------------
   
'''

    So , histograms help to analyse the intensities 
    of the pixels in the given image . Like how many 
    pixels are there with certain intensity and all.

'''

# -------------------------------------------------

img = cv.imread("cat.jpg")
cv.imshow("Cat", img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow("Gray_Image", gray)

blank_gray = np.zeros(img.shape[:2], dtype = "uint8")
cv.imshow("Blank",blank_gray)

mask = cv.circle(blank_gray, (blank_gray.shape[1]//2 , blank_gray.shape[0]//2) , 100 , 255, -1)

masked_image =  cv.bitwise_and(gray , gray , mask =  mask )
cv.imshow("Masked_Image", masked_image)

# Grayscale Histogram 

gray_hist = cv.calcHist([gray], [0] , None , [256] , [0,256] )

gray_hist_mask = cv.calcHist([gray], [0], mask , [256], [0,256])

plt.figure()
plt.title('Gray_SCale _Hisogram ')
plt.xlabel("Bins")
plt.ylabel("Number of pixels ")
plt.plot(gray_hist)
plt.show()


plt.title('Gray_SCale_Hisogram_with mask ')
plt.xlabel("Bins")
plt.ylabel("Number of pixels ")
plt.plot(gray_hist_mask)
plt.show()


# Coloured Image Histogram ::

# second parameter is the histogram index number

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.title("Color_Histogram ")
plt.show()


cv.waitKey(0)