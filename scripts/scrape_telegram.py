from telethon.sync import TelegramClient
import os
import json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
channels = ["https://t.me/lobelia4cosmetics", "https://t.me/tikvahpharma"]

client = TelegramClient("anon", api_id, api_hash)

async def scrape():
    await client.start()
    for url in channels:
        entity = await client.get_entity(url)
        messages = []
        async for msg in client.iter_messages(entity, limit=100):
            messages.append({
                "id": msg.id,
                "text": msg.message,
                "date": msg.date.isoformat(),
                "has_media": bool(msg.media),
            })

        date_str = datetime.now().strftime("%Y-%m-%d")
        fname = f"data/raw/{date_str}_{entity.username}.json"
        with open(fname, "w") as f:
            json.dump(messages, f, indent=2)

with client:
    client.loop.run_until_complete(scrape())
