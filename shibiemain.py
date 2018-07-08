#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cv2
import numpy as np
import time

aaa=0
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('/home/yck/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rect = cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5),flags=cv2.CASCADE_SCALE_IMAGE)
    for x, y, z, w in rect:
        cv2.rectangle(frame, (x, y), (x + z, y + w), (0, 0, 255), 2)
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    lenrect=len(rect)
    aaa = lenrect+aaa
    if aaa >= 50:
        cv2.imwrite("text.jpg",frame) 
        break
cap.release()
cv2.destroyAllWindows()

