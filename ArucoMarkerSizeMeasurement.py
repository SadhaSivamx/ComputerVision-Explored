import cv2
from object_detector import *
import numpy as np
img=cv2.imread("Deco4.jpg")
img=cv2.resize(img,(500,500))
detector=HomogeneousBgDetector()
contors=detector.detect_objects(img)
Yrperimeter=9.5
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)
corners,_,_=cv2.aruco.detectMarkers(img,dictionary,parameters=parameters)
# Drawing a polygon
corners=np.int_(corners)
#finding the ratio
aruco_perimeter=cv2.arcLength(corners[0],True)
ratio=aruco_perimeter/Yrperimeter

cv2.polylines(img,corners,True,(0,255,0),5)

for cnt in contors:
    (x,y),(w,h),angle=cv2.minAreaRect(cnt)
    Params=(x,y),(w,h),angle
    cv2.circle(img,(int(x),int(y)),5,(0,0,255),-1)
    box=cv2.boxPoints(Params)
    box=np.int0(box)
    cv2.polylines(img,[box],True,(255,102,102),2)
    cv2.putText(img, "Width {} cm".format(round(w/ratio, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN,1, (100, 200, 0), 2)
    cv2.putText(img, "Height {} cm".format(round(h/ratio, 1)), (int(x - 100), int(y + 15)),cv2.FONT_HERSHEY_PLAIN, 1, (100, 200, 0), 2)

cv2.imshow("fr",img)
cv2.imwrite("Frame3.png",img)
cv2.waitKey(0)
