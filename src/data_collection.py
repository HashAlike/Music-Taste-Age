import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("LASTFM_API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"


def get_recent_tracks(username, limit=10):
    params = {
        "method": "user.getRecentTracks",
        "user": username,
        "api_key": API_KEY,
        "format": "json",
        "limit": limit,
    }

    response = requests.get(BASE_URL, params=params)

    print("Status code:", response.status_code)

    return response.json()