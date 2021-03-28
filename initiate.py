import cv2
from video_initializer import VideoInitializer

if __name__ == '__main__':
    video_initializer = VideoInitializer()

    while True:
        frame = video_initializer.get_frame()
        resized_frame = video_initializer.resize_frame(frame, (640, 480))
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break