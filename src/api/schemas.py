# Pydantic schemas
from pydantic import BaseModel
from datetime import datetime

class ProductResponse(BaseModel):
    product: str
    count: int

class ChannelActivityResponse(BaseModel):
    channel: str
    total_posts: int
    average_post_length: float
