import face_recognition
import pickle
import os

face_encodings = {}

for person in os.listdir("dataset"):
    images = os.listdir(f"dataset/{person}")
    encodings = []

    for img in images:
        image = face_recognition.load_image_file(f"dataset/{person}/{img}")
        encoding = face_recognition.face_encodings(image)

        if encoding:
            encodings.append(encoding[0])

    if encodings:
        face_encodings[person] = encodings[0]

# Save the encodings
with open("models/face_encodings.pkl", "wb") as file:
    pickle.dump(face_encodings, file)

print("Training completed! Face encodings saved.")
