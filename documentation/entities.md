# General
Humans, Elves, Dwarfs, Orcs and Trolls are populating the dungeon the Player is trying to navigate.

## Attributes
### Entities in general 
Every entity in this game as a certain set of attributes:
- Kind (Enum->Kinds): kind
- Health (int): health
- Damage (int): dmg
- Armor (int): arm
- Damage resistance (int): dmgres
- Name (str): name
- Living or dead? (bool): is_alive
  
The base value for these stats varies with the kind of entity concerned.
There are multiple kinds of species in this game.
### Human
- kind: HUMAN
- health: 10
- dmg: 4
- arm: 3
- dmgres: 0
- name: 'Steven'
- is_alive: True
### Elf
- kind: ELF
- health: 12
- dmg: 3
- arm: 3
- dmgres: 2
- name: 'Twinkle'
- is_alive: True
### Dwarf
- kind: DWARF
- health: 13
- dmg: 5
- arm: 5
- dmgres: 0
- name: 'Grobnob'
- is_alive: True
### Orc
- Kind (Enum->Kinds): kind
- health: 8
- dmg: 4
- arm: 3
- dmgres: 0
- name: 'Krsprk'
- is_alive: True
### Troll
- Kind (Enum->Kinds): kind
- health: 35
- dmg: 22
- arm: 10
- dmgres: 15
- name: 'Dum-Dum'
- is_alive: True

## Functions
### Entities in general 
### Human
### Elf
### Dwarf
### Orc
### Troll