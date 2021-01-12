#resizing and cropping
from cv2 import cv2

img  = cv2.imread(r"cat.png",1)

print(img.shape)#(height = 246,width = 205,channel(BGR)=3)

img_resize = cv2.resize(img,(300,200))
print(img_resize.shape)

cv2.imshow("Original Cat",img)
cv2.imshow("Resized Cat",img_resize)

##Cropping

img_cropped  =img[100:150,200:300]#height,width
cv2.imshow("Cropped_cat",img_cropped)


cv2.waitKey(0)
