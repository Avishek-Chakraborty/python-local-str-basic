import cv2

# Load the pre-trained models
model = cv2.dnn_superres.DnnSuperResImpl_create()
model.readModel('FSRCNN_x3.pb')
model.setModel("fsrcnn", 3)

# RTSP URL for the Raspberry Pi stream
udp_url = "udp://192.168.29.232:5001"

# Create a VideoCapture object
cap = cv2.VideoCapture(udp_url)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream")
    exit()

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        # Upscale the frame
        frame = model.upsample(frame)

        # Display the frame
        cv2.imshow("Raspberry Pi Stream", frame)

        # Press 'q' to exit the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
except KeyboardInterrupt:
    # Handle the Ctrl-C shortcut
    print("Interrupted by user")

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
