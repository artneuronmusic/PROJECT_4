from dotenv import load_dotenv
import os
load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
PRODUCER = os.environ.get("PRODUCER")
CASTING_ASSIS = os.environ.get("CASTING_ASSIS")
CASTING_DIRECTOR = os.environ.get("CASTING_DIRECTOR")
AUTH0_DOMAIN_SETTING = os.environ.get('AUTH0_DOMAIN_SETTING')
ALGORITHMS_SETTING = os.environ.get('ALGORITHMS_SETTING')
API_AUDIENCE_SETTING = os.environ.get('API_AUDIENCE_SETTING')

# DB_USER = os.environ.get("DB_USER")
# DB_PASSWORD = os.environ.get("DB_PASSWORD")


"""
or use the below
from decouple import config

API_USERNAME = config('USER')
API_KEY = config('KEY')
"""