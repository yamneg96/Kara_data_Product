# CRUD logic
from sqlalchemy.orm import Session
from api.database import SessionLocal

# Sample dummy logic for query (to be replaced by real SQLAlchemy queries if connected to DB)

def get_top_products(limit: int):
    return [{"product": "paracetamol", "count": 32}] * limit

def get_channel_activity(channel_name: str):
    return {
        "channel": channel_name,
        "total_posts": 120,
        "average_post_length": 156.4
    }
