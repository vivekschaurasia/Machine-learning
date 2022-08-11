# Face Recognition

#Import libraries
import cv2

#Importing Cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

# Defining a function that will do the detections
def detect(img , frame): 
    face = face_cascade.detectMultiScale( img , 1.3 , 5 )  
                                       
    for (x , y , w , h )in face:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (255,0,0) , 2 )
        roi_img = img[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_img, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        smile = smile_cascade.detectMultiScale(roi_img, 1.7, 22)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0 ,255), 2)
    return frame




# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
video_capture.set(3 , 640)
video_capture.set(4 , 640)
#video_capture.set(10 , 100)


while True:
    _ , frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

"""
#For black and white
while True:
    _ , frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    blaclANDwhite = cv2.cvtColor(canvas , cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', blaclANDwhite)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

video_capture.release()
cv2.destroyAllWindows()



