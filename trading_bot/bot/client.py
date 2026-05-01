import os
from typing import Optional

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()


def _build_futures_url(base_url: Optional[str]) -> Optional[str]:
    if not base_url:
        return None

    normalized_url = base_url.rstrip("/")
    if normalized_url.endswith("/fapi"):
        return normalized_url
    return f"{normalized_url}/fapi"


def get_client() -> Client:
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        testnet=True,
    )

    futures_url = _build_futures_url(os.getenv("BASE_URL"))
    if futures_url:
        client.FUTURES_URL = futures_url

    return client
