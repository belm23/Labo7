import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara")
    exit()

ruta = "/home/embebidos2/lab7/Captures"
cv2.namedWindow('Webcam')
cont = 1

def menu():
    print("Escoger imagen para volver a escala de grises y dividir:")
    for i in range(1, cont):
        print(f"{i}. imagen{str(i)}.jpg")
    op = int(input("Escribe el numero de imagen:\n"))
    
    ruta2 = f"/home/embebidos2/lab7/Captures/imagen{op}.jpg"
    if not os.path.exists(ruta2):
        print("Error: La imagen seleccionada no existe.")
        return None
    img = cv2.imread(ruta2)
    return img

def rgb_a_grises(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imshow(f"Escala de grises", imagen_gris)
    cv2.waitKey(0)
    cv2.destroyWindow(f'Escala de grises')
    return imagen_gris

def particion(imagen):
    alto, ancho = imagen.shape[:2]
    mitad_alto = alto // 2
    mitad_ancho = ancho // 2

    cuadrante1 = imagen[0:mitad_alto, 0:mitad_ancho]
    cuadrante2 = imagen[0:mitad_alto, mitad_ancho:ancho]
    cuadrante3 = imagen[mitad_alto:alto, 0:mitad_ancho]
    cuadrante4 = imagen[mitad_alto:alto, mitad_ancho:ancho]

    cuadrantes = [cuadrante1, cuadrante2, cuadrante3, cuadrante4]
    for i, cuadrante in enumerate(cuadrantes, 1):
        cv2.imshow(f'Cuadrante {i}', cuadrante)
        cv2.waitKey(0)
        cv2.destroyWindow(f'Cuadrante {i}')

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: No se pudo leer el frame")
        break

    cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('e'):  # e=Exit
        break
    elif key == ord('c'):  # c=Capturar 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imagen = f"/home/embebidos2/lab7/Captures/imagen{cont}.jpg"
        cv2.imwrite(imagen, gray)
        print(f"Capturado el frame como: imagen{cont}.jpg")
        cont += 1

cap.release()
cv2.destroyAllWindows()

img2 = menu()
if img2 is not None:
    img3 = rgb_a_grises(img2)
    particion(img3)
