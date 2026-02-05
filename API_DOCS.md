# 📚 API Documentation

## Base URL
```
http://localhost:8000
```

Replace with your deployed URL for production.

---

## Authentication

All protected endpoints require API key authentication.

**Header:**
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```

---

## Endpoints

### 1. Health Check

**GET** `/health`

Check if the service is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "Agentic Scam Honeypot",
  "version": "1.0.0",
  "timestamp": "2024-02-06T10:30:00.000Z"
}
```

---

### 2. Root Information

**GET** `/`

Get API information and available endpoints.

**Response:**
```json
{
  "service": "Agentic Scam Honeypot API",
  "version": "1.0.0",
  "endpoints": {
    "detect": "/api/detect",
    "manual_end": "/api/manual-end/{session_id}",
    "session_info": "/api/session/{session_id}",
    "health": "/health"
  },
  "authentication": "x-api-key header required",
  "api_key_header": "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK"
}
```

---

### 3. Detect & Respond (Main Endpoint)

**POST** `/api/detect`

Main endpoint for scam detection and agent response.

**Headers:**
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
Content-Type: application/json
```

**Request Body:**

#### First Message (No History)
```json
{
  "sessionId": "unique-session-id-123",
  "message": {
    "sender": "scammer",
    "text": "Your bank account will be blocked today. Verify immediately.",
    "timestamp": 1770005528731
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
```

#### Follow-up Message (With History)
```json
{
  "sessionId": "unique-session-id-123",
  "message": {
    "sender": "scammer",
    "text": "Share your UPI ID to avoid suspension.",
    "timestamp": 1770005528731
  },
  "conversationHistory": [
    {
      "sender": "scammer",
      "text": "Your bank account will be blocked today. Verify immediately.",
      "timestamp": 1770005528731
    },
    {
      "sender": "user",
      "text": "Why will my account be blocked?",
      "timestamp": 1770005528731
    }
  ],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "reply": "Which account are you talking about? I have multiple accounts."
}
```

**Status Codes:**
- `200` - Success
- `401` - Invalid API Key
- `422` - Validation Error
- `500` - Internal Server Error

---

### 4. Get Session Information

**GET** `/api/session/{session_id}`

Retrieve current session data and extracted intelligence.

**Headers:**
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```

**Response:**
```json
{
  "sessionId": "unique-session-id-123",
  "data": {
    "scam_detected": true,
    "messages_count": 5,
    "extracted_intelligence": {
      "bankAccounts": ["1234567890"],
      "upiIds": ["scammer@paytm"],
      "phishingLinks": ["http://malicious-link.com"],
      "phoneNumbers": ["+919876543210"],
      "suspiciousKeywords": ["urgent", "verify", "blocked"]
    },
    "agent_notes": [
      "Scam detected (confidence: 0.85) - Categories: urgency, account_threat",
      "Intelligence extracted from message",
      "Maintaining victim persona"
    ]
  }
}
```

**Status Codes:**
- `200` - Success
- `401` - Invalid API Key
- `404` - Session Not Found

---

### 5. Manual Session End

**POST** `/api/manual-end/{session_id}`

Manually trigger session termination and send final results to GUVI.

**Headers:**
```
x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```

**Response:**
```json
{
  "status": "success",
  "sessionId": "unique-session-id-123",
  "intelligence": {
    "bankAccounts": ["1234567890"],
    "upiIds": ["scammer@paytm"],
    "phishingLinks": ["http://malicious-link.com"],
    "phoneNumbers": ["+919876543210"],
    "suspiciousKeywords": ["urgent", "verify", "blocked"]
  }
}
```

**Status Codes:**
- `200` - Success
- `401` - Invalid API Key
- `404` - Session Not Found

---

## Request/Response Field Descriptions

### Message Object
| Field | Type | Description |
|-------|------|-------------|
| sender | string | "scammer" or "user" |
| text | string | Message content |
| timestamp | integer | Epoch time in milliseconds |

### Metadata Object
| Field | Type | Description |
|-------|------|-------------|
| channel | string | Communication channel (SMS/WhatsApp/Email/Chat) |
| language | string | Language of the message |
| locale | string | Country/region code |

### Extracted Intelligence Object
| Field | Type | Description |
|-------|------|-------------|
| bankAccounts | array[string] | Bank account numbers found |
| upiIds | array[string] | UPI IDs extracted |
| phishingLinks | array[string] | Suspicious URLs |
| phoneNumbers | array[string] | Phone numbers |
| suspiciousKeywords | array[string] | Scam-related keywords |

---

## Example Scenarios

### Scenario 1: Bank Account Blocking Scam

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "bank-scam-001",
    "message": {
      "sender": "scammer",
      "text": "Your account will be suspended in 2 hours. Verify now at http://fake-bank.com",
      "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {
      "channel": "SMS",
      "language": "English",
      "locale": "IN"
    }
  }'
```

**Expected Response:**
```json
{
  "status": "success",
  "reply": "Which account is this about? I have savings and current account."
}
```

---

### Scenario 2: UPI Fraud

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "upi-fraud-001",
    "message": {
      "sender": "scammer",
      "text": "Send Rs 100 to scammer@paytm for account verification",
      "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {
      "channel": "WhatsApp",
      "language": "English",
      "locale": "IN"
    }
  }'
```

**Expected Response:**
```json
{
  "status": "success",
  "reply": "Why do I need to pay for verification? My bank never asked for this."
}
```

---

### Scenario 3: Prize/Lottery Scam

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "lottery-scam-001",
    "message": {
      "sender": "scammer",
      "text": "Congratulations! You won Rs 10 lakh lottery. Call +919876543210 to claim",
      "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {
      "channel": "SMS",
      "language": "English",
      "locale": "IN"
    }
  }'
```

**Expected Response:**
```json
{
  "status": "success",
  "reply": "Really? How did I win? I don't remember entering any lottery."
}
```

---

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Invalid API Key"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "sessionId"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error: [error message]"
}
```

---

## Rate Limiting

Currently no rate limiting is enforced. In production, consider:
- 100 requests per minute per IP
- 1000 requests per hour per session

---

## Best Practices

1. **Use Unique Session IDs**: Generate unique IDs for each conversation
2. **Maintain History**: Always include full conversation history for context
3. **Handle Errors**: Implement retry logic with exponential backoff
4. **Monitor Sessions**: Use `/api/session/{id}` to track progress
5. **Manual Control**: Use `/api/manual-end/{id}` when needed

---

## GUVI Callback

The system automatically sends final results to GUVI when:
- 10+ messages exchanged
- 5+ pieces of intelligence extracted
- Scammer requests sensitive data (OTP, PIN, CVV)

**Callback Endpoint:**
```
POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult
```

**Payload:**
```json
{
  "sessionId": "unique-session-id-123",
  "scamDetected": true,
  "totalMessagesExchanged": 12,
  "extractedIntelligence": {
    "bankAccounts": ["1234567890"],
    "upiIds": ["scammer@paytm"],
    "phishingLinks": ["http://malicious-link.com"],
    "phoneNumbers": ["+919876543210"],
    "suspiciousKeywords": ["urgent", "verify", "blocked"]
  },
  "agentNotes": "Scammer used urgency tactics and payment redirection"
}
```

---

## Testing

Use the included `test_api.py` script:

```bash
python test_api.py
```

This will run a full test suite including:
- Health check
- Scam conversation simulation
- Legitimate message handling
- Session information retrieval
- Manual session termination

---

## Support

For issues or questions:
- Check logs: `docker-compose logs -f`
- Verify API key is correct
- Test locally with `test_api.py`
- Check health endpoint: `/health`
