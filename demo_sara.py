#!/usr/bin/env python3
"""
Sara Demo - Live Conversation Simulation
Shows how Sara responds to scam messages
"""

import re
import json
from datetime import datetime

# Color codes for terminal
class Colors:
    SCAMMER = '\033[91m'  # Red
    SARA = '\033[92m'      # Green
    SYSTEM = '\033[93m'    # Yellow
    INFO = '\033[94m'      # Blue
    RESET = '\033[0m'      # Reset

# Scam detection patterns
SCAM_PATTERNS = {
    "urgency": ["urgent", "immediately", "today", "abhi", "jaldi"],
    "account_threat": ["block", "suspend", "freeze", "band"],
    "verification": ["verify", "confirm", "update", "KYC"],
    "payment": ["UPI", "bank account", "OTP", "payment", "paisa"],
    "prize": ["won", "prize", "lottery", "jeeta"],
    "authority": ["bank", "police", "income tax", "government"]
}

def detect_scam(message):
    """Detect if message is a scam"""
    message_lower = message.lower()
    scam_signals = []
    
    for category, patterns in SCAM_PATTERNS.items():
        for pattern in patterns:
            if pattern in message_lower:
                scam_signals.append(category)
                break
    
    return len(scam_signals) >= 2, scam_signals

def extract_intelligence(message):
    """Extract intelligence from message"""
    intelligence = {
        "upi_ids": re.findall(r'[\w\.-]+@[\w\.-]+', message),
        "phone_numbers": re.findall(r'\+?\d{10,13}', message),
        "amounts": re.findall(r'Rs\.?\s*\d+', message),
        "keywords": []
    }
    
    # Extract keywords
    for category, patterns in SCAM_PATTERNS.items():
        for pattern in patterns:
            if pattern in message.lower():
                intelligence["keywords"].append(pattern)
    
    return intelligence

def sara_response(scammer_message, conversation_number):
    """
    Generate Sara's response based on message
    This is a simplified version - real version uses Claude AI
    """
    
    message_lower = scammer_message.lower()
    
    # Sara's responses based on keywords
    responses = {
        # Account blocking
        1: "Kya? Kaunsa account block ho raha?",
        
        # KYC/Verification
        2: "Achha... KYC matlab kya hota hai? Mujhe technology zyada nahi aati",
        
        # Link sharing
        3: "Link? Woh kaise click karte hain? Safe hai na?",
        
        # Payment request
        4: "Payment? Aapka UPI ID kya hai?",
        
        # OTP request
        5: "OTP? Woh kahan milega? SMS mein aayega?",
        
        # Closing
        6: "Hmm... rukiye, pehle bank jaa ke dekhti hoon. Baad mein baat karti hoon"
    }
    
    return responses.get(conversation_number, "Haan ji... bolo kya baat hai?")

def print_header():
    """Print demo header"""
    print("\n" + "="*70)
    print(f"{Colors.INFO}🍯 SARA DEMO - Live Scam Detection & Conversation{Colors.RESET}")
    print("="*70)
    print(f"{Colors.SYSTEM}Sara: 40-50 year old Indian school teacher{Colors.RESET}")
    print(f"{Colors.SYSTEM}Style: Natural Hinglish (confused, polite, hesitant){Colors.RESET}")
    print("="*70 + "\n")

