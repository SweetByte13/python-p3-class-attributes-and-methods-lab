class Song:
    
    count = 0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}
    
    def __init__(self, name="", artist='', genre=''):
        self.artist = artist
        self.genre = genre
        self.name = name
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(self)
        self.add_to_artist_count(self)
        
    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
        
    @classmethod
    def add_to_genres(cls, self):
        cls.genres.append(self)
        
    @classmethod
    def add_to_artists(cls, self):
        cls.artists.append(self)
        
    @classmethod
    def add_to_genre_count(cls, self):
        cls.genres.append(self)
        
    @classmethod
    def add_to_artist_count(cls, self):
        cls.artists.append(self)
        
    @classmethod
    def add_to_genre_count(cls, self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
            
    @classmethod
    def add_to_artist_count(cls,self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1    