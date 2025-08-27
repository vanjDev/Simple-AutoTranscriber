import whisper
import torch

def transcribe_audio(file_path):
    model = whisper.load_model("small")  # try "medium" or "large-v2" if you want max accuracy
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    audio_file = "sample.mp3"
    text = transcribe_audio(audio_file)
    print("Transcription:\n", text)
