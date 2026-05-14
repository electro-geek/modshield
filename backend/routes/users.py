from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models import database

router = APIRouter()

@router.get("/")
async def get_risky_users(db: Session = Depends(get_db)):
    users = db.query(database.User).order_by(database.User.risk_score.desc()).limit(20).all()
    return users

@router.get("/{username}")
async def get_user_history(username: str, db: Session = Depends(get_db)):
    user = db.query(database.User).filter(database.User.reddit_username == username).first()
    if not user:
        return {"error": "User not found"}
    
    events = db.query(database.ModerationEvent).join(
        database.FlaggedContent, database.ModerationEvent.post_id == database.FlaggedContent.post_id
    ).filter(database.FlaggedContent.author == username).all()
    
    return {
        "user": user,
        "history": events
    }
