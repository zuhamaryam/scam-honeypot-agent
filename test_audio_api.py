"""
Audio Input Test for GUVI Hackathon
Tests the API with audio input (base64 encoded)
"""

import requests
import json
import base64

# Configuration
BASE_URL = "https://scam-honeypot-agent-production-518a.up.railway.app"  # Replace with your deployed URL
API_KEY = "HONEY-POT-SECURE-KEY-2024-GUVI-HACK"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}


def convert_audio_to_base64(audio_file_path):
    """Convert audio file to base64"""
    with open(audio_file_path, 'rb') as audio_file:
        audio_data = audio_file.read()
        base64_audio = base64.b64encode(audio_data).decode('utf-8')
        return base64_audio


def test_with_audio_base64():
    """Test API with audio in base64 format"""
    print("\n=== Testing Audio Input (Base64) ===\n")
    
    # For actual testing, you would convert your audio file
    # audio_base64 = convert_audio_to_base64("path/to/your/audio.mp3")
    
    # Mock audio base64 (for demonstration)
    # In real scenario, use actual audio file
    audio_base64 = "SGVsbG8gd29ybGQh"  # This is just "Hello world!" encoded
    
    payload = {
        "sessionId": "audio-test-001",
        "message": {
            "sender": "scammer",
            "text": None,  # No text, only audio
            "timestamp": 1770005528731,
            "audio_base64": audio_base64,
            "audio_url": None
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "Phone",
            "language": "hindi",
            "locale": "IN"
        }
    }
    
    print("Sending audio input to API...")
    print(f"Endpoint: {BASE_URL}/api/detect")
    
    response = requests.post(
        f"{BASE_URL}/api/detect",
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ SUCCESS!")
        print(f"Status: {result['status']}")
        print(f"Sara's Reply: {result['reply']}")
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(response.text)


def test_with_audio_url():
    """Test API with audio URL"""
    print("\n=== Testing Audio Input (URL) ===\n")
    
    # Example audio URL (replace with actual MP3 URL)
    audio_url = "https://example.com/scam-call.mp3"
    
    payload = {
        "sessionId": "audio-url-test-001",
        "message": {
            "sender": "scammer",
            "text": None,
            "timestamp": 1770005528731,
            "audio_base64": None,
            "audio_url": audio_url
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "Phone",
            "language": "hindi",
            "locale": "IN"
        }
    }
    
    print("Sending audio URL to API...")
    print(f"Audio URL: {audio_url}")
    
    response = requests.post(
        f"{BASE_URL}/api/detect",
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"\n✅ SUCCESS!")
        print(f"Sara's Reply: {result['reply']}")
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(response.text)


def test_with_text_and_audio():
    """Test with both text and audio (text takes priority if both provided)"""
    print("\n=== Testing Text + Audio Input ===\n")
    
    payload = {
        "sessionId": "mixed-test-001",
        "message": {
            "sender": "scammer",
            "text": "Madam aapka account block hone wala hai",
            "timestamp": 1770005528731,
            "audio_base64": "SGVsbG8=",
            "audio_url": None
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "Phone",
            "language": "hindi",
            "locale": "IN"
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/api/detect",
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ SUCCESS!")
        print(f"Sara's Reply: {result['reply']}")
    else:
        print(f"❌ ERROR: {response.status_code}")


def create_guvi_compatible_request():
    """
    Create request format exactly as shown in GUVI hackathon images
    """
    print("\n=== GUVI Hackathon Compatible Request ===\n")
    
    # This matches the format shown in your screenshot
    payload = {
        "sessionId": "guvi-test-session-001",
        "message": {
            "sender": "scammer",
            "text": None,  # Will be transcribed from audio
            "timestamp": 1770005528731,
            "audio_base64": "BASE64_ENCODED_AUDIO_HERE",  # Replace with actual base64
            "audio_url": None  # Or provide MP3 URL here
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "Phone",
            "language": "hindi",  # As shown in screenshot
            "locale": "IN"
        }
    }
    
    print("Request format for GUVI submission:")
    print(json.dumps(payload, indent=2))
    
    print("\n" + "="*60)
    print("TO USE THIS:")
    print("1. Replace BASE64_ENCODED_AUDIO_HERE with actual audio base64")
    print("2. Or provide audio_url with link to MP3 file")
    print("3. Send to your deployed endpoint")
    print("="*60)


def main():
    print("="*60)
    print("AUDIO INPUT TESTING FOR GUVI HACKATHON")
    print("="*60)
    
    # Show GUVI format
    create_guvi_compatible_request()
    
    # Uncomment to test with your deployed API:
    # test_with_audio_base64()
    # test_with_audio_url()
    # test_with_text_and_audio()


if __name__ == "__main__":
    main()
