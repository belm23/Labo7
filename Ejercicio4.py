import cv2
for i in range(1, 4):  
    ruta = f"/home/embebidos2/lab7/colors/imagen{i}.png"
    img = cv2.imread(ruta)
    img2=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = img2[:,:,0]
    if (h >= 0).any() and (h <= 10).any() or (h >= 170).any() and (h <= 180).any():
        cv2.imshow("ROJO",img)
        print(f"La imagen{i},es de color rojo")
    if (h >= 100).any() and (h <= 140).any():
       cv2.imshow("AZUL",img)
       print(f"La imagen{i},es de color azul") 
    if (h >= 35).any() and (h <= 85).any():
        cv2.imshow("VERDE", img)
        print(f"La imagen{i},es de color verde")
cv2.waitKey(0)
cv2.destroyAllWindows()

