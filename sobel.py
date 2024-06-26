import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread(r"C:\Users\schoo\Edge Detection\waiwai.JPG", cv.IMREAD_GRAYSCALE)
rows, cols = img.shape

sobel_horizontal = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

#cv.imshow('Original', img)
#cv.imshow('Sobel horizontal', sobel_horizontal)
#cv.imshow('Sobel vertical', sobel_vertical)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])


plt.subplot(122),plt.imshow(sobel_horizontal,cmap = 'gray')
plt.title('Sobel horizontal'), plt.xticks([]), plt.yticks([])

plt.show()
