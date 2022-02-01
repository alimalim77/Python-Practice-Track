from collections import deque
from typing import Deque
graph = {}
graph['you'] = ['alice', 'bob m', 'claire']
graph['alice'] = ['peggy']
graph['bob m'] = ['anum','peggy']
graph['claire'] = []
graph['anum'] = []
graph['peggy'] = []

search_queue = Deque()
search_queue += graph['you']
searched = []
def is_seller(person):
    return person[-1] == 'm'


while search_queue:
    person = search_queue.popleft()
    
    if is_seller(person) and person not in searched:
        searched.append(person)
        print(person, 'is mango seller')
    if person not in searched:
        searched.append(person)
    
    search_queue += graph[person]
