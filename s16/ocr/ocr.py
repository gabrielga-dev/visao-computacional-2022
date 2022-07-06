# -*- coding: utf-8 -*-


"""
## Instalação
* macOS: brew install tesseract - todos os idiomas
* ubuntu: sudo apt-get install o tesseract-ocr
* pip instalar Pillow
* pip instalar pytesseract
* pip instalar tesserocr

# tesserocr melhor uso

## Run
* Saída padrão, sem saída para o arquivo TXT:
Tesseract images / example_01.png stdout
* py ocr.py -i example_01.png -p desfocagem


## Tesseract Guia do Usuário
- um
"""

# import the necessary packages
from PIL import Image

import cv2

import pytesseract

image = cv2.imread("./sample.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
gray = cv2.medianBlur(gray, 3)


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
#text = pytesseract.image_to_string(filename)
#text = pytesseract.image_to_string(Image.open(filename))
text = pytesseract.image_to_string(gray)
#os.remove(filename)
print(text)

cv2.imshow("Output", gray)
cv2.waitKey(0)

