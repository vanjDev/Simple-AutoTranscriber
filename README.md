# 🎙️ Whisper Transcriber

A simple Python script that uses [OpenAI Whisper](https://github.com/openai/whisper) to transcribe audio or video into text.  
Supports **CPU-only** or **GPU (CUDA)** for much faster transcriptions.

---

## 🚀 Features
- Convert **.mp3, .wav, .m4a, .mp4** and other audio/video files into text  
- Runs completely **offline** (no API costs)  
- Uses **GPU acceleration** if available
- Supports multiple model sizes: `tiny`, `base`, `small`, `medium`, `large`

---

## 📦 Requirements

1. Install Whisper:
   - pip install openai-whisper
2. Install PyTorch
   - For CPU only: ```bash pip install torch --index-url https://download.pytorch.org/whl/cpu
   - For NVIDIA GPU: ```bash pip install torch --index-url https://download.pytorch.org/whl/cu121
