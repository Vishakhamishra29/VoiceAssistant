import cv2

# Open the webcam (0 is for the default webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        print("Failed to grab frame")
        break

    # Show the frame in a window
    cv2.imshow("Webcam Feed", frame)

    # Press 'q' to close the feed window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
