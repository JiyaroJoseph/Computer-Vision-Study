import cv2

cap= cv2.VideoCapture(0)        #############

frame_width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec= cv2.VideoWriter_fourcc(*'XVID')
#Cv2.VideoWriter(filename, codec, fps, frame_size)
recorded= cv2.VideoWriter("new_video.avi",codec, 20, (frame_width, frame_height))


while True:
  ret, image= cap.read()      ##############

  if not ret:
    break

  cv2.imshow("recording live", image)
  recorded.write(image)     ####################

  if cv2.waitKey(1) & 0xFF== ord('q'):
    break

cap.release()             ########################
recorded.release()
cv2.destroyAllWindows()
