class Song:
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
        return Song(dict_entry["track_name"],
                   dict_entry['artist_name'],
                   dict_entry['album_name'])


class Artist:
	def __init__(self,
				 name):
		self.name = name

class Album:
	def __init__(self, title, artist):
		self.title = title
		self.artist = artist