# 📝 Whisper Transcriber - Chrome Extension + FastAPI Backend

An open-source Chrome extension that allows users to transcribe audio files using OpenAI's Whisper AI, with a FastAPI backend.

Project Structure

whisper-transcriber-project/
│
├── backend/                     # 🛠 Backend server for Whisper AI
│   ├── backend.py               # FastAPI server
│   ├── requirements.txt         # Python dependencies         
│
├── chrome-extension/            # 🌐 Chrome Extension files
│   ├── manifest.json            # Chrome extension metadata
│   ├── popup.html               # UI for the extension
│   ├── popup.js                 # JavaScript logic (API calls)
│   ├── styles.css               # Styling for the extension
│   └── icons/                   # Extension icons
│       ├── icon16.png
│       ├── icon48.png
│       └── icon128.png
│


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
