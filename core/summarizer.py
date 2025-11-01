from transformers import pipeline
from nltk.tokenize import sent_tokenize

class Summarizer:
    def __init__(self, model_name="philschmid/bart-large-cnn-samsum"):
        print(f"[+] Loading summarization model: {model_name}")
        self.model = pipeline("summarization", model=model_name)

    def chunk_text(self, text, max_words=700):
        sentences = sent_tokenize(text)
        chunks, chunk, length = [], [], 0
        for s in sentences:
            count = len(s.split())
            if length + count <= max_words:
                chunk.append(s)
                length += count
            else:
                chunks.append(" ".join(chunk))
                chunk, length = [s], count
        if chunk: chunks.append(" ".join(chunk))
        return chunks

    def summarize(self, text, max_length=120, min_length=40):
        chunks = self.chunk_text(text)
        results = []
        for idx, chunk in enumerate(chunks):
            print(f" ↳ Summarizing chunk {idx+1}/{len(chunks)}...")
            summary = self.model(chunk, max_length=max_length, min_length=min_length, truncation=True)[0]['summary_text']
            results.append(summary.strip())
        return " ".join(results)
