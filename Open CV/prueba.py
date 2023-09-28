import cv2

cap = cv2.VideoCapture(0)

 ##DE TAREA CREAR DOS REPRODUCTORES DE VIDEO QUE HAGA QUE UNO MUESTRE UN PEDACITO DE VIDEO DEL ORIGINAL
while(True):
    _, frame = cap.read()

    cv2.imshow("Mi primer OPENCV", frame)
    cv2.rectangle(frame,(100, 150), (500, 600),(255,0,0),-1)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cap.destroyAllWindows()