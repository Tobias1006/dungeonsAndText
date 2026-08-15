from enum import Enum

class Kinds(Enum):
    HUMAN = 'human'
    DWARF = 'dwarf'
    ELF = 'elf'
    ORC = 'orc'
    TROLL = 'troll'

class Rooms(Enum):
    FIGHT = 'fight',
    STORY = 'story',
    HALLWAY = 'hallway',
    END = 'end'

class Actions(Enum):
    REST = 'rest',
    SEARCH = 'search',
    EAT = 'eat',
    FIGHT = 'fight',
    FLEE = 'flee'