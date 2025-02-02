# 📝 Whisper Transcriber - Chrome Extension + FastAPI Backend

An open-source Chrome extension that allows users to transcribe audio files using OpenAI's Whisper AI, with a FastAPI backend.

## 🚀 Features
✅ Upload an audio file (.mp3, .wav, etc.)  
✅ Transcribe the file using Whisper AI  
✅ View transcription inside the Chrome extension  

## 📌 How to Install the Chrome Extension
1. Clone this repository:
2. Open **Chrome** and go to:
3. Enable **Developer Mode**.
4. Click **Load Unpacked** and select the `chrome-extension/` folder.
5. The extension is now installed! 🎉

## 🛠️ How to Run the Backend
1. Install dependencies:
2. Start the FastAPI server:
3. Test the API with `curl`:
```bash
curl -X POST "http://localhost:8000/transcribe" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@your-audio-file.mp3"

Feel free to fork this repository, make improvements, and submit pull requests.

If you have any issues, email me at ahmad.akhlaq.5983@gmail.com
