from ultralytics import YOLO

# Load a YOLOv8 model (you can use 'yolov8n.pt' for the nano version)
model = YOLO('yolov8n.pt')  # or 'yolov8s.pt', 'yolov8m.pt', etc.

# Train the model with the dataset
model.train(data='dataset/data.yaml', epochs=50, imgsz=640, batch=16)
