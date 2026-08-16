# Key Functionalities
## Output
The game output will be written directly into the console in which the player has run the game. There will be no additional window created for now. This might change in the future.
## Input
The game will get the users input from the same consol. Upon presenting the player with information about the room and the different options they can take, the game will listen for input from the player in the form of the number of the action they want to take, e.g.:
- Game output
	You find yourself in an empty room. What do you want to do?
	1. Search the room.
	2. Eat something to heal.
	3. Hone your weapon to increase damage.
	4. Move on.
- Player input
	3
# Entities
## Fighting
Fighting will be handled in the entity-class. Damage done is calculated as follows (Ent1 attacks Ent2): 
1. Ent2.Armor is subtracted from Ent1.Damage
2. Remaining Ent1.Damage is reduced by Ent2.DamageResistance
3. Damage surpassing Ent2.Health kills Ent2

Each attack does at least 1 damage.
## Healing
Healing will be handled in the subclasses for all entities separately to not allow overhealing.

# Rooms

## Moving through rooms
Upon choosing the action to move on from a room, the player will be presented with a list of adjacent rooms - provided as numbers - without knowing what rooms they are.
The selection of the new room follows the normal input/output scheme.
## Taking actions in a room
Upon Player input the selected action will be taken and a new output will be generated. A Player can only take one action before moving on from the room.
- Idea: Honing your weapon or searching the room could have a chance to spawn an enemy?
## Story in rooms
Upon moving into a room, the output presented for the player may contain a bit of story. Story will be provided as a larger block of text in the output window.
Certain Story elements may be expanded based on the character selected by the player. 