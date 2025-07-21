import os
from transcriber import transcribe_audio
from summarizer import summarize_text

def main():
    # Path to video
    video_path = "sample_videos/sample.mp4"

    # Step 1: Transcribe
    print("\n[1] Transcribing audio from video...")
    transcription = transcribe_audio(video_path)

    if not transcription.strip():
        print("[ERROR] No transcription generated.")
        return

    print("[✔] Transcription done.")

    # Step 2: Summarize
    print("\n[2] Summarizing transcription...")
    summary = summarize_text(transcription)
    print("[✔] Summarization complete.")

    # Step 3: Save to file
    filename = os.path.splitext(os.path.basename(video_path))[0]
    output_path = f"summaries/{filename}_summary.txt"

    os.makedirs("summaries", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== TRANSCRIPTION ===\n\n")
        f.write(transcription + "\n\n")
        f.write("=== SUMMARY ===\n\n")
        f.write(summary)

    print(f"\n[✔] Summary saved to {output_path}")

if __name__ == "__main__":
    main()
