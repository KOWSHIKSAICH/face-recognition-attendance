# **Face Recognition-Based Automatic Attendance System**

## **📌 Project Overview**
The **Face Recognition-Based Automatic Attendance System** is an AI-powered solution that automates attendance marking using **facial recognition**. The system detects and recognizes faces from a live camera feed and records attendance in a **CSV file**, which can be accessed via a **Flask web application**.

### **🎯 Features**
✅ **Face Detection & Recognition** using OpenCV and Dlib  
✅ **Real-time Camera Capture** for recognizing students/employees  
✅ **Automated Attendance Logging** in `attendance.csv`  
✅ **Web Interface** (Flask) to View Attendance Records  
✅ **Data Storage** using CSV or Firebase (Optional)  

---

---

## **🛠️ Tools & Libraries Used**

### **1️⃣ Programming Language**
- **Python** 🐍 → Used for backend, face recognition, and data processing  

### **2️⃣ Machine Learning & AI**
- **OpenCV** → For image processing and real-time face detection  
- **Face Recognition (Dlib)** → To recognize faces and match them with stored data  

### **3️⃣ Backend**
- **Flask** → Used to create a web-based interface for viewing attendance records  
- **Pandas** → For handling CSV files and attendance data  
- **Pickle** → To store trained face encodings  

### **4️⃣ Database & Storage**
- **CSV (attendance.csv)** → Simple data storage  
- **Firebase (Optional)** → Cloud-based attendance tracking  

### **5️⃣ Frontend (Web Interface)**
- **HTML, CSS** → Used in Flask templates for displaying attendance records  

---

## **🛠️ How It Works?**

### **1️⃣ Capture and Train Faces**
- The system captures multiple images of a person’s face and stores them in the `dataset/` folder.  
- **train.py** extracts face embeddings and saves them as `face_encodings.pkl`.  

### **2️⃣ Real-time Face Recognition & Attendance Marking**
- **main.py** opens the webcam, detects faces, and compares them with the trained data.  
- If a face is **recognized**, it marks attendance in `attendance.csv`.  

### **3️⃣ View Attendance in Web Dashboard**
- **Flask app (`app.py`)** reads `attendance.csv` and displays attendance records on a webpage.  

---

## **🚀 Future Enhancements**
✔ **Deploy Online (AWS, Heroku, Firebase)**  
✔ **Mobile App (Flutter) for Attendance Tracking**  
✔ **Live Notifications (Email, SMS Alerts)**  
✔ **Improve Accuracy Using Deep Learning (FaceNet, CNNs)**  

---

## **📌 How to Run the Project?**


# 1️⃣ Clone the Repository
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance

# 2️⃣ Install Dependencies
pip install -r requirements.txt

# 3️⃣ Capture Faces
python capture_faces.py

# 4️⃣ Train Face Recognition Model
python train.py

# 5️⃣ Run Face Recognition & Mark Attendance
python main.py

# 6️⃣ Start Flask Web App
python web/app.py
