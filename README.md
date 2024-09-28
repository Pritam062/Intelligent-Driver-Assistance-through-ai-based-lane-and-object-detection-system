# Intelligent Driver Assistance through AI-based Lane and Object Detection System

## Overview

This project is focused on building an intelligent driver assistance system (IDAS) that enhances road safety by detecting lanes and objects in real-time. By leveraging computer vision techniques such as Canny Edge Detection, Hough Transform, and the YOLO object detection algorithm, this system is designed to provide lane-keeping assistance and alert drivers to obstacles on the road. It aims to reduce accidents caused by lane drifting or unnoticed obstacles.

Features

Lane Detection : Identifies and tracks road lanes using Canny Edge Detection and Hough Transform.
Curve Detection : Accurately identifies curved road segments to help navigate turns.
Object Detection : Utilizes the YOLO (You Only Look Once) algorithm to detect objects such as vehicles, pedestrians, and road signs in real-time.
Real-time Performance : Processes video streams from a dashboard camera to provide lane and object information in real-time.

 How It Works

1. Lane Detection : 
   - The system extracts edges from the video stream using the Canny Edge Detection algorithm.
   - Hough Line Transform is then applied to detect lane markings on the road.
   - Lane curves and turns are recognized to alert the driver.

2. Object Detection :
   - YOLO is used to identify objects like vehicles, pedestrians, and road signs.
   - The algorithm performs object detection across frames in real-time, providing bounding boxes and classifying detected objects.

3. Driver Assistance :
   - The system combines lane and object detection to assist the driver with lane-keeping and obstacle avoidance.
   - Visual and audio cues (if applicable) can be provided to warn the driver.

Technologies Used

Python : Primary programming language.
OpenCV: For image and video processing (Canny Edge Detection, Hough Transform).
YOLOv5: Pre-trained deep learning model for object detection.
NumPy: For numerical computations.
Matplotlib: For visualizing the lane and object detection process.
TensorFlow/PyTorch: For running deep learning models (YOLO).


 Demo

A sample demo of the system in action can be seen.
