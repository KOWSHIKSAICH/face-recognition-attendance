import pyrebase
import datetime

firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT.firebaseapp.com",
    "databaseURL": "https://YOUR_PROJECT.firebaseio.com",
    "storageBucket": "YOUR_PROJECT.appspot.com"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

def mark_attendance_firebase(name):
    db.child("Attendance").push({"name": name, "time": str(datetime.datetime.now())})
