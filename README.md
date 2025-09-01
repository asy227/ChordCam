# **ChordCam**
ChordCam is an interactive desktop app that uses your computer’s webcam to detect hand positions and map them to ukulele chords. It uses MediaPipe Hands for real-time hand landmark detection and can play back audio recordings of defined chords.

## ✨ Features:
    - Detects your hand and recognizes custom chord gestures
    - Plays chord audio when a gesture is recognized
    - Inverted camera view for easier playing orientation
    - Extensible — add more chords and custom finger positions without rewriting core logic  

  
## 🎶Prerequisites:
    - Python 3.10–3.11 (MediaPipe doesn’t yet support 3.12+)
    - Webcam
  

## 🛠️ Tech Stack:
    - Python
    - MediaPipe Hands
    - OpenCV
    - Pygame (for audio playback)
  

## 🎸 Right now, the following ukulele chords are mapped to simple “finger up” patterns:
C → Index up
G → Index + Middle up
Am → Index + Middle + Ring up
F → Index + Middle + Ring + Pinky up

