import cv2
image= cv2.imread("Dataset/Resources/Photos/park.jpg",-1)


# blurred= cv2.GaussianBlur(image, (kernel_size_x, kernel_size__y), sigma)
blurred= cv2.GaussianBlur(image, (7,7), 3)


cv2.imshow("original image", image)
cv2.imshow("blurred image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows
cv2.imwrite("blurred_image.png",blurred)
