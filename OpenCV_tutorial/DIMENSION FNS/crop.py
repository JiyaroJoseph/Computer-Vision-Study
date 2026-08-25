import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

# image[y_start:y_end, x_start:x_end].....that is width, height
cropped= image[100:400, 50:550]

cv2.imshow("cropped image", cropped)
cv2.imshow("original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("cropped_image.png", cropped)

