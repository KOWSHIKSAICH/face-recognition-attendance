from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

attendance_file = "attendance/attendance.csv"

@app.route("/")
def index():
    if os.path.exists(attendance_file):
        try:
            df = pd.read_csv(attendance_file)
            print("\n[DEBUG] Attendance Data Read from CSV:\n", df)  # Debugging step
            
            if df.empty:
                print("[DEBUG] CSV file is empty (only headers).")
                records = []
            else:
                records = df.to_dict(orient="records")
        except Exception as e:
            print("[ERROR] Could not read CSV file:", e)
            records = []
    else:
        print("[DEBUG] CSV file does not exist.")
        records = []

    return render_template("index.html", attendance=records)

if __name__ == "__main__":
    app.run(debug=True)
