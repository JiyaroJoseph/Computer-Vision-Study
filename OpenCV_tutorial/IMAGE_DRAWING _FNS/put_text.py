import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

# cv2.putText(image, text, org, font, fontSize, color, thickness).......trick..TOFF
# org means (x,y) for the bottom left corner

cv2.putText(image, "hello there", (50,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 3)


cv2.imshow("window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("put_text.png", image)