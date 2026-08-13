from constAndEnum import Kinds

class Entitiy:
    def __init__(self, 
                 kind: Kinds, 
                 health: int,
                 dmg: int, 
                 spd: int, 
                 arm: int = None, 
                 dmgres: int = None,
                 name:str = None):
        self.name = name
        self.kind = kind
        self.health = health
        self.dmg = dmg
        self.spd = spd
        # Armor (arm) is a flat reduction to damage.  
        self.arm = arm
        # Damage resistance (dmgres) is a percentage reduction to damage applied after armor
        # Dmgres 20 = 20% less damage
        self.dmgres = dmgres

    def attack(self, other):
        pass
    
class Human(Entitiy):
    def __init__(self, name:str):
        super.__init__(Kinds.HUMAN, 
                       100, 
                       30, 
                       10, 
                       3)
        self.name = name

class Elf(Entitiy):
    def __init__(self, name:str):
        super.__init__(Kinds.ELF, 
                       115, 
                       40, 
                       8, 
                       4, 
                       2)
        self.name = name

class Dwarf(Entitiy):
    def __init__(self, name:str):
        super.__init__(Kinds.DWARF, 
                       130, 
                       20, 
                       15, 
                       5)
        self.name = name

class Orc(Entitiy):
    def __init__(self):
        super.__init__(Kinds.ORC, 
                       80, 
                       30, 
                       8, 
                       3)

class Troll(Entitiy):
    def __init__(self):
        super.__init__(Kinds.TROLL, 
                       350, 
                       15, 
                       22, 
                       10, 
                       15)