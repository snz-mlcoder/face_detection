# 🧠 Face Recognition with OpenCV (LBPH)

This project demonstrates a simple but effective face recognition system using OpenCV's LBPH face recognizer (`cv2.face.LBPHFaceRecognizer_create()`), Haar cascades for face detection, and real-time webcam input.

---

## 📁 Project Structure

- `faces.csv` – CSV file with training image paths and labels
- `data/` – Directory containing grayscale face images
- `model.yml` – Trained LBPH model (saved after training)
- `cascades/haarcascade_frontalface_default.xml` – Haar cascade XML for face detection
- `main.py` – Training and real-time recognition script

---

## ⚙️ How It Works

1. **Reads face images from CSV**  
   The `faces.csv` should have lines like:

user1/face1.png;0
user1/face2.png;0
user2/face1.png;1


2. **Trains an LBPH face recognizer**  
The model is saved to `model.yml` after training.

3. **Launches webcam and performs real-time face recognition**  
- Detects faces using Haar cascade
- Predicts identity using trained model
- Displays name + confidence score on screen

---

## 🚀 Requirements

- Python 3
- OpenCV (with `opencv-contrib-python`)
- Webcam (for real-time mode)

Install dependencies:

```bash
pip install opencv-contrib-python


▶️ Run the Project
bash
Copy code
python main.py
Press q to quit the webcam window.
