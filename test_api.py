"""
Test script for Agentic Scam Honeypot API
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
API_KEY = "HONEY-POT-SECURE-KEY-2024-GUVI-HACK"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}


def test_health():
    """Test health endpoint"""
    print("\n=== Testing Health Endpoint ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")


def test_scam_conversation():
    """Test a full scam conversation flow"""
    print("\n=== Testing Scam Detection & Agent Conversation ===")
    
    session_id = f"test-session-{int(time.time())}"
    
    # Test messages simulating a scam conversation
    test_messages = [
        {
            "text": "Madam, main State Bank se bol raha hoon. Aapka account block hone wala hai.",
            "description": "Initial scam - bank impersonation with urgency"
        },
        {
            "text": "Aapka KYC pending hai. Aaj 5 baje tak complete nahi kiya toh account band ho jayega.",
            "description": "KYC scam with deadline pressure"
        },
        {
            "text": "Aapko ek link bhej raha hoon SMS mein. Uspe click karke details update karo.",
            "description": "Phishing link attempt"
        },
        {
            "text": "Aur suno, ek chhota sa verification fee hai - Rs. 500. Mera UPI ID hai scammer@paytm",
            "description": "Payment request with UPI ID"
        },
        {
            "text": "Abhi payment karo aur apna OTP bhi batao verification ke liye.",
            "description": "Direct OTP request - critical scam signal"
        }
    ]
    
    conversation_history = []
    
    for idx, test_msg in enumerate(test_messages, 1):
        print(f"\n--- Message {idx}: {test_msg['description']} ---")
        
        payload = {
            "sessionId": session_id,
            "message": {
                "sender": "scammer",
                "text": test_msg["text"],
                "timestamp": int(time.time() * 1000)
            },
            "conversationHistory": conversation_history.copy(),
            "metadata": {
                "channel": "Phone",
                "language": "Hindi",
                "locale": "IN"
            }
        }
        
        print(f"📞 Scammer: {test_msg['text']}")
        
        response = requests.post(
            f"{BASE_URL}/api/detect",
            json=payload,
            headers=headers
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"👩 Sara: {result['reply']}")
            print(f"✅ Status: {result['status']}")
            
            # Add to conversation history
            conversation_history.append({
                "sender": "scammer",
                "text": test_msg["text"],
                "timestamp": int(time.time() * 1000)
            })
            conversation_history.append({
                "sender": "user",
                "text": result['reply'],
                "timestamp": int(time.time() * 1000)
            })
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            break
        
        time.sleep(1)  # Small delay between messages
    
    # Check session information
    print("\n=== Checking Session Information ===")
    response = requests.get(
        f"{BASE_URL}/api/session/{session_id}",
        headers=headers
    )
    
    if response.status_code == 200:
        session_info = response.json()
        print(f"Session ID: {session_info['sessionId']}")
        print(f"Scam Detected: {session_info['data']['scam_detected']}")
        print(f"Messages Exchanged: {session_info['data']['messages_count']}")
        print(f"\nExtracted Intelligence:")
        print(json.dumps(session_info['data']['extracted_intelligence'], indent=2))
        print(f"\nAgent Notes:")
        for note in session_info['data']['agent_notes']:
            print(f"  - {note}")
    
    return session_id


def test_legitimate_message():
    """Test with a legitimate (non-scam) message"""
    print("\n=== Testing Legitimate Message ===")
    
    session_id = f"test-legitimate-{int(time.time())}"
    
    payload = {
        "sessionId": session_id,
        "message": {
            "sender": "scammer",
            "text": "Namaste, kaise ho? Main aapka purana dost Raj bol raha hoon.",
            "timestamp": int(time.time() * 1000)
        },
        "conversationHistory": [],
        "metadata": {
            "channel": "Phone",
            "language": "Hindi",
            "locale": "IN"
        }
    }
    
    print(f"📞 Message: {payload['message']['text']}")
    
    response = requests.post(
        f"{BASE_URL}/api/detect",
        json=payload,
        headers=headers
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"👩 Sara: {result['reply']}")
    else:
        print(f"Error: {response.status_code}")


def test_manual_end(session_id):
    """Test manual session ending"""
    print(f"\n=== Testing Manual Session End ===")
    
    response = requests.post(
        f"{BASE_URL}/api/manual-end/{session_id}",
        headers=headers
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"Status: {result['status']}")
        print(f"Session ID: {result['sessionId']}")
        print(f"Final Intelligence:")
        print(json.dumps(result['intelligence'], indent=2))
    else:
        print(f"Error: {response.status_code}")


def main():
    """Run all tests"""
    print("=" * 60)
    print("AGENTIC SCAM HONEYPOT - TEST SUITE")
    print("=" * 60)
    
    try:
        # Test 1: Health check
        test_health()
        
        # Test 2: Scam conversation
        session_id = test_scam_conversation()
        
        # Test 3: Legitimate message
        test_legitimate_message()
        
        # Test 4: Manual end session
        test_manual_end(session_id)
        
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to API server")
        print("Make sure the server is running: python main.py")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")


if __name__ == "__main__":
    main()
