import cv2
import mediapipe as mp

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.6)

# Function to detect fist and its position
def detect_object_position():
    cap = cv2.VideoCapture(0)  # Iriun webcam stream

    direction = None
    success, frame = cap.read()

    if not success:
        cap.release()
        return None

    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get tip positions of fingers
        finger_tips = [8, 12, 16, 20]  # Index to pinky
        folded_fingers = 0

        for tip in finger_tips:
            if hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y:
                folded_fingers += 1

        # Fist = all fingers folded
        if folded_fingers >= 4:
            # Get x position of wrist to determine left/center/right
            wrist_x = hand_landmarks.landmark[0].x

            if wrist_x < 0.33:
                direction = "left"
            elif wrist_x > 0.66:
                direction = "right"
            else:
                direction = "center"
        else:
            direction = None  # Not a fist
    else:
        direction = None

    cap.release()
    return direction
