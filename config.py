import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан в окружении или .env")

DB_PATH = os.getenv("DB_PATH", "bot.sqlite3")
DB_URL = f"sqlite+aiosqlite:///{Path(DB_PATH).expanduser()}"

