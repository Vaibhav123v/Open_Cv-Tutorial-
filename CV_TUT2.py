#importing a video using opencv
from cv2 import cv2
            
cap = cv2.VideoCapture(r"k.mp4")

# A video is a sequence of images so we will use a  while loop to capture our image

while True:
    success,img = cap.read()
    cv2.imshow("Video ",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
     