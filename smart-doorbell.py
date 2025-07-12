import cv2
import face_recognition
import playsound
import threading

# Start video capture
cap = cv2.VideoCapture(0)
sound_played = False
def ring_bell():
    playsound.playsound('doorbell.mp3')
while True:
    _, frame = cap.read()

    # Detect face locations
    faces = face_recognition.face_locations(frame)
    # Draw rectangles around detected faces
    if faces and not sound_played:
        threading.Thread(target=ring_bell).start()
        sound_played = True
    elif not faces and sound_played:
        sound_played = False
    # Display the resulting frame
    cv2.imshow('Smart Doorbell', frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(10) == ord('q'):
        break
