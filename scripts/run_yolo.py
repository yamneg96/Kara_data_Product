from ultralytics import YOLO
import os
import json

model = YOLO("yolov8n.pt")

image_dir = "data/raw/images"
detections = []

for image in os.listdir(image_dir):
    if image.endswith(".jpg") or image.endswith(".png"):
        results = model(image_dir + "/" + image)
        for r in results:
            for box in r.boxes.data.tolist():
                detections.append({
                    "image": image,
                    "class": r.names[int(box[5])],
                    "confidence": box[4]
                })

with open("data/raw/yolo_detections.json", "w") as f:
    json.dump(detections, f, indent=2)
