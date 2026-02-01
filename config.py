# Імпортуємо необхідні модулі
import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env файлу
load_dotenv()

# Отримуємо токен з .env файлу
CHATGPT_TOKEN = os.getenv("CHATGPT_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
