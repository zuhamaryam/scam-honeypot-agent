# 🍯 Agentic Scam Honeypot - GUVI Hackathon

> AI-powered scam detection system featuring **Sara** - a natural-sounding Indian AI agent that engages scammers and extracts intelligence.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)](https://fastapi.tiangolo.com/)
[![Claude AI](https://img.shields.io/badge/Claude-Sonnet%204-orange.svg)](https://www.anthropic.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 👩 Meet Sara - The AI Agent

<div align="center">

**Sara** is a 40-50 year old Indian school teacher who speaks natural Hinglish and sounds completely authentic.

</div>

| Feature | Description |
|---------|-------------|
| 🗣️ **Language** | Natural Hinglish (Hindi-English mix) |
| 🎭 **Personality** | Confused, polite, hesitant - like a real person |
| 🧠 **Intelligence** | Asks innocent questions that extract scammer info |
| 🛡️ **Safety** | Never shares OTP, PIN, CVV or sensitive data |
| 🎯 **Effectiveness** | Scammers believe they're talking to a real victim |

### Example Conversation:

```
📞 Scammer: "Madam, aapka account block hone wala hai"
👩 Sara:    "Kya? Kaunsa account? Main confused hoon"

📞 Scammer: "State Bank account. KYC pending hai"
👩 Sara:    "Achha... toh kya karna hoga?"

📞 Scammer: "Rs 500 payment karo. UPI: scammer@paytm"
👩 Sara:    "Payment? Aapka UPI ID kya hai?"
           
✅ Intelligence Extracted: scammer@paytm, Rs 500
```

---

## 🚀 Quick Start

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/scam-honeypot-agent.git
cd scam-honeypot-agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set API Key

```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

### 4️⃣ Run Server

```bash
python main.py
```

Server starts at: `http://localhost:8000` 🎉

---

## ✨ Features

### 🔍 Intelligent Scam Detection
- Multi-pattern analysis (7 scam categories)
- Confidence scoring
- Context-aware detection
- Real-time analysis

### 👩 Sara - Natural AI Agent
- Powered by Claude Sonnet 4
- Speaks natural Hinglish
- Confused victim persona
- Environmental context (school, network issues)
- Multi-turn conversations

### 📊 Intelligence Extraction
- ✅ Bank account numbers
- ✅ UPI IDs
- ✅ Phone numbers
- ✅ Phishing links
- ✅ Suspicious keywords

### 🔐 Security & API
- REST API with FastAPI
- API key authentication
- Automatic GUVI callback
- Session management
- Docker containerization

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| 📘 [README.md](README.md) | Complete project documentation |
| ⚡ [QUICKSTART.md](QUICKSTART.md) | 5-minute setup guide |
| 👩 [SARA_PERSONA.md](SARA_PERSONA.md) | Sara's character & behavior |
| 💬 [EXAMPLE_CONVERSATIONS.md](EXAMPLE_CONVERSATIONS.md) | Realistic conversation examples |
| 🔧 [API_DOCS.md](API_DOCS.md) | Complete API reference |
| 🚀 [DEPLOYMENT.md](DEPLOYMENT.md) | Cloud deployment guide |
| 🐙 [GITHUB_DEPLOYMENT.md](GITHUB_DEPLOYMENT.md) | GitHub + Railway/Render setup |
| 📋 [SUMMARY.md](SUMMARY.md) | Project overview |

---

## 🔑 API Keys Explained

### 1. Anthropic API Key (Private)
```bash
# Get from: https://console.anthropic.com/
export ANTHROPIC_API_KEY="sk-ant-api03-xxxxx"
```
- **Purpose:** Powers Claude AI (Sara's brain)
- **Where to use:** Environment variable
- **Security:** ⚠️ NEVER commit to GitHub!

### 2. Your API Key (Public)
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```
- **Purpose:** Authentication for API requests
- **Where to use:** Request header
- **Security:** ✅ Safe to share with testers

---

## 🐳 Docker Deployment

### Using Docker Compose (Easiest)

```bash
# Set your API key in .env file
echo "ANTHROPIC_API_KEY=your-key" > .env

# Start the service
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop service
docker-compose down
```

### Manual Docker

```bash
# Build image
docker build -t scam-honeypot .

# Run container
docker run -d \
  -p 8000:8000 \
  -e ANTHROPIC_API_KEY="your-key" \
  --name honeypot \
  scam-honeypot
```

---

## 🌐 Deploy to Cloud

### Railway (Recommended - Free Tier)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. "New Project" → "Deploy from GitHub"
4. Select your repo
5. Add environment variable: `ANTHROPIC_API_KEY`
6. Deploy! ✅

**Live in 2 minutes!** Your URL: `https://your-app.railway.app`

### Render (Alternative)

1. Go to [render.com](https://render.com)
2. "New Web Service"
3. Connect GitHub repo
4. Environment: Docker
5. Add `ANTHROPIC_API_KEY` variable
6. Deploy! ✅

---

## 🧪 Testing

### Run Demo (No Server Required)

```bash
python demo_sara.py
```

See Sara in action with a simulated scam conversation!

### Run Full Test Suite

```bash
python test_api.py
```

### Manual API Test

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "test-001",
    "message": {
      "sender": "scammer",
      "text": "Madam account block hone wala hai!",
      "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {
      "channel": "Phone",
      "language": "Hindi",
      "locale": "IN"
    }
  }'
```

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/health` | GET | Health check |
| `/api/detect` | POST | Main scam detection & response |
| `/api/session/{id}` | GET | Get session information |
| `/api/manual-end/{id}` | POST | Manually end session |

**Full API Reference:** [API_DOCS.md](API_DOCS.md)

---

## 🎯 Scam Categories Detected

1. ⏰ **Urgency Tactics** - "immediately", "urgent", "jaldi"
2. 🏦 **Account Threats** - "blocked", "suspended", "freeze"
3. ✅ **Verification Requests** - "verify", "KYC", "update"
4. 💰 **Payment Scams** - "UPI", "OTP", "PIN", "CVV"
5. 🎁 **Prize/Lottery** - "won", "prize", "lottery"
6. 👮 **Authority Impersonation** - "bank", "police", "government"
7. 🔗 **Phishing Links** - Suspicious URLs

---

## 🏗️ Architecture

```
┌─────────────────┐
│ Scammer Message │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Scam Detection  │ ← Multi-pattern analysis
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Sara (Claude AI)│ ← Natural Hinglish response
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Intelligence    │ ← Extract UPI, phone, links
│ Extraction      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GUVI Callback   │ → Final intelligence report
└─────────────────┘
```

---

## 📊 Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Backend language |
| **FastAPI** | REST API framework |
| **Claude Sonnet 4** | AI agent (Sara's brain) |
| **Docker** | Containerization |
| **Pydantic** | Data validation |
| **Requests** | HTTP client |

---

## 🎓 How It Works

1. **Receive Message** → API receives scammer's message
2. **Detect Scam** → Multi-pattern analysis
3. **Sara Responds** → Claude AI generates natural Hinglish reply
4. **Extract Intel** → Automatically extract UPI IDs, phone numbers, etc.
5. **Continue Chat** → Sara keeps scammer engaged
6. **End Safely** → Sara exits naturally without suspicion
7. **Report to GUVI** → Final intelligence sent to evaluation endpoint

---

## 🏆 GUVI Hackathon Submission

### What to Submit:

1. **Deployed API URL**
   ```
   https://your-app.railway.app
   ```

2. **API Endpoint**
   ```
   POST https://your-app.railway.app/api/detect
   ```

3. **API Key**
   ```
   x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
   ```

4. **GitHub Repository**
   ```
   https://github.com/YOUR-USERNAME/scam-honeypot-agent
   ```

### Evaluation Criteria Covered:

- ✅ Scam Detection Accuracy (7 pattern categories)
- ✅ Quality of Agentic Engagement (Sara persona)
- ✅ Intelligence Extraction (5 data types)
- ✅ API Stability (FastAPI + error handling)
- ✅ Ethical Behavior (no impersonation, no illegal acts)

---

## 📁 Project Structure

```
scam-honeypot-agent/
├── main.py                      # Main FastAPI application
├── test_api.py                  # Test suite
├── demo_sara.py                 # Interactive demo
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker container
├── docker-compose.yml           # Docker orchestration
├── .env                         # Environment variables
├── .gitignore                   # Git ignore rules
├── README_GITHUB.md            # This file (GitHub version)
├── README.md                    # Full documentation
├── QUICKSTART.md                # Quick setup guide
├── SARA_PERSONA.md             # Sara character guide
├── EXAMPLE_CONVERSATIONS.md    # Conversation examples
├── API_DOCS.md                  # API reference
├── DEPLOYMENT.md                # Cloud deployment
├── GITHUB_DEPLOYMENT.md        # GitHub setup guide
└── SUMMARY.md                   # Project summary
```

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Anthropic** for Claude AI
- **GUVI** for the hackathon opportunity
- **FastAPI** team for the amazing framework

---

## 📞 Support

Having issues? Check:

1. 📖 [Documentation](README.md)
2. 🚀 [Quick Start Guide](QUICKSTART.md)
3. 🐙 [Deployment Guide](GITHUB_DEPLOYMENT.md)
4. 🧪 Run `python test_api.py` for diagnostics

---

## 🌟 Star This Repo!

If you find this project useful, please give it a ⭐ on GitHub!

---

<div align="center">

**Built with ❤️ for GUVI Hackathon 2024**

[Documentation](README.md) • [Quick Start](QUICKSTART.md) • [API Docs](API_DOCS.md) • [Deploy](GITHUB_DEPLOYMENT.md)

</div>
