import argparse
import imutils
import cv2

# Dodanie dodatkowych informacji do naszego programu przy jego starcie
# Nowy argument będzie wymagany w lini komend
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# Funkcja 1 - Załadowanie obrazka z lini komend
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# Funkcja 2 - Konwertowanie obrazka na szary kolor

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Funkcja 3 - Wykrywanie krańców

edged = cv2.Canny(gray, 20, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# Funkcja 4 - Progowanie

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# Funckja 5 - Wykrywanie i rysowanie konturów

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

# Funkcja 6 - Zliczanie wykrytych konturów oraz rysowanie ich
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

# Funkcja 7 - Erozja i Dylatacja
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

### Funkcja 8 - Dylatacja działa w sposób odwrotny do erozji
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

# Funkcja 9 - Operacje maskowe i bitowe
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output - Bitwise", output)
cv2.waitKey(0)