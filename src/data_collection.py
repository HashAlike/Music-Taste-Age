import os
import requests
import time
import pandas as pd
from dotenv import load_dotenv
from src.data_cleaning import clean_track_info
from src.data_cleaning import clean_tracks


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

    return response.json()


def get_total_pages(data):
    return int(data["recenttracks"]["@attr"]["totalPages"])



def get_all_recent_tracks(user, limit=200,max_pages=None, delay=0.25):
    first = get_recent_tracks(user, page=1, limit=limit)

    total_pages = get_total_pages(first)

    all_tracks = list(first["recenttracks"]["track"])

    if max_pages==None:
            for page in range(2, total_pages + 1):
                data = get_recent_tracks(user, page=page, limit=limit)
                all_tracks.extend(data["recenttracks"]["track"])

                time.sleep(delay)

            return all_tracks

    else:
        for page in range(2,max_pages +1 ):
            data= get_recent_tracks(user,page=page, limit=limit)
            all_tracks.extend(data["recenttracks"]["track"])

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


    if "track" not in response.json(): 
        print(f"Error, track not found: {artist}-{track}!")
    else:
        return response.json()

cache={}



def enrich_tracks(user,limit=200, max_pages=None):

    global cache

    # Get recent tracks
    df= get_all_recent_tracks(user,limit,max_pages)
    df= clean_tracks(df)
    df=pd.DataFrame(df)
    # Take all unique value
    uq=df.drop_duplicates(["artist","name"])

    # Get all track info
    with_info=[]
    for i in uq.itertuples():
        # cache status check
        if (i.artist,i.name) in cache:
            if cache[i.artist,i.name]== None:
                continue
            else:
                clean= clean_track_info(cache[i.artist,i.name])
                with_info.append(clean)
        else:
            a=get_track_info(i.artist,i.name)
            cache[i.artist,i.name]=a
            # None status check
            if a == None:
                continue
            else:
                clean= clean_track_info(a)
                with_info.append(clean)


    # Make them all a dataframe
    df_info= pd.DataFrame(with_info)

    # Merging two DFs
    data= pd.merge(df, df_info, how='left', on=["artist","name"], sort=False,\
                    suffixes=('_', '_info'))


    return data
