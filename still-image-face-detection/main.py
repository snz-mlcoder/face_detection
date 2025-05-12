import cv2


def detect(filename):
    face_cascade = cv2.CascadeClassifier(
        './cascades/haarcascade_frontalface_default.xml')

    img = cv2.imread(filename)
    if img is None:
        print("⛔ Image not loaded! Check the path.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.namedWindow('ّFaces Detected!!')
    cv2.imshow('Faces Detected!!', img)
    cv2.imwrite('./Faces.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Put the path to your image file here:
filename = 'Friends.jpg'
detect(filename)
