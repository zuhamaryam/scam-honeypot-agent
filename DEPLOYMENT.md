# 🚀 Deployment Guide

## Quick Deployment Options

### 1. Railway (Recommended - Free Tier Available)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Add Anthropic API key
railway variables set ANTHROPIC_API_KEY=your-key-here

# Deploy
railway up
```

**Railway will automatically:**
- Detect Dockerfile
- Build container
- Deploy with public URL
- Provide HTTPS

Your API will be live at: `https://your-app.railway.app`

---

### 2. Render (Free Tier)

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Configure:
   - **Environment:** Docker
   - **Region:** Choose closest
   - **Plan:** Free
6. Add Environment Variable:
   - Key: `ANTHROPIC_API_KEY`
   - Value: Your API key
7. Click "Create Web Service"

Your API will be at: `https://your-service.onrender.com`

---

### 3. Fly.io (Free Tier)

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Launch app
fly launch

# Set secret
fly secrets set ANTHROPIC_API_KEY=your-key-here

# Deploy
fly deploy
```

Your API will be at: `https://your-app.fly.dev`

---

### 4. Google Cloud Run (Pay as you go)

```bash
# Install gcloud CLI
# Then:

# Set project
gcloud config set project YOUR_PROJECT_ID

# Build container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/honeypot

# Deploy
gcloud run deploy honeypot \
  --image gcr.io/YOUR_PROJECT_ID/honeypot \
  --platform managed \
  --region asia-south1 \
  --set-env-vars ANTHROPIC_API_KEY=your-key-here \
  --allow-unauthenticated
```

---

### 5. AWS EC2 (Traditional)

```bash
# SSH into EC2 instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Docker
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker

# Clone/upload your code
git clone your-repo-url
cd scam-honeypot-agent

# Set environment
export ANTHROPIC_API_KEY=your-key-here

# Run with Docker Compose
sudo docker-compose up -d

# Check status
sudo docker-compose logs -f
```

Configure Security Group:
- Allow inbound TCP 8000 from anywhere (0.0.0.0/0)

---

### 6. Local with Ngrok (Testing)

```bash
# Terminal 1: Run server
python main.py

# Terminal 2: Expose with ngrok
ngrok http 8000
```

Copy the ngrok URL (e.g., `https://abc123.ngrok.io`)

---

## Production Checklist

### Before Deployment:

- [ ] Set `ANTHROPIC_API_KEY` environment variable
- [ ] Verify API key in code: `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`
- [ ] Test locally with `test_api.py`
- [ ] Check Dockerfile builds successfully
- [ ] Verify GUVI callback endpoint is accessible

### After Deployment:

```bash
# Test health endpoint
curl https://your-domain.com/health

# Test API endpoint
curl -X POST https://your-domain.com/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "test-1",
    "message": {
      "sender": "scammer",
      "text": "Your account is blocked",
      "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {"channel": "SMS", "language": "English", "locale": "IN"}
  }'
```

---

## Environment Variables Required

```
ANTHROPIC_API_KEY=your-anthropic-api-key-here
```

Optional:
```
API_KEY=HONEY-POT-SECURE-KEY-2024-GUVI-HACK
PORT=8000
HOST=0.0.0.0
```

---

## Troubleshooting

### Container won't start
```bash
docker logs scam-honeypot-agent
```

### API returning 401
- Verify x-api-key header: `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`

### Claude API errors
- Check ANTHROPIC_API_KEY is set correctly
- Verify you have API credits

### GUVI callback failing
- Check internet connectivity from container
- Verify callback URL: `https://hackathon.guvi.in/api/updateHoneyPotFinalResult`

---

## Performance Optimization

### For High Traffic:

1. **Enable Redis for Session Storage:**
```python
# In main.py, replace defaultdict with Redis
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
```

2. **Add Rate Limiting:**
```bash
pip install slowapi
```

3. **Scale Horizontally:**
```bash
docker-compose up --scale honeypot-api=3
```

4. **Use Load Balancer:**
- Add nginx reverse proxy
- Distribute requests across instances

---

## Monitoring

### Check Logs:
```bash
# Docker
docker logs -f scam-honeypot-agent

# Docker Compose
docker-compose logs -f

# Kubernetes
kubectl logs -f deployment/honeypot
```

### Health Checks:
```bash
# Simple ping
curl https://your-domain.com/health

# Monitor endpoint
watch -n 5 'curl -s https://your-domain.com/health | jq'
```

---

## Recommended: Railway Deployment (Easiest)

Railway offers the easiest deployment with:
- ✅ Automatic HTTPS
- ✅ Free tier available
- ✅ GitHub integration
- ✅ One-click deploy
- ✅ Built-in monitoring

**Steps:**
1. Push to GitHub
2. Go to railway.app
3. Click "New Project" → "Deploy from GitHub"
4. Select repo
5. Add ANTHROPIC_API_KEY variable
6. Deploy!

Your public API URL will be ready in ~2 minutes.

---

## Support

Need help? Check:
1. Health endpoint: `/health`
2. Root endpoint: `/`
3. Test with: `python test_api.py`
4. Logs: `docker-compose logs -f`
