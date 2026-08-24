import cv2

#read image
image= cv2.imread("Dataset/Resources/Photos/cat.jpg",-1) #1= color, 0= grayscale, -1= unchanged

#display image
cv2.imshow("Window Name", image)
cv2.waitKey(0)    #keep window open, until a key is pressed
cv2.destroyAllWindows()

#save the image into your system after making changes like dilation etc
cv2.imwrite("new_output_image.jpg",image)



