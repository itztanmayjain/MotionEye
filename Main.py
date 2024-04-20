import cv2
import winsound

cam=cv2.VideoCapture(0)
while cam.isOpened():
    result,frame1= cam.read()
    result,frame2= cam.read()
    diff=cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    for c in contours:
        if cv2.contourArea(c) < 5000:                                           #To capture bigger contour
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)               #Make Rectangle contour 
        #winsound.Beep(500,200)                                                 #To make alert sound (volume,duration(milisec) ) 
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)                     #To make customize alert sound 
        cv2.imwrite("alert.png", frame1)                                        #To capture motion 




    if cv2.waitKey(10)==ord('q'):                                               #To kill camera             
        break
    cv2.imshow('Tanmay Cam',frame1)