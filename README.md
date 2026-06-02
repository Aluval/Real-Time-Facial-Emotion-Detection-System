# 🎭 Real-Time Facial Emotion Detection System - BlinkVerify AI

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Detection-orange)
![DeepFace](https://img.shields.io/badge/DeepFace-Emotion%20Recognition-red)
![AI](https://img.shields.io/badge/AI-Deep%20Learning-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Project Overview

**Real-Time Facial Emotion Detection System** is an AI-powered computer vision project that detects human faces from webcam input and analyzes facial expressions using deep learning models.

The system identifies emotions such as **happy, sad, angry, surprise, fear, disgust, and neutral**, and displays the **dominant emotion with confidence percentage** on the screen in real time.

This project demonstrates the practical implementation of **Artificial Intelligence, Computer Vision, and Deep Learning** technologies.

---

# 🧠 Technologies Used

| Technology         | Purpose                            |
| ------------------ | ---------------------------------- |
| Python             | Core programming language          |
| OpenCV             | Video capture and image processing |
| MediaPipe          | Face detection                     |
| DeepFace           | Emotion recognition model          |
| NumPy              | Numerical computations             |
| AI & Deep Learning | Emotion classification             |

---

# ⚙️ System Architecture

```
Webcam Input
     ↓
OpenCV Video Capture
     ↓
MediaPipe Face Detection
     ↓
Face Cropping & Preprocessing
     ↓
DeepFace Emotion Model
     ↓
Emotion Classification
     ↓
Display Emotion + Confidence
```

---

# 🔧 Project Modules

### 1️⃣ Face Detection Module

Uses **MediaPipe Face Detection** to detect human faces in real-time video frames.

### 2️⃣ Face Processing Module

Extracts the detected face region and prepares it for emotion analysis.

### 3️⃣ Emotion Recognition Module

Uses the **DeepFace deep learning model** to analyze facial expressions and classify emotions.

### 4️⃣ Visualization Module

Displays:

* Face bounding box
* Emotion label
* Confidence percentage
* Developer watermark

### 5️⃣ Real-Time Processing Module

Processes webcam frames continuously for live emotion detection.

---

# 🚀 Features

✔ Real-time facial emotion detection
✔ Deep learning-based emotion classification
✔ Confidence percentage display
✔ Face bounding box visualization
✔ Live webcam processing
✔ Developer watermark overlay
✔ Lightweight and efficient

---

# 📷 Example Output

```
Emotion Detection

🙂 Happy (91.4%)

DEV BY ALUVALA EDIGA HARSHA VARDHAN GOUD
```

---

# 🌍 Applications

This module can be applied in various sectors such as:

### 🚗 Driver Monitoring Systems

Detect driver stress, fatigue, or emotional states.

### 🧠 Mental Health Analysis

Monitor emotional patterns for psychological studies.

### 🎓 Smart Classrooms

Analyze student engagement and attention.

### 🛒 Customer Sentiment Analysis

Understand customer reactions in retail environments.

### 🤖 Human-Computer Interaction

Improve interaction between humans and intelligent systems.

### 🔐 Security & Surveillance

Detect unusual emotional behavior in monitored areas.

---

# 📂 Project Structure

```
Emotion-Detection-System
│
├── facedetectionsemotions.py
├── README.md
└── requirements.txt
```

---

# ⚡ Installation

### Clone the repository

```
git clone https://github.com/yourusername/emotion-detection-system.git
```

### Navigate to project folder

```
cd emotion-detection-system
```

### Install dependencies

```
pip install opencv-python
pip install mediapipe
pip install deepface
pip install numpy
```

### Run the program

```
python facedetectionsemotions.py
```

Press **Q** to exit the webcam window.

---

# 📊 AI Model

The project uses **DeepFace Emotion Recognition Model**, a deep learning-based facial expression classifier trained on large emotion datasets.

Detected emotions include:

* Happy
* Sad
* Angry
* Fear
* Surprise
* Disgust
* Neutral

---

# 👨‍💻 Developer

**Aluvala Ediga Harsha Vardhan Goud**

AI & Machine Learning Enthusiast
MCA Student

---

# ⚠️ Educational Usage Notice

This project is created **for educational and research purposes**.

The code is publicly shared to demonstrate the implementation of **AI, Computer Vision, and Deep Learning techniques**.

If you use this project in your work, **please provide proper credit to the developer**.

---

# ⚖️ Project Ownership Notice

This project belongs to **Aluvala Ediga Harsha Vardhan Goud**.

Unauthorized activities such as:

* Removing developer credit
* Claiming the project as your own
* Re-selling the project code
* Misleading usage without attribution

may lead to **serious action under academic integrity and intellectual property policies**.

---

# 📜 License

MIT License

---

# ⭐ Support

If you like this project, please **star the repository** on GitHub ⭐
