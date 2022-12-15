import cv2
import numpy as np

picture=np.zeros((540,540,3),np.uint8)

cv2.imshow("resim",picture)
cv2.waitKey()
cv2.destroyAllWindows()







#cam = cv2.VideoCapture(0)
# vid.get(3)
# vid.get(4)

# vid.set(3,240)
# vid.set(4,500)

# while(True):
      
   
#     ret, frame = vid.read()
  
#     cv2.imshow('frame', frame)
      
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
  

# vid.release()
#  # cv2.destroyAllWindows()
