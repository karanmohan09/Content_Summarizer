
# 🎬 AI Video Summarizer

**Automatic Video Transcription and Summarization using Whisper + BART**

A full end-to-end AI application that converts videos or audio files into concise summaries.  
It uses **OpenAI Whisper** for speech-to-text transcription and **BART/SAMSum** for intelligent text summarization.

Built with a **modular Python architecture**, **Streamlit web interface**, and fully **Dockerized** for reproducibility and deployment.

----------

## 🚀 Features

✅ **Automatic Transcription** — Extracts text from any MP4, MP3, or WAV file using OpenAI Whisper  
✅ **Smart Summarization** — Generates clear, concise summaries using BART/SAMSum  
✅ **Interactive Web UI** — Clean Streamlit interface for uploading and viewing results  
✅ **FastAPI Backend** — Optional REST API for programmatic access  
✅ **Reproducible with Docker** — Run anywhere with one command  
✅ **Modular Design** — Easy to extend or swap models

----------

## 🧱 Project Structure

📦 **Content_Summarizer_EndToEnd/**

Content_Summarizer_EndToEnd/
│
├── app/
│   ├── api.py             # FastAPI backend
│   ├── ui.py              # Streamlit web app
│   └── __init__.py
│
├── core/
│   ├── transcriber.py     # Whisper transcription logic
│   ├── summarizer.py      # BART summarization logic
│   ├── evaluator.py       # ROUGE metric evaluator
│   └── __init__.py
│
├── utils/
│   ├── io_utils.py        # Helper functions (save/load)
│   └── __init__.py
│
├── main.py                # FastAPI entrypoint
├── Dockerfile             # Docker configuration
├── .dockerignore
├── .gitignore
└── requirements.txt


----------

## 🧠 Tech Stack

| Component        | Technology                                         |
|------------------|----------------------------------------------------|
| Frontend (UI)    | Streamlit                                          |
| Backend API      | FastAPI                                            |
| Transcription    | OpenAI Whisper                                     |
| Summarization    | BART / SAMSum via Hugging Face Transformers        |
| Language         | Python 3.10                                        |
| Containerization | Docker                                             |
| Evaluation       | ROUGE Score                                        |


----------

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the repository

`git clone https://github.com/<your-username>/Content_Summarizer_EndToEnd.git cd Content_Summarizer_EndToEnd` 

### 2️⃣ Create & activate virtual environment

`python -m venv vidsum_env
.\vidsum_env\Scripts\activate # Windows  # OR  source vidsum_env/bin/activate # macOS/Linux` 

### 3️⃣ Install dependencies

`pip install -r requirements.txt` 

### 4️⃣ Run Streamlit app

`streamlit run app/ui.py` 

### 5️⃣ Access the app

➡️ Open http://localhost:8501 in your browser.

----------

## 🐳 Run with Docker (Recommended)

### 1️⃣ Build the image

`docker build -t video-summarizer .` 

### 2️⃣ Run the container

`docker run -p 8501:8501 video-summarizer` 

### 3️⃣ Open the app

➡️ http://localhost:8501

----------

## 🧪 Example Workflow

1.  Upload a `.mp4`, `.mp3`, or `.wav` file.
    
2.  The app automatically transcribes the speech → text.
    
3.  Summarizer processes the text into concise highlights.
    
4.  View, copy, or download your summary instantly.
    

----------

## 📈 Example Output

**Input (transcribed text snippet):**

> “Michael discussed the team’s pre-season progress, injuries, and readiness for upcoming matches.”

**Output (summary):**

> “The coach reviewed training progress and confirmed the team’s preparation for the next game.”

----------

## 🧰 Environment Variables (Optional)

| Variable              | Description                         | Default                                |
|------------------------|-------------------------------------|----------------------------------------|
| `MODEL_NAME`           | Hugging Face summarization model     | `philschmid/bart-large-cnn-samsum`     |
| `WHISPER_MODEL`        | Whisper model size                   | `small`                                |
| `STREAMLIT_SERVER_PORT`| Streamlit port                       | `8501`                                |


----------

## 🧩 API Mode (Optional)

To run as an API server instead of Streamlit, modify your Dockerfile:

`CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]` 

Then run:

`docker build -t video-summarizer-api .
docker run -p 8000:8000 video-summarizer-api` 

Access interactive docs at:  
➡️ http://localhost:8000/docs

----------

## 📦 Deployment Options

-   **Docker Hub** → Push and share your image
    
-   **Render / Railway** → Host FastAPI backend
    
-   **Hugging Face Spaces** → Host Streamlit UI
    
-   **AWS ECS / GCP Cloud Run** → Production-grade deployments


    
----------

## 🪶 License

This project is licensed under the **MIT License** — free to use, modify, and share.
