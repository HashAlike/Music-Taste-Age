from transformers import pipeline
from src.data_collection import enrich_tracks
from src.data_cleaning import clean_track_info, clean_tracks
import pandas as pd




classifier=pipeline(\
    "zero-shot-classification",\
    model= "MoritzLaurer/bge-m3-zeroshot-v2.0"\
)

labels= ["Music","Non-Music"]

df= enrich_tracks("duzeniduzenadam",10,3)

true_label=[
            "Music","Music","Music","Music","Music","Music",\
            "Music","Music","Music","Music","Music","Music",\
            "Music","Music","Music","Non-Music","Non-Music","Non-Music",\
            "Non-Music","Non-Music","Non-Music","Non-Music","Music","Music",\
            "Music","Music","Music","Non-Music","Non-Music","Music"
            ]

df["true_label"]= true_label

results=[]
data= {}
for i in range(len(df)):
    name= df["name"][i]
    artist= df["artist"][i]
    text= str(name + " - " + artist)
    result= classifier(text,candidate_labels=labels)

    data={
        "name": df["name"][i],
        "artist": df["artist"][i],
        "text":text,
        "true_label": df["true_label"][i],
        "predict_label": result["labels"][0],
        "predict_score": result["scores"][0]
        }

    results.append(data)


dataf= pd.DataFrame(results)
print(dataf)

