import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

# cv2.line(image, pt1, pt2, color, thickness)
''' HERE THE COORDINATES IN THE POINTS ARE PIXELS, so coordinates not same for evry image; varies
wrt size of the image '''
pt1= (0,100)
pt2= (500,100)
color= (0,0,255)    # BGR VALUES.... 

cv2.line(image, pt1, pt2, color, 5)



cv2.imshow("drawn line",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("draw_line.png", image)