import psycopg2
import json
import os
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("PGHOST"),
    database=os.getenv("PGDB"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD")
)
cursor = conn.cursor()

def load_data(file_path):
    with open(file_path) as f:
        messages = json.load(f)

    for msg in messages:
        cursor.execute("""
            INSERT INTO raw_telegram_messages (id, text, date, has_media)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (msg["id"], msg["text"], msg["date"], msg["has_media"]))

    conn.commit()

for file in os.listdir("data/raw/"):
    if file.endswith(".json"):
        load_data(os.path.join("data/raw/", file))
