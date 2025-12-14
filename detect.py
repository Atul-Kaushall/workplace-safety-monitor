from ultralytics import YOLO
import cv2
import time
import requests
import json

# Load YOLO model
model = YOLO("yolov8n.pt")  # small model

# Hazard detection keywords (simple beginner rules)
HAZARDS = ["person"]

def detect_hazards(frame):
    results = model(frame)
    hazards_found = []
    for r in results:
        for box in r.boxes:
            cls = model.names[int(box.cls[0])]
            if cls in HAZARDS:
                hazards_found.append(cls)
    return hazards_found

# Read sample CCTV video
cap = cv2.VideoCapture("sample.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hazards = detect_hazards(frame)
    
    if hazards:
        print("⚠️ Hazard detected:", hazards)

        # Trigger Kestra workflow
        requests.post("http://localhost:8080/api/v1/executions", 
                      json={"flowId": "safety.alert"})

    cv2.imshow("AI Safety Monitor", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
