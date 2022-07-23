import tkinter as tk
import ffmpeg
import youtube_dl
# Top level window
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
GUI = False
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

config = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
}

def download(url):
    
    with youtube_dl.YoutubeDL(config) as ydl:
        ydl.download([url])
        title = ydl.extract_info(url, download = False)["title"]
    print("Done")

def gui_download():
    url = inputtxt.get(1.0, "end-1c")
    
    with youtube_dl.YoutubeDL(config) as ydl:
        ydl.download([url])
        title = ydl.extract_info(url, download = False)["title"]
    print("Done")




if __name__ == "__main__":
    download(url)


# if GUI:
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





