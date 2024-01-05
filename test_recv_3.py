import cv2

# UDP URL for the Raspberry Pi stream
udp_url = "udp://192.168.29.232:5001"

# Create a VideoCapture object
cap = cv2.VideoCapture(udp_url)

# Set the desired output size
output_size = (960, 720)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Resize the frame to the desired size
    frame = cv2.resize(frame, output_size)

    # Display the frame
    cv2.imshow("Raspberry Pi Stream", frame)

    # Press 'q' to exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
