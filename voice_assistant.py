import torch
import cv2
import numpy as np
import pyttsx3
import time
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load YOLOv5 model (download if not already cached)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

# Initialize speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Speak text aloud
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen for the keyword "open camera"
def wait_for_command():
    speak("Say 'open camera' to start.")
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("🎤 Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)
                print("Heard:", command)
                if "open camera" in command.lower():
                    speak("Opening camera now.")
                    return True
                else:
                    speak("Please say 'open camera'.")
            except sr.WaitTimeoutError:
                print("⏰ Listening timed out, retrying...")
            except sr.UnknownValueError:
                speak("I didn't catch that.")
            except sr.RequestError:
                speak("Speech recognition service error.")
                break

# Start camera and detect objects
def detect_objects():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak("Camera failed to open.")
        return

    spoken_labels = set()
    last_spoken_time = time.time()

    cv2.namedWindow("Object Detection", cv2.WINDOW_NORMAL)
    speak("Camera is open. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLOv5 inference (no gradient needed)
        with torch.no_grad():
            results = model(frame)

        detections = results.pandas().xyxy[0]
        detected_labels = set()

        for _, row in detections.iterrows():
            if row['confidence'] > 0.5:
                label = row['name']
                detected_labels.add(label)

                # Draw bounding box
                x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {row['confidence']:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Speak labels every 5 seconds
        now = time.time()
        if now - last_spoken_time > 5 and detected_labels:
            new_labels = detected_labels - spoken_labels
            if new_labels:
                speak("I see: " + ", ".join(new_labels))
                spoken_labels.update(new_labels)
                last_spoken_time = now

        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# === MAIN ===
if __name__ == "__main__":
    success = wait_for_command()
    if success:
        detect_objects()