import cv2
from video_initializer import VideoInitializer
from face_detector import FaceDetector

if __name__ == '__main__':
    video_initializer = VideoInitializer()
    face_detector = FaceDetector()

    while True:
        frame = video_initializer.get_frame()
        resized_frame = video_initializer.resize_frame(frame, (640, 480))
        face_coords = face_detector.detect_faces(resized_frame)
        # face_detector.plot_coords(resized_frame, face_coords)
        cropped_face = face_detector.get_cropped_face(resized_frame, face_coords)
        cv2.imshow('Face', cropped_face)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break