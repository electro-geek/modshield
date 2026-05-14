from sqlalchemy import Column, String, Float, DateTime, JSON, ForeignKey, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import enum
import uuid

Base = declarative_base()

class ModerationStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REMOVED = "removed"
    ESCALATED = "escalated"

class Priority(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    reddit_username = Column(String, unique=True, index=True)
    risk_score = Column(Float, default=0.0)
    account_age_days = Column(Integer, default=0) # Note: Integer is fine for data, just not the ID
    total_violations = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class FlaggedContent(Base):
    __tablename__ = "flagged_content"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(String, unique=True, index=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id")) # Matches User.id type
    author_name = Column(String)
    subreddit = Column(String)
    status = Column(Enum(ModerationStatus), default=ModerationStatus.PENDING)
    priority = Column(Enum(Priority), default=Priority.LOW)
    assigned_moderator = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class AIAnalysis(Base):
    __tablename__ = "ai_analysis"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(String, ForeignKey("flagged_content.post_id"), index=True)
    toxicity_score = Column(Float)
    spam_score = Column(Float)
    scam_score = Column(Float)
    risk_score = Column(Float)
    suggested_action = Column(String)
    reasoning = Column(String)
    analysis_json = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ModerationEvent(Base):
    __tablename__ = "moderation_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(String, ForeignKey("flagged_content.post_id"), index=True)
    action = Column(String)
    reason = Column(String)
    moderator = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
