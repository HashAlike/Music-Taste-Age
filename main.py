from src.data_collection import get_all_recent_tracks
from src.data_cleaning import clean_tracks


username = input("Enter your last.fm username: ")

data = get_all_recent_tracks(username,10,3)
cleaned_data= clean_tracks(data)
print(len(cleaned_data))

