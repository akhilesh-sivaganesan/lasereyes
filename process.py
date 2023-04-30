import cv2
import numpy as np
from PIL import Image
import sys

# Load the input image
#input_path = "input_image.jpg"
input_path = sys.argv[1]
img = cv2.imread(input_path)
img1 = Image.open(input_path)
# Opening the secondary image (overlay image)
img2 = Image.open("lensflare_small.png")
# Convert the input image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Load the Haar cascade classifier for eye detection
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Detect eyes in the grayscale image
eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
img2 = img2.resize((eyes[0][2] * 4,eyes[0][3] * 4))

img1.paste(img2, (eyes[0][0] + eyes[0][2] // 2 - img2.width // 2, eyes[0][1] + eyes[0][3] // 2 - img2.height // 2), mask = img2)
img1.paste(img2, (eyes[1][0] + eyes[1][2] // 2 - img2.width // 2 , eyes[1][1] + eyes[1][3] // 2 - img2.height // 2 ), mask = img2)
img1.save('process_output.jpg')