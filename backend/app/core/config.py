from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class Settings(BaseSettings):
    # Base de données
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # Directus
    DIRECTUS_URL: str = os.getenv("DIRECTUS_URL", "http://directus:8055")
    DIRECTUS_TOKEN: str = os.getenv("DIRECTUS_TOKEN", "")
    
    # CORS
    CORS_ORIGINS: List[str] = []
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret_key_for_jwt")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 jours
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Traiter manuellement CORS_ORIGINS
        cors_origins_str = os.getenv("CORS_ORIGINS", "http://localhost:3000")
        self.CORS_ORIGINS = [origin.strip() for origin in cors_origins_str.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 