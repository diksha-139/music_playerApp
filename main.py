from app.models.music_player import MusicPlayer
from app.models.playlist import PlayList
import app

if __name__ == "__main__":
    musicplayer = MusicPlayer()
    
    linked_list = app.create_linked_list()
    
    playlist = PlayList(1, 'Songs', linked_list)
    
    print("\nAdding playlist to the Music Player \n")
    musicplayer.add_playlist(playlist)
    
    print(f'Playing all songs in the playlist : {playlist.playlist_name}: \n')
    musicplayer.play_playlist('Songs')
    
    print(f'\nDeleting the Song with name : Old And Secrets \n')
    musicplayer.delete_song_from_playlist('Songs', 'Old And Secrets')
    musicplayer.play_playlist('Songs')
    
    print('\nPlaying all songs after sorting based on song names: \n')
    musicplayer.sort_playlist('Songs')
    musicplayer.play_playlist('Songs')
    
    print('\nPlaying shuffled song \n')
    musicplayer.play_shuffled_song('Songs')