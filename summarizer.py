from transformers import pipeline
from nltk.tokenize import sent_tokenize

# Load summarization pipeline using BART
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_words=400):
    """
    Splits the text into sentence-based chunks of ~400 words each.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_len = 0

    for sentence in sentences:
        word_count = len(sentence.split())
        if current_len + word_count <= max_words:
            current_chunk.append(sentence)
            current_len += word_count
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]
            current_len = word_count

    # Add the last chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def clean_summary(summary_text):
    """
    Cleans common filler words from the summary.
    """
    fillers = ["But yeah, ", "So yeah, ", "Yeah, ", "obviously ", "you know, "]
    for filler in fillers:
        summary_text = summary_text.replace(filler, "")
    return summary_text.strip()

def summarize_text(text, max_length=60, min_length=25):
    """
    Summarizes long text by chunking and summarizing each chunk individually.
    Returns a combined summary.
    """
    if not text.strip():
        return "[Error] Empty transcription passed to summarizer."

    chunks = chunk_text(text)
    print(f"[+] Summarizing {len(chunks)} chunk(s)...")

    summary_chunks = []
    for idx, chunk in enumerate(chunks):
        print(f"    ↳ Summarizing chunk {idx + 1}...")
        summary = summarizer(
            chunk,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
            truncation=True
        )
        cleaned = clean_summary(summary[0]['summary_text'])
        print(f"        ✔ Chunk {idx + 1} summary: {cleaned}")
        summary_chunks.append(cleaned)

    return "\n".join(summary_chunks)

if __name__ == "__main__":
    sample_text = """
    Facebook, founded by Mark Zuckerberg, started as a social networking site for college students and grew into one of the biggest tech companies globally. 
    Over the years, it has acquired multiple companies like Instagram and WhatsApp. Despite its success, Facebook has faced criticism over data privacy 
    and misinformation. It recently rebranded to Meta, focusing on building the metaverse as its next major platform.
    """
    print("\n--- Summary ---\n")
    print(summarize_text(sample_text))
