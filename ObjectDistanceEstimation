import cv2
from ultralytics import YOLO
import math

url = 'http://192.168.1.8:8080/video'
cap = cv2.VideoCapture(url)
model = YOLO("yolov8n.pt")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot receive frame. Exiting...")
        break
    Shape=frame.shape
    print(Shape)
    frame=cv2.resize(frame, (int(Shape[1]*0.50),int(Shape[0]*0.50)))
    results = model.predict(frame)
    Dans = results[0]
    try:
        NUM = None
        liso = list(map(int, Dans.boxes.cls))
        for i in range(len(liso)):
            if liso[i] == 0:
                NUM = i
        box = Dans.boxes[NUM]
        # Finding Objects Coordinatz
        dim = box.xywh[0]
        print(dim)
        x, y, w, h = list(map(int, dim))
        print(x, y, w, h)
        Nimg = cv2.rectangle(frame, (x - (w // 2), y - (h // 2)), (x + (w // 2), y + (h // 2)), (255, 0, 0), 3)
        height=h
        print("Object Height :",height,"PX")
        #Focal = (h*30)/5.5
        Focal=818
        print("Focal-Length :",Focal)
        Distance=(Focal*5.5)/height
        print("Distance from Camera :",Distance)
        cv2.putText(Nimg, f"Distance: {Distance:.1f} cm", (x - (w // 2), y - (h // 2)-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv2.imshow('Frame', Nimg)
    except:
        cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
