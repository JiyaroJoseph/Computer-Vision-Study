import cv2

# READ IMAGE AS GRAYSCALE
image= img= cv2.imread("Dataset/Resources/Photos/cat.jpg", cv2.IMREAD_GRAYSCALE)


# edges= cv2.Canny(image, threshold1, threshold2, method)
# THRESH_BINARY means that if a pixel value > 120, make it completely WHITE...else BLACK

# USUALLY THRESHOLD VALUES= 100, 120, 150 ARE USED FOR BEST RESULTS
edges= cv2.Canny(image, 120, 255, cv2.THRESH_BINARY)


cv2.imshow("original", image)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("canny_using_bin_thresholding.png", edges)