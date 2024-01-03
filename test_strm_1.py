import cv2

# Replace this with the IP address and port you used in the Raspberry Pi command
stream_url = 'udp://192.168.29.232:8001'

cap = cv2.VideoCapture(stream_url)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Live Video Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
