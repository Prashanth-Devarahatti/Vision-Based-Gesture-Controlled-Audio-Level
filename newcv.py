import cv2
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

# Function to calculate volume based on hand distance
def calculate_volume(length):
    vol_range = volume.GetVolumeRange()
    min_vol, max_vol = vol_range[0], vol_range[1]
    return np.interp(length, [50, 00], [min_vol, max_vol])

# Function to draw landmarks on hands
def draw_landmarks(img, multi_hand_landmarks):
    lmList = []
    if multi_hand_landmarks:
        for handLms in multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    return lmList

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,  # Corrected attribute access
    CLSCTX_ALL,
    None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Process hand landmarks
    lmList = draw_landmarks(img, results.multi_hand_landmarks)

    if lmList:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        z1, z2 = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        if length < 50:
            cv2.circle(img, (z1, z2), 15, (255, 255, 255), cv2.FILLED)

        vol = calculate_volume(length)
        volume.SetMasterVolumeLevel(vol, None)
        volBar = np.interp(length, [50, 300], [400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])

        cv2.rectangle(img, (50, 150), (85, 400), (123, 213, 122), 3)
        cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 231, 23), cv2.FILLED)
        cv2.putText(img, str(int(volPer)), (40, 450), cv2.FONT_HERSHEY_PLAIN, 4, (24, 34, 34), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
