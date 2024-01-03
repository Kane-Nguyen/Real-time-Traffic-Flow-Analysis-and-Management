# eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-
### Table of contents
- 1 Purpose
- 2 Introduction our Project
- 3 Content of files above

## 1 Purpose
The "Real-time Traffic Flow Analysis and Management Using YOLOv8" project is designed to create an intelligent system capable of analyzing and managing traffic flow in real-time. The primary objectives include:
    
1. **Real-time Analysis:**
- Conducting continuous analysis of traffic conditions in real-time.
- Providing swift information about the current state of traffic flow.

2. **Traffic Flow Management:**
- Implementing an intelligent guidance and control system for traffic flow.
- Aiming to reduce congestion and enhance the overall flow of vehicles.
3. **Utilizing YOLOv8:**
- Integrating the YOLOv8 model for object detection and tracking.
- Focusing on precise identification of traffic objects, such as cars and motorcycles, to provide detailed and accurate information on traffic conditions.

The ultimate goal is to contribute to the improvement of safety and efficiency within urban transportation systems by leveraging advanced technologies for real-time traffic analysis and intelligent traffic flow management. This project seeks to address the challenges of urban congestion and enhance the overall urban commuting experience.
## 2 Introduction our Project
Welcome to the "Real-time Traffic Flow Analysis and Management Using YOLOv8" project! In urban environments, efficient traffic flow management is crucial for both safety and convenience. This project harnesses the power of YOLOv8, a state-of-the-art object detection model, to create an intelligent system capable of analyzing and managing traffic conditions in real-time.

### Project Highlights

- **Real-time Analysis:** Continuously monitors and analyzes traffic conditions, providing instant insights into the current state of traffic flow.
- **Traffic Flow Management:** Implements an intelligent guidance and control system to reduce congestion and enhance overall vehicle flow within urban areas.
- **YOLOv8 Integration:** Utilizes the YOLOv8 model for accurate and detailed identification and tracking of traffic objects, such as cars and motorcycles.

### Objectives

Our project aims to:

1. Improve safety and efficiency within urban transportation systems.
2. Address challenges related to urban congestion.
3. Enhance the overall urban commuting experience.

Feel free to explore the documentation to understand the functionalities, installation instructions, and how you can contribute to making urban commuting smarter and more effective!

## 3 Content of project
### [CCTV-detection.py](https://github.com/Kane-Nguyen/eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-/blob/main/CCTV-detection.py) 

1. Imported Libraries:
-  Imports necessary libraries such as OpenCV, Pandas, NumPy, and others.
- Utilizes the YOLOv8 model from the Ultralytics library for object detection.

2. Functionality:
- Reads a video file (23.mp4).
- Utilizes the YOLOv8 model to perform object detection on each frame.
- Implements a tracking algorithm using a Tracker class to assign and update IDs for tracked objects.
- Evaluates crowd density based on the number of detected vehicles in a predefined area.
- Displays real-time analysis results, including object tracking, IDs, car count, total cars, and crowd density.
- Applies visual indicators such as circles and rectangles to highlight tracked objects.

3. User Interaction:
- Allows the user to interact with the script through the mouse to obtain real-time coordinates (X, Y) information.

### [Tracker.py](https://github.com/Kane-Nguyen/eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-/blob/main/tracker.py)

1. Tracker Class:
- Initializes a Tracker class with attributes to store center points of tracked objects and manage object IDs.
- Provides a method (update) for updating the tracked objects based on their bounding boxes.
- Assigns and updates unique IDs for each tracked object.
- Cleans the dictionary of center points to remove IDs that are no longer in use.

### [Dataset Link](https://github.com/Kane-Nguyen/eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-/blob/main/Dataset%20Link.txt)
is the link to our data in image format

### [Videos-detection.py](https://github.com/Kane-Nguyen/eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-/blob/main/Videos-detection.py)
This Python script is the core of a project focused on real-time traffic analysis. It combines the power of YOLOv8 for object detection with a custom tracking algorithm. Key features include mouse event handling, dynamic crowdedness analysis, and visual feedback on a defined tracking area. The script continuously evaluates car count, providing insights into overall crowdedness and contributing to intelligent traffic flow management in urban environments.

### [analysis.xlsx](https://github.com/Kane-Nguyen/eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-/blob/main/analysis.xlsx)
The "analysis.xlsx" file serves as a comprehensive record of traffic scenarios, capturing the dynamics of various video sequences at specific time intervals. Below is a condensed overview of the content:

**Column Definitions:**
- ***Video Name***: Identifies each distinct video scenario.
- ***Status***: Describes the traffic condition at designated time intervals (10s, 20s, 30s, 40s, 60s, 90s) using classifications such as "Deserted," "Medium," or "Crowded."
- ***10s, 20s, 30s, 40s, 60s, 90s***: Represents the vehicle count at respective time intervals.

### [Detect.xlsx](https://github.com/Kane-Nguyen/eal-time-Traffic-Flow-Analysis-and-Management-Using-YOLOv8-/blob/main/Detect.xlsx)
Dossier Details Vehicles in Designated Frame, Counts Cars Passing Each Second, and Aggregates Results by Total Cars in Each Second. Includes Link to Original Video.



