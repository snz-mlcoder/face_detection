# Still Image Face Detection

This project performs face detection on a **static image** using OpenCV and Haar cascade classifiers.

It loads an image, detects faces, draws bounding boxes around them, and displays the result.  
A copy of the processed image is also saved as `Faces.jpg`.

## 📸 How it works
- Loads the image from the given file path.
- Converts the image to grayscale (as face detection operates in grayscale).
- Uses `haarcascade_frontalface_default.xml` to detect faces.
- Draws blue rectangles around detected faces.
- Displays the final image and saves it.

## 📁 Files
- `main.py` – Python script for face detection
- `Friends.jpg` – Sample input image (you can change this)
- `cascades/haarcascade_frontalface_default.xml` – Face detection model

## ▶️ Usage

1. Make sure you have OpenCV installed:
    ```
    pip install opencv-python
    ```

2. Run the script:
    ```bash
    python main.py
    ```

3. Press any key to close the image window.


