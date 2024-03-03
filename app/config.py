from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')


# LINKS
ALL_DATA_LINK = os.environ.get('ALL_DATA_LINK')
SPECIFIC_DATA_LINK = os.environ.get('SPECIFIC_DATA_LINK')

# API
API_TOKEN = os.environ.get('API_TOKEN')

# AUTH TOKEN
AUTH_SECRET = os.environ.get('AUTH_SECRET')
