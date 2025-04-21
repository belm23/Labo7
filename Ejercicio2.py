import cv2
import os
def rgb_a_grises(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    return imagen_gris

def procesar_imagenes(folder_path="colors"):
    for file_name in os.listdir(folder_path):
        if file_name.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)

            gray = rgb_a_grises(image)

            cv2.imshow(f"Original - {file_name}", image)
            cv2.imshow(f"Escala de grises - {file_name}", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    procesar_imagenes()
