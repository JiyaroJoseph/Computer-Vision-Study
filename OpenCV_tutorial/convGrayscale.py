
import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

# convert COLOR to GRAYSCALE:- to reduce processing time and complexity
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("window",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
