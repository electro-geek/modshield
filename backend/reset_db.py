from database.session import engine
from models.database import Base
import models.database # Ensure all models are registered

def reset_database():
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("Recreating all tables...")
    Base.metadata.create_all(bind=engine)
    print("Database schema fixed!")

if __name__ == "__main__":
    reset_database()
