import ffmpeg
import youtube_dl
import json
import spotipy
from youtubesearchpython import *
import pandas as pd
import numpy as np

track_file = "tracks.csv"

# spotify credentials

with open("auth.json", "rb") as auth_file:
    auth = json.load(auth_file)


# spotipy.oauth2.SpotifyClientCredentials(client_id=auth['client_id'],
#                                         client_secret=auth['client_secret'])

# spotify tracklist
tracks = dict(pd.read_csv("tracks.csv", index_col=0).T)

# youtube search
keys = "track_name artist_name album_name".split(" ")

def download(url):
    
    with youtube_dl.YoutubeDL(config) as ydl:
        ydl.download([url])
        title = ydl.extract_info(url, download = False)["title"]
    print("Done")

for i in np.random.randint(0, len(tracks), 50):
    query = " ".join([tracks[i][key] for key in keys]) + " lyrics"
    search = CustomSearch(query, VideoSortOrder.relevance, limit = 1)
    url = search.result()['result'][0]['link']


    # youtube download

      




    config = {
        'outtmpl': 'downloads/test_%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '256',
        }],
    }
    # config = {
    #     'outtmpl': f'downloads/test_{tracks[i]["track_name"]}.mp3',
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '256',
    #     }],
    # }
    try:
        download(url)
    except:
        pass








# if __name__ == "__main__":
#     download(url)


# if GUI:
    # def gui_download():
        # url = inputtxt.get(1.0, "end-1c")
        
        # with youtube_dl.YoutubeDL(config) as ydl:
        #     ydl.download([url])
        #     title = ydl.extract_info(url, download = False)["title"]
        # print("Done")
    # import tkinter as tk

    # Top level window
    # frame = tk.Tk()
    # frame.title("TextBox Input")
    # frame.geometry('400x200')
    # Function for getting Input
    # from textbox and printing it 
    # at label widget
#     # TextBox Creation
#     inputtxt = tk.Text(frame,
#                        height = 5,
#                        width = 20)
      
#     inputtxt.pack()
      
#     # Button Creation
#     printButton = tk.Button(frame,
#                             text = "Download", 
#                             command = gui_download)
#     printButton.pack()
      
#     # Label Creation
#     lbl = tk.Label(frame, text = "")
#     lbl.pack()
#     frame.mainloop()
# else:
#     download(url)





