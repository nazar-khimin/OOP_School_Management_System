# from database import engine, Base  # Import from your database setup
from database import Base, engine

# Create all tables in the database
Base.metadata.create_all(engine)

print("Database tables created successfully!")