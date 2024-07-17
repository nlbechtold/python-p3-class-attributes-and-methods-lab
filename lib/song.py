class Song:
    artists =[]
    genres = []
    count = 0
    artist_count={}
    genre_count ={}

   
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)
        Song.add_to_artist_count(artist)
        Song.add_song_to_count()
        Song.add_to_genre_count(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count +=1




    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            Song.artists.append(artist) 
            
        
     
    @classmethod   
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            Song.genres.append(genre)

     

    @classmethod  
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
      
#     def add_song_to_count(self):
#         pass
# new_song = Song("gold digger", "yeezy", "rap")

# all_songs = Song(add_to_artists)

# print(Song.artists)
# add to count
# add to artist - needs if

# song count is an object (look at addidas add)