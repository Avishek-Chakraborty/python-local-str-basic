from ultralytics import YOLO
import cv2

udp_url = 'udp://192.168.29.232:5001'
cap = cv2.VideoCapture(udp_url)
output_size = (960, 720)

model = YOLO("Coustom_model\yolov8n_100e.pt")

for name, param in model.named_parameters():
    print(name, param.data)

# results = model(source='0', show = True, conf=0.4,device='cpu' , save=True)
results = model(source='0', show = True, conf=0.4)

print(results)
