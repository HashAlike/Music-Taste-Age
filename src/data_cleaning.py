def clean_tracks(data):
    records=[]

    for i in data:
        record={}
        record["name"]= i["name"]
        record["artist"]= i["artist"]["#text"]
        record["album"]=i["album"]["#text"]
        record["date"]= i["date"]["#text"]
        record["timestamp"]= i["date"]["uts"]

        records.append(record)

    return records

