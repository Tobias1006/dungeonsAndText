import unittest
from entities import Human, Dwarf, Elf, Orc, Troll
from constAndEnum import Kinds

class TestParentNode(unittest.TestCase):
    def test_create_human(self):
        ent1 = Human('Greg')
        print('Create Human: Greg')
        list1 = [ent1.kind, 
                 ent1.health,
                 ent1.spd,
                 ent1.dmg, 
                 ent1.arm, 
                 ent1.dmgres,
                 ent1.name
                 ]
        list2 = [Kinds.HUMAN,
                 100,
                 30,
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
                 ent1.spd,
                 ent1.dmg, 
                 ent1.arm, 
                 ent1.dmgres,
                 ent1.name
                 ]
        list2 = [Kinds.ELF,
                 115,
                 40, 
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
                 ent1.spd, 
                 ent1.dmg, 
                 ent1.arm, 
                 ent1.dmgres, 
                 ent1.name
                 ]
        list2 = [Kinds.DWARF,
                 130,
                 20, 
                 15, 
                 5, 
                 0,
                 'Dunarin'
                 ]
        self.assertEqual(list1, list2)

    def test_human_vs_elf(self):
        ent1 = Human('Greg')
        ent2 = Elf('Twinkle')
        print('Greg attacks Twinkle')
        ent1.attack(ent2)
        list1 = [ent2.kind, 
                ent2.health,
                ent2.spd,
                ent2.dmg, 
                ent2.arm, 
                ent2.dmgres,
                ent2.name
                ]
        list2 = [Kinds.ELF,
                 109,
                 40, 
                 8, 
                 4, 
                 2,
                 'Twinkle'
                 ]
        print(list1, list2)
        self.assertEqual(list1, list2)

    def test_human_vs_elf_wrong(self):
        ent1 = Human('Greg')
        ent2 = Elf('Twinkle')
        print('Wait... Twinkle attacks Greg!')
        ent2.attack(ent1)
        list1 = [ent1.kind, 
                ent1.health,
                ent1.spd,
                ent1.dmg, 
                ent1.arm, 
                ent1.dmgres,
                ent1.name
                ]
        list2 = [Kinds.HUMAN,
                 100,
                 30,
                 10,
                 3,
                 0,
                 'Greg'
                 ]
        print(list1, list2)
        self.assertNotEqual(list1, list2)

if __name__ == '__main__':
    unittest.main()
