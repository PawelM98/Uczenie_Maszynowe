import imutils
import cv2

# Funkcja 1 - Ladowanie i wyświetlanie obrazu

image = cv2.imread("herkules.jpeg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

cv2.imshow("Image", image)
cv2.waitKey(0)

# Funkcja 2 - Otrzymywanie indywidualnych pixeli

(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# Funkcja 3 - Przycinanie obrazka

roi = image[30:130, 210:310]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# Funkcja 4 - Zmiana rozmiaru obrazka

resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# Funkcja 5 - Zmiana rozmiaru obrazka

r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# Funkcja 6 - Zmiana rozmiaru obrazka

resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# Funkcja 7 - Obracanie obrazka

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# Funkcja 8 - Obracanie obrazka

rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# Funkcja 9 - Obracanie obrazka

rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# Funkcja 10 - Rozmazanie obrazka

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# Funkcja 11 - Rysowanie na obrazku

output = image.copy()
cv2.rectangle(output, (350, 160), (450, 260), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# Funkcja 12 - Rysowanie na obrazku

output = image.copy()
cv2.circle(output, (492, 200), 15, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# Funkcja 13 - Rysowanie na obrazku

output = image.copy()
cv2.line(output, (300, 40), (600, 190), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# Funkcja 14 - Rysowanie na obrazku

output = image.copy()
cv2.putText(output, "Herkules & Phil", (300, 20),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)

