import cv2

image= cv2.imread("Dataset/Resources/Photos/cat.jpg")

if image is not None:
  h, w, c= image.shape     #dimensions
  print(f"height: {h}, width: {w}, color channels: {c}")

else:
  print('failed')




