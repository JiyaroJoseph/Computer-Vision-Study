import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

flipped_horiz= cv2.flip(image, 1)  #1- horiz, 0- vertical, -1: both horiz and vert
flipped_vert= cv2.flip(image, 0)
flipped_both= cv2.flip(image, -1)


cv2.imshow("original",image)
cv2.imshow("flip horizontal", flipped_horiz)
cv2.imshow("flip vertical", flipped_vert)
cv2.imshow("flip both axes", flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("flipped_horizontal.png", flipped_horiz)
cv2.imwrite("flipped_vertical.png", flipped_vert)
cv2.imwrite("flipped_horiz_&_vert.png", flipped_both)