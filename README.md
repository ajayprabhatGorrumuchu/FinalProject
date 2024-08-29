# YOLOv8 Parking Space Detection

## Project Overview

This project utilizes the YOLOv8 model for detecting cars in a parking lot and determining the occupancy status of parking spaces. The system processes a video input, identifies cars using object detection, and maps them to predefined parking spaces to determine which spots are occupied and which are available.

## Files Included

- **`ssd_parking_detection.py`**: A script for parking detection using an SSD (Single Shot Multibox Detector) model.
- **`yolov8_training.py`**: A script for training the YOLOv8 model on a custom dataset.
- **`yolov8_parking_detection.py`**: The main script that uses the trained YOLOv8 model to detect cars in a parking lot and determine parking space occupancy.
- **`requirements.txt`**: A file listing all necessary Python packages to run the project.
- **`README.md`**: This file.

## Prerequisites

- Python 3.8 or higher
- A working GPU environment is recommended for faster processing, but the code can also run on a CPU.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yolov8-parking-detection.git
    cd yolov8-parking-detection
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that you have the necessary video files and dataset for training.

## Usage

### 1. Train the YOLOv8 Model

To train the YOLOv8 model on your custom dataset, use the `yolov8_training.py` script:

```bash
python yolov8_training.py
