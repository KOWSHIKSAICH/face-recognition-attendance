import cv2
import os

# Load OpenCV's face detector
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_faces(name):
    cap = cv2.VideoCapture(0)
    count = 0
    path = f"dataset/{name}"
    os.makedirs(path, exist_ok=True)

    while count < 50:  # Capture 50 images per person
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y + h, x:x + w]
            cv2.imwrite(f"{path}/{count}.jpg", face)
            count += 1

        cv2.imshow('Capturing Faces', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Enter a person's name
name = input("Enter name of person: ")
capture_faces(name)
