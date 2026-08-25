import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

#cv2.circle(image, centre, radius, color, thickness)

cv2.circle(image, (50,100), 25, (255,0,0), -1)  # -1 MEANS FILL THE DRAWN FULL CIRCLE WITH COLOR


cv2.imshow("drawn circle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("draw_circle.png", image)