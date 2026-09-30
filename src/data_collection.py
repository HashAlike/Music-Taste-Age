import os
import requests
import time
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("LASTFM_API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"


def get_recent_tracks(username, limit=200,page=1):
    params = {
        "page": page,
        "method": "user.getRecentTracks",
        "user": username,
        "api_key": API_KEY,
        "format": "json",
        "limit": limit,
    }

    response = requests.get(BASE_URL, params=params)

    print("Status code:", response.status_code)

    return response.json()


def get_total_pages(data):
    return int(data["recenttracks"]["@attr"]["totalPages"])


def get_all_recent_tracks(user, limit=200,max_pages=None, delay=0.25):
    first = get_recent_tracks(user, page=1, limit=limit)

    total_pages = get_total_pages(first)
    print(f"totalPages = {total_pages}")

    all_tracks = list(first["recenttracks"]["track"])

    if max_pages==None:
            for page in range(2, total_pages + 1):
                data = get_recent_tracks(user, page=page, limit=limit)
                all_tracks.extend(data["recenttracks"]["track"])

                if page % 50 == 0:
                    print(f"{page}/{total_pages} page is complicated!")

                time.sleep(delay)

            return all_tracks

    else:
        for page in range(2,max_pages +1 ):
            data= get_recent_tracks(user,page=page, limit=limit)
            all_tracks.extend(data["recenttracks"]["track"])

            if page % 50==0:
                print(f"{page}/{max_pages} page is complicated!")

            time.sleep(delay)

        return all_tracks


def get_track_info(artist, track):
    parameters={
        "method":"track.getInfo",
        "artist": artist,
        "track":track,
        "api_key": API_KEY,
        "format":"json"
    }
    response = requests.get(BASE_URL, params=parameters)

    print("Status code:", response.status_code)

    return response.json()