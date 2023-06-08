import csv
from app.models.linked_list import LinkedList, ListNode
from app.models.song import Song

def create_linked_list():
    with open('app/app_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        linked_list = LinkedList()
        for row in reader:
            song = Song(row['Song ID'], row['Song Name'], row['Song Length'])
            listnode = ListNode(song)
            linked_list.insert_at_start(listnode)
            
    return linked_list