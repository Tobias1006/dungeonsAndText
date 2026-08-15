import unittest
from entities import Entity, Human, Dwarf, Elf, Orc, Troll
from const_and_enum import Kinds

class TestAttackEntity(unittest.TestCase):
    def test_attack_standard_dmg(self):
        ent1 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        print('Attack: standard damage')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 2)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 0)
        self.assertEqual(ent2.dmgres, 0)
        self.assertEqual(ent2.name, None)
        
    def test_attack_dmg_reduced_by_arm(self):
        ent1 = Dwarf()
        ent2 = Human()
        print('Attack: reduced damage due to armor')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, Kinds.HUMAN)
        self.assertEqual(ent2.health, 8)
        self.assertEqual(ent2.dmg, 4)
        self.assertEqual(ent2.arm, 3)
        self.assertEqual(ent2.dmgres, 0)
        self.assertEqual(ent2.name, 'Steven')

    def test_attack_dmg_reduced_by_dmgres(self):
        ent1 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 100, name = None)
        print('Attack: reduced damage due to dmgres')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 4)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 0)
        self.assertEqual(ent2.dmgres, 100)
        self.assertEqual(ent2.name, None)

    def test_attack_dmg_reduced_by_arm_and_dmgres(self):
        ent1 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm = 1, dmgres = 100, name = None)
        print('Attack: reduced damage due to dmgres')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 4)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 1)
        self.assertEqual(ent2.dmgres, 100)
        self.assertEqual(ent2.name, None)

    def test_attack_dmg_floor_minimum(self):
        ent1 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm =6, dmgres = 0, name = None)
        print('Attack: reduced damage due to dmgres')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 4)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 6)
        self.assertEqual(ent2.dmgres, 0)
        self.assertEqual(ent2.name, None)

    def test_attack_dmg_rounding(self):
        ent1 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm = 1, dmgres = 25, name = None)
        print('Attack: reduced damage due to dmgres')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 3)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 1)
        self.assertEqual(ent2.dmgres, 25)
        self.assertEqual(ent2.name, None)

    def test_attack_dmg_less_than_arm(self):
        ent1 = Elf()
        ent2 = Troll()
        print('Attack: dmg lower than arm')
        ent1.attack(ent2)        
        self.assertEqual(ent2.kind, Kinds.TROLL)
        self.assertEqual(ent2.health, 34)
        self.assertEqual(ent2.dmg, 22)
        self.assertEqual(ent2.arm, 10)
        self.assertEqual(ent2.dmgres, 15)
        self.assertEqual(ent2.name, 'Dum-Dum')

    def test_attack_dmg_exact_lethal(self):
        ent1 = Entity(kind = None, health = 5, dmg = 5, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        print('Attack: dmg exact lethal')
        ent1.attack(ent2)        
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 0)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 0)
        self.assertEqual(ent2.dmgres, 0)
        self.assertEqual(ent2.name, None)
        self.assertEqual(ent2.is_alive, False)

    def test_attack_dmg_overkill(self):
        ent1 = Entity(kind = None, health = 5, dmg = 18, arm = 0, dmgres = 0, name = None)
        ent2 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        print('Attack: dmg overkill')
        ent1.attack(ent2)        
        self.assertEqual(ent2.kind, None)
        self.assertEqual(ent2.health, 0)
        self.assertEqual(ent2.dmg, 3)
        self.assertEqual(ent2.arm, 0)
        self.assertEqual(ent2.dmgres, 0)
        self.assertEqual(ent2.name, None)
        self.assertEqual(ent2.is_alive, False)
        
    def test_attack_self(self):
        ent1 = Entity(kind = None, health = 5, dmg = 3, arm = 0, dmgres = 0, name = None)
        result = ent1.attack(ent1)  
        print(result)      
        self.assertEqual(ent1.kind, None)
        self.assertEqual(ent1.health, 5)
        self.assertEqual(ent1.dmg, 3)
        self.assertEqual(ent1.arm, 0)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, None)
        self.assertEqual(ent1.is_alive, True)
        self.assertEqual(result, 'Can not attack yourself, sorry')

    def test_attack_corpse(self):
        ent1 = Entity(kind = None, health = 0, dmg = 3, arm = 0, dmgres = 0, name = None)
        ent1.is_alive = False
        ent2 = Troll()    
        result = ent2.attack(ent1)  
        print(result)      
        self.assertEqual(ent1.kind, None)
        self.assertEqual(ent1.health, 0)
        self.assertEqual(ent1.dmg, 3)
        self.assertEqual(ent1.arm, 0)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, None)
        self.assertEqual(ent1.is_alive, False)
        self.assertEqual(result, 'We do not do that here')

if __name__ == '__main__':
    unittest.main()