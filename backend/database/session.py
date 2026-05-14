from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from configparser import ConfigParser

# Load config
config = ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.properties')

# Fallback to default if config doesn't exist
try:
    with open(config_path) as f:
        config.read_file(f)
except FileNotFoundError:
    pass

# Get the full URL from environment (Vercel/Nile style) or build it
SQLALCHEMY_DATABASE_URL = os.environ.get('POSTGRES_URL') or os.environ.get('NILEDB_URL')

if not SQLALCHEMY_DATABASE_URL:
    POSTGRES_USER = os.environ.get('POSTGRES_USER', config.get('DEFAULT', 'POSTGRES_USER', fallback='postgres'))
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', config.get('DEFAULT', 'POSTGRES_PASSWORD', fallback='password'))
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', config.get('DEFAULT', 'POSTGRES_HOST', fallback='localhost'))
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', config.get('DEFAULT', 'POSTGRES_PORT', fallback='5432'))
    POSTGRES_DB = os.environ.get('POSTGRES_DB', config.get('DEFAULT', 'POSTGRES_DB', fallback='modshield'))
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# SQLAlchemy requires postgresql:// instead of postgres://
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
