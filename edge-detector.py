import mss
import numpy as np
import cv2 as cv


bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

sct = mss.mss()

while True:
    # So many edges, it is hard to determine what is a ledge that can be jumped on
    # Maybe searching for corners, and testing if it can jump on the surface the
    # corner is connected to.
    screen = sct.grab(bounding_box)
    img = np.array(screen)
    edges = cv.Canny(img,100,200)
    
    scaled_img = cv.resize(edges, (960, 540))
    cv.imshow("edges", np.array(scaled_img))    
    if cv.waitKey(1) & 0xFF == 27:
       break
    
cv.destroyAllWindows()