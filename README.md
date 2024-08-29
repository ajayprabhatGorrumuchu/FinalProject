# Building a Parking Space Recognition System

## Project Overview

This project utilizes the YOLOv8x, ssd, fasterrcnn model for detecting cars in a parking lot and determining the occupancy status of parking spaces. The system processes a video input, identifies cars using object detection, and maps them to predefined parking spaces to determine which spots are occupied and which are available.

## Files Included

- **`fasterRcnnInference.py`**: A script for parking detection using an fasterRcnn  model.
- **`ssdTraining.py`**: A script for training the ssd model on a custom dataset.
- **`ssdInference.py`**: The script that uses the trained ssd model to detect cars in a parking lot and determine parking space occupancy.
- **`trainYolo.py`**: A script for training the yolov8x model on a custom dataset.
- **`yolov8xInference.py`**: The script that uses the trained yolov8x model to detect cars in a parking lot and determine parking space occupancy.
- **`requirements.txt`**: A file listing all necessary Python packages to run the project.
- **`README.md`**: This file.

## Prerequisites

- Python 3.8 or higher
- A working GPU environment is recommended for faster processing, but the code can also run on a CPU.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ajayprabhatGorrumuchu/FinalProject
    cd FinalProject
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that you have the necessary video files and dataset for training.We can download required files from below links.
- video input file : https://drive.google.com/file/d/1smnIbcz23RP1vDaQxbpE0Siy9AhkY5oj/view?usp=share_link
- Dataset Link : https://storage.googleapis.com/openimages/web/visualizer/index.html
?type=detection&set=train&c=%2Fm%2F0k4j




