import requests

def GetPlaylistAPI():
    url = "https://api.freeapi.app/api/v1/public/youtube/playlists?page=1&limit=5"
    response  = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        playlist_data = data["data"]["data"]
        first_playlist = playlist_data[0]
        id = first_playlist["id"]
        channelTitle = first_playlist["snippet"]["channelTitle"]
        video_title = first_playlist["snippet"]["title"]

        return id, channelTitle, video_title
    else:
        raise Exception("Failed to fetch data")
    

def main():
    try:
        id,channeltitle, videotitle = GetPlaylistAPI()
        print()
        print("-------------------------")
        print(f"ID: {id}\nChannel Title: {channeltitle}\nVideo Title: {videotitle}")
        print("-------------------------")
        print()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

