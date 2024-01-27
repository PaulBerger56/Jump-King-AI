import cv2, mss, os, threading
import numpy as np

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
image_folder_path = r"Images"

files = os.listdir(image_folder_path)
reference_images = []

for file_name in files:
    
    if file_name.endswith('.PNG'):
       file_path = os.path.join(image_folder_path, file_name)
       
       image =  cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
       
       reference_images.append(image)
       
sct = mss.mss()

while True:
    sct_img = sct.grab(bounding_box)    
    img = np.array(sct_img)    
    
    for ref_img in reference_images:
        w = ref_img.shape[1]
        h = ref_img.shape[0]
        
        ref_img_result = cv2.matchTemplate(img, ref_img, cv2.TM_CCOEFF_NORMED)
        ref_img_min_val, ref_img_max_val, ref_img_min_loc, ref_img_max_loc = cv2.minMaxLoc(ref_img_result)
        
        ref_img_threshold = .48
        ref_img_yloc, ref_img_xloc = np.where(ref_img_result >= ref_img_threshold)
        
        rectangles = []
        for (x, y) in zip(ref_img_xloc, ref_img_yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])    
        
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        for (x, y, w, h) in rectangles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
            
        
            
    
    scaled_img = cv2.resize(img, (960, 540))
    cv2.imshow('Screen Capture', np.array(scaled_img))
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()