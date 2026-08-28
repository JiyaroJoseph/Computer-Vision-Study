import cv2

''' contours, hierarchy= cv2.findContours(BINARY_image, RETRIEVAL_mode, method) '''

# MODE MEANS- HOW MANY CONTOURS TO RETURN, AND WHAT KIND
# RETR_EXTERNAL returns only outermost shape
# RETR_TREE returns all shapes with hierarchy
# RETR_LIST returns all shapes BUT WITHOUT HIERARCHY

# SUPPOSE THERE IS A SQUARE INSIDE A SQUARE, retr_external returns only the outer square
# retr_tree returns both the outer square and the inner square and also WHO IS INSIDE WHOM
# retr_list returns both the squares both doesnt tell the hierarchy

# METHOD TELLS HOW MUCH DETAIL TO RETURN FOR EACH CONTOUR
# EG: chain_approx_simple stores only the corner points]
# chain_approx_none stores all THE PIXELS OF THE CONTOUR....used for detailing like handwriting detection


img= cv2.imread("Dataset/Resources/Photos/cat.jpg", -1)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


''' _ is a placeholder, telling python that this will return some value BUT I DONT NEED IT FOR NOW, 
SKIP IT....IT IS USED BY PROFESSIONALS AND SAVES MEMORY'''
_, thresh= cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)


contours, hierarchy= cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )