from cv2 import cv2
cap  = cv2.VideoCapture(0)#for your default webcam or add id 
cap.set(3,640)# 3 is id for width 
cap.set(4,480)# 4 is id for height
cap.set(10,85)#10 for brightness

while True:
    success,img = cap.read()
    cv2.imshow("Web Cam",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break