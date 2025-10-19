# core/config.py
import os
from pydantic_settings import BaseSettings
from pathlib import Path

# Define the base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    WEATHER_API_KEY: str
    GEMINI_API_KEY: str
    DATA_GOV_API_KEY: str
    TWILIO_ACCOUNT_SID: str  # <-- ADD THIS
    TWILIO_AUTH_TOKEN: str   # <-- ADD THIS

    # Paths
    MODEL_PATH: str = os.path.join(BASE_DIR, 'model', 'saved_model', 'krishi_multicrop_model.keras')
    CLASS_NAMES_PATH: str = os.path.join(BASE_DIR, 'model', 'class_names.json')
    INDIAN_CITIES_PATH: str = os.path.join(BASE_DIR, 'static', 'data.json')

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')

settings = Settings()