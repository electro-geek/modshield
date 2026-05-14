from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
from configparser import ConfigParser
from database.session import engine
from models.database import Base
from routes import analyze, moderation, analytics, users

# Load config
config = ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.properties')
config.read(config_path)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ModShield AI Backend")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(analyze.router, prefix="/api/analyze", tags=["Analysis"])
app.include_router(moderation.router, prefix="/api/moderation", tags=["Moderation"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "ModShield AI API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.get('DEFAULT', 'HOST', fallback='0.0.0.0'), port=int(config.get('DEFAULT', 'PORT', fallback=8000)))
