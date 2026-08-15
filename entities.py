from const_and_enum import Kinds

class Entity:
    def __init__(self, 
                 kind: Kinds, 
                 health: int,
                 dmg: int, 
                 arm: int, 
                 dmgres: int,
                 name:str) -> None:
        self.name = name
        self.kind = kind
        self.health = health
        self.dmg = dmg
        # Armor (arm) is a flat reduction to damage.  
        self.arm = arm
        # Damage resistance (dmgres) is a percentage reduction to damage applied after armor
        # Dmgres 20 = 20% less damage
        self.dmgres = dmgres
        self.is_alive = True

    def attack(self, other) -> int:
        if other == self:
            result = 'Can not attack yourself, sorry'
            return result
        if other.is_alive:
            net_dmg = (self.dmg-other.arm)*(1-(other.dmgres/100))
            dmg_done = max(1, int(round(net_dmg)))
            other.health = max(0, other.health-dmg_done)
            if other.health == 0:
                other.die()
            return dmg_done
        else:
            result = 'We do not do that here'
            return result
        
            
    
    def die(self) -> None:
        self.is_alive = False

class Human(Entity):
    def __init__(self, name:str = 'Steven') -> None:
        super().__init__(Kinds.HUMAN, 
                       10, 
                       4, 
                       3,
                       0, 
                       name)

class Elf(Entity):
    def __init__(self, name:str = 'Twinkle') -> None:
        super().__init__(Kinds.ELF, 
                       12, 
                       3, 
                       3, 
                       2, 
                       name)

class Dwarf(Entity):
    def __init__(self, name:str = 'Grobnob') -> None:
        super().__init__(Kinds.DWARF, 
                       13, 
                       5, 
                       5,
                       0,
                       name)

class Orc(Entity):
    def __init__(self, name:str = 'Krsprk') -> None:
        super().__init__(Kinds.ORC, 
                       8, 
                       4, 
                       3,
                       0,
                       name)

class Troll(Entity):
    def __init__(self, name:str = 'Dum-Dum') -> None:
        super().__init__(Kinds.TROLL, 
                       35, 
                       22, 
                       10, 
                       15,
                       name)