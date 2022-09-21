#Exercise #2

class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for x in self.lyrics:
            print(x)

song = Songs("Baby shark", "do do", "do do do do",
"Baby shark", "do do", "do do do do",
"Baby shark", "do do", "do do do do"
"Baby shark")
song.sing_me_a_song()
