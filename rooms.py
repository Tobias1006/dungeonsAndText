from enum import Enum
from entities import Entity
from const_and_enum import Rooms

class Room:
    def __init__(self,
                 kind: Rooms,
                 adj_rooms: list,
                 entity: Entity = None,
                 story: int = None) -> None:
        self.kind = kind
        # adj_rooms is a list of all adjoining rooms and always contains at least the room that was just left
        self.adj_rooms = adj_rooms
        # Story is an index that points to the story-element triggered when entering the room 
        self.story = story
        # entity defines the kind of entity met upon entering the room.
        self.entity = entity
        self.already_visited = False


class Hallway(Room):
    def __init__(self,  
                 adj_rooms: list,
                 entity: Entity = None,                 
                 story: int = None) -> None:
        super().__init__(Rooms.HALLWAY, adj_rooms, entity)

class Story(Room):
    def __init__(self,  
                 adj_rooms: list,
                 story: int, 
                 entity: Entity = None) -> None:
        super().__init__(Rooms.STORY, adj_rooms, entity, story)

class Fight(Room):
    def __init__(self, 
                 adj_rooms: list,
                 entity: Entity, 
                 story: int = None) -> None:
        super().__init__(Rooms.FIGHT, adj_rooms, entity)

class End(Room):
    def __init__(self, 
                 adj_rooms: list,
                 entity: Entity,
                 story: int) -> None:
        super().__init__(Rooms.END, adj_rooms, entity, story)