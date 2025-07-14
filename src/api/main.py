# FastAPI entry
from fastapi import FastAPI
from api.crud import get_top_products, get_channel_activity
from api.schemas import ProductResponse, ChannelActivityResponse

app = FastAPI()

@app.get("/api/reports/top-products", response_model=list[ProductResponse])
def top_products(limit: int = 10):
    return get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity", response_model=ChannelActivityResponse)
def channel_activity(channel_name: str):
    return get_channel_activity(channel_name)
