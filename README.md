# ModShield AI

## Overview

ModShield AI is an AI-powered Reddit moderation copilot designed to help moderators detect scams, spam, toxicity, and harmful content in real time. The platform prioritizes dangerous content, provides AI-generated moderation suggestions, and automates moderation workflows to reduce moderator workload and improve community safety.

---

# Core Features

## AI Moderation Engine

Analyzes Reddit posts and comments for:
- toxicity
- spam
- scams
- phishing attempts
- harmful language
- suspicious activity

The AI engine generates:
- risk scores
- moderation recommendations
- moderation explanations
- confidence scores

---

## Smart Moderation Queue

The moderation queue prioritizes content based on:
- toxicity score
- scam probability
- spam likelihood
- urgency
- user behavior history

Moderators can:
- approve content
- remove content
- ban users
- escalate cases

---

## AI Moderation Suggestions

For each flagged post, the system provides:
- suggested moderator action
- AI-generated explanation
- moderation reasoning
- similarity to previous incidents

---

## Community Health Analytics

Dashboard analytics include:
- toxicity trends
- spam activity
- moderator activity
- flagged content statistics
- risky users
- community health metrics

---

## User Risk Intelligence

The system analyzes:
- user behavior
- repeated violations
- suspicious posting patterns
- scam similarity
- account activity

Generates:
- user risk scores
- repeat offender tracking
- suspicious user alerts

---

## Semantic Similarity Engine

Detects:
- reposts
- repeated scams
- coordinated spam
- similar phishing campaigns

Using:
- embeddings
- vector similarity search
- semantic analysis

---

# System Architecture

```text
Reddit
   ↓
Devvit App
   ↓
FastAPI Backend
   ↓
AI Moderation Engine
   ↓
PostgreSQL + Redis + Vector DB
   ↓
Next.js Dashboard
```

---

# Tech Stack

## Frontend
- Next.js
- Tailwind CSS
- shadcn/ui
- Recharts

---

## Backend
- FastAPI
- PostgreSQL
- Redis
- Qdrant

---

## AI Stack
- OpenAI API / Gemini API
- Perspective API
- sentence-transformers

---

## Reddit Integration
- Devvit SDK

---

# Backend Configuration

Backend uses:

```text
config.properties
```

Location:

```text
backend/config.properties
```

Responsibilities:
- API configuration
- database configuration
- Redis configuration
- AI API keys
- backend settings

---

# Frontend Configuration

Frontend uses:

```text
.env
```

Location:

```text
frontend/.env
```

Responsibilities:
- backend API URLs
- frontend configuration
- development environment variables

---

# Backend Functionalities

## APIs

### Moderation APIs
- analyze posts
- generate moderation suggestions
- remove/approve actions

---

### Analytics APIs
- toxicity metrics
- spam trends
- dashboard metrics

---

### User APIs
- user risk scoring
- offender history
- suspicious activity tracking

---

# Frontend Functionalities

## Dashboard
Displays:
- flagged content overview
- community health
- moderation metrics

---

## Moderation Queue
Displays:
- AI-flagged content
- risk scores
- moderation actions

---

## Analytics Dashboard
Displays:
- charts
- trends
- moderation statistics

---

## User Intelligence Dashboard
Displays:
- risky users
- repeat offenders
- suspicious behavior analysis

---

# Devvit Functionalities

The Devvit app handles:
- Reddit event triggers
- moderation integration
- post/comment monitoring
- moderator actions
- backend communication

---

# AI Functionalities

## Toxicity Detection
Detects:
- hate speech
- harassment
- abusive language

---

## Scam Detection
Detects:
- phishing
- fake giveaways
- malicious promotions

---

## Spam Detection
Detects:
- repetitive posting
- suspicious promotions
- bot activity

---

## AI Reasoning
Generates:
- moderation explanations
- action suggestions
- AI summaries

---

# Planned Advanced Features

- raid detection
- AI moderator memory
- semantic repost detection
- real-time threat monitoring
- community sentiment analysis
- AI-generated moderation reports

---

# Running The Project

## Backend

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

---

## Frontend

```bash
cd frontend
npm run dev
```

---

## Devvit

```bash
cd modshieldai
devvit playtest
```

---

# Project Goal

The goal of ModShield AI is to build an intelligent moderation operating system for Reddit communities that helps moderators reduce manual workload, improve moderation speed, and maintain safer and healthier online communities.
