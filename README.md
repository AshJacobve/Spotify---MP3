# Spotify Playlist to YouTube Downloader
This is a Python script that allows you to download audio from the tracks in a Spotify playlist and save them as MP3 files using YouTube as the audio source.

Prerequisites
Before running the script, make sure you have the following libraries installed:

requests: for making HTTP requests
base64: for encoding and decoding base64 data
googleapiclient: for interacting with the YouTube API
pytube: for downloading YouTube videos


You can install these libraries using pip or conda by running the following commands:


pip install requests base64 google-api-python-client pytube

Getting Started
Clone the repository or download the script file to your local machine.

Replace the values of CLIENT_ID and CLIENT_SECRET with your own Spotify API credentials. You can obtain these credentials by creating a Spotify Developer account and registering a new application.

Replace the value of playlist_id with the ID of the Spotify playlist that you want to download from.

Replace the value of ytkey with your own YouTube API key. You can obtain a YouTube API key by creating a project in the Google Developers Console and enabling the YouTube Data API.

Run the script using a Python interpreter.

The script will retrieve the tracks from the Spotify playlist and search for the corresponding audio on YouTube. It will download the audio as MP3 files and save them to the destination folder specified in the destination variable.

After the download is complete, you will see a success message with the title of the downloaded track.

Note: Please be aware of the terms of use of the Spotify and YouTube APIs, as well as the terms of use of the downloaded audio files. Make sure to comply with all applicable laws and regulations related to copyright and intellectual property rights.




