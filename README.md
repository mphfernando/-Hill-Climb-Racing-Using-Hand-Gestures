# -Hill-Climb-Racing-Using-Hand-Gestures
This project implements a gesture-controlled interface for the Hill Climb Racing game, leveraging MediaPipe Hands for real-time hand tracking and gesture recognition. The project enables users to play the game using their index finger movements, providing an innovative and interactive experience.

## Features
Tracks hand landmarks using MediaPipe Hands.
Maps index finger movements to game actions:
GAS (Accelerate): Index finger moves right.
BRAKE: Index finger moves left.
Simulates keyboard inputs using PyAutoGUI for seamless integration with the game.
## How It Works
Video Capture: Uses OpenCV to capture video from the webcam.
Hand Tracking: MediaPipe detects and tracks hand landmarks in real time.
Gesture Recognition: Calculates the position of the index finger tip to determine the action.
Keyboard Simulation: PyAutoGUI sends "right" and "left" key presses based on the recognized gesture.
  
## Tools/Technologies Used
MediaPipe: Hand tracking and gesture recognition.
OpenCV: Video frame processing.
PyAutoGUI: Keyboard event simulation.
## Future Enhancements
Add more gestures to control additional game actions.
Integrate with other games or applications for gesture-based control.
Enhance gesture detection for multi-player support.


