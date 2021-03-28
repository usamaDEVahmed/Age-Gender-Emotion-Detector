import cv2
from video_initializer import VideoInitializer
from face_detector import FaceDetector

if __name__ == '__main__':
    video_initializer = VideoInitializer()
    face_detector = FaceDetector()

    while True:
        frame = video_initializer.get_frame()
        resized_frame = video_initializer.resize_frame(frame, (640, 480))
        faces_coords = face_detector.detect_faces(resized_frame)
        face_detector.plot_coords(resized_frame, faces_coords)
        cv2.imshow('Face Detector', resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break