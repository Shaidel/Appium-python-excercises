import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('C://Toast.png',cv2.IMREAD_COLOR)
img2 = cv2.imread('C://Activity.png',cv2.IMREAD_COLOR)

grayToast = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
grayToast = cv2.bilateralFilter(grayToast, 13, 15, 15) 

grayActivity = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) 
grayActivity = cv2.bilateralFilter(grayActivity, 13, 15, 15) 

maskToast = np.zeros(grayToast.shape,np.uint8)
maskActivity = np.zeros(grayActivity.shape,np.uint8)

(x, y) = np.where(maskToast == 0)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
ToastTestImage = grayToast[topx:bottomx+1, topy:bottomy+1]

(x, y) = np.where(maskActivity == 0)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
ActivityTestImage = grayActivity[topx:bottomx+1, topy:bottomy+1]

textToast = pytesseract.image_to_string(ToastTestImage)

if "Hello selendroid toast!" in textToast:
    print ("Hello selendroid toast!")
    print ("Test 1 OK")
else:
    print ("Toast not found")
    print ("Test 1 FAIL")

textActivity = pytesseract.image_to_string(ActivityTestImage)

if "Activity will continue" in textActivity:
    print ("Activity will continue")
    print ("Test 2 OK")
else:
    print ("Toast not found")
    print ("Test 2 FAIL")