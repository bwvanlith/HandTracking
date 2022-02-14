import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

#### Webcam Settings ####
wCam, hCam = 1080, 720
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
# time for fps
pTime = 0

# create object from handtrackingmodule class
detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    # find the hand
    img = detector.findHands(img)
    #list all positions of the 21 points
    lmList = detector.findPosition(img, draw=False)
    # check is list isn't empty
    if len(lmList) != 0:
        #print position of landmark 4 and 8
        #print(lmList[4], lmList[8])

        #draw circle on 4 and 8
        x1, y1 = lmList[4][1],lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

        # create line between 4 and 8
        cv2.line(img, (x1,y1),(x2,y2), (255,0,255), 3)

        # get center of the line
        cx, cy = (x1+x2)//2, (y1+y2)//2
        #draw circle on the center of the line
        cv2.circle(img, (cx, cy), 10, (255,0,255), cv2.FILLED)

        # find the length of the line between 4 and 8
        length = math.hypot(x2-x1,y2-y1)
        print(length)

        # change dot color if length is less than 50
        if length<50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        # change volume based on length of line


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(40,70), cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),2)
    cv2.imshow("Img", img)
    cv2.waitKey(1)
