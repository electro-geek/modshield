from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from models import database
from ai.toxicity import ToxicityDetector
from ai.scam_detection import ScamDetector
from ai.llm_reasoning import AIReasoningEngine
from pydantic import BaseModel
import os
from configparser import ConfigParser

router = APIRouter()

# Load config for API keys
config = ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.properties')
config.read(config_path)

toxicity_detector = ToxicityDetector(api_key=os.environ.get('PERSPECTIVE_API_KEY', config.get('DEFAULT', 'PERSPECTIVE_API_KEY', fallback=None)))
scam_detector = ScamDetector()
reasoning_engine = AIReasoningEngine(api_key=os.environ.get('GEMINI_API_KEY', config.get('DEFAULT', 'GEMINI_API_KEY', fallback=None)))

class AnalysisRequest(BaseModel):
    post_id: str
    title: str
    content: str
    author: str
    subreddit: str

@router.post("/")
async def analyze_post(request: AnalysisRequest, db: Session = Depends(get_db)):
    # 1. Toxicity Analysis
    toxicity_results = toxicity_detector.analyze(request.content)
    
    # 2. Scam Analysis
    scam_results = scam_detector.analyze(request.content)
    
    # 3. Spam Analysis (Placeholder for now)
    spam_score = 0.1 # Mock
    
    # 4. Calculate Risk Score
    risk_score = (toxicity_results.get('toxicity', 0) * 0.4 + 
                  scam_results.get('scam_score', 0) * 0.5 + 
                  spam_score * 0.1) * 100
    
    # 5. AI Reasoning
    suggestion = reasoning_engine.generate_moderation_suggestion(
        request.title, request.content, 
        {"toxicity": toxicity_results.get('toxicity'), "scam": scam_results.get('scam_score'), "spam": spam_score}
    )
    
    # 6. Save to DB
    # Ensure user exists
    user = db.query(database.User).filter(database.User.reddit_username == request.author).first()
    if not user:
        user = database.User(reddit_username=request.author)
        db.add(user)
        db.commit()
    
    # FlaggedContent (Check for existing first)
    flagged = db.query(database.FlaggedContent).filter(database.FlaggedContent.post_id == request.post_id).first()
    if not flagged:
        flagged = database.FlaggedContent(
            post_id=request.post_id,
            title=request.title,
            content=request.content,
            author_id=user.id,
            author_name=request.author,
            subreddit=request.subreddit,
            priority=database.Priority.HIGH if risk_score > 70 else database.Priority.MEDIUM if risk_score > 30 else database.Priority.LOW
        )
        db.add(flagged)
    else:
        # Update existing record
        flagged.author_id = user.id
        flagged.author_name = request.author
        flagged.priority = database.Priority.HIGH if risk_score > 70 else database.Priority.MEDIUM if risk_score > 30 else database.Priority.LOW
        flagged.status = database.ModerationStatus.PENDING # Reset to pending if re-analyzed
    
    db.commit()
    
    # AI Analysis record (Check for existing first)
    analysis = db.query(database.AIAnalysis).filter(database.AIAnalysis.post_id == request.post_id).first()
    if not analysis:
        analysis = database.AIAnalysis(
            post_id=request.post_id,
            toxicity_score=toxicity_results.get('toxicity'),
            spam_score=spam_score,
            scam_score=scam_results.get('scam_score'),
            risk_score=risk_score,
            suggested_action=suggestion.get('suggested_action'),
            reasoning=suggestion.get('reasoning'),
            analysis_json={"toxicity": toxicity_results, "scam": scam_results}
        )
        db.add(analysis)
    else:
        # Update existing analysis
        analysis.toxicity_score = toxicity_results.get('toxicity')
        analysis.spam_score = spam_score
        analysis.scam_score = scam_results.get('scam_score')
        analysis.risk_score = risk_score
        analysis.suggested_action = suggestion.get('suggested_action')
        analysis.reasoning = suggestion.get('reasoning')
        analysis.analysis_json = {"toxicity": toxicity_results, "scam": scam_results}
    
    db.commit()
    
    return {
        "post_id": request.post_id,
        "risk_score": risk_score,
        "suggested_action": suggestion.get('suggested_action'),
        "reasoning": suggestion.get('reasoning')
    }
