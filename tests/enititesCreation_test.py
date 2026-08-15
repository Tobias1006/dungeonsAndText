import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from constAndEnum import Kinds

class TestCreateEntity(unittest.TestCase):
    def test_create_human(self):
        ent1 = Human('Greg')
        print('Create Human: Greg')
        list1 = [ent1.kind, 
                 ent1.health,
                 ent1.dmg, 
                 ent1.arm, 
                 ent1.dmgres,
                 ent1.name
                 ]
        list2 = [Kinds.HUMAN,
                 100,
                 10,
                 3,
                 0,
                 'Greg'
                 ]
        self.assertEqual(list1, list2)
    
    def test_create_elf(self):
        ent1 = Elf('Twinkle')
        print('Create Elf: Twinkle')
        list1 = [ent1.kind, 
                 ent1.health,
                 ent1.dmg, 
                 ent1.arm, 
                 ent1.dmgres,
                 ent1.name
                 ]
        list2 = [Kinds.ELF,
                 115,
                 8, 
                 4, 
                 2,
                 'Twinkle'
                 ]
        self.assertEqual(list1, list2)

    def test_create_dwarf(self):
        ent1 = Dwarf('Dunarin')
        print('Create Dwarf: Dunarin')
        list1 = [ent1.kind, 
                 ent1.health, 
                 ent1.dmg, 
                 ent1.arm, 
                 ent1.dmgres, 
                 ent1.name
                 ]
        list2 = [Kinds.DWARF,
                 130,
                 15, 
                 5, 
                 0,
                 'Dunarin'
                 ]
        self.assertEqual(list1, list2)

if __name__ == '__main__':
    unittest.main()
