# from database import engine, Base  # Import from your database setup
from models.base import Base, engine
from models import *

# Create all tables in the database
Base.metadata.create_all(engine)

print("Database tables created successfully!")