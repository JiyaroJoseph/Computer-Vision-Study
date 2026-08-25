import cv2

cap= cv2.VideoCapture(0)   ########## # 0-webcam, 1-ext. connected cam, 2- 

while True:
  ret, frame= cap.read()      #########

  if not ret:
    print("couldnt read frame")
    break

  cv2.imshow("webcam window", frame)

 # USE "bitwise &" AND NOT "AND".....since when using, waitKey()...IF ANY KEY IS PRESSED, 
 # IT returns an ASCII value and check if that==q
  # wait for 1ms and check if q is pressed, if so...EXIT
  if cv2.waitKey(1) & 0xFF== ord('q'):    
    print("quitting")      
    break

cap.release           ########### to stop saving the video, similar to destroywin() for images
cv2.destroyAllWindows()