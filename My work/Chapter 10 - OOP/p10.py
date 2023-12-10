class Music:
    def __init__(self, performer, song, album, year):
        self.perfomer = performer
        self.song = song
        self.album = album
        self.year = year
    def __str__(self):
        return ("{:<10} | {:<10}\n{:<10} | {:<10}\n{:<10} | {:<10}\n{:<10} | {:<10}".format("Performer:", self.perfomer, "Song:", self.song, "Album:",self.album,"Year:",self.year))
mysong1 = Music("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)
mysong = Music("Queen", "Bohemian Rhapsody", "A Night at the Opera", "1975")
print(mysong1)
