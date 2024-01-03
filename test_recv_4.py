import cv2

# RTSP URL for the Raspberry Pi stream
udp_url = 'udp://192.168.29.232:5001'

# Create a VideoCapture object
cap = cv2.VideoCapture(udp_url)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Display the frame
    cv2.imshow('Raspberry Pi Stream', frame)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
