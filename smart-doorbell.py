import cv2
import face_recognition

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Detect face locations
    faces = face_recognition.face_locations(frame)

    # Draw rectangles around detected faces
     if faces:
        
    # Display the resulting frame
    cv2.imshow('Smart Doorbell', frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# Release the capture and destroy windows
# cap.release()
# cv2.destroyAllWindows()
