import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from const_and_enum import Kinds

class TestAttackEntity(unittest.TestCase):
    def test_attack_correct(self):
        ent1 = Human('Greg')
        ent2 = Elf('Twinkle')
        print('Attack: happy path')
        ent1.attack(ent2)
        self.assertEqual(ent2.kind, Kinds.ELF)
        self.assertEqual(ent2.health, 109)
        self.assertEqual(ent2.dmg, 8)
        self.assertEqual(ent2.arm, 4)
        self.assertEqual(ent2.dmgres, 2)
        self.assertEqual(ent2.name, 'Twinkle')

    def test_attack_dmg_less_than_arm(self):
        ent1 = Elf('Twinkle')
        ent2 = Troll()
        print('Attack: dmg lower than arm')
        ent1.attack(ent2)        
        self.assertEqual(ent2.kind, Kinds.TROLL)
        self.assertEqual(ent2.health, 350)
        self.assertEqual(ent2.dmg, 22)
        self.assertEqual(ent2.arm, 10)
        self.assertEqual(ent2.dmgres, 15)
        self.assertEqual(ent2.name, None)

if __name__ == '__main__':
    unittest.main()