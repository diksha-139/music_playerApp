import random
from app.models.song import Song
import time

class ListNode:
    def __init__(self, song:Song):
        self.song = song
        self.next = None
        
    def __str__(self):
        return str(self.song)
    
    
class LinkedList:
    def __init__(self):
        self.head_node = None
        self.count = 0
    
    def traversal(self):
        if self.head_node is None:
            return
        
        temp_node = self.head_node
        
        while(temp_node != None):
            print(temp_node.song)
            time.sleep(2)
            temp_node = temp_node.next
        
        time.sleep(2)
        
        return
    
    def insert_at_start(self, node):
        if self.head_node is None:
            self.head_node = node
            self.count = self.count + 1
            return True
        
        node.next = self.head_node
        self.head_node = node
        
        return True
        
    def insert_after(self, song_name, node):
        temp_node = self.head_node
        
        while(temp_node.song.song_name!=song_name):
            temp_node = temp_node.next
            
        if temp_node is None:
            return False
        else:
            if temp_node.next == None:
                temp_node.next = node
            else:
                node.next = temp_node.next
                temp_node.next = node
            
            return True
        
    def insert_before(self, song_name, node):
        temp_node = self.head_node
        prev_node = None
        
        while(temp_node.song.song_name!=song_name):
            prev_node = temp_node
            temp_node = temp_node.next
        
        if temp_node == None:
            return False
        
        if prev_node == None:
            node.next = self.head_node
            self.head_node = node
            return True
        
        prev_node.next = node
        node.next = temp_node
        
        return True
    
    def delete_song(self, song_name):
        if self.head_node is None:
            return True
        
        temp_node = self.head_node
        prev_node = None
        
        while(temp_node.song.song_name!=song_name):
            prev_node = temp_node
            temp_node = temp_node.next
        
        if temp_node is None:
            return False
        
        if prev_node is None:
            self.head_node = None
            return True
        
        prev_node.next = temp_node.next
        
        return True
    
    def sort_list(self):
        if self.head_node is None:
            return
        
        nodes_list = list()
        
        temp_node = self.head_node
        
        while(temp_node is not None):
            nodes_list.append(ListNode(temp_node.song))
            temp_node = temp_node.next
            
        nodes_list = sorted(nodes_list, key = lambda node : node.song.song_name, reverse=True)
        self.head_node = None
        
        for node in nodes_list:
            self.insert_at_start(node)
        
        return
    
    def shuffle_song(self):
        if self.head_node is None:
            return None
        
        nodes_list = list()
        
        temp_node = self.head_node
        
        while(temp_node):
            nodes_list.append(ListNode(temp_node.song))
            temp_node = temp_node.next
            
        return nodes_list[random.randint(0, len(nodes_list)-1)]