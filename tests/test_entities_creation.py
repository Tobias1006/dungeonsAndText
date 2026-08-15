import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from const_and_enum import Kinds

class TestCreateEntity(unittest.TestCase):
    def test_create_human(self):
        ent1 = Human('Greg')
        print('Create Human: Greg')        
        self.assertEqual(ent1.kind, Kinds.HUMAN)
        self.assertEqual(ent1.health, 100)
        self.assertEqual(ent1.dmg, 10)
        self.assertEqual(ent1.arm, 3)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, 'Greg')
    
    def test_create_elf(self):
        ent1 = Elf('Twinkle')
        print('Create Elf: Twinkle')        
        self.assertEqual(ent1.kind, Kinds.ELF)
        self.assertEqual(ent1.health, 115)
        self.assertEqual(ent1.dmg, 8)
        self.assertEqual(ent1.arm, 4)
        self.assertEqual(ent1.dmgres, 2)
        self.assertEqual(ent1.name, 'Twinkle')

    def test_create_dwarf(self):
        ent1 = Dwarf('Dunarin')
        print('Create Dwarf: Dunarin')
        self.assertEqual(ent1.kind, Kinds.DWARF)
        self.assertEqual(ent1.health, 130)
        self.assertEqual(ent1.dmg, 15)
        self.assertEqual(ent1.arm, 5)
        self.assertEqual(ent1.dmgres, 0)
        self.assertEqual(ent1.name, 'Dunarin')

if __name__ == '__main__':
    unittest.main()
