from fastapi import FastAPI, UploadFile
from core.transcriber import Transcriber
from core.summarizer import Summarizer
from utils.io_utils import save_text
import os

app = FastAPI(title="🎬 Video Summarizer API")

transcriber = Transcriber()
summarizer = Summarizer()

@app.post("/summarize/")
async def summarize_video(file: UploadFile):
    os.makedirs("temp", exist_ok=True)
    temp_path = f"temp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    text = transcriber.transcribe(temp_path)
    summary = summarizer.summarize(text)

    save_text(f"summaries/{file.filename}_summary.txt", summary)
    return {"summary": summary}
