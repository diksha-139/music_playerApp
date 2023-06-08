from app.models.playlist import PlayList

class MusicPlayer:
    def __init__(self):
        self.playlists = list()
        
    def add_playlist(self, new_playlist:PlayList):
        self.playlists.append(new_playlist)
        
    def play_playlist(self, playlist_name):
        for playlist in self.playlists:
            if playlist.get_playlist_name() == playlist_name:
                playlist.get_playlist().traversal()
            else:
                print('No such playlist exists in the Music Player')
        
    def delete_song_from_playlist(self, playlist_name, song_name):
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist is None:
            print("No such playlist exists in the Music Player.")
            return
        playlist.get_playlist().delete_song(song_name)
        return
        
    def sort_playlist(self, playlist_name):
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist is None:
            print("No such playlist exists in the Music Player.")
            return
        playlist.get_playlist().sort_list()
        return
    
    def play_shuffled_song(self, playlist_name):
        playlist = self.search_playlist_by_name(playlist_name)
        if playlist is None:
            print("No such playlist exists in the Music Player.")
            return
        print(playlist.get_playlist().shuffle_song())
        return
    
    def list_all_playlists(self):
        for playlist in self.playlists:
            print(playlist.playlist_name)
            
    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                return playlist
            
        return None
    
    def delete_playlist(self, name):
        for playlist in self.playlists:
            if playlist.playlist_name == name:
                del playlist
                return True
        
        return False