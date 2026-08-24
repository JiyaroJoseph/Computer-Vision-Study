import cv2
image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

h, w= image.shape[:2]
centre= (w//2, h//2)  

# M= cv2.getRotationMatrix2D(centre, angle, scale)
# rotated_image= cv2.warpAffine(image, M, (width,height))

M= cv2.getRotationMatrix2D(centre, 90, 1.5)
rotated_image= cv2.warpAffine(image, M, (w,h))


cv2.imshow("rotated image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rotated_image.png",rotated_image)
