import ffmpeg
import youtube_dl
from youtubesearchpython import CustomSearch, VideoSortOrder

import os


class Track:
    def __init__(self,
                 title,
                 artist,
                 album,
                 length=None):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        
    
    def create(dict_entry):
        return Track(dict_entry["track_name"],
                   dict_entry['artist_name'],
                   dict_entry['album_name'])
    
    def create_path(self):
        if not os.path.exists("Downloads"):
            os.mkdir("Downloads")
        if not os.path.exists(os.path.join("Downloads", self.artist)):
            os.mkdir(os.path.join("Downloads", self.artist))
        if not os.path.exists(os.path.join("Downloads", self.artist, self.album)):
            os.mkdir(os.path.join("Downloads", self.artist, self.album))
        return os.path.join("Downloads", self.artist, self.album)
    
    def search(self):
        query = " ".join([self.title, self.artist, self.album]) 
        search = CustomSearch(query, VideoSortOrder.relevance, limit = 1)
        url = search.result()['result'][0]['link']
        return url
    
    
    def download(self):
        path = self.create_path()
        url = self.search()
        config = {
            'verbose': True,
            'outtmpl': f'downloads/{os.path.join(path, self.title)}.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }]}
        
        with youtube_dl.YoutubeDL(config) as ydl:
            ydl.download([url])
            title = ydl.extract_info(url, download = False)["title"]
        print("Done")
        


class Artist:
    def __init__(self,
                 name):
        self.name = name

class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist