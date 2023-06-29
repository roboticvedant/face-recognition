import cv2 as cv
import pickle
cap = cv.VideoCapture(0)
haar_cascade=cv.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
labels = {}
with open("labels.pickle",'rb') as f:
    og_labels = pickle.load(f)
    labels ={v:k for k,v in og_labels.items()}
while True:
    ret, frame = cap.read()
    #cv.imshow("Output", frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_rect = haar_cascade.detectMultiScale(gray, 1.1, 10)
    for(x,y,w,h) in face_rect:
        box = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        #frame_flip=cv.flip(frame, 1)
        roi_gray = gray[y:y+h,x:x+w]
        #img_item="my_img.png"

        id_,conf = recognizer.predict(roi_gray)
        if conf>=45:
            print(labels[id_])
            cv.putText(frame,labels[id_],(x,y),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,0))

        #cv.imwrite(img_item,roi_gray)
        cv.imshow("Output",frame)



    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
