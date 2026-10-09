from transformers import pipeline
from src.data_collection import enrich_tracks
from src.data_cleaning import clean_track_info, clean_tracks
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay ,accuracy_score,precision_score,recall_score,f1_score,classification_report



classifier=pipeline(\
    "zero-shot-classification",\
    model= "MoritzLaurer/bge-m3-zeroshot-v2.0"\
)

labels= ["Music","Non-Music"]

df= enrich_tracks("flaneur",10,3)

true_label = [
    "Music","Music","Music","Music","Music","Music",
    "Music","Music","Music","Music","Music","Music",
    "Music","Music","Music","Music","Music","Music",
    "Music","Music","Music","Music","Music","Music",
    "Music","Music","Music","Music","Music","Music"
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
#print(dataf)

cm = confusion_matrix(dataf["true_label"], dataf["predict_label"], labels=["Music","Non-Music"])

print(cm)


ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Music", "Non-Music"]
).plot()

#plt.savefig("/home/hashalike/Belgeler/Yazılım/Projeler/Music Taste & Age/notebooks")")
#plt.show()


accuracy= accuracy_score(dataf["true_label"],dataf["predict_label"])
precision= precision_score(dataf["true_label"],dataf["predict_label"],pos_label="Music")
recall= recall_score(dataf["true_label"],dataf["predict_label"],pos_label="Music")
f1= f1_score(dataf["true_label"],dataf["predict_label"],pos_label="Music")



print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")


# print(classification_report(
#     dataf["true_label"],
#     dataf["predict_label"],
#     labels=["Non-Music", "Music"],
#     target_names=["Non-Music", "Music"],
#     zero_division=0
# ))

fail= dataf[(dataf["true_label"]=="Non-Music") & (dataf["predict_label"]=="Music")]
print(fail)