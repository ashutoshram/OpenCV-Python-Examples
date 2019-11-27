import cv2


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    red = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    terra = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original", frame)
    cv2.imshow("Gray", gray)
    cv2.imshow("Red", red)
    cv2.imshow("Terra", terra)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
    
