import requests
import base64
from googleapiclient.discovery import build
from pytube import YouTube
import googleapiclient.errors
import os


CLIENT_ID = '561f89b327814a9092fdd301ce7f8fd3'
CLIENT_SECRET = 'f821c69d57f34881b3833294b1da70fd'

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
playlist_id = '0H2vQV8bqaJnIUbVeQEIG0'

# AUTHORIZATION
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
# RUNNING FOR PLAYLIST ON SPOTIFY'S API
r = requests.get(BASE_URL + 'playlists/' + playlist_id, headers=headers)

r = r.json()

# GOES THROUGH PLAYLIST, GATHERING NAME AND ARTIST OF EACH SONG IN PLAYLIST
tracks = []
for i in r['tracks']['items']:
    tracks.append({
        'title' : i['track']['album']['name'],
        'artists' : i['track']['album']['artists'][0]['name'],
    })


ytkey= 'AIzaSyD07hZiacEJYvvnvJwFAaHPV1mm4Xu1H94'

youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=ytkey)
# RUNS THE SONG NAME ALONG WITH 'audio only' ON YT, GETTING THE LINK OF THE FIRST VIDEO FOUND
for track in tracks:
    print(track)
    first_value = list(track.values())[0]
    second_value = list(track.values())[1]

    request = youtube.search().list(
        part="snippet",
        maxResults=1,
        order="viewCount",
        q="first_value",
    )
    response = request.execute()

    for i in response:
        print(i)
        if i=='items':
           p=response[i]
           dicts=p[0]
           print(p)
           for j in dicts:
              if j=='id':
                for k in dicts[j]:
                    if k=='videoId':
                        linkurl=str(dicts[o][k])
    yt=("https://www.youtube.com/watch?v="+linkurl)   
    print(yt)                 
    yt=YouTube("https://www.youtube.com/watch?v="+linkurl)
    print(yt)
    video = yt.streams.filter(only_audio=True).first()
  
# replace destination with the path where you want to save the downloaded file
    destination = (r"C:/Users/itsme\Downloads")
  
# download the file
    out_file = video.download(output_path=destination)
  
# save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  
# result of success
    print(yt.title + " has been successfully downloaded.")