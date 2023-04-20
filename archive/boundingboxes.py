import cv2
import numpy as np
import pytesseract

# Load the image
img = cv2.imread('screenshot.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Apply OCR to the image to detect text regions
text = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
for i in range(len(text['text'])):
    if int(text['conf'][i]) > 50:
        x, y, w, h = text['left'][i], text['top'][i], text['width'][i], text['height'][i]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Create a mask to exclude text regions
mask = np.ones(img.shape[:2], dtype="uint8") * 255
for i in range(len(text['text'])):
    if int(text['conf'][i]) > 50:
        x, y, w, h = text['left'][i], text['top'][i], text['width'][i], text['height'][i]
        mask[y:y+h, x:x+w] = 0

# Apply the mask to the image
masked = cv2.bitwise_and(img, img, mask=mask)

# Display the masked image
cv2.imshow('masked', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Apply edge detection to the image
edges = cv2.Canny(masked, 100, 200)

# Apply Hough Line Transform to the image
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=150, maxLineGap=10)

# Draw the lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Apply contour detection to the image
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    # Ignore very small boxes
    if w*h > 500:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with the bounding boxes
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# used ChatGPT to help generate code