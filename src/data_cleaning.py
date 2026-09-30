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
    record={}
    record["track_mbid"]= info_data["track"]["mbid"]
    record["duration"]= info_data["track"]["duration"]
    record["listeners"]=info_data["track"]["listeners"]
    record["playcount"]=info_data["track"]["playcount"]

    record["artist_mbid"]= info_data["track"]["artist"]["mbid"]
    record["artist"]= info_data["track"]["artist"]["name"]
    record["album"]= info_data["track"]["album"]["title"]

    tag=[]
    for i in info_data["track"]["toptags"]["tag"]:
        tag.append(i["name"])

    record["tags"]=tag

    return record