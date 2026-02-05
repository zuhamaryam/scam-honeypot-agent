# ⚡ Quick Start Guide

Get your Agentic Scam Honeypot running in 5 minutes!

## 🎯 What You'll Get

✅ **Sara** - Natural-sounding Indian AI agent (school teacher persona)
✅ Hinglish conversations that sound completely real
✅ AI-powered scam detection system
✅ Autonomous conversation agent (Claude AI)
✅ Intelligence extraction engine
✅ REST API with authentication
✅ Automatic GUVI callback
✅ Ready for hackathon submission

---

## 📋 Prerequisites

- Python 3.9+ OR Docker
- Anthropic API Key (get from: https://console.anthropic.com/)
- 5 minutes of your time

---

## 🚀 Option 1: Quick Local Setup (Recommended for Testing)

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Set your Anthropic API key
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Step 3: Run the server
python main.py
```

Server will start at: `http://localhost:8000`

---

## 🐳 Option 2: Docker (Recommended for Deployment)

```bash
# Step 1: Set your API key in .env file
echo "ANTHROPIC_API_KEY=sk-ant-your-key-here" > .env

# Step 2: Run with Docker Compose
docker-compose up -d

# Step 3: Check logs
docker-compose logs -f
```

Server will start at: `http://localhost:8000`

---

## ✅ Verify Installation

### Test 1: Health Check
```bash
curl http://localhost:8000/health
```

Expected: `{"status":"healthy",...}`

### Test 2: API Info
```bash
curl http://localhost:8000/
```

Expected: API information and endpoints

### Test 3: Run Full Test Suite
```bash
python test_api.py
```

Expected: All tests pass with green checkmarks

---

## 🧪 Send Your First Request

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "test-001",
    "message": {
      "sender": "scammer",
      "text": "Madam, aapka account block hone wala hai. Abhi verify karo!",
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

**You should get a response like:**
```json
{
  "status": "success",
  "reply": "Kya? Kaunsa account block ho raha?"
}
```

---

## 🌐 Deploy to Internet (For Hackathon Submission)

### Option A: Railway (Easiest)

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub"
4. Select your repo
5. Add environment variable: `ANTHROPIC_API_KEY`
6. Deploy!

**Your API will be live at:** `https://your-app.railway.app`

### Option B: Render

1. Go to [render.com](https://render.com)
2. Create "New Web Service"
3. Connect GitHub repo
4. Set Docker environment
5. Add `ANTHROPIC_API_KEY` variable
6. Deploy!

**Your API will be live at:** `https://your-service.onrender.com`

### Option C: Ngrok (For Local Testing)

```bash
# Terminal 1: Run server
python main.py

# Terminal 2: Expose to internet
ngrok http 8000
```

**Your API will be live at:** `https://abc123.ngrok.io`

---

## 📝 API Key for Requests

**Your API Key:** `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`

Include this in every request header:
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```

---

## 🎯 How It Works

1. **Scammer sends message** → Your API receives it
2. **System detects scam** → Multi-pattern analysis
3. **Sara (AI Agent) responds** → Natural Hinglish reply like "Kya? Kaunsa account?"
4. **Intelligence extracted** → Bank accounts, UPI IDs, etc.
5. **Conversation continues** → Sara keeps scammer engaged naturally
6. **Final callback sent** → Results sent to GUVI automatically

**Sara sounds so real that scammers believe they're talking to a confused Indian woman!**

---

## 📊 Monitor Your System

### Check Session Status
```bash
curl http://localhost:8000/api/session/test-001 \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK"
```

### Manual End Session
```bash
curl -X POST http://localhost:8000/api/manual-end/test-001 \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK"
```

---

## 🔧 Troubleshooting

### Server won't start
```bash
# Check if port 8000 is free
lsof -i :8000

# Kill process if needed
kill -9 <PID>
```

### API returns 401
- Verify API key: `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`
- Check header: `x-api-key`

### Claude API errors
- Verify `ANTHROPIC_API_KEY` is set
- Check you have API credits at console.anthropic.com

### Docker issues
```bash
# Restart containers
docker-compose down
docker-compose up -d

# Check logs
docker-compose logs -f
```

---

## 📚 Next Steps

1. ✅ **Test Locally** - Run `python test_api.py`
2. ✅ **Deploy** - Choose Railway/Render/Ngrok
3. ✅ **Submit** - Provide your public API URL to hackathon
4. ✅ **Monitor** - Watch logs and session data

---

## 🎉 You're Ready!

Your Agentic Scam Honeypot is now operational!

**Key Files:**
- `main.py` - Main application
- `test_api.py` - Test suite
- `README.md` - Full documentation
- `API_DOCS.md` - API reference
- `DEPLOYMENT.md` - Deployment guide

**API Endpoint:** `http://localhost:8000/api/detect`

**API Key:** `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`

---

## 🆘 Need Help?

1. Check `README.md` for detailed documentation
2. Check `API_DOCS.md` for API examples
3. Check `DEPLOYMENT.md` for deployment options
4. Run `python test_api.py` to verify setup
5. Check logs: `docker-compose logs -f`

---

## 🏆 Hackathon Submission Checklist

- [ ] Server running successfully
- [ ] Health endpoint working
- [ ] Test API with scam messages
- [ ] Deploy to public URL
- [ ] Test from external network
- [ ] Verify GUVI callback works
- [ ] Submit API endpoint URL
- [ ] Submit API key to evaluators

---

**Good luck with your hackathon! 🚀**
