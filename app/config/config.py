import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    
    KEYS_FOLDER = os.environ.get('KEYS_FOLDER') or os.path.join(os.getcwd(), 'keys')
    
    # Google API Configuration
    GCP_KEY_FILE_NAME = os.environ.get('GCP_FILE_NAME') or 'gcp_key.json'

    # Upload Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg'}
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or os.path.join(os.getcwd(), 'uploads')