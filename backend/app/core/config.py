from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[3]  # rental/
BACKEND_DIR = BASE_DIR / "backend"

# Load DB config directly from CollabHub if present
collab_candidates = [
    BASE_DIR.parent / "CollabHub" / "backend" / ".env",
    BASE_DIR.parent / "Collabhub" / "backend" / ".env",
    BASE_DIR.parent / "COLLABHUB" / "backend" / ".env",
]
for p in collab_candidates:
    if p.exists():
        load_dotenv(p, override=False)
        COLLAB_ENV_PATH = p
        break
else:
    COLLAB_ENV_PATH = collab_candidates[0]

# Load app-local env (allows local overrides like working DATABASE_URL)
load_dotenv(BACKEND_DIR / ".env", override=True)

class Settings:
    PROJECT_NAME: str = "Rental Marketplace MVP"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "rental_mvp")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "dev-secret-change-me")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    CORS_ORIGINS: list[str] = [o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:5500,http://127.0.0.1:5500,http://localhost:4173,http://localhost:8000").split(",") if o.strip()]
    COLLAB_ENV_PATH: str = str(COLLAB_ENV_PATH)

settings = Settings()
