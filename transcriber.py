import whisper
import os

# Load the Whisper model — "base" is fast and decent; you can try "small" or "medium" for better accuracy.
model = whisper.load_model("small")

def transcribe_audio(audio_path):
    """
    Transcribes audio from a given file using Whisper.
    Supports audio and video formats like .mp3, .wav, .mp4.
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"File not found: {audio_path}")
    
    print(f"[+] Transcribing: {audio_path}")
    result = model.transcribe(audio_path,language='en')
    return result['text']

if __name__ == "__main__":
    # Test the transcriber on a sample video/audio
    sample_path = "sample_videos/sample.mp4"  # Replace with your actual file
    transcription = transcribe_audio(sample_path)
    print("\n--- Transcription Result ---\n")
    print(transcription)
