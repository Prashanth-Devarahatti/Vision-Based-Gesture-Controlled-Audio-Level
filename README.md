# Vision-Based Gesture-Controlled Audio Level

This project utilizes computer vision techniques to control the audio level based on hand gestures captured via a webcam. The system tracks hand movements in real-time and adjusts the volume accordingly.

## Dependencies:

- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- NumPy (`numpy`)
- PyCaw (`pycaw`)

You can install the required dependencies via pip:

```
pip install opencv-python mediapipe numpy pycaw
```

## Usage:

1. Connect a webcam to your computer.
2. Run the Python script provided in this repository.
3. The webcam feed will open, and your hand gestures will be tracked.
4. Adjust the volume by moving your hand up or down:
   - Move your hand up to increase the volume.
   - Move your hand down to decrease the volume.
5. The current volume level will be displayed on the screen.

## Code Structure:

- **calculate_volume(length)**: This function calculates the volume level based on the distance between two points on the hand.
- **draw_landmarks(img, multi_hand_landmarks)**: This function draws landmarks on detected hands in the webcam feed.
- **AudioUtilities.GetSpeakers()**: Retrieves the audio output device (speakers).
- **hands.process(imgRGB)**: Processes the webcam feed to detect hand landmarks.
- **while True:**: The main loop continuously captures frames from the webcam, processes them, and adjusts the volume based on hand gestures.
- **cv2.imshow("Image", img)**: Displays the webcam feed with hand landmarks and volume information.
- **cv2.waitKey(1)**: Waits for a key press to exit the program.

## Notes:

- Ensure that you have a working webcam connected to your system.
- Make sure that your environment is suitable for hand detection (sufficient lighting, clear background, etc.).
- Experiment with different hand gestures and distances to control the volume effectively.
- This project utilizes the `pycaw` library to interact with the system's audio controls. Ensure that it is installed and functioning correctly.
- Feel free to modify and extend the code according to your requirements.

