#INSTALLING REQUIRED DEPENDENCIES
!pip install mediapipe opencv-python 
!pip install pyautogui
import numpy as np
import mediapipe as mp
import cv2

import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(model_complexity = 0, min_detection_confidence = 0.8, min_tracking_confidence = 0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read() 

        # CONVERTING BGR IMAGE TO RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h,w,c = image.shape

        #FLIPPING THE IMAGE HORIZONTALLY 
        image = cv2.flip(image, 1)

        #IMPROVING PERFORMANCE 
        image.flags.writeable = False 

        #PROCESSING THE IMAGE AND FINDING HANDS  
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        print(results)

        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color = (1, 1, 1), thickness = 2, circle_radius = 4),
                                          mp_drawing.DrawingSpec(color = (1, 1, 1), thickness = 2, circle_radius = 2),
                                         )
                
                index_finger_tip = hand.landmark[0]
        
                index_finger_tip_x = index_finger_tip.x * w
                index_finger_tip_y = index_finger_tip.y * w
        
                if index_finger_tip_x > w/2:
                    cv2.putText(image, "GAS", (500, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('left')
                elif index_finger_tip_x < w/2:
                    cv2.putText(image, "BRAKE", (500,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('right')
        
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    

cap.release()
cv2.destroyAllWindows()
