import cv2

def detect():
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')

    if face_cascade.empty() or eye_cascade.empty():
        print("⛔ Cascade files could not be loaded. Check paths.")
        return

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("⛔ Could not access the camera.")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.03,
                minNeighbors=5,
                flags=0,
                minSize=(40, 40)
            )

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow("camera", frame)

        if cv2.waitKey(1) != -1:
          break


    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()
