pip install pyserial
pip install opencv-python

import cv2
import serial

arduino = serial.Serial('COM16', 9600)

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges in HSV
    colors = {
    'RED': ((0, 100, 100), (10, 255, 255)),
    'GREEN': ((35, 50, 50), (85, 255, 255)),
    'YELLOW': ((20, 100, 100), (35, 255, 255))}


    for color, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, lower, upper)
        
        if cv2.countNonZero(mask) > 500:  # Threshold for detection
            arduino.write(color[0].encode())  # Send 'R', 'G', or 'Y'
            return color
cap = cv2.VideoCapture(0)
while True: 
    ret, frame = cap.read() 
    if not ret:
        break
    
    color = detect_color(frame)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
