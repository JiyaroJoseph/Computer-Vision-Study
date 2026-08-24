import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")


pt1= (0,100)       # PT1 is TOP LEFT CORNER of the rectangle
pt2= (500,300)     # PT2 is BOTTOM RIGHT CORNER 
color= (0,0,255)    

cv2.rectangle(image, pt1, pt2, color, 5)


cv2.imshow("drawn rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("draw_rect.png", image)