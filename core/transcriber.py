import whisper
import os

class Transcriber:
    def __init__(self, model_name="small"):
        print(f"[+] Loading Whisper model: {model_name}")
        self.model = whisper.load_model(model_name)

    def transcribe(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        print(f"[+] Transcribing: {file_path}")
        result = self.model.transcribe(file_path, language='en')
        return result['text']
