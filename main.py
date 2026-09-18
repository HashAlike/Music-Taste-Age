from src.data_collection import get_recent_tracks


username = input("Last.fm kullanıcı adını gir: ")

data = get_recent_tracks(username)

print(data)