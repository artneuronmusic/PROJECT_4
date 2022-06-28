from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)
DB_NAME = os.getenv('DB_NAME')
AUTH0_DOMAIN_SETTING = os.getenv('AUTH0_DOMAIN_SETTING')
ALGORITHMS_SETTING = os.getenv('ALGORITHMS_SETTING')
API_AUDIENCE_SETTING = os.getenv('API_AUDIENCE_SETTING')
DATABASE_URL_SETTING = os.getenv('DATABASE_URL')
PRODUCER = os.getenv('PRODUCER')
CASTING_ASSIS = os.getenv('CASTING_ASSIS')
CASTING_DIRECTOR = os.getenv('CASTING_DIRECTOR')
