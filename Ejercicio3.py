import cv2
import os

class ColorConverter:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_name = os.path.splitext(os.path.basename(image_path))[0]
        self.image_bgr = cv2.imread(image_path)
        
        self.image_rgb = cv2.cvtColor(self.image_bgr, cv2.COLOR_BGR2RGB)
        self.image_hsv = cv2.cvtColor(self.image_bgr, cv2.COLOR_BGR2HSV)
        self.image_gray = cv2.cvtColor(self.image_bgr, cv2.COLOR_BGR2GRAY)

    def show_and_save_images(self):
        cv2.imshow(f"RGB - {self.image_name}", self.image_bgr)
        cv2.imshow(f"HSV - {self.image_name}", self.image_hsv)
        cv2.imshow(f"Grayscale - {self.image_name}", self.image_gray)

        cv2.imwrite(f"modify/{self.image_name}_rgb.jpg", self.image_rgb)
        cv2.imwrite(f"modify/{self.image_name}_hsv.jpg", self.image_hsv)
        cv2.imwrite(f"modify/{self.image_name}_gray.jpg", self.image_gray)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    path = "colors/Alicia_Miller.jpg"
    converter = ColorConverter(path)
    converter.show_and_save_images()
