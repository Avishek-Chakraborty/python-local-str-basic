import cv2

model = cv2.dnn_superres.DnnSuperResImpl_create()
model.readModel('FSRCNN_x3.pb')
model.setModel("fsrcnn", 3)

input_video = cv2.VideoCapture('test_video.mp4')

if not input_video.isOpened():
    print("Error opening video file")
    exit()

frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
output_video = cv2.VideoWriter('upscaled_video.mp4', fourcc, fps, (frame_width*3, frame_height*3))

try:
    while True:
        ret, frame = input_video.read()

        if not ret:
            print("Finished processing frames. Exiting...")
            break

    
        frame = model.upsample(frame)

    
        output_video.write(frame)

except KeyboardInterrupt:

    print("Interrupted by user")

input_video.release()
output_video.release()
cv2.destroyAllWindows()
