from cv2 import cv2
#img = cv2.imread(r"C:\Users\asus\Pictures\Screenshots\t.png",1)#reading the image 
img2 = cv2.imread(r"C:\Users\asus\Desktop\cat.png",1)
print(cv2.__version__) #for getting the current version of cv2
#cv2.imshow("Original image",img)#for dispalying the image
cv2.imshow("Cat Image",img2)
cv2.waitKey(0)#to hold the output screen (0) infinite delay (x) time 

