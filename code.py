import cv2
videocapureobject=cv2.VideoCapture(0)
ret,frame=videocapureobject.read()
cv2.imwrite('capture.png',frame)
videocapureobject.release()
cv2.destroyAllWindows()