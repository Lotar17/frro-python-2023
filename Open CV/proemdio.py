import cv2
import numpy as np

cap = cv2.VideoCapture("/home/lkblkb/TPIK/frro-python-2023/Proyectos Kivy/Video Player/Videos TPI/fish.mp4")

_, img = cap.read()

averageValue1= np.float32(img)

while(1):
    _, img = cap.read()

    cv2.accumulateWeighted(img,averageValue1, 0.02)

    resultingFrames1 = cv2.convertScaleAbs(averageValue1)

    cv2.imshow('InputWindow', img)

    cv2.imshow('averageValue1', resultingFrames1)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break