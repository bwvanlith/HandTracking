import cv2
import time
import os
import HandTrackingModule as htm
import math


# Webcam settings
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


# load the hand images from folder and store them in a list
folderPath = "Hand_Images"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    # load the hand images from folder
    image = cv2.imread(f'{folderPath}/{imPath}')
    # store/append the hand images to list
    overlayList.append(image)

# print length of the list
# print(len(overlayList))

# create object from handtracking module class
detector = htm.handDetector(detectionCon=0.75)



while True:
    success, img = cap.read()
    # find hands with and return the image
    img = detector.findHands(img)
    # create list from detected landmarks without drawing cause we already do that
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # lmList item 8 has 1,2,3 values (x,y,z position)
        # so compare height of 8 with height with 6
        #if lmList[8][2] < lmList[6][2]:
        #   print("index finger open")
        #else:
        #   print("index finget closed")

        #############  CUSTOM CODE #########################
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[5][1], lmList[5][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        x4, y4 = lmList[9][1], lmList[9][2]
        x5, y5 = lmList[16][1], lmList[16][2]
        x6, y6 = lmList[13][1], lmList[13][2]
        x7, y7 = lmList[20][1], lmList[20][2]
        x8, y8 = lmList[17][1], lmList[17][2]

        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x4, y4), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x5, y5), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x6, y6), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x7, y7), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x8, y8), 10, (255, 0, 255), cv2.FILLED)

        # create line between 4 and 8
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.line(img, (x3, y3), (x4, y4), (255, 0, 255), 2)
        cv2.line(img, (x5, y5), (x6, y6), (255, 0, 255), 2)
        cv2.line(img, (x7, y7), (x8, y8), (255, 0, 255), 2)

        # get center of the line
        #cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        # draw circle on the center of the line
        #cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        # find the length of the line between 4 and 8
        lengthindex = math.hypot(x2 - x1, y2 - y1)
        lengthmiddle = math.hypot(x4 - x3, y4 - y3)
        lengthring = math.hypot(x6 - x5, y6 - y5)
        lengthpinky = math.hypot(x8 - x7, y8 - y7)
        lengthList = [lengthindex, lengthmiddle, lengthring, lengthpinky]
        #print(lengthList)


        #from playsound import playsound
        #playsound('audio.mp3')


        #############  CUSTOM CODE #########################




    # show the loaded hand images on screen at position (0,height) and (0,width)
    h,w,c = overlayList[0].shape
    img[0:h, 0:w] = overlayList[0]

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # print fps on screen
    cv2.putText(img, f'FPS: {int(fps)}', (320,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)

    #show webcam image
    cv2.imshow("Image", img)
    cv2.waitKey(1)
