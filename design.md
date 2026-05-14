# ModShield AI — System Design

## Project Vision
ModShield AI is an AI-powered moderation operating system for Reddit communities. The platform assists moderators by prioritizing dangerous content, automating moderation workflows, and providing AI-driven insights.

---

# Design Goals

## Primary Goals
- Reduce moderator burnout
- Improve moderation speed
- Detect harmful content early
- Provide explainable AI moderation
- Build a scalable moderation platform

---

# High-Level System Design

```text
                   ┌────────────────────┐
                   │   Reddit Platform  │
                   └─────────┬──────────┘
                             │
                             ▼
                   ┌────────────────────┐
                   │    Devvit App      │
                   └─────────┬──────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   FastAPI Backend    │
                  └─────────┬────────────┘
                            │
        ┌───────────────────┼────────────────────┐
        ▼                   ▼                    ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ AI Moderation  │ │ Analytics      │ │ Risk Engine    │
│ Engine         │ │ Engine         │ │                │
└────────────────┘ └────────────────┘ └────────────────┘
        │                   │                    │
        └───────────────────┼────────────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Data Layer          │
                 │ PostgreSQL + Redis  │
                 │ + Vector Database   │
                 └─────────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Moderator Dashboard │
                 └─────────────────────┘
```

---

# Core Modules

# 1. Devvit Integration Layer

## Responsibilities
- Listen to Reddit events
- Receive new posts/comments
- Access moderation queues
- Trigger backend analysis
- Execute moderator actions

## Events Handled
- New posts
- New comments
- Reported content
- User reports
- Moderator actions

---

# 2. AI Moderation Engine

## Purpose
Analyze Reddit content and generate moderation intelligence.

---

## Input
```json
{
  "title": "Free crypto giveaway",
  "body": "Send wallet details now",
  "author": "user123",
  "subreddit": "crypto"
}
```

---

## Output
```json
{
  "toxicity": 0.15,
  "spam": 0.92,
  "scam": 0.95,
  "risk_score": 96,
  "suggested_action": "remove",
  "reason": "Likely phishing scam"
}
```

---

## Internal Components

### Toxicity Detector
Detects:
- harassment
- hate speech
- insults
- threats

---

### Scam Detector
Detects:
- phishing attempts
- fake giveaways
- crypto scams
- malicious links

---

### Spam Detector
Detects:
- repetitive posting
- bot-like behavior
- suspicious promotion

---

### Semantic Similarity Engine
Detects:
- reposts
- repeated scams
- coordinated campaigns

---

### AI Reasoning Layer
Generates:
- moderation explanations
- suggested actions
- moderation summaries

---

# 3. Risk Intelligence Engine

## Purpose
Generate user and content risk scores.

---

## Risk Signals
- Account age
- Posting frequency
- Toxicity history
- Repeated violations
- Similarity to known scams
- Link reputation

---

## Output
```text
Risk Score: 0–100
```

---

# 4. Moderator Dashboard

## Main Features

### Live Moderation Queue
Displays:
- flagged posts
- risk scores
- AI suggestions
- moderation history

---

### Analytics Page
Displays:
- toxicity trends
- spam trends
- moderator actions
- community health metrics

---

### User Intelligence Page
Displays:
- risky users
- repeated offenders
- behavioral analysis

---

# 5. Analytics Engine

## Purpose
Generate moderation and community insights.

---

## Metrics
- Toxicity over time
- Spam attack frequency
- Moderator workload
- Most flagged users
- Scam trends

---

# Database Design

# PostgreSQL Tables

## users
```text
id
reddit_username
risk_score
account_age
created_at
```

---

## moderation_events
```text
id
post_id
action
reason
moderator
timestamp
```

---

## ai_analysis
```text
id
post_id
toxicity_score
spam_score
scam_score
risk_score
analysis_json
created_at
```

---

## flagged_content
```text
id
post_id
status
priority
assigned_moderator
created_at
```

---

# Real-Time Flow Design

## Moderation Pipeline

```text
New Reddit Post
      ↓
Devvit Trigger
      ↓
FastAPI Endpoint
      ↓
AI Analysis
      ↓
Risk Scoring
      ↓
Queue Prioritization
      ↓
Dashboard Update
      ↓
Moderator Action
```

---

# Explainable AI Design

## Goal
Avoid black-box moderation decisions.

---

## AI Explanation Example

```text
This content was flagged because:
- Contains suspicious giveaway language
- Includes high-risk URL
- Similar to 12 previously removed scams
```

---

# UI/UX Design

## Theme
- Dark mode
- Cybersecurity-inspired aesthetic
- Real-time indicators
- Clean dashboards

---

## UI Components
- Risk score badges
- AI confidence bars
- Queue priority indicators
- Threat heatmaps
- Trend charts

---

# Security Design

## Security Measures
- JWT authentication
- Secure API keys
- Role-based access
- API rate limiting
- HTTPS-only APIs

---

# Scalability Design

## Horizontal Scalability
- Stateless FastAPI services
- Redis-based caching
- Background workers
- Queue-based processing

---

# Future Enhancements

## Planned Features
- Raid detection
- AI moderator memory
- Cross-subreddit intelligence
- Community sentiment analysis
- AI-generated moderation reports

---

# Demo Design Strategy

## Demo Flow

1. Suspicious post appears
2. AI analyzes content live
3. Dashboard updates instantly
4. AI explains reasoning
5. Moderator removes post
6. Analytics update in real time

---

# Final System Goals

ModShield AI should feel like:
- an intelligent moderation assistant
- a security operations center for Reddit
- a real-time AI moderation platform
- a productivity multiplier for moderators

