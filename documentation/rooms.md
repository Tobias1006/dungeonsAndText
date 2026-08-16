# General

## Attributes
### Rooms in general 
Every room in this game as a certain set of attributes:
- Kind (Enum->Rooms): kind
- Adjacent rooms (list[int]): adj_rooms
- Entity (Entity): entity
- Story (int): story
- Was the room alreadz visited? (bool): already_visited
  
The values for these attributes will vary for each room and will be hard-coded. There will be a list of rooms and the level will be static. In the future this may be exchanged for a randomly generated layout.
### Hallway
- Entity = None
- Story = None
### Fight
- Entity != None
- Story = None
### Story
- Entity may be None
- Story != None
### End
- Entity != None
- Story != None

## Functions
### Entities in general 
### Hallway
### Fight
### Story
### End