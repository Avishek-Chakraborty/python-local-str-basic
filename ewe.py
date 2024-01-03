import cv2
import ctypes

# UDP URL for the Raspberry Pi stream
udp_url = 'udp://192.168.29.232:5001'

# Create a VideoCapture object
cap = cv2.VideoCapture(udp_url)

# Get screen resolution
user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Resize the frame to the screen resolution
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Display the frame
    cv2.imshow('Raspberry Pi Stream', frame)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
