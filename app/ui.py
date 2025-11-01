import sys, os

# Force Python to treat project root as importable
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)


import streamlit as st
from core.transcriber import Transcriber
from core.summarizer import Summarizer
import os

st.set_page_config(page_title="🎬 AI Video Summarizer", layout="wide")
st.title("🎥 AI-Powered Video Summarizer")

@st.cache_resource
def load_models():
    transcriber = Transcriber(model_name="small")
    summarizer = Summarizer(model_name="philschmid/bart-large-cnn-samsum")
    return transcriber, summarizer

transcriber, summarizer = load_models()

uploaded_file = st.file_uploader("📂 Upload a video or audio file", type=["mp4", "mp3", "wav"])

if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Only transcribe if not already done
    if "transcription" not in st.session_state or st.session_state["file"] != uploaded_file.name:
        with st.spinner("🎧 Transcribing audio..."):
            text = transcriber.transcribe(file_path)
        st.session_state["transcription"] = text
        st.session_state["file"] = uploaded_file.name
    else:
        text = st.session_state["transcription"]

    st.subheader("🗒️ Transcription")
    st.text_area("Transcribed Text", text, height=200)

    # Only summarize if not already done
    if "summary" not in st.session_state or st.session_state["file"] != uploaded_file.name:
        with st.spinner("✍️ Generating summary..."):
            summary = summarizer.summarize(text)
        st.session_state["summary"] = summary
    else:
        summary = st.session_state["summary"]

    st.success("✅ Summary generated successfully!")
    st.subheader("📜 Summary")
    st.text_area("Generated Summary", summary, height=250)

    st.download_button("💾 Download Summary", summary, file_name="summary.txt")
else:
    st.info("👆 Upload an MP4, MP3, or WAV file to begin.")
