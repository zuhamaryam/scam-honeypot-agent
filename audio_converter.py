"""
Audio File to Base64 Converter
Converts audio files (OGG, MP3, WAV) to base64 format for API testing
"""

import base64
import os
import sys


def convert_audio_to_base64(audio_file_path):
    """
    Convert audio file to base64 string
    """
    if not os.path.exists(audio_file_path):
        print(f"❌ Error: File not found: {audio_file_path}")
        return None
    
    try:
        # Read audio file
        with open(audio_file_path, 'rb') as audio_file:
            audio_data = audio_file.read()
        
        # Convert to base64
        base64_audio = base64.b64encode(audio_data).decode('utf-8')
        
        # Get file size
        file_size = len(audio_data)
        base64_size = len(base64_audio)
        
        print(f"✅ Conversion successful!")
        print(f"📁 File: {audio_file_path}")
        print(f"📊 Original size: {file_size:,} bytes ({file_size/1024:.2f} KB)")
        print(f"📊 Base64 size: {base64_size:,} bytes ({base64_size/1024:.2f} KB)")
        print(f"\n📝 Base64 (first 100 chars):")
        print(base64_audio[:100] + "...")
        
        # Save to file
        output_file = audio_file_path + ".base64.txt"
        with open(output_file, 'w') as f:
            f.write(base64_audio)
        
        print(f"\n💾 Full base64 saved to: {output_file}")
        
        return base64_audio
        
    except Exception as e:
        print(f"❌ Error converting file: {str(e)}")
        return None


def create_api_request_json(audio_base64, session_id="audio-test-001"):
    """
    Create complete API request JSON with audio
    """
    import json
    
    request_json = {
        "sessionId": session_id,
        "message": {
            "sender": "scammer",
            "text": None,
            "timestamp": 1770005528731,
            "audio_base64": audio_base64[:50] + "...",  # Truncated for display
            "audio_url": None
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "Phone",
            "language": "hindi",
            "locale": "IN"
        }
    }
    
    print("\n📋 API Request Format:")
    print("="*60)
    print(json.dumps(request_json, indent=2))
    print("="*60)
    print("\n💡 Replace audio_base64 '...' with full base64 from saved file")


def main():
    print("="*60)
    print("🎵 AUDIO TO BASE64 CONVERTER")
    print("="*60)
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python audio_converter.py <audio_file_path>")
        print("\nExample:")
        print("  python audio_converter.py my_audio.mp3")
        print("  python audio_converter.py scam_call.ogg")
        print("  python audio_converter.py voice_message.wav")
        print()
        
        # Try to find audio files in current directory
        audio_extensions = ['.mp3', '.ogg', '.wav', '.m4a']
        found_files = []
        
        for file in os.listdir('.'):
            if any(file.lower().endswith(ext) for ext in audio_extensions):
                found_files.append(file)
        
        if found_files:
            print("📁 Audio files found in current directory:")
            for f in found_files:
                print(f"  - {f}")
            print("\nRun again with one of these files:")
            print(f"  python audio_converter.py {found_files[0]}")
        
        return
    
    audio_file = sys.argv[1]
    
    # Convert to base64
    base64_audio = convert_audio_to_base64(audio_file)
    
    if base64_audio:
        # Create sample API request
        create_api_request_json(base64_audio)
        
        print("\n" + "="*60)
        print("✅ CONVERSION COMPLETE!")
        print("="*60)
        print("\n📝 Next steps:")
        print("1. Copy base64 from the .base64.txt file")
        print("2. Use in API request as audio_base64 field")
        print("3. Test with test_audio_api.py script")
        print()


if __name__ == "__main__":
    main()
