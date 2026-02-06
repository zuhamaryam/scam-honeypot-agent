# 🎵 Audio Input Support - GUVI Hackathon

## 📋 Overview

Aapka scam honeypot ab **audio input** support karta hai! GUVI hackathon ke requirement ke mutabik.

---

## 🔊 Audio Input Formats Supported

### 1️⃣ **Audio Base64** (Recommended)
```json
{
  "message": {
    "sender": "scammer",
    "text": null,
    "audio_base64": "BASE64_ENCODED_AUDIO_STRING",
    "audio_url": null
  }
}
```

### 2️⃣ **Audio URL** (MP3/OGG)
```json
{
  "message": {
    "sender": "scammer",
    "text": null,
    "audio_base64": null,
    "audio_url": "https://example.com/scam-call.mp3"
  }
}
```

### 3️⃣ **Text + Audio** (Text priority)
```json
{
  "message": {
    "sender": "scammer",
    "text": "Madam account block hone wala hai",
    "audio_base64": "...",
    "audio_url": null
  }
}
```

---

## 🛠️ Audio Ko Base64 Mein Convert Karna

### Method 1: Python Script Use Karo

```bash
# Audio converter script use karo
python audio_converter.py your_audio_file.mp3

# Output:
# - Prints base64
# - Saves to .base64.txt file
# - Shows API request format
```

### Method 2: Online Tool

1. https://base64.guru/converter/encode/audio pe jao
2. Audio file upload karo
3. Base64 copy karo

### Method 3: Command Line

```bash
# Linux/Mac
base64 audio_file.mp3

# Windows PowerShell
[Convert]::ToBase64String([IO.File]::ReadAllBytes("audio_file.mp3"))
```

---

## 📝 Complete API Request Example

### Headers:
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
Content-Type: application/json
```

### Request Body:
```json
{
  "sessionId": "audio-test-001",
  "message": {
    "sender": "scammer",
    "text": null,
    "timestamp": 1770005528731,
    "audio_base64": "T2dnUwACAAAAAAAAAAAAAAAAAAAAACqCBoIBE09wdXNI...",
    "audio_url": null
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "Phone",
    "language": "hindi",
    "locale": "IN"
  }
}
```

### Response:
```json
{
  "status": "success",
  "reply": "Haan ji... bolo kya baat hai?"
}
```

---

## 🧪 Testing Audio Input

### Using Provided Scripts:

```bash
# 1. Convert audio to base64
python audio_converter.py sample_audio.mp3

# 2. Test the API
python test_audio_api.py
```

### Using cURL:

```bash
curl -X POST https://your-app.railway.app/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d @guvi_audio_test_request.json
```

---

## 📋 GUVI Hackathon Format

GUVI ki requirement exactly yeh hai:

```json
{
  "sessionId": "session-id",
  "message": {
    "sender": "scammer",
    "text": null,
    "timestamp": 1770005528731,
    "audio_base64": "BASE64_STRING_HERE",
    "audio_url": null
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "Phone",
    "language": "hindi",
    "locale": "IN"
  }
}
```

**Key Fields:**
- ✅ `language: "hindi"` - As shown in screenshot
- ✅ `audio_base64` - Base64 encoded audio
- ✅ `audio_url` - Alternative MP3 URL
- ✅ `text: null` - When only audio provided

---

## 🔄 How Audio Processing Works

1. **Audio Received** → API receives base64 or URL
2. **Transcription** → Audio converted to text
3. **Scam Detection** → Text analyzed for scam patterns
4. **Sara Responds** → Natural Hinglish reply generated
5. **Intelligence Extracted** → UPI IDs, phone numbers, etc.
6. **GUVI Callback** → Final report sent

---

## 📁 Files Provided

| File | Purpose |
|------|---------|
| `audio_converter.py` | Convert audio to base64 |
| `test_audio_api.py` | Test audio API endpoint |
| `guvi_audio_test_request.json` | Sample request |
| `sample_audio_base64.txt` | Sample base64 audio |

---

## 🎯 Sample Workflow

### Step 1: Convert Audio
```bash
python audio_converter.py scam_call.mp3
# Output: scam_call.mp3.base64.txt
```

### Step 2: Copy Base64
```bash
cat scam_call.mp3.base64.txt
# Copy the base64 string
```

### Step 3: Create Request
```json
{
  "sessionId": "test-001",
  "message": {
    "audio_base64": "PASTE_BASE64_HERE"
  }
}
```

### Step 4: Send to API
```bash
curl -X POST https://your-url/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -d @request.json
```

---

## ⚠️ Important Notes

### Audio Size Limits:
- Maximum: 5 MB
- Recommended: < 1 MB
- Format: MP3, OGG, WAV

### Audio Quality:
- Sample Rate: 16kHz or higher
- Channels: Mono recommended
- Bitrate: 64 kbps minimum

### Transcription:
- Currently placeholder implementation
- Production: Integrate OpenAI Whisper
- Or: Use Google Speech-to-Text
- Or: Azure Speech Services

---

## 🚀 Production Integration

For production deployment, integrate actual speech-to-text:

### Option 1: OpenAI Whisper
```python
import openai

async def transcribe_audio(audio_base64):
    response = await openai.Audio.atranscribe(
        model="whisper-1",
        file=audio_data
    )
    return response["text"]
```

### Option 2: Google Speech-to-Text
```python
from google.cloud import speech

async def transcribe_audio(audio_base64):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        language_code="hi-IN"
    )
    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript
```

---

## ✅ Testing Checklist

Before GUVI submission:

- [ ] Audio converts to base64
- [ ] API accepts audio_base64 field
- [ ] API accepts audio_url field
- [ ] Language field set to "hindi"
- [ ] Sara responds naturally
- [ ] Intelligence extraction works
- [ ] GUVI callback successful
- [ ] Deployed URL working

---

## 📞 Sample Audio Test

File provided: `sample_audio_base64.txt`

Use this to test your deployment:

```bash
# Quick test
curl -X POST https://your-app.railway.app/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d @guvi_audio_test_request.json
```

---

## 🆘 Troubleshooting

### Error: "Either text or audio must be provided"
**Solution:** Make sure either `text` or `audio_base64/audio_url` is present

### Error: "Invalid base64"
**Solution:** Check base64 encoding is correct, no extra characters

### Audio not transcribing
**Solution:** For production, integrate Whisper or Google Speech-to-Text

---

**Audio support ready! Test karo aur GUVI mein submit karo! 🎉**
