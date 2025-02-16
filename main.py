import face_recognition
import os
import cv2
import pickle
import datetime
import pandas as pd

# Check if the trained model exists
if not os.path.exists("models/face_encodings.pkl"):
    print("Error: 'models/face_encodings.pkl' not found. Please train the model first.")
    exit()

# Load trained face encodings
with open("models/face_encodings.pkl", "rb") as file:
    known_faces = pickle.load(file)

cap = cv2.VideoCapture(0)

# Create or load attendance file
attendance_file = "attendance/attendance.csv"
if not os.path.exists(attendance_file) or os.stat(attendance_file).st_size == 0:
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_csv(attendance_file, index=False)

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(list(known_faces.values()), encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = list(known_faces.keys())[match_index]

            # Mark attendance
            df = pd.read_csv(attendance_file)

            new_entry = pd.DataFrame([{"Name": name, "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}])
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(attendance_file, index=False)

            # Debug: Print Attendance Data
            print("\n[DEBUG] Attendance Updated:\n", df)

        # Draw rectangle and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Face Recognition Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
