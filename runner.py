#Welcome to the code
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Real-Time Video Analysis', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()