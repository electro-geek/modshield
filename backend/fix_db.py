from sqlalchemy import text, inspect
from database.session import engine

def fix_schema():
    try:
        with engine.connect() as conn:
            inspector = inspect(engine)
            existing_columns = [c['name'] for c in inspector.get_columns('users')]
            
            print(f"Existing columns in 'users': {existing_columns}")
            
            # List of columns to add if missing
            # format: (name, type)
            to_add = [
                ("reddit_username", "VARCHAR"),
                ("risk_score", "FLOAT DEFAULT 0.0"),
                ("account_age_days", "INTEGER DEFAULT 0"),
                ("total_violations", "INTEGER DEFAULT 0"),
                ("created_at", "TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP"),
                ("updated_at", "TIMESTAMP WITH TIME ZONE")
            ]
            
            for col_name, col_type in to_add:
                if col_name not in existing_columns:
                    print(f"Adding column '{col_name}'...")
                    conn.execute(text(f"ALTER TABLE users ADD COLUMN {col_name} {col_type}"))
            
            # Add unique index for reddit_username if it was just added
            if "reddit_username" not in existing_columns:
                 conn.execute(text("CREATE UNIQUE INDEX IF NOT EXISTS ix_users_reddit_username ON users (reddit_username)"))
            
            conn.commit()
            print("Successfully synchronized 'users' table schema.")
            
    except Exception as e:
        print(f"Error fixing schema: {e}")
        print("Attempting a full table recreation as fallback...")
        from models.database import Base
        Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    fix_schema()
