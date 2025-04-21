import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara")
    exit()

show_grayscale = True

cv2.namedWindow('Webcam')

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo leer el frame")
        break

    if show_grayscale:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Webcam', gray_frame)
    else:
        cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('e'):  # e=Exit
        break
    elif key == ord('r'):  # r cambiar color
        cv2.destroyWindow('Webcam')
        show_grayscale = not show_grayscale
        cv2.namedWindow('Webcam')

cap.release()
cv2.destroyAllWindows()
