import cv2
import numpy as np
import os

def read_csv(csv_path):
    images, labels = [], []
    with open(csv_path, 'r') as file:
        for line in file:
            path, label = line.strip().split(';')
            image = cv2.imread(os.path.join('data', path), cv2.IMREAD_GRAYSCALE)
            if image is None:
                continue
            images.append(image)
            labels.append(int(label))
    return images, labels

def train_model(images, labels):
    model = cv2.face.LBPHFaceRecognizer_create()

    model.train(images, np.array(labels))
    model.save('model.yml')
    print(" Model trained and saved as model.yml")
    return model

def recognize(model):
    names = ["Snz"]
    camera = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (200, 200))
            label, confidence = model.predict(roi)

            print(f" Recognized ID: {label}, Confidence: {confidence:.2f}")

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, f"{names[label]} ({confidence:.0f})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    images, labels = read_csv('faces.csv')
    model = train_model(images, labels)
    recognize(model)