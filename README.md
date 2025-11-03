# ✋🤖 Gesture-Based UAV Navigation Using Real-Time Vision and ArduPilot Simulation

> ✈️ A Python-based drone control system that uses **MediaPipe hand tracking** and **DroneKit-ArduPilot simulation** to navigate UAVs through **fist gestures** detected from a live webcam feed, enabling intuitive, hands-free flight control.

---

### 🧠 Department of Computer Science and Business Systems  
**Mukesh Patel School of Technology Management and Engineering (NMIMS University, Mumbai)**  
**Authors:**  
- Rishi Kaushik  
- Diya Uday Nayak  
- Riya Bhalavat  

---

## 📖 Overview
This project introduces a **gesture-controlled UAV navigation system** using **real-time vision-based fist detection**.  
By integrating **MediaPipe** for gesture tracking and **DroneKit-Python** with **ArduPilot SITL**, the system enables drones to turn left, right, or continue forward based on a user’s hand position.  
This approach eliminates the need for handheld controllers, providing a **low-cost**, **intuitive**, and **hands-free** way to navigate drones.

---

## 🔗 Model File (Google Drive Link)
Due to GitHub’s file size limitations, the trained model file has been uploaded to Google Drive.  
You can download it using the link below and place it in the project directory before running the code.

👉 **Download Model:** [https://drive.google.com/file/d/1AQ3pEfdXgGr7AfehElrzMWBAK1bS7QNt/view?usp=drive_link]

---

## 🎯 Objectives
- Enable **real-time gesture-based UAV control** using a live webcam feed.  
- Implement **DroneKit-ArduPilot** communication for guided-mode flight.  
- Achieve **smooth, stable navigation** without GPS jumps.  
- Create a **lightweight, portable system** for educational and practical UAV use.

---

## 🧩 Methodology

### 1. Video Frame Capture
- Live webcam input is streamed via **Iriun Webcam**, simulating mobile camera usage.

### 2. Frame Preprocessing
- Frames resized and converted using **OpenCV** to optimize for speed and clarity.

### 3. Gesture Recognition
- **MediaPipe Hand Tracking** detects hand landmarks.
- A rule-based classifier identifies **closed-fist gestures**.
- The camera frame is divided into zones:
  - **Left Zone →** Drone turns right  
  - **Center/Right Zone →** Drone turns left  
  - **No Fist Detected →** Drone continues forward

### 4. UAV Control
- **DroneKit-Python** commands UAV heading adjustments using MAVLink protocol.
- Operates in **GUIDED mode** for controlled and stable simulation.

### 5. Real-Time Loop
- Continuous 60-second control cycle:
  - Reads camera input → Detects gesture → Sends command → Moves forward
- Ends with a **safe landing sequence**.

---

## 🧱 Software Stack

| Component | Description |
|------------|-------------|
| **Language** | Python 3.10 |
| **Gesture Detection** | MediaPipe |
| **Computer Vision** | OpenCV |
| **UAV Control** | DroneKit-Python + MAVLink |
| **Simulation** | ArduPilot SITL + MAVProxy |
| **Webcam Feed** | Iriun Webcam |
| **Environment** | Linux/Windows |

---

## 📦 Dependencies

Install all dependencies with:

```bash
pip install dronekit pymavlink opencv-python mediapipe
