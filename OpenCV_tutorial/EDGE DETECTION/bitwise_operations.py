import cv2
import numpy as np

### THREE IMPORTANT POINTS- 1. IMG1, IMG2 HEIGHT AND WIDTH SHUD BE SAME
# 2. USE ONLY BLACK AND WHITE
# 3. FORM A MASK LIKE WHITE CIRCLE ON A BLACK BACKGROUND BEFORE DOING THE BITWISE OPS

''' cv2.bitwise_and(img1, img2)
    cv2.bitwise_or(img1, img2)
    cv2.bitwise_not(img1)
'''

img1= np.zeros((300,300), dtype="uint8")
img2= np.zeros((300,300), dtype="uint8")
'''
np.zeros((300, 300))
This creates a 300 × 300 grid filled with zeros.
Think of it like this:
0  0  0  0  0  ...
0  0  0  0  0  ...
0  0  0  0  0  ...
...
There are:
300 rows → height
300 columns → width

dtype="uint8" tells numpy 
"Store each number as an 8-bit unsigned integer."

That's why the code creates a black image first:
img1 = np.zeros((300, 300), dtype="uint8")

Then this:
cv2.circle(img1, (150, 150), 100, 255, -1)
draws a white circle onto that black NumPy array.
'''

cv2.circle(img1, (150,150), 100, 255, -1)
cv2.rectangle(img2, (100,100), (250,250), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.imwrite("bitwise_and.png", bitwise_and)
cv2.imwrite("bitwise_or.png", bitwise_or)
cv2.imwrite("bitwise_not.png", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows