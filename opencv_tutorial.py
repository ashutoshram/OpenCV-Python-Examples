import cv2
import numpy as np


def startCamera():
    cap = cv2.VideoCapture(0)
    
    fourcc = cv2.VideoWriter.fourcc('Y', 'U', 'Y', 'V');
    cap.set(cv2.CAP_PROP_FOURCC, fourcc)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1088)
    

    
    while True:
        ret, frame = cap.read()

        # Converting to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frames
        
        cv2.imshow('gray', gray)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

startCamera()
