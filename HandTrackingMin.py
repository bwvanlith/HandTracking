import cv2
import mediapipe as mp
import time

# create video object from webcam 1
cap = cv2.VideoCapture(0)

# create object from the class hand - see Hands for parameters
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# draw both hands
mpDraw = mp.solutions.drawing_utils

# previous and current time
pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    # send in rgb images to hand object
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # extract multiple and check if multiple hands or not
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        # extract information for each hand
        for handLms in results.multi_hand_landmarks:
            # get hand info, coordinates and id (0 is bottem, etc.)
            for id, lm in enumerate(handLms.landmark):
                # width and height
                h, w, c = img.shape
                # get center position for each landmark
                cx, cy = int(lm.x*w), int(lm.y*h)
                # if id == 0:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # draw both hands
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    # calculate fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # display fps on screen: position, font, size, color, scale
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)