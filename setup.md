# ModShield AI — Remaining Setup Guide

## Current Project Status

Completed:
- Devvit app setup
- Frontend folder initialized
- Frontend packages installed
- Backend virtual environment created
- Devvit app name: `modshieldai`

Remaining work includes:
- Backend API implementation
- Database setup
- AI integration
- Frontend dashboard development
- Devvit ↔ Backend integration
- Deployment

---

# Recommended Final Folder Structure

```text
modshield/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── services/
│   ├── hooks/
│   ├── public/
│   └── .env
│
├── backend/
│   ├── api/
│   ├── routes/
│   ├── services/
│   ├── ai/
│   ├── models/
│   ├── utils/
│   ├── database/
│   ├── config/
│   ├── main.py
│   └── config.properties
│
├── modshieldai/
│   ├── src/
│   ├── webroot/
│   ├── package.json
│   └── devvit.json
│
└── docs/
```

---

# Backend Setup

# Step 1 — Activate Virtual Environment

```bash
cd backend
source venv/bin/activate
```

---

# Step 2 — Install Required Packages

```bash
pip install fastapi uvicorn python-dotenv sqlalchemy psycopg2-binary redis requests openai sentence-transformers qdrant-client
```

Optional:

```bash
pip install google-generativeai
```

---

# Step 3 — Create Backend Config File

Create:

```text
backend/config.properties
```

Example:

```properties
HOST=0.0.0.0
PORT=8000
DEBUG=True

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=modshield
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password

REDIS_HOST=localhost
REDIS_PORT=6379

OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key

QDRANT_URL=http://localhost:6333

FRONTEND_URL=http://localhost:3000
```

---

# Step 4 — Create Main Backend Entry

Create:

```text
backend/main.py
```

Responsibilities:
- initialize FastAPI app
- load config.properties
- include routes
- enable CORS
- initialize database

---

# Step 5 — Setup Backend Routes

Recommended routes:

```text
/routes
    analyze.py
    moderation.py
    analytics.py
    users.py
    health.py
```

---

# Step 6 — Create AI Service Layer

Recommended structure:

```text
/ai
    toxicity.py
    scam_detection.py
    embeddings.py
    llm_reasoning.py
```

Responsibilities:
- toxicity scoring
- scam detection
- semantic similarity
- AI moderation reasoning

---

# Step 7 — Setup Database

Install PostgreSQL locally.

Create database:

```sql
CREATE DATABASE modshield;
```

---

# Step 8 — Setup Redis

Install Redis locally.

Run:

```bash
redis-server
```

Used for:
- caching
- live moderation queues
- temporary moderation state

---

# Step 9 — Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# Frontend Setup

# Step 1 — Create Frontend Environment File

Create:

```text
frontend/.env
```

Example:

```env
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_APP_NAME=ModShield AI
NEXT_PUBLIC_DEV_MODE=true
```

---

# Step 2 — Recommended Frontend Structure

```text
frontend/
│
├── app/
│   ├── dashboard/
│   ├── analytics/
│   ├── queue/
│   ├── users/
│   └── settings/
│
├── components/
│   ├── charts/
│   ├── tables/
│   ├── cards/
│   ├── sidebar/
│   └── moderation/
│
├── services/
│   ├── api.ts
│   └── websocket.ts
│
└── hooks/
```

---

# Step 3 — Dashboard Pages To Build

## Dashboard
Shows:
- total flagged posts
- risk score overview
- community health metrics

---

## Moderation Queue
Shows:
- flagged content
- AI suggestions
- moderation actions

---

## Analytics
Shows:
- toxicity trends
- spam trends
- moderator activity

---

## Users
Shows:
- risky users
- repeated offenders
- user risk analysis

---

# Step 4 — Run Frontend

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# Devvit Integration Setup

# Step 1 — Setup Devvit Triggers

Inside:

```text
modshieldai/src/
```

Create triggers for:
- new posts
- new comments
- reports

---

# Step 2 — Connect Devvit To Backend

Devvit app responsibilities:
- capture Reddit events
- send content to backend
- receive AI analysis
- perform moderation actions

---

# Step 3 — Add Moderator Actions

Recommended actions:
- Remove Post
- Approve Post
- Ban User
- Escalate Risk
- Analyze With AI

---

# Step 4 — Setup Playtest

Run:

```bash
cd modshieldai

devvit playtest
```

Install app in your test subreddit.

---

# Recommended Development Order

## Phase 1
- Backend APIs
- AI moderation endpoint
- Frontend dashboard skeleton

---

## Phase 2
- Devvit triggers
- Backend integration
- Real-time moderation flow

---

## Phase 3
- Analytics dashboard
- User risk engine
- AI reasoning layer

---

## Phase 4
- Semantic similarity
- Repost detection
- Raid detection

---

# Final Local Run Workflow

## Terminal 1 — Backend

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

---

## Terminal 2 — Frontend

```bash
cd frontend
npm run dev
```

---

## Terminal 3 — Devvit

```bash
cd modshieldai
devvit playtest
```

---

# Deployment Recommendations

## Frontend
Deploy on:
- Vercel

---

## Backend
Deploy on:
- Railway
- Render
- VPS

---

## Database
Use:
- Neon PostgreSQL
- Supabase

---

# Recommended MVP Completion Checklist

- Devvit triggers working
- Backend APIs functional
- AI moderation scoring functional
- Dashboard displaying data
- Real-time moderation queue working
- Moderator actions functional
- Demo-ready workflow completed


