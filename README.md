# Face Recognition Application

Welcome to the Face Recognition Application project! This application uses OpenCV and face_recognition to detect and identify faces from a video feed, with pre-trained face encodings organized by person in the `dataset` directory.

<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.8+-ffd343.svg" alt="Python">
    </a>
    <a href="https://opencv.org/">
        <img src="https://img.shields.io/badge/OpenCV-4.x-blue.svg" alt="OpenCV">
    </a>
    <a href="https://pypi.org/project/face-recognition/">
        <img src="https://img.shields.io/badge/face__recognition-1.3.0-6ba539.svg" alt="face_recognition">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="MIT License">
    </a>
</p>

This project allows you to recognize faces in real-time using a webcam. Faces are identified based on pre-encoded images stored in a structured dataset directory.

## 🌟 **Introduction**

This project demonstrates a simple and effective way to perform face recognition using Python. It uses:
- **OpenCV**: For capturing video frames and annotating faces.
- **face_recognition**: For detecting and encoding faces.
- **Dataset Structure**: Organizes known faces in a hierarchical folder structure.

## 🚀 **Getting Started**

### **1. Setup Your Environment**

#### Install Dependencies

Ensure you have Python installed. Then, install the required packages:

```
pip install opencv-python face_recognition numpy
```

Create a Virtual Environment

To keep your project dependencies isolated, create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### **2. Dataset Structure**
Organize your known face images in the following structure:

```
dataset/
    ├── Person1/
    │   ├── img1.jpg
    │   └── img2.jpg
    ├── Person2/
    │   └── img1.jpg
    └── ...
main.py
```
Each subdirectory under dataset should be named after the person it represents and contain images of that person.

### **3. Running the Application**

**Prepare the Dataset:** Place images in the dataset directory as shown above.

**Run the Script:** Execute the script to start the face recognition:

```
python main.py
```

### **4. Understanding the Code**

`main.py`: Contains the core logic for encoding known faces and recognizing faces from a webcam feed.

### **5. Using the Face Recognition Application**

**Video Feed:** A webcam feed will open, detecting and identifying faces based on the pre-encoded images.
**Real-time Detection:** Detected faces are annotated with the name and confidence score.

## **🛠️ Project Structure**

Here's how the project is organized:

```
netclues-face-recognition-application/
├── dataset/
│   ├── Person1/
│   └── Person2/
├── main.py
└── README.md
dataset/: Directory containing subdirectories for each person with their images.
main.py: Python script for face recognition.
README.md: This guide.
```

## **📦 Quick Start**

### **Install the Dependencies**

```
pip install -r requirements.txt
```

### **Run the Project**

```
python main.py
```

### **Access the Application**

The application will use your default webcam to start face recognition.

## 👩‍💻 **Contributing**
Feel free to fork this repository and make improvements. Contributions are welcome!

## 📄 **License**
This project is licensed under the MIT License.

