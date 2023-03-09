from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m-seg.yaml")  # build a new model from scratch
#model = YOLO("yolov8n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model
model.train(data="faceplate-seg.yaml", epochs=300, imgsz=704,batch=4)
