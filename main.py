import cv2
import  numpy as np
import os 
from PIL import ImageGrab
import cv2.aruco as aruco

def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):
    # change image to grey scale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters= arucoParam)
    print(ids)
    if draw:
        aruco.drawDetectedMarkers(img,bboxs)


def main():

    while(True):
        #printscreen_pil =  ImageGrab.grab()
        printscreen_numpy =  printscreen =  np.array(ImageGrab.grab(bbox=(0,0,700,700)))
        frame = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)
        findArucoMarkers(frame)
        cv2.imshow('window',frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows
      
if (__name__ == "__main__"):

    print("main")
    main()

