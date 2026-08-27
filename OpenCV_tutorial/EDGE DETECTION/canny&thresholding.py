import cv2

# READ IMAGE AS GRAYSCALE
image= img= cv2.imread("Dataset/Resources/Photos/cat.jpg", cv2.IMREAD_GRAYSCALE)


#CANNY EDGE DETECTION
# t1- lower boundary to detect weak edges....0<= t1<= 255
# t2- upper boundary to detect strong edges....0<= t2<= 255
# edges= cv2.Canny(image, threshold1, threshold2, method)
edges= cv2.Canny(image, 50, 150)



cv2.imshow("original", image)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("canny_without_method.png", edges)