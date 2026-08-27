import cv2
import numpy as np
image= cv2.imread("Dataset/Resources/Photos/park.jpg",-1)
blur_image= cv2.imread("Dataset/Resources/Photos/blur.png",-1)


# GAUSSIAN BLUR.... SMOOTHENS THE IMAGE
# blurred= cv2.GaussianBlur(image, (kernel_size_x, kernel_size__y), sigma)
blurred= cv2.GaussianBlur(image, (7,7), 3)


# MEDIAN BLUR....used to remove random small small spots
# blurred2= cv2.medianBlur(image, kernel_size)
blurred2= cv2.medianBlur(image, 5)


# SHARPENING BLUR....USED FOR CRISPIER & SHARP IMAGES, IT HIGHLIGHTS EDGES OF IMAGES AND BOOSTS 
# CONTRASTS BTW PIXELS
# sharpened= cv2.filter2D(image, depth, kernel)
''''CONSIDER THIS 3x3 KERNEL, let initially all the values be 1, now boost the centre
pixel say 5 times, and subtract other, ALSO COMPLETLY IGNORE THE CORNER (thats y they are 0)....
this makes the center pixel completely stand out.'''

sharpen_kernel= np.array([
  [0, -1, 0],
  [-1, 5, -1],
  [0, -1, 0]
])
sharpened= cv2.filter2D(blur_image, -1, sharpen_kernel) #-1 means o/p same as i/p




cv2.imshow("original image", image)
cv2.imshow("original blur image", blur_image)
cv2.imshow("gaussian blur", blurred)
cv2.imshow("median blur", blurred2)
cv2.imshow("sharpened image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows
cv2.imwrite("gaussian_blur.png",blurred)
cv2.imwrite("median_blur.png",blurred2)
cv2.imwrite("sharpened_blur.png",sharpened)
