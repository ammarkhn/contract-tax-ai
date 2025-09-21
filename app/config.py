import os
from dotenv import load_dotenv
# Load .env file
load_dotenv()

class Settings:
    # APP_NAME: str = os.getenv("APP_NAME", "Speech Backend API")
    # APP_ENV: str = os.getenv("APP_ENV", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    # JWT_SECRET: str = os.getenv("JWT_SECRET", "changeme")
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
 # Google OAuth
    # GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    # GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    # SESSION_SECRET: str = os.getenv("SESSION_SECRET", "fallback-secret")
settings = Settings()
