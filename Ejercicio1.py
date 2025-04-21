import cv2
for i in range(1, 4):  
    ruta = f"/home/embebidos2/lab7/colors/imagen{i}.png"
    img = cv2.imread(ruta)
    cv2.imshow(f"imagen{i}",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

