from constAndEnum import Kinds

class Entity:
    def __init__(self, 
                 kind: Kinds, 
                 health: int,
                 dmg: int, 
                 arm: int = 0, 
                 dmgres: int = 0,
                 name:str = None) -> None:
        self.name = name
        self.kind = kind
        self.health = health
        self.dmg = dmg
        # Armor (arm) is a flat reduction to damage.  
        self.arm = arm
        # Damage resistance (dmgres) is a percentage reduction to damage applied after armor
        # Dmgres 20 = 20% less damage
        self.dmgres = dmgres

    def attack(self, other) -> int:
        dmg_done = int(round((self.dmg-other.arm)*(1-(other.dmgres/100))))
        if dmg_done > 0:
            other.health -= dmg_done
        return other.health
    
class Human(Entity):
    def __init__(self, name:str) -> None:
        super().__init__(Kinds.HUMAN, 
                       100, 
                       10, 
                       3)
        self.name = name

class Elf(Entity):
    def __init__(self, name:str) -> None:
        super().__init__(Kinds.ELF, 
                       115, 
                       8, 
                       4, 
                       2)
        self.name = name

class Dwarf(Entity):
    def __init__(self, name:str) -> None:
        super().__init__(Kinds.DWARF, 
                       130, 
                       15, 
                       5)
        self.name = name

class Orc(Entity):
    def __init__(self) -> None:
        super().__init__(Kinds.ORC, 
                       80, 
                       8, 
                       3)

class Troll(Entity):
    def __init__(self) -> None:
        super().__init__(Kinds.TROLL, 
                       350, 
                       22, 
                       10, 
                       15)