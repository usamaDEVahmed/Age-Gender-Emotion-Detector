import cv2
import numpy as np

class FaceDetector():

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    

    def preprocess(self, frame):
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return gray_image

    def detect_faces(self, frame):
        gray_image = self.preprocess(frame)
        faces_coords = self.face_cascade.detectMultiScale(gray_image)
        
        return faces_coords

    def plot_coords(self, frame, coords):
        for x, y, w, h in coords:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)