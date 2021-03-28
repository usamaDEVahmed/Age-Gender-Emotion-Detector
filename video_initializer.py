import cv2

class VideoInitializer():

    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)

    
    def get_frame(self):
        return_flag, frame = self.video_capture.read()
        
        if return_flag:
            return frame
        else:
            return []

    
    def resize_frame(self, frame, size):
        resized_frame = cv2.resize(frame, size)
        return resized_frame
