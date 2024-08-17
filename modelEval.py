from ultralytics import YOLO

# Load the trained model
model = YOLO('yolov8_trained.pt')

# Evaluate the model on the validation set
results = model.val(data='/Users/ajayprabhat/Downloads/Final_project_Parking/dataset/data.yaml',
                    imgsz=640)

# Print evaluation metrics
print("Precision:", results['metrics']['precision'])
print("Recall:", results['metrics']['recall'])
print("mAP_50:", results['metrics']['map_50'])
print("mAP_50_95:", results['metrics']['map'])
print("F1-score:", results['metrics']['f1'])
