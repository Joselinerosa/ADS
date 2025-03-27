class iPod:
    def __init__(self):
        self.songs = {}  
        self.playlist = []  
        self.recently_played = []  
        self.total_play_time = 0 

    def addSong(self, S, A, D):
        if S in self.songs:
            print("ERROR addSong")
        else:
            self.songs[S] = (A, D)

    def addToPlaylist(self, S):
        if S not in self.songs:
            print("ERROR addToPlaylist")
        elif S not in self.playlist:
            self.playlist.append(S)
            self.total_play_time += self.songs[S][1]

    def current(self):
        if not self.playlist:
            print("ERROR current")
        else:
            print(self.playlist[0])

    def play(self):
        if not self.playlist:
            print("No hay canciones en la lista.")
        else:
            song = self.playlist.pop(0)
            self.total_play_time -= self.songs[song][1]

            if song in self.recently_played:
                self.recently_played.remove(song)
            self.recently_played.insert(0, song)

            print(f"Sonando {song}")

    def totalTime(self):
        print(f"Tiempo total {self.total_play_time}")

    def recent(self, N):
        if not self.recently_played:
            print("No hay canciones recientes")
        else:
            R = min(N, len(self.recently_played))
            print(f"Las {R} mas recientes")
            for song in self.recently_played[:R]:
                print(f"    {song}")

    def deleteSong(self, S):
        if S in self.songs:
            del self.songs[S]
            
            if S in self.playlist:
                self.playlist.remove(S)
                self.total_play_time -= self.songs[S][1]
            
            if S in self.recently_played:
                self.recently_played.remove(S)
