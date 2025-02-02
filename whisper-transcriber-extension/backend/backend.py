from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import whisper
import os
import torch  # Import torch

app = FastAPI()

# Allow CORS for your Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Adjust if necessary)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the Whisper model on the GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("base").to(device)  # Load the model on the GPU

@app.get("/")
async def root():
    return {"message": "Whisper Transcriber API is running!"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Save the uploaded file temporarily
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Transcribe the audio using Whisper
        result = model.transcribe(file_path)
        transcription = result["text"]

        # Clean up the temporary file
        os.remove(file_path)

        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
