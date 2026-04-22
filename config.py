import os
from dotenv import load_dotenv

load_dotenv()

N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL', 'https://n8n-webhook-url')
OPEN_CLOUD_API_KEY = os.getenv('OPEN_CLOUD_API_KEY', '')
