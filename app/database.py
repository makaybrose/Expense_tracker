#CONNECTING APP TO DATABASE

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Extract the database URL
DATABASE_PATH = os.getenv("DATABASE_URL")
print("Database URL:", DATABASE_PATH)

# Create the engine
engine = create_engine(DATABASE_PATH)

#testing the database connection
try:
    with engine.connect() as connection:
        print("Database connection is successful") 

except Exception as e:
    print("Database connection failed")
    print ("Error:",e)

# autocommit to save files,sessionlocal keeps records
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()