import cv2
import mediapipe as mp
import pygame

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Pygame for sound
pygame.mixer.init()

# Load sounds (replace these with your own recordings!)
chord_sounds = {
    1: "sounds/C_chord.wav",
    2: "sounds/G_chord.wav",
    3: "sounds/Am_chord.wav",
    4: "sounds/F_chord.wav"
}
current_chord = None

# Function to count fingers up (simplified)
def count_fingers(hand_landmarks):
    tips_ids = [8, 12, 16, 20]  # index, middle, ring, pinky tips
    count = 0
    for tip_id in tips_ids:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            count += 1
    return count

# Function to play sound
def play_chord(finger_count):
    global current_chord
    if finger_count in chord_sounds and current_chord != finger_count:
        current_chord = finger_count
        pygame.mixer.music.load(chord_sounds[finger_count])
        pygame.mixer.music.play()

# Open webcam
cap = cv2.VideoCapture(0)  # Use 1 or -1 if you need to invert the camera source

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip frame horizontally for mirror view
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_up = count_fingers(hand_landmarks)
            play_chord(fingers_up)

            # Show current chord
            cv2.putText(frame, f"Chord: {fingers_up} fingers", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("ChordCam", frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
