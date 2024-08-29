from ultralytics import YOLO

model = YOLO('yolov8x.pt')

# Train the model with your dataset
results = model.train(data='/Users/ajayprabhat/Downloads/Final_project_Parking/dataset/data.yaml',
                      epochs=50,
                      imgsz=640)

# Debug: Print the model checkpoint
print("Model checkpoint state:", model.ckpt)

# Save the trained model
if model.ckpt is not None:
    model.save("yolov8x_trained.pt") #weights file
else:
    print("Error: Model checkpoint is None, model not saved.")
