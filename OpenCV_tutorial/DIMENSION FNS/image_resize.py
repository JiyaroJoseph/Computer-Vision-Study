
# Resizing i.e. smaller images increases processing

import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

resized= cv2.resize(image, (300,300))  ## (300 X 300 px) means width X height not h X w

cv2.imshow("original image", image)
cv2.imshow("Resized image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("resized_image.png",resized)