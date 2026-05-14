from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database.session import get_db
from models import database
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/summary")
async def get_summary(db: Session = Depends(get_db)):
    total_flagged = db.query(database.FlaggedContent).count()
    total_actions = db.query(database.ModerationEvent).count()
    
    # Average risk score
    avg_risk = db.query(func.avg(database.AIAnalysis.risk_score)).scalar() or 0
    
    # Fetch 5 most recent alerts
    recent_flagged = db.query(database.FlaggedContent).order_by(database.FlaggedContent.created_at.desc()).limit(5).all()
    recent_alerts = [
        {
            "message": f"Potential {item.priority.value} risk in r/{item.subreddit}",
            "time": f"ID: {item.post_id}"
        } for item in recent_flagged
    ]
    
    # Mock trends for UI visualization
    trends = [
        {"value": 40}, {"value": 70}, {"value": 55}, {"value": 90}, {"value": 65}, {"value": 80}, {"value": 50}
    ]
    
    return {
        "total_flagged": total_flagged,
        "total_actions": total_actions,
        "avg_risk_score": round(avg_risk, 1),
        "community_health": 92 if total_flagged < 5 else 78 if total_flagged < 20 else 45,
        "trends": trends,
        "recent_alerts": recent_alerts
    }
