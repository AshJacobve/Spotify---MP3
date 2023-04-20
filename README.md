# __Spotify Playlist to YouTube Downloader__

#### This is a Python script that allows you to *__download audio__* from the tracks in a Spotify playlist and save them as *__MP3 files__* using YouTube as the audio source.

## __Prerequisites__

#### Before running the script, make sure you have the following libraries installed:

\- *__requests__*: for making __HTTP requests__   
\- *__base64__*: for __encoding and decoding base64 data__    
\- *__googleapiclient__*: for interacting with the __YouTube API__    
\- *__pytube__*: for __downloading__ YouTube videos    


#### You can install these libraries using __'pip'__ or __'conda'__ by running the following commands:

*pip install requests base64 google-api-python-client pytube*

## __Getting Started__

#### 1) Clone the repository or download the script file to your local machine.

#### 2) Replace the values of __'CLIENT_ID'__ and __'CLIENT_SECRET'__ with your own Spotify API credentials. You can obtain these credentials by creating a Spotify Developer account and registering a new application.

#### 3) Replace the value of __'playlist_id'__ with the ID of the Spotify playlist that you want to download from.

#### 4) Replace the value of __'ytkey'__ with your own YouTube API key. You can obtain a YouTube API key by creating a project in the Google Developers Console and enabling the YouTube Data API.

#### 5) Run the script using a Python interpreter.

#### 6) The script will retrieve the tracks from the Spotify playlist and search for the corresponding audio on YouTube. It will download the audio as MP3 files and save them to the destination folder specified in the __destination__ variable.

#### 7) After the download is complete, you will see a success message with the title of the downloaded track.

Note: Please be aware of the terms of use of the Spotify and YouTube APIs, as well as the terms of use of the downloaded audio files. Make sure to comply with all applicable laws and regulations related to copyright and intellectual property rights.

## __Drawbacks to the program__

The program relies on the use of YouTube's API, which restricts the number of requests sent in per day. Therefore, the program won't run too many times per day

This problem can be dodged if we use another API to access YouTube, however, it is __illegal__ and highly advised against.





