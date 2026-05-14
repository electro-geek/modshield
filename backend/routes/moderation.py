from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from models import database
from pydantic import BaseModel

router = APIRouter()

class ModerationAction(BaseModel):
    post_id: str
    action: str # approve, remove, ban
    reason: str
    moderator: str

@router.get("/queue")
async def get_queue(db: Session = Depends(get_db)):
    flagged = db.query(database.FlaggedContent).filter(database.FlaggedContent.status == database.ModerationStatus.PENDING).all()
    
    results = []
    for item in flagged:
        analysis = db.query(database.AIAnalysis).filter(database.AIAnalysis.post_id == item.post_id).first()
        results.append({
            "id": item.id,
            "post_id": item.post_id,
            "title": item.title,
            "content": item.content,
            "author": item.author_name,
            "subreddit": item.subreddit,
            "priority": item.priority,
            "risk_score": analysis.risk_score if analysis else 0,
            "suggested_action": analysis.suggested_action if analysis else "review",
            "reasoning": analysis.reasoning if analysis else "No analysis available"
        })
    
    return sorted(results, key=lambda x: x['risk_score'], reverse=True)

@router.post("/action")
async def perform_action(action: ModerationAction, db: Session = Depends(get_db)):
    flagged = db.query(database.FlaggedContent).filter(database.FlaggedContent.post_id == action.post_id).first()
    if not flagged:
        raise HTTPException(status_code=404, detail="Post not found in queue")
    
    # Update status
    if action.action == "approve":
        flagged.status = database.ModerationStatus.APPROVED
    elif action.action == "remove":
        flagged.status = database.ModerationStatus.REMOVED
    elif action.action == "ban":
        flagged.status = database.ModerationStatus.REMOVED
        # Logic to ban user would go here (interacting with Reddit API)
    
    # Log event
    event = database.ModerationEvent(
        post_id=action.post_id,
        action=action.action,
        reason=action.reason,
        moderator=action.moderator
    )
    db.add(event)
    db.commit()
    
    return {"message": f"Action {action.action} performed successfully"}
