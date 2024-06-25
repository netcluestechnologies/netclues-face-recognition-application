import face_recognition
import os
import sys
import cv2
import numpy as np
import math


def face_confidence(face_distance, face_match_threshold=0.6):
    """
    Calculate the confidence level of a face match.

    :param face_distance: The distance between the faces.
    :param face_match_threshold: The threshold for a match.
    :return: Confidence as a string percentage.
    """
    if face_distance > face_match_threshold:
        return f'{round((1 - face_distance) * 100, 2)}%'
    else:
        range_val = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range_val * 2.0)
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return f'{round(value, 2)}%'


class FaceRecognition:
    def __init__(self, dataset_dir='dataset', video_source=0):
        """
        Initialize the FaceRecognition system.

        :param dataset_dir: Directory containing subdirectories of known faces.
        :param video_source: Video source (default is 0 for webcam).
        """
        self.dataset_dir = dataset_dir
        self.video_source = video_source
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.known_face_encodings = []
        self.known_face_names = []
        self.process_current_frame = True

        self.encode_faces()

    def encode_faces(self):
        """Load and encode known faces from the dataset directory."""
        try:
            for person_name in os.listdir(self.dataset_dir):
                person_dir = os.path.join(self.dataset_dir, person_name)
                if os.path.isdir(person_dir):
                    for image_name in os.listdir(person_dir):
                        image_path = os.path.join(person_dir, image_name)
                        if os.path.isfile(image_path) and image_name.lower().endswith(('png', 'jpg', 'jpeg')):
                            face_image = face_recognition.load_image_file(image_path)
                            face_encodings = face_recognition.face_encodings(face_image)
                            if face_encodings:
                                self.known_face_encodings.append(face_encodings[0])
                                self.known_face_names.append(person_name)
                                print(f"Encoded {person_name}: {image_name}")
        except Exception as e:
            print(f"Error encoding faces: {e}")
            sys.exit(1)

    def run_recognition(self):
        """Start face recognition using the video source."""
        video_capture = cv2.VideoCapture(self.video_source)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        try:
            while True:
                ret, frame = video_capture.read()
                if not ret:
                    print("Failed to capture image")
                    break

                if self.process_current_frame:
                    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

                    # Find all faces in the current frame
                    self.face_locations = face_recognition.face_locations(rgb_small_frame)
                    self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                    self.face_names = []
                    for face_encoding in self.face_encodings:
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                        name = 'Unknown'
                        confidence = '0%'

                        face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)

                        if matches[best_match_index]:
                            name = self.known_face_names[best_match_index]
                            confidence = face_confidence(face_distances[best_match_index])

                        self.face_names.append(f'{name} ({confidence})')

                self.process_current_frame = not self.process_current_frame

                self.annotate_frame(frame)

                cv2.imshow('Face Recognition', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()

    def annotate_frame(self, frame):
        """
        Draw rectangles and names around detected faces.

        :param frame: The current video frame.
        """
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top = top * 4 - 20
            right = right * 4 + 20
            bottom = bottom * 4 + 20
            left = left * 4 - 20

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)  # Blue color in BGR

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 0), -1)  # Blue color in BGR
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)


if __name__ == '__main__':
    FaceRecognition().run_recognition()
