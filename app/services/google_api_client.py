import os

from google.cloud import translate_v2 as translate
from config.config import Config

class GoogleAPIClient:
    def __init__(self):
        self.client = self.create_connection()
    
    def create_connection(self):
        folder = Config.KEYS_FOLDER
        key_path = os.path.join(folder, Config.GCP_KEY_FILE_NAME)
        client = translate.Client.from_service_account_json(key_path)
        return client

    def translate_text(self, text):
        result = self.client.translate(text, target_language='es')
        return result['translatedText']