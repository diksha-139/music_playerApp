from app.models.linked_list import LinkedList

class PlayList:
    def __init__(self, id, playlist_name, linked_list:LinkedList):
        self.playlist_id = id
        self.playlist_name = playlist_name
        self.playlist_linked_list = linked_list
        
    def get_playlist(self):
        return self.playlist_linked_list
    
    def get_playlist_name(self):
        return self.playlist_name
    
    def get_playlist_id(self):
        return self.playlist_id