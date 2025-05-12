# Video Face and Eye Detection 🎥👁️

This project uses OpenCV and Haar cascade classifiers to detect **faces and eyes in real-time** from a webcam feed.

## 💡 Features
- Detects faces using `haarcascade_frontalface_default.xml`
- Detects eyes **within** the detected face region using `haarcascade_eye.xml`
- Draws blue rectangles around faces and green rectangles around eyes
- Real-time performance via webcam
- Press **any key** to exit

## 📂 Project Structure

video-face-eye-detection/
│
├── video-face-eye-detection.py # Main detection script
├── cascades/
│ ├── haarcascade_frontalface_default.xml
│ └── haarcascade_eye.xml
└── README.md # You're reading it!


## ▶️ Usage

1. Make sure you have Python and OpenCV installed:

```bash
pip install opencv-python

2. Run the script:
python video-face-eye-detection.py
