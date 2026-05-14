# ModShield AI — Technical Stack

## Overview
ModShield AI is an AI-powered Reddit moderation copilot built for the Reddit Mod Tools and Migrated Apps Hackathon. The platform helps moderators detect scams, reduce toxicity, prioritize dangerous content, and automate moderation workflows.

---

# Core Architecture

```text
Reddit (Devvit App)
        ↓
FastAPI Backend
        ↓
AI Moderation Pipeline
 ├── Toxicity Detection
 ├── Scam Detection
 ├── Spam Detection
 ├── Semantic Similarity
 ├── AI Reasoning Engine
 └── Analytics Engine
        ↓
PostgreSQL + Redis + Vector DB
        ↓
Next.js Moderator Dashboard
```

---

# Frontend Stack

## Framework
### Next.js
Purpose:
- Moderator dashboard
- Analytics UI
- Admin controls
- Real-time moderation queue

Why:
- Fast development
- Excellent React ecosystem
- SSR support
- Easy deployment on Vercel

---

## Styling
### Tailwind CSS
Purpose:
- Rapid UI development
- Responsive layouts
- Dashboard styling

---

## UI Components
### shadcn/ui
Purpose:
- Tables
- Dialogs
- Buttons
- Cards
- Command palettes

---

## Charts & Visualization
### Recharts
Purpose:
- Toxicity trends
- Spam analytics
- Moderator activity graphs
- Community health metrics

---

# Backend Stack

## Framework
### FastAPI
Purpose:
- REST APIs
- AI inference APIs
- Reddit event processing
- Analytics processing

Why:
- Async support
- High performance
- Easy OpenAPI generation
- Excellent Python AI ecosystem support

---

## Authentication
### JWT Authentication
Purpose:
- Moderator authentication
- Session handling
- Secure dashboard access

---

## API Communication
### REST APIs
Purpose:
- Communication between Devvit app and backend
- Dashboard APIs
- AI analysis APIs

---

# Reddit Integration

## Devvit SDK
Purpose:
- Reddit moderation integration
- Mod queue access
- Post/comment monitoring
- Moderator actions

Features:
- Remove posts
- Approve posts
- Ban users
- Comment moderation
- Modmail integration

---

# AI Stack

## LLM Provider
### Gemini API or OpenAI API
Purpose:
- AI moderation reasoning
- Moderation suggestions
- Summaries
- Auto-generated removal reasons

---

## Toxicity Detection
### Perspective API
Purpose:
- Toxicity scoring
- Harassment detection
- Hate speech analysis

---

## NLP Embeddings
### sentence-transformers
Purpose:
- Semantic similarity
- Duplicate detection
- Scam similarity analysis
- Pattern clustering

Recommended Models:
- all-MiniLM-L6-v2
- bge-small-en

---

## Vector Database
### Qdrant
Purpose:
- Similarity search
- Repost detection
- Scam memory
- Historical moderation intelligence

---

# Database Stack

## Primary Database
### PostgreSQL
Purpose:
- Moderation history
- User risk data
- AI analysis logs
- Analytics storage

---

## Cache & Queue
### Redis
Purpose:
- Real-time queues
- Temporary AI caching
- Rate limiting
- Live dashboard updates

---

# Infrastructure

## Frontend Hosting
### Vercel
Purpose:
- Next.js hosting
- Global CDN
- Fast deployments

---

## Backend Hosting
### Railway or Render
Purpose:
- FastAPI hosting
- API deployment
- Background workers

---

## Containerization
### Docker
Purpose:
- Reproducible deployments
- Local development consistency
- Easier cloud deployment

---

## CI/CD
### GitHub Actions
Purpose:
- Automated testing
- Linting
- Deployment pipelines

---

# Observability

## Logging
### Loguru
Purpose:
- Structured backend logging
- Error tracking
- AI pipeline debugging

---

## Monitoring
### Prometheus + Grafana
Purpose:
- API metrics
- Queue monitoring
- AI latency tracking

---

# Security

## API Security
- JWT authentication
- API rate limiting
- Secure secrets management
- HTTPS-only communication

---

# Recommended Folder Structure

```text
modshield-ai/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── charts/
│   └── lib/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── models/
│   ├── ai/
│   ├── moderation/
│   └── analytics/
│
├── modshieldai/
│   ├── actions/
│   ├── triggers/
│   └── ui/
│
├── docker/
├── docs/
└── scripts/
```

---

# Recommended Development Workflow

1. Setup Devvit integration
2. Build FastAPI moderation APIs
3. Integrate AI moderation engine
4. Build moderation dashboard
5. Add analytics layer
6. Add semantic similarity features
7. Polish UI and demo flow

---

# Recommended MVP Features

## Must Have
- AI moderation scoring
- Toxicity detection
- Scam detection
- Moderator queue
- AI action suggestions
- One-click moderation actions

---

## Nice To Have
- Raid detection
- Community health score
- AI thread summaries
- Duplicate detection
- Moderator memory system

