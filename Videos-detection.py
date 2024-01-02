import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import*
import cvzone
import time

model=YOLO('yolov8s.pt')



def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture('23.mp4')
start_time = time.time()

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0
cy1=424
area1=[(87,330) , ( 320,480), ( 750,340 ),(402,282 ) ]
downcar={}


tracker1=Tracker()
tracker2=Tracker()
tracker3=Tracker()



counter1=[]
counter2=[]
counter3=[]
offset=6
while True:    
    ret,frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue
    
    frame=cv2.resize(frame,(1020,500))
   

    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list1=[]
    motorcycle=[]
    list2=[]
    car=[]
    list3=[]
    truck=[]
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'motorcycle' or 'bus' or 'bicycle' or 'car' or 'truck' in c:
          list1.append([x1,y1,x2,y2])
    bbox1_idx=tracker1.update(list1)
    for bbox1 in bbox1_idx:
        # for i in motorcycle:
        x3,y3,x4,y4,id1=bbox1
        cx=int(x3+x4)//2
        cy=int(y3+y4)//2     
        result=cv2.pointPolygonTest(np.array(area1,np.int32),((cx,cy)),False)
        if result >=0:
           downcar[id1] = (cx,cy)
        if id1 in downcar:
            cv2.circle(frame,(cx,cy),4,(0,255,0),-1)
            cv2.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),1)
            cvzone.putTextRect(frame,f'{id1}',(x3,y3),1,1)
            if counter1.count(id1)==0:
                counter1.append(id1)
                counter2.append(id1)
   
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(0,255,0),2)

  
    carcount=(len(counter1))
    totalcars=(len(counter2))
    cvzone.putTextRect(frame,f'Cars :{carcount}',(19,30),2,1)
    cvzone.putTextRect(frame,f'Total cars :{totalcars}',(19,80),2,1)
     # Check if 10 seconds have passed, reset counters
    if time.time() - start_time > 20:
        counter1 = []
        carcount = 0
        start_time = time.time()

    if carcount > 15:
        cvzone.putTextRect(frame, 'Crowded', (100, 200), 3, 2)
    elif carcount < 15 and carcount > 12:
        cvzone.putTextRect(frame, 'Medium', (100, 200), 3, 2)
    else:
        cvzone.putTextRect(frame, 'Deserted', (100, 200), 3, 2)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()