def simulate_conversation():
    """Simulate a realistic scam conversation"""
    
    print_header()
    
    # Realistic Indian scam conversation
    conversation = [
        {
            "scammer": "Madam, main State Bank se bol raha hoon. Aapka account block hone wala hai.",
            "context": "Initial scam - Bank impersonation + Urgency"
        },
        {
            "scammer": "Aapka KYC pending hai. Aaj 5 baje tak complete nahi kiya toh account band ho jayega.",
            "context": "KYC scam with deadline pressure"
        },
        {
            "scammer": "Aapko ek link bhej raha hoon SMS mein. Uspe click karke details update karo.",
            "context": "Phishing link attempt"
        },
        {
            "scammer": "Aur suno, ek chhota sa verification fee hai - Rs. 500. Mera UPI ID hai scammer@paytm",
            "context": "Payment request with UPI ID"
        },
        {
            "scammer": "Abhi payment karo aur apna OTP bhi batao verification ke liye.",
            "context": "Direct OTP request - CRITICAL scam signal"
        },
        {
            "scammer": "Madam time khatam ho raha hai! Jaldi karo!",
            "context": "Urgency tactics"
        }
    ]
    
    total_intelligence = {
        "upi_ids": [],
        "phone_numbers": [],
        "amounts": [],
        "keywords": []
    }
    
    scam_detected = False
    
    for idx, turn in enumerate(conversation, 1):
        # Print scammer message
        print(f"\n{Colors.SCAMMER}📞 SCAMMER (Message {idx}):{Colors.RESET}")
        print(f"   {turn['scammer']}")
        
        # Detect scam
        is_scam, signals = detect_scam(turn['scammer'])
        
        if is_scam and not scam_detected:
            print(f"\n{Colors.SYSTEM}⚠️  SYSTEM: Scam Detected! Categories: {', '.join(signals)}{Colors.RESET}")
            scam_detected = True
        
        # Extract intelligence
        intel = extract_intelligence(turn['scammer'])
        
        # Merge intelligence
        for key in total_intelligence:
            total_intelligence[key].extend(intel[key])
        
        # Show extraction if any
        if any(intel.values()):
            print(f"{Colors.SYSTEM}🔍 Intelligence Extracted:{Colors.RESET}")
            if intel['upi_ids']:
                print(f"   • UPI IDs: {', '.join(intel['upi_ids'])}")
            if intel['phone_numbers']:
                print(f"   • Phone: {', '.join(intel['phone_numbers'])}")
            if intel['amounts']:
                print(f"   • Amounts: {', '.join(intel['amounts'])}")
        
        # Sara's response
        sara_reply = sara_response(turn['scammer'], idx)
        print(f"\n{Colors.SARA}👩 SARA:{Colors.RESET}")
        print(f"   {sara_reply}")
        
        # Context info
        print(f"\n{Colors.INFO}💡 Context: {turn['context']}{Colors.RESET}")
        
        # Separator
        print("\n" + "-"*70)
        
        # Small delay for readability
        import time
        time.sleep(0.5)
    
    # Final summary
    print("\n" + "="*70)
    print(f"{Colors.SYSTEM}📊 FINAL INTELLIGENCE REPORT{Colors.RESET}")
    print("="*70)
    
    print(f"\n{Colors.INFO}Session ID:{Colors.RESET} demo-session-001")
    print(f"{Colors.INFO}Scam Detected:{Colors.RESET} ✅ YES")
    print(f"{Colors.INFO}Total Messages:{Colors.RESET} {len(conversation)}")
    
    print(f"\n{Colors.INFO}Extracted Intelligence:{Colors.RESET}")
    print(json.dumps({
        "upiIds": list(set(total_intelligence['upi_ids'])),
        "phoneNumbers": list(set(total_intelligence['phone_numbers'])),
        "amounts": list(set(total_intelligence['amounts'])),
        "suspiciousKeywords": list(set(total_intelligence['keywords']))[:10]
    }, indent=2))
    
    print(f"\n{Colors.SYSTEM}📤 Final Report Sent to GUVI Endpoint{Colors.RESET}")
    print(f"{Colors.SYSTEM}✅ Session Completed Successfully{Colors.RESET}")
    
    print("\n" + "="*70)
    print(f"{Colors.INFO}🎯 SARA'S PERFORMANCE:{Colors.RESET}")
    print("="*70)
    print("✅ Sounded completely natural and real")
    print("✅ Used Hinglish (Hindi-English mix)")
    print("✅ Appeared confused and hesitant")
    print("✅ Asked innocent questions that extracted info")
    print("✅ Never revealed scam detection")
    print("✅ Safely exited conversation")
    print("✅ Protected all sensitive information (no OTP shared!)")
    print("\n" + "="*70 + "\n")

def show_sara_persona():
    """Show Sara's character traits"""
    print(f"\n{Colors.INFO}👩 SARA'S PERSONA:{Colors.RESET}")
    print("="*70)
    print("Name: Sara")
    print("Age: 40-50 years")
    print("Role: School teacher/staff")
    print("Tech Knowledge: Very limited (bahut kam)")
    print("Language: Natural Hinglish")
    print("Personality: Polite, confused, slow, hesitant")
    print("\n" + "="*70)
    
    print(f"\n{Colors.INFO}🗣️  HOW SARA SPEAKS:{Colors.RESET}")
    print("="*70)
    print("✓ 'Haan ji... bolo?'")
    print("✓ 'Achha... samajh nahi aa raha'")
    print("✓ 'Rukiye... slow boliye'")
    print("✓ 'Kya? Kaunsa account?'")
    print("✓ 'Hmm... mujhe technology nahi aati'")
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    # Show Sara's persona first
    show_sara_persona()
    
    # Wait for user
    input(f"{Colors.INFO}Press ENTER to start the conversation demo...{Colors.RESET}\n")
    
    # Run simulation
    simulate_conversation()
    
    print(f"\n{Colors.SARA}Demo completed! This is how Sara engages with scammers! 🎉{Colors.RESET}\n")
