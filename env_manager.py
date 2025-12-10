import os
from google import genai
from dotenv import load_dotenv, set_key
from pathlib import Path

# --- VERSIONING ---
VERSION_MAJOR = 0
VERSION_MINOR = 1 # MANUAL UPDATE: Minor version incremented for Release 0.3.7
CHANGELOG = [
    "Starting at 0.1, after re-initializing log."
]
# --- END VERSIONING ---

class GeminiEnvManager:
    """Manages the GEMINI_API_KEY environment variable and .env file."""

    def __init__(self, env_path=".env"):
        self.env_path = Path(env_path).resolve()
        if not self.env_path.exists():
            self.env_path.touch()
        load_dotenv(self.env_path) 
        self._key = os.getenv("GEMINI_API_KEY")

    def get_key(self):
        return self._key

    def update_key(self, new_key: str):
        try:
            set_key(str(self.env_path), "GEMINI_API_KEY", new_key)
            self._key = new_key
            return True, "Configuration updated successfully."
        except Exception as e:
            return False, f"Error saving key to file: {e}"

    def test_key_validity(self):
        key = self.get_key()
        if not key:
            return False, "Key is missing or empty."
        
        try:
            client = genai.Client(api_key=key)
            client.models.list()
            return True, "Key is valid and connected to Google AI."
        except Exception as e:
            return False, f"Key validation failed. Error: {e}"

if __name__ == '__main__':
    print(f"env_manager.py Version: {VERSION_MAJOR}.{VERSION_MINOR}.{len(CHANGELOG)}")