Voice Assistant for Blind People

This project is designed to help visually impaired users interact with a computer using voice commands. 
The application listens to user input, executes the command, and provides spoken feedback. 
One of the key features is object detection through the camera, which enables users to recognize objects in their surroundings.

🔹 Features

🎙️ Voice Interaction – The system speaks "Listening..." and waits for user commands.
📷 Camera Access – Opens the camera when the user says "open camera".
🧠 Object Detection – Uses deep learning (YOLOv5) to detect and identify objects in real-time.
🗣️ Text-to-Speech (TTS) – Reads out the results to the user, making the experience fully hands-free.
♿ Accessibility – Specially built to support blind and visually impaired people.

🔹 How It Works

User runs the application.

1.System announces: "Listening..."
2.User gives a voice command (e.g., "open camera").
3.Application opens the webcam.
4.Real-time object detection is performed.

Detected objects are spoken out loud for the user.

🔹 Tech Stack

1.Python (Backend logic)
2.OpenCV (Camera handling)
3.YOLOv5 (Object detection)
4.SpeechRecognition (Voice input)
5.pyttsx3 / gTTS (Text-to-Speech)

🔹 Installation

Clone the repository:

git clone https://github.com/Vishakhamishra29/VoiceAssistant.git
cd VoiceAssistant


Install dependencies:

pip install -r requirements.txt


Run the project:

python voice_assistant.py

🔹 Future Improvements

🔹Adding more voice commands (e.g., read documents, navigation).
🔹Support for multiple languages.
🔹Integration with smart devices.

🔹 Contribution

Contributions are welcome! Feel free to fork the repo and submit a pull request.
