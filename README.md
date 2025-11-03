# ✋🤖 Gesture-Based UAV Navigation Using Real-Time Vision and ArduPilot Simulation

### 🧠 Department of Computer Science and Business Systems  
**Mukesh Patel School of Technology Management and Engineering (NMIMS University, Mumbai)**  
**Authors:**  
- Rishi Kaushik  
- Diya Uday Nayak  
- Riya Bhalavat  

---

## 📖 Overview
This project introduces a **gesture-based drone navigation system** that allows users to control UAVs using real-time **fist gestures** captured through a webcam feed.  
The model integrates **Google MediaPipe** for gesture recognition and **DroneKit-Python** with **ArduPilot SITL** simulation to command UAV movements.

By mapping the position of a detected closed fist (left, center, right) within the camera frame, the drone adjusts its flight path dynamically — turning left, right, or moving forward.  
The system provides an **intuitive, contactless, and low-cost** method for hands-free UAV control, suitable for **disaster response**, **warehouse inspection**, and **assistive robotics**.

---

## 🎯 Objectives
- Enable **real-time gesture-based UAV navigation** using fist detection.
- Develop a **low-cost**, **vision-based control interface** using open-source tools.
- Implement **DroneKit-ArduPilot integration** for dynamic heading control.
- Ensure stable flight behavior and safe landing procedures in simulation.

---

## 🧩 Methodology

### 1. **Video Frame Acquisition**
- Real-time feed captured from a mobile device via **Iriun Webcam**.
- Ensures portability and replicates realistic use cases.

### 2. **Frame Preprocessing**
- Frames resized and optimized using **OpenCV** to improve detection speed and accuracy.

### 3. **Gesture Detection (MediaPipe)**
- **MediaPipe Hand Tracking** detects landmarks and identifies closed-fist gestures.
- The system divides the camera frame into three zones:
  - **Left Zone →** Drone turns right  
  - **Center/Right Zone →** Drone turns left  
  - **No Gesture →** Drone maintains forward flight

### 4. **Drone Control (DroneKit-Python)**
- **DroneKit** sends real-time commands to a simulated ArduPilot drone.
- Movement adjustments are relative (based on heading), not absolute GPS jumps.
- Operates in **GUIDED mode** for stable flight.

### 5. **Simulation and Testing**
- Conducted using **ArduPilot SITL** (Software-in-the-Loop) for safe testing.
- The drone executes continuous flight for one minute while responding to gestures.
- Includes safe **landing routine** post mission.

---

## 🧱 Software Stack

| Component | Description |
|------------|--------------|
| **Programming Language** | Python 3.10 |
| **Gesture Detection** | MediaPipe |
| **Computer Vision** | OpenCV |
| **Drone Communication** | DroneKit-Python, MAVLink |
| **Simulation** | ArduPilot SITL, MAVProxy |
| **Camera Feed** | Iriun Webcam |
| **OS / Environment** | Linux / Windows (tested) |

---

## 📦 Dependencies

Install dependencies with:

```bash
pip install dronekit pymavlink opencv-python mediapipe
