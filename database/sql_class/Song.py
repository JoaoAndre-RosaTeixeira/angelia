from database.sql_class import Artist


class Song:

    def __init__(self, id: str, name: str, popularity: int, duration: int, explicit: bool, artists: list[Artist], release_date: any,danceability, energy, acousticness, tempo):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.duration = duration
        self.explicit = explicit
        self.artists = artists
        self.release_date = release_date
        self.danceability = danceability
        self.energy = energy
        self.acousticness = acousticness
        self.tempo = tempo

    def get_artist_names(self):
        str_artist = []
        for artist in self.artists:
            str_artist.append(artist.name)
        return str_artist


