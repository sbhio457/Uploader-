#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28161387"))
API_HASH = environ.get("API_HASH", "911b975dad78e1c06faff0ec21cc99a6")
BOT_TOKEN = environ.get("BOT_TOKEN", "8423500157:AAFRmG9z3OgnThUcakfEZPxS6qwEA_0xF0M")

OWNER = int(environ.get("OWNER", "6923038522"))
CREDIT = environ.get("CREDIT", "𝐒𝐡𝐚𝐝𝐨𝐰 ⛦")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6923038522').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6923038522').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

