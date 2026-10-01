def clean_tracks(data):
    records=[]

    for i in data:

        record={}
        if "date" not in i:
            print(i)
        else:
            record["name"]= i["name"]
            record["artist"]= i["artist"]["#text"]
            record["album"]=i["album"]["#text"]
            record["date"]= i["date"]["#text"]
            record["timestamp"]= i["date"]["uts"]

            records.append(record)

    return records

def clean_track_info(info_data): 
    tracks= info_data["track"]
    record={}
    record["name"]= tracks.get("name")
    record["track_mbid"]= tracks.get("mbid")
    record["duration"]= tracks.get("duration")
    record["listeners"]=tracks.get("listeners")
    record["playcount"]=tracks.get("playcount")

    if tracks.get("artist")==None:
        record["artist_mbid"]= None
        record["artist"]= None
    else:
        record["artist_mbid"]= tracks["artist"].get("mbid")
        record["artist"]= tracks["artist"].get("name")

    if tracks.get("album")==None:
        record["album"]= None
    else:
        record["album"]= tracks["album"].get("title")

    if tracks.get("toptags")==None:
        record["tags"]=[]
    else:
        tag=[]
        if tracks["toptags"].get("tag")==None:
            record["tags"]=[]
        else:
            for i in tracks["toptags"]["tag"]:
                tag.append(i["name"])

            record["tags"]=tag

    return record