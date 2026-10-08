import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
AAKASH_SMS_TOKEN = os.getenv("AAKASH_SMS_TOKEN")