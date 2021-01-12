from cv2 import cv2 
import numpy as np #numpy here for matrices i.e kernel 

#defining a kernel

kernel = np.ones((5,5),np.uint8)


img = cv2.imread(r"cat.png",1)
#cv2.imshow("Cat",img)

#to convert int gray

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("GRAY CAT",img_gray)
#gaussian blurr
# for making the blurred one from original
img_blurr = cv2.GaussianBlur(img,(7,7),0)#kernel must be odd and sigma x = 0

cv2.imshow("Blurr CAT",img_blurr)

##canny edge detector (for detecting the edges of the image )
# This can be used further in real life application like self driving car.
img_canny  = cv2.Canny(img,150,200)

cv2.imshow("Canny cat",img_canny)

##dialation of canny images edges

img_dialation  =  cv2.dilate(img_canny,kernel,iterations=1)

cv2.imshow("Dialated cat",img_dialation)

##opposite of dialation that is erode

img_erode = cv2.erode(img_dialation,kernel,iterations=1)

cv2.imshow("Eroded cat",img_erode)

cv2.waitKey(0)