# 🎬 Video Content Summarizer

This project automatically summarizes spoken content in videos using OpenAI Whisper (speech-to-text) and BART (text summarization). Built with Python, PyTorch, HuggingFace Transformers, and NLTK.

## 📂 Features

- Transcribes audio from `.mp4` videos
- Generates concise summaries from transcriptions
- Supports long inputs via intelligent chunking
- Outputs clean text files

## ⚙️ Technologies

- Python
- OpenAI Whisper
- HuggingFace Transformers (BART)
- NLTK

## 📁 Usage

```bash
conda activate vidsum
python main.py
```

## 📄 Outputs

```bash
output/transcript.txt → Full transcript of the video's audio
output/summary.txt → Clean, concise summary of the transcript
```